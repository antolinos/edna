#!/usr/bin/env python
# DriverHelper.py
#
#   Copyright (C) 2006 CCLRC, Graeme Winter
#
#   This code is distributed under the BSD license, a copy of which is 
#   included in the root directory of this package.
#
# 24th may 2006
# 
# Helper functions (mostly abstraction layer) for the Driver implementations.
# 
# Implemented functions:
# kill_process(Popen process instance)
#
# script_writer(String name, String exec,
#               String [] command_line, String [] input)
# 
# executable_exists(executable) - see Change 1/SEP/06 in DefaultDriver - 
# This will search the path for something which will respond to executable.
# 
# Functions to be implemented:
# 
# Modification log:
# 20/JUN/06 added getting-of-status to bash scripts -> script_name.xstatus
#           this means that if this file exists, then the job has run...
# 1/SEP/06  added method to search for executables in the command environment
#           also added code to use "call" for batch files on windows - 
#           this still passes in the output and input redirection, which
#           documentation at:
# 
#           http://www.microsoft.com/resources/documentation/
#           windows/xp/all/proddocs/en-us/batch.mspx?mfr=true
#
#           says won't work - however, testing against ExampleProgram
#           StandardInput < input.txt > output.txt with something
#           in input.txt appears to behave as expected. Beware - this
#           could be a hidden gremlin, though is in general not an
#           important problem.

import os
import signal
import stat
import random

def script_writer(working_directory,
                  script_name,
                  executable,
                  command_line_tokens,
                  environment,
                  input_records,
                  mkdirs = []):
    '''Write a script to run a program for either UNIX or Windows.
    mkdirs[] will allow instructions to make directories to be passed
    in.'''

    if os.name == 'nt':
        # write out a windows batch file

        script = open('%s.bat' % os.path.join(working_directory,
                                              script_name), 'w')

        # try to delete the .xstatus file - if it exists
        script.write('@if exist %s.xstatus del %s.xstatus\n' % \
                     (script_name, script_name))

        # make the directories we've been asked to
        for dir in mkdirs:
            script.write('@mkdir %s\n' % dir)

        # FIXME 1/SEP/06 - if the "executable" is a batch file on
        # windows then this should be called. We know in here that
        # we're on win32, so...
        
        if executable.split('.')[-1] == 'bat':
            script.write('@call %s ' % executable)
        else:
            script.write('@%s ' % executable)
            
        for c in command_line_tokens:
            script.write('"%s" ' % c)

        script.write('< %s.xin > %s.xout\n' % (script_name, script_name))

        # add the status stuff - for NT this will be NULL.
        script.write('@echo 0 > %s.xstatus\n' % script_name)

        script.close()

        input = open('%s.xin' % os.path.join(working_directory,
                                             script_name), 'w')
        for i in input_records:
            input.write('%s' % i)
        input.close()

    if os.name == 'posix':
        # write out a bash script

        script = open('%s.sh' % os.path.join(working_directory,
                                             script_name), 'w')

        script.write('#!/bin/bash\n\n')

        for name in environment:
            added = environment[name][0]
            for value in environment[name][1:]:
                added += '%s%s' % (os.pathsep, value)
            script.write('export %s=%s%s$%s\n' % (name, added,
                                                  os.pathsep, name))

        # delete the xatstus file if it exists
        script.write('rm -f %s.xstatus\n' % script_name)

        # make the directories we have been asked to
        for dir in mkdirs:
            script.write('mkdir -p %s\n' % dir)
        
        script.write('%s ' % executable)

        for c in command_line_tokens:
            script.write('\'%s\' ' % c)

        script.write('<< eof > %s.xout\n' % script_name)

        for i in input_records:
            script.write('%s' % i)
            
        script.write('eof\n')

        # record the status from this script
        script.write('echo "$?" > %s.xstatus\n' % script_name)        

        script.close()

        os.chmod(os.path.join(working_directory, '%s.sh' % script_name),
                 stat.S_IEXEC|stat.S_IREAD|stat.S_IWRITE)

    return

# implementatin of the kill_process method - which takes a subprocess.Popen
# object...

def kill_process(process):
    if os.name == 'nt':
        '''A wrapper for the Win32 API TerminateProcess method.'''
        import win32api

        # caveat user: this is using undocumented API
        handle = int(process._handle)

        win32api.TerminateProcess(handle, -1)

        return

    else:
        '''A wrapper for the os.kill() function.'''
        pid = process.pid

        os.kill(pid, signal.SIGKILL)

        return

def error_no_program(record):
    '''Look in a record (output from program) for signs that this died
    due to a missing program.'''

    if os.name == 'nt':
        if 'is not recognized as an internal' in record:
            raise RuntimeError, 'executable "%s" does not exist' % \
                  record.split('\'')[1]
    else:
        if 'command not found' in record:
            raise RuntimeError, 'executable "%s" does not exist' % \
                  record.split()[-4].replace(':', '')

def error_missing_library(record):
    '''Look in the record for indications that a library was missing.'''

    if os.name == 'nt':
        # FIXME need to code for this
        pass
    else:
        if 'error while loading shared libraries' in record:
            # figure out what is missing (bug # 2378)
            missing_library = ''
            record_bits = record.split(':')
            for token in record_bits:
                if token[:3] == 'lib':
                    missing_library = token
                    break

            if missing_library:
                raise RuntimeError, 'child missing library %s' % \
                      missing_library
            else:
                raise RuntimeError, 'child missing library (%s)' % \
                      record.strip()

def error_segv(record):
    '''Look in record for signs of a segmentation fault.'''

    if os.name == 'nt':
        # there is no output when a segmentation violation happens
        # on an XP box
        pass

    else:
        if 'Segmentation fault' in record:
            raise RuntimeError, 'child segmentation fault'

def error_fp(record):
    '''Look for signs of a floating point exception.'''
    if os.name == 'nt':
        pass

    else:
        if 'Floating Exception' in record:
            raise RuntimeError, 'child killed'

def error_kill(record):
    '''Look in record for signs of a killed child process.'''

    if os.name == 'nt':
        # there is no output when a segmentation violation happens
        # on an XP box
        pass

    else:
        if 'Killed' in record:
            raise RuntimeError, 'child killed'

def error_abrt(record):
    '''Look in record for signs of a abort signal.'''

    if os.name == 'nt':
        # there is no output when a segmentation violation happens
        # on an XP box
        pass

    else:
        # this is a posix compliant system which will mean that the
        # os.uname call will work

        name = os.uname()[0]
        
        if name == 'Linux' and 'Aborted' in record:
            raise RuntimeError, 'child aborted'

        if name == 'Darwin' and 'Abort trap' in record:
            raise RuntimeError, 'child aborted'

def check_return_code(code):
    '''Check the return code for indications of errors.'''


    if os.name == 'nt':
        if code == 3:
            raise RuntimeError, 'child error'

    else:
        if code >= 0:
            return

        # return codes in POSIX are -ve

        segv = signal.SIGSEGV * -1
        kill = signal.SIGKILL * -1
        abrt = signal.SIGABRT * -1

        if code == segv:
            raise RuntimeError, 'child segmentation fault'

        if code == kill:
            raise RuntimeError, 'child killed'

        if code == abrt:
            raise RuntimeError, 'child aborted'

def executable_exists(executable):
    '''Search the PATH for this executable, return "" if it is not
    found, full path otherwise. Caveat Emptor.'''

    # first check if this is an absolute path, and if it is,
    # see if it exists. FIXME in here need to be able to cope
    # with someone setting the .exe or whatever explicitly...
    # ok, check for this if the platform is windows.

    # FIXME need to correctly handle "~" on UNIX platforms.
    # This is Bug # 2221

    if os.name == 'nt':
        if not executable.split('.')[-1] in ['exe', 'bat']:
            executable_files = ['%s.bat' % executable,
                                '%s.exe' % executable]
        else:
            executable_files = [executable]
    else:
        executable_files = [executable]

    # absolute path is defined simply as starting with '/' on UNIX
    # and '\' or 'd:\' on windows - so the path doesn't have to
    # exist

    if os.path.isabs(executable):
        for file in executable_files:
            if os.path.exists(file):
                return file
            
        # if we have reached here we have an absolute path
        # without a matching executable file

        return ''

    # then search the path if it is not an absolute path

    path_env = os.environ['PATH']

    if os.name == 'nt':
        pathsplit_token = ';'
    else:
        pathsplit_token = ':'

    path = path_env.split(pathsplit_token)

    for directory in path:
        for file in executable_files:
            if os.path.exists(os.path.join(directory, file)):
                # FIXME should probably check that this file
                # is executable here...
                return os.path.join(directory, file)
            
    return ''

class _RandomNamer:
    '''A class to generate random names.'''

    def __init__(self):
        
        if not os.environ.has_key('XIA2CORE_ROOT'):
            raise RuntimeError, 'XIA2CORE_ROOT not defined'
    
        self._names = []
        self._used_names = []

        for l in open(os.path.join(os.environ['XIA2CORE_ROOT'],
                                   'Data', 'Random', 'names.txt')).readlines():
            self._names.append(l.strip())

        self._last = 0

    def generate(self):
        '''Generate a random name.'''

        if True:
            self._last += 1
            return '%08d' % self._last

        name = ''

        # FIXME in extreme cases this will result in an infinate loop
        # as we try to find an unused name from the 80,000        

        while name in self._used_names or name == '':
            i = int(random.random() * len(self._names))
            name = self._names[i]
            
        self._used_names.append(name)
        
        return 'xia-%s' % name

RandomNamer = _RandomNamer()
        
def generate_random_name():
    '''Generate a random name to use as a handle for a job.'''

    return RandomNamer.generate()

if __name__ == '__main__':

    for i in range(10):
        print '"%s"' % generate_random_name()

    
