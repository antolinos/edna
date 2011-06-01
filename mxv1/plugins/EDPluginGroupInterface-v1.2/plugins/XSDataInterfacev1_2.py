#!/usr/bin/env python

#
# Generated Tue Jan 25 09:34:27 2011 by EDGenerateDS.py.
#

import sys
import getopt
import StringIO
from xml.dom import minidom
from xml.dom import Node

#
# If you have installed IPython you can uncomment and use the following.
# IPython is available from http://ipython.scipy.org/.
#

## from IPython.Shell import IPShellEmbed
## args = ''
## ipshell = IPShellEmbed(args,
##     banner = 'Dropping into IPython',
##     exit_msg = 'Leaving Interpreter, back to program.')

# Then use the following line where and when you want to drop into the
# IPython shell:
#    ipshell('<some message> -- Entering ipshell.\nHit Ctrl-D to exit')

#
# Support/utility functions.
#

def showIndent(outfile, level):
    for idx in range(level):
        outfile.write('    ')

def quote_xml(inStr):
    s1 = inStr
    s1 = s1.replace('&', '&amp;')
    s1 = s1.replace('<', '&lt;')
    s1 = s1.replace('"', '&quot;')
    return s1

def quote_python(inStr):
    s1 = inStr
    if s1.find("'") == -1:
        if s1.find('\n') == -1:
            return "'%s'" % s1
        else:
            return "'''%s'''" % s1
    else:
        if s1.find('"') != -1:
            s1 = s1.replace('"', '\\"')
        if s1.find('\n') == -1:
            return '"%s"' % s1
        else:
            return '"""%s"""' % s1


class MixedContainer:
    # Constants for category:
    CategoryNone = 0
    CategoryText = 1
    CategorySimple = 2
    CategoryComplex = 3
    # Constants for content_type:
    TypeNone = 0
    TypeText = 1
    TypeString = 2
    TypeInteger = 3
    TypeFloat = 4
    TypeDecimal = 5
    TypeDouble = 6
    TypeBoolean = 7
    def __init__(self, category, content_type, name, value):
        self.category = category
        self.content_type = content_type
        self.name = name
        self.value = value
    def getCategory(self):
        return self.category
    def getContenttype(self, content_type):
        return self.content_type
    def getValue(self):
        return self.value
    def getName(self):
        return self.name
    def export(self, outfile, level, name):
        if self.category == MixedContainer.CategoryText:
            outfile.write(self.value)
        elif self.category == MixedContainer.CategorySimple:
            self.exportSimple(outfile, level, name)
        else:    # category == MixedContainer.CategoryComplex
            self.value.export(outfile, level, name)
    def exportSimple(self, outfile, level, name):
        if self.content_type == MixedContainer.TypeString:
            outfile.write('<%s>%s</%s>' % (self.name, self.value, self.name))
        elif self.content_type == MixedContainer.TypeInteger or \
                self.content_type == MixedContainer.TypeBoolean:
            outfile.write('<%s>%d</%s>' % (self.name, self.value, self.name))
        elif self.content_type == MixedContainer.TypeFloat or \
                self.content_type == MixedContainer.TypeDecimal:
            outfile.write('<%s>%f</%s>' % (self.name, self.value, self.name))
        elif self.content_type == MixedContainer.TypeDouble:
            outfile.write('<%s>%g</%s>' % (self.name, self.value, self.name))
    def exportLiteral(self, outfile, level, name):
        if self.category == MixedContainer.CategoryText:
            showIndent(outfile, level)
            outfile.write('MixedContainer(%d, %d, "%s", "%s"),\n' % \
                (self.category, self.content_type, self.name, self.value))
        elif self.category == MixedContainer.CategorySimple:
            showIndent(outfile, level)
            outfile.write('MixedContainer(%d, %d, "%s", "%s"),\n' % \
                (self.category, self.content_type, self.name, self.value))
        else:    # category == MixedContainer.CategoryComplex
            showIndent(outfile, level)
            outfile.write('MixedContainer(%d, %d, "%s",\n' % \
                (self.category, self.content_type, self.name,))
            self.value.exportLiteral(outfile, level + 1)
            showIndent(outfile, level)
            outfile.write(')\n')


class _MemberSpec(object):
    def __init__(self, name='', data_type='', container=0):
        self.name = name
        self.data_type = data_type
        self.container = container
    def set_name(self, name): self.name = name
    def get_name(self): return self.name
    def set_data_type(self, data_type): self.data_type = data_type
    def get_data_type(self): return self.data_type
    def set_container(self, container): self.container = container
    def get_container(self): return self.container


#
# Data representation classes.
#

class XSConfiguration:
    subclass = None
    def __init__(self, XSPluginList=None):
        self.XSPluginList = XSPluginList
    def factory(*args_, **kwargs_):
        if XSConfiguration.subclass:
            return XSConfiguration.subclass(*args_, **kwargs_)
        else:
            return XSConfiguration(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getXSPluginList(self): return self.XSPluginList
    def setXSPluginList(self, XSPluginList): self.XSPluginList = XSPluginList
    def export(self, outfile, level, name_='XSConfiguration'):
        showIndent(outfile, level)
        outfile.write('<%s>\n' % name_)
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='XSConfiguration'):
        pass
    def exportChildren(self, outfile, level, name_='XSConfiguration'):
        if self.getXSPluginList() != None :
            if self.XSPluginList:
                self.XSPluginList.export(outfile, level)

    #Only to export the entire XML tree to a file stream on disk
    def outputFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write("<?xml version=\"1.0\" ?>\n")
        self.export( outfile, 0, name_='XSConfiguration' )
        outfile.close()


    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSConfiguration.factory()
        rootObj.build(rootNode)
        return rootObj
    parseString = staticmethod( parseString ) 


    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSConfiguration.factory()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile ) 


    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO.StringIO()
        oStreamString.write('<?xml version="1.0" ?>\n')
        self.export( oStreamString, 0, name_="XSConfiguration" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    def exportLiteral(self, outfile, level, name_='XSConfiguration'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        pass
    def exportLiteralChildren(self, outfile, level, name_):
        if self.XSPluginList:
            showIndent(outfile, level)
            outfile.write('XSPluginList=XSPluginList(\n')
            self.XSPluginList.exportLiteral(outfile, level)
            showIndent(outfile, level)
            outfile.write('),\n')
    def build(self, node_):
        attrs = node_.attributes
        self.buildAttributes(attrs)
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildAttributes(self, attrs):
        pass
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'XSPluginList':
            obj_ = XSPluginList.factory()
            obj_.build(child_)
            self.setXSPluginList(obj_)
# end class XSConfiguration


class XSData(object):
    subclass = None
    def __init__(self, valueOf_=''):
        self.valueOf_ = valueOf_
    def factory(*args_, **kwargs_):
        if XSData.subclass:
            return XSData.subclass(*args_, **kwargs_)
        else:
            return XSData(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getValueOf_(self): return self.valueOf_
    def setValueOf_(self, valueOf_): self.valueOf_ = valueOf_
    def export(self, outfile, level, name_='XSData'):
        showIndent(outfile, level)
        outfile.write('<%s>' % name_)
        self.exportChildren(outfile, level + 1, name_)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='XSData'):
        pass
    def exportChildren(self, outfile, level, name_='XSData'):
        pass
    #Only to export the entire XML tree to a file stream on disk
    def outputFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write("<?xml version=\"1.0\" ?>\n")
        self.export( outfile, 0, name_='XSData' )
        outfile.close()


    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSData.factory()
        rootObj.build(rootNode)
        return rootObj
    parseString = staticmethod( parseString ) 


    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSData.factory()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile ) 


    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO.StringIO()
        oStreamString.write('<?xml version="1.0" ?>\n')
        self.export( oStreamString, 0, name_="XSData" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    def exportLiteral(self, outfile, level, name_='XSData'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        pass
    def exportLiteralChildren(self, outfile, level, name_):
        showIndent(outfile, level)
        outfile.write('valueOf_ = "%s",\n' % (self.valueOf_,))
    def build(self, node_):
        attrs = node_.attributes
        self.buildAttributes(attrs)
        self.valueOf_ = ''
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildAttributes(self, attrs):
        pass
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.TEXT_NODE:
            self.valueOf_ += child_.nodeValue
# end class XSData


class XSDataArray(XSData):
    subclass = None
    def __init__(self, shape=None, size=-1, dtype='', data='', coding=None, md5sum=None):
        XSData.__init__(self)
        if shape is None:
            self.shape = []
        else:
            self.shape = shape
        self.size = size
        self.dtype = dtype
        self.data = data
        self.coding = coding
        self.md5sum = md5sum
    def factory(*args_, **kwargs_):
        if XSDataArray.subclass:
            return XSDataArray.subclass(*args_, **kwargs_)
        else:
            return XSDataArray(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getShape(self): return self.shape
    def setShape(self, shape): self.shape = shape
    def addShape(self, value): self.shape.append(value)
    def insertShape(self, index, value): self.shape[index] = value
    def getSize(self): return self.size
    def setSize(self, size): self.size = size
    def getDtype(self): return self.dtype
    def setDtype(self, dtype): self.dtype = dtype
    def getData(self): return self.data
    def setData(self, data): self.data = data
    def getCoding(self): return self.coding
    def setCoding(self, coding): self.coding = coding
    def getMd5sum(self): return self.md5sum
    def setMd5sum(self, md5sum): self.md5sum = md5sum
    def export(self, outfile, level, name_='XSDataArray'):
        showIndent(outfile, level)
        outfile.write('<%s>\n' % name_)
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='XSDataArray'):
        XSData.exportAttributes(self, outfile, level, name_='XSDataArray')
    def exportChildren(self, outfile, level, name_='XSDataArray'):
        for shape_ in self.getShape():
            showIndent(outfile, level)
            outfile.write('<shape>%d</shape>\n' % shape_)
        showIndent(outfile, level)
        outfile.write('<size>%d</size>\n' % self.getSize())
        showIndent(outfile, level)
        outfile.write('<dtype>%s</dtype>\n' % quote_xml(self.getDtype()))
        showIndent(outfile, level)
        outfile.write('<data>%s</data>\n' % quote_xml(self.getData()))
        if self.getCoding() != None :
            if self.coding:
                self.coding.export(outfile, level, name_='coding')
        if self.getMd5sum() != None :
            if self.md5sum:
                self.md5sum.export(outfile, level, name_='md5sum')
        XSData.exportChildren(self, outfile, level, name_)

    #Only to export the entire XML tree to a file stream on disk
    def outputFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write("<?xml version=\"1.0\" ?>\n")
        self.export( outfile, 0, name_='XSDataArray' )
        outfile.close()


    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataArray.factory()
        rootObj.build(rootNode)
        return rootObj
    parseString = staticmethod( parseString ) 


    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataArray.factory()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile ) 


    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO.StringIO()
        oStreamString.write('<?xml version="1.0" ?>\n')
        self.export( oStreamString, 0, name_="XSDataArray" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    def exportLiteral(self, outfile, level, name_='XSDataArray'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        pass
        XSData.exportLiteralAttributes(self, outfile, level, name_)
    def exportLiteralChildren(self, outfile, level, name_):
        showIndent(outfile, level)
        outfile.write('shape=[\n')
        level += 1
        for shape in self.shape:
            showIndent(outfile, level)
            outfile.write('%d,\n' % shape)
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
        showIndent(outfile, level)
        outfile.write('size=%d,\n' % self.getSize())
        showIndent(outfile, level)
        outfile.write('dtype=%s,\n' % quote_python(self.getDtype()))
        showIndent(outfile, level)
        outfile.write('data=%s,\n' % quote_python(self.getData()))
        if self.coding:
            showIndent(outfile, level)
            outfile.write('coding=XSDataString(\n')
            self.coding.exportLiteral(outfile, level, name_='coding')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.md5sum:
            showIndent(outfile, level)
            outfile.write('md5sum=XSDataString(\n')
            self.md5sum.exportLiteral(outfile, level, name_='md5sum')
            showIndent(outfile, level)
            outfile.write('),\n')
        XSData.exportLiteralChildren(self, outfile, level, name_)
    def build(self, node_):
        attrs = node_.attributes
        self.buildAttributes(attrs)
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildAttributes(self, attrs):
        XSData.buildAttributes(self, attrs)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'shape':
            if child_.firstChild:
                sval_ = child_.firstChild.nodeValue
                try:
                    ival_ = int(sval_)
                except ValueError:
                    raise ValueError('requires integer -- %s' % child_.toxml())
                self.shape.append(ival_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'size':
            if child_.firstChild:
                sval_ = child_.firstChild.nodeValue
                try:
                    ival_ = int(sval_)
                except ValueError:
                    raise ValueError('requires integer -- %s' % child_.toxml())
                self.size = ival_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'dtype':
            dtype_ = ''
            for text__content_ in child_.childNodes:
                dtype_ += text__content_.nodeValue
            self.dtype = dtype_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'data':
            data_ = ''
            for text__content_ in child_.childNodes:
                data_ += text__content_.nodeValue
            self.data = data_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'coding':
            obj_ = XSDataString.factory()
            obj_.build(child_)
            self.setCoding(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'md5sum':
            obj_ = XSDataString.factory()
            obj_.build(child_)
            self.setMd5sum(obj_)
# end class XSDataArray


class XSDataBoolean(XSData):
    subclass = None
    def __init__(self, value=0):
        XSData.__init__(self)
        self.value = value
    def factory(*args_, **kwargs_):
        if XSDataBoolean.subclass:
            return XSDataBoolean.subclass(*args_, **kwargs_)
        else:
            return XSDataBoolean(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getValue(self): return self.value
    def setValue(self, value): self.value = value
    def export(self, outfile, level, name_='XSDataBoolean'):
        showIndent(outfile, level)
        outfile.write('<%s>\n' % name_)
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='XSDataBoolean'):
        XSData.exportAttributes(self, outfile, level, name_='XSDataBoolean')
    def exportChildren(self, outfile, level, name_='XSDataBoolean'):
        showIndent(outfile, level)
        outfile.write('<value>%d</value>\n' % self.getValue())
        XSData.exportChildren(self, outfile, level, name_)

    #Only to export the entire XML tree to a file stream on disk
    def outputFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write("<?xml version=\"1.0\" ?>\n")
        self.export( outfile, 0, name_='XSDataBoolean' )
        outfile.close()


    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataBoolean.factory()
        rootObj.build(rootNode)
        return rootObj
    parseString = staticmethod( parseString ) 


    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataBoolean.factory()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile ) 


    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO.StringIO()
        oStreamString.write('<?xml version="1.0" ?>\n')
        self.export( oStreamString, 0, name_="XSDataBoolean" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    def exportLiteral(self, outfile, level, name_='XSDataBoolean'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        pass
        XSData.exportLiteralAttributes(self, outfile, level, name_)
    def exportLiteralChildren(self, outfile, level, name_):
        showIndent(outfile, level)
        outfile.write('value=%d,\n' % self.getValue())
        XSData.exportLiteralChildren(self, outfile, level, name_)
    def build(self, node_):
        attrs = node_.attributes
        self.buildAttributes(attrs)
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildAttributes(self, attrs):
        XSData.buildAttributes(self, attrs)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'value':
            if child_.firstChild:
                sval_ = child_.firstChild.nodeValue
                if sval_ in ('true', '1'):
                    ival_ = 1
                elif sval_ in ('false', '0'):
                    ival_ = 0
                else:
                    raise ValueError('requires boolean -- %s' % child_.toxml())
                self.value = ival_
# end class XSDataBoolean


class XSDataDictionary:
    subclass = None
    def __init__(self, keyValuePair=None):
        if keyValuePair is None:
            self.keyValuePair = []
        else:
            self.keyValuePair = keyValuePair
    def factory(*args_, **kwargs_):
        if XSDataDictionary.subclass:
            return XSDataDictionary.subclass(*args_, **kwargs_)
        else:
            return XSDataDictionary(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getKeyValuePair(self): return self.keyValuePair
    def setKeyValuePair(self, keyValuePair): self.keyValuePair = keyValuePair
    def addKeyValuePair(self, value): self.keyValuePair.append(value)
    def insertKeyValuePair(self, index, value): self.keyValuePair[index] = value
    def export(self, outfile, level, name_='XSDataDictionary'):
        showIndent(outfile, level)
        outfile.write('<%s>\n' % name_)
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='XSDataDictionary'):
        pass
    def exportChildren(self, outfile, level, name_='XSDataDictionary'):
        for keyValuePair_ in self.getKeyValuePair():
            keyValuePair_.export(outfile, level, name_='keyValuePair')

    #Only to export the entire XML tree to a file stream on disk
    def outputFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write("<?xml version=\"1.0\" ?>\n")
        self.export( outfile, 0, name_='XSDataDictionary' )
        outfile.close()


    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataDictionary.factory()
        rootObj.build(rootNode)
        return rootObj
    parseString = staticmethod( parseString ) 


    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataDictionary.factory()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile ) 


    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO.StringIO()
        oStreamString.write('<?xml version="1.0" ?>\n')
        self.export( oStreamString, 0, name_="XSDataDictionary" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    def exportLiteral(self, outfile, level, name_='XSDataDictionary'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        pass
    def exportLiteralChildren(self, outfile, level, name_):
        showIndent(outfile, level)
        outfile.write('keyValuePair=[\n')
        level += 1
        for keyValuePair in self.keyValuePair:
            showIndent(outfile, level)
            outfile.write('XSDataKeyValuePair(\n')
            keyValuePair.exportLiteral(outfile, level, name_='keyValuePair')
            showIndent(outfile, level)
            outfile.write('),\n')
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
    def build(self, node_):
        attrs = node_.attributes
        self.buildAttributes(attrs)
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildAttributes(self, attrs):
        pass
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'keyValuePair':
            obj_ = XSDataKeyValuePair.factory()
            obj_.build(child_)
            self.keyValuePair.append(obj_)
# end class XSDataDictionary


class XSDataDisplacement:
    subclass = None
    def __init__(self, value=0.0, unit=None, error=None):
        self.value = value
        self.unit = unit
        self.error = error
    def factory(*args_, **kwargs_):
        if XSDataDisplacement.subclass:
            return XSDataDisplacement.subclass(*args_, **kwargs_)
        else:
            return XSDataDisplacement(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getValue(self): return self.value
    def setValue(self, value): self.value = value
    def getUnit(self): return self.unit
    def setUnit(self, unit): self.unit = unit
    def getError(self): return self.error
    def setError(self, error): self.error = error
    def export(self, outfile, level, name_='XSDataDisplacement'):
        showIndent(outfile, level)
        outfile.write('<%s>\n' % name_)
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='XSDataDisplacement'):
        pass
    def exportChildren(self, outfile, level, name_='XSDataDisplacement'):
        showIndent(outfile, level)
        outfile.write('<value>%e</value>\n' % self.getValue())
        if self.getUnit() != None :
            if self.unit:
                self.unit.export(outfile, level, name_='unit')
        if self.getError() != None :
            if self.error:
                self.error.export(outfile, level, name_='error')

    #Only to export the entire XML tree to a file stream on disk
    def outputFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write("<?xml version=\"1.0\" ?>\n")
        self.export( outfile, 0, name_='XSDataDisplacement' )
        outfile.close()


    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataDisplacement.factory()
        rootObj.build(rootNode)
        return rootObj
    parseString = staticmethod( parseString ) 


    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataDisplacement.factory()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile ) 


    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO.StringIO()
        oStreamString.write('<?xml version="1.0" ?>\n')
        self.export( oStreamString, 0, name_="XSDataDisplacement" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    def exportLiteral(self, outfile, level, name_='XSDataDisplacement'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        pass
    def exportLiteralChildren(self, outfile, level, name_):
        showIndent(outfile, level)
        outfile.write('value=%e,\n' % self.getValue())
        if self.unit:
            showIndent(outfile, level)
            outfile.write('unit=XSDataString(\n')
            self.unit.exportLiteral(outfile, level, name_='unit')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.error:
            showIndent(outfile, level)
            outfile.write('error=XSDataDouble(\n')
            self.error.exportLiteral(outfile, level, name_='error')
            showIndent(outfile, level)
            outfile.write('),\n')
    def build(self, node_):
        attrs = node_.attributes
        self.buildAttributes(attrs)
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildAttributes(self, attrs):
        pass
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'value':
            if child_.firstChild:
                sval_ = child_.firstChild.nodeValue
                try:
                    fval_ = float(sval_)
                except ValueError:
                    raise ValueError('requires float (or double) -- %s' % child_.toxml())
                self.value = fval_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'unit':
            obj_ = XSDataString.factory()
            obj_.build(child_)
            self.setUnit(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'error':
            obj_ = XSDataDouble.factory()
            obj_.build(child_)
            self.setError(obj_)
# end class XSDataDisplacement


class XSDataDouble(XSData):
    subclass = None
    def __init__(self, value=0.0):
        XSData.__init__(self)
        self.value = value
    def factory(*args_, **kwargs_):
        if XSDataDouble.subclass:
            return XSDataDouble.subclass(*args_, **kwargs_)
        else:
            return XSDataDouble(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getValue(self): return self.value
    def setValue(self, value): self.value = value
    def export(self, outfile, level, name_='XSDataDouble'):
        showIndent(outfile, level)
        outfile.write('<%s>\n' % name_)
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='XSDataDouble'):
        XSData.exportAttributes(self, outfile, level, name_='XSDataDouble')
    def exportChildren(self, outfile, level, name_='XSDataDouble'):
        showIndent(outfile, level)
        outfile.write('<value>%e</value>\n' % self.getValue())
        XSData.exportChildren(self, outfile, level, name_)

    #Only to export the entire XML tree to a file stream on disk
    def outputFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write("<?xml version=\"1.0\" ?>\n")
        self.export( outfile, 0, name_='XSDataDouble' )
        outfile.close()


    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataDouble.factory()
        rootObj.build(rootNode)
        return rootObj
    parseString = staticmethod( parseString ) 


    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataDouble.factory()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile ) 


    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO.StringIO()
        oStreamString.write('<?xml version="1.0" ?>\n')
        self.export( oStreamString, 0, name_="XSDataDouble" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    def exportLiteral(self, outfile, level, name_='XSDataDouble'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        pass
        XSData.exportLiteralAttributes(self, outfile, level, name_)
    def exportLiteralChildren(self, outfile, level, name_):
        showIndent(outfile, level)
        outfile.write('value=%e,\n' % self.getValue())
        XSData.exportLiteralChildren(self, outfile, level, name_)
    def build(self, node_):
        attrs = node_.attributes
        self.buildAttributes(attrs)
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildAttributes(self, attrs):
        XSData.buildAttributes(self, attrs)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'value':
            if child_.firstChild:
                sval_ = child_.firstChild.nodeValue
                try:
                    fval_ = float(sval_)
                except ValueError:
                    raise ValueError('requires float (or double) -- %s' % child_.toxml())
                self.value = fval_
# end class XSDataDouble


class XSDataDoubleWithUnit(XSDataDouble):
    subclass = None
    def __init__(self, value=0.0, unit=None, error=None):
        XSDataDouble.__init__(self, value)
        self.unit = unit
        self.error = error
    def factory(*args_, **kwargs_):
        if XSDataDoubleWithUnit.subclass:
            return XSDataDoubleWithUnit.subclass(*args_, **kwargs_)
        else:
            return XSDataDoubleWithUnit(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getUnit(self): return self.unit
    def setUnit(self, unit): self.unit = unit
    def getError(self): return self.error
    def setError(self, error): self.error = error
    def export(self, outfile, level, name_='XSDataDoubleWithUnit'):
        showIndent(outfile, level)
        outfile.write('<%s>\n' % name_)
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='XSDataDoubleWithUnit'):
        XSDataDouble.exportAttributes(self, outfile, level, name_='XSDataDoubleWithUnit')
    def exportChildren(self, outfile, level, name_='XSDataDoubleWithUnit'):
        if self.getUnit() != None :
            if self.unit:
                self.unit.export(outfile, level, name_='unit')
        if self.getError() != None :
            if self.error:
                self.error.export(outfile, level, name_='error')
        XSDataDouble.exportChildren(self, outfile, level, name_)

    #Only to export the entire XML tree to a file stream on disk
    def outputFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write("<?xml version=\"1.0\" ?>\n")
        self.export( outfile, 0, name_='XSDataDoubleWithUnit' )
        outfile.close()


    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataDoubleWithUnit.factory()
        rootObj.build(rootNode)
        return rootObj
    parseString = staticmethod( parseString ) 


    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataDoubleWithUnit.factory()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile ) 


    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO.StringIO()
        oStreamString.write('<?xml version="1.0" ?>\n')
        self.export( oStreamString, 0, name_="XSDataDoubleWithUnit" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    def exportLiteral(self, outfile, level, name_='XSDataDoubleWithUnit'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        pass
        XSDataDouble.exportLiteralAttributes(self, outfile, level, name_)
    def exportLiteralChildren(self, outfile, level, name_):
        if self.unit:
            showIndent(outfile, level)
            outfile.write('unit=XSDataString(\n')
            self.unit.exportLiteral(outfile, level, name_='unit')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.error:
            showIndent(outfile, level)
            outfile.write('error=XSDataDouble(\n')
            self.error.exportLiteral(outfile, level, name_='error')
            showIndent(outfile, level)
            outfile.write('),\n')
        XSDataDouble.exportLiteralChildren(self, outfile, level, name_)
    def build(self, node_):
        attrs = node_.attributes
        self.buildAttributes(attrs)
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildAttributes(self, attrs):
        XSDataDouble.buildAttributes(self, attrs)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'unit':
            obj_ = XSDataString.factory()
            obj_.build(child_)
            self.setUnit(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'error':
            obj_ = XSDataDouble.factory()
            obj_.build(child_)
            self.setError(obj_)
        XSDataDouble.buildChildren(self, child_, nodeName_)
# end class XSDataDoubleWithUnit


class XSDataExecutionInfo:
    subclass = None
    def __init__(self, baseDirectory=None, executionTime=None, pluginName=None, startOfExecution=None, systeminfo=None, workingDirectory=None, configuration=None):
        self.baseDirectory = baseDirectory
        self.executionTime = executionTime
        self.pluginName = pluginName
        self.startOfExecution = startOfExecution
        self.systeminfo = systeminfo
        self.workingDirectory = workingDirectory
        self.configuration = configuration
    def factory(*args_, **kwargs_):
        if XSDataExecutionInfo.subclass:
            return XSDataExecutionInfo.subclass(*args_, **kwargs_)
        else:
            return XSDataExecutionInfo(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getBaseDirectory(self): return self.baseDirectory
    def setBaseDirectory(self, baseDirectory): self.baseDirectory = baseDirectory
    def getExecutionTime(self): return self.executionTime
    def setExecutionTime(self, executionTime): self.executionTime = executionTime
    def getPluginName(self): return self.pluginName
    def setPluginName(self, pluginName): self.pluginName = pluginName
    def getStartOfExecution(self): return self.startOfExecution
    def setStartOfExecution(self, startOfExecution): self.startOfExecution = startOfExecution
    def getSysteminfo(self): return self.systeminfo
    def setSysteminfo(self, systeminfo): self.systeminfo = systeminfo
    def getWorkingDirectory(self): return self.workingDirectory
    def setWorkingDirectory(self, workingDirectory): self.workingDirectory = workingDirectory
    def getConfiguration(self): return self.configuration
    def setConfiguration(self, configuration): self.configuration = configuration
    def export(self, outfile, level, name_='XSDataExecutionInfo'):
        showIndent(outfile, level)
        outfile.write('<%s>\n' % name_)
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='XSDataExecutionInfo'):
        pass
    def exportChildren(self, outfile, level, name_='XSDataExecutionInfo'):
        if self.baseDirectory:
            self.baseDirectory.export(outfile, level, name_='baseDirectory')
        if self.executionTime:
            self.executionTime.export(outfile, level, name_='executionTime')
        if self.pluginName:
            self.pluginName.export(outfile, level, name_='pluginName')
        if self.startOfExecution:
            self.startOfExecution.export(outfile, level, name_='startOfExecution')
        if self.systeminfo:
            self.systeminfo.export(outfile, level, name_='systeminfo')
        if self.workingDirectory:
            self.workingDirectory.export(outfile, level, name_='workingDirectory')
        if self.configuration:
            self.configuration.export(outfile, level, name_='configuration')

    #Only to export the entire XML tree to a file stream on disk
    def outputFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write("<?xml version=\"1.0\" ?>\n")
        self.export( outfile, 0, name_='XSDataExecutionInfo' )
        outfile.close()


    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataExecutionInfo.factory()
        rootObj.build(rootNode)
        return rootObj
    parseString = staticmethod( parseString ) 


    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataExecutionInfo.factory()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile ) 


    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO.StringIO()
        oStreamString.write('<?xml version="1.0" ?>\n')
        self.export( oStreamString, 0, name_="XSDataExecutionInfo" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    def exportLiteral(self, outfile, level, name_='XSDataExecutionInfo'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        pass
    def exportLiteralChildren(self, outfile, level, name_):
        if self.baseDirectory:
            showIndent(outfile, level)
            outfile.write('baseDirectory=XSDataFile(\n')
            self.baseDirectory.exportLiteral(outfile, level, name_='baseDirectory')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.executionTime:
            showIndent(outfile, level)
            outfile.write('executionTime=XSDataTime(\n')
            self.executionTime.exportLiteral(outfile, level, name_='executionTime')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.pluginName:
            showIndent(outfile, level)
            outfile.write('pluginName=XSDataString(\n')
            self.pluginName.exportLiteral(outfile, level, name_='pluginName')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.startOfExecution:
            showIndent(outfile, level)
            outfile.write('startOfExecution=XSDataDate(\n')
            self.startOfExecution.exportLiteral(outfile, level, name_='startOfExecution')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.systeminfo:
            showIndent(outfile, level)
            outfile.write('systeminfo=XSDataSysteminfo(\n')
            self.systeminfo.exportLiteral(outfile, level, name_='systeminfo')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.workingDirectory:
            showIndent(outfile, level)
            outfile.write('workingDirectory=XSDataFile(\n')
            self.workingDirectory.exportLiteral(outfile, level, name_='workingDirectory')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.configuration:
            showIndent(outfile, level)
            outfile.write('configuration=XSConfiguration(\n')
            self.configuration.exportLiteral(outfile, level, name_='configuration')
            showIndent(outfile, level)
            outfile.write('),\n')
    def build(self, node_):
        attrs = node_.attributes
        self.buildAttributes(attrs)
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildAttributes(self, attrs):
        pass
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'baseDirectory':
            obj_ = XSDataFile.factory()
            obj_.build(child_)
            self.setBaseDirectory(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'executionTime':
            obj_ = XSDataTime.factory()
            obj_.build(child_)
            self.setExecutionTime(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'pluginName':
            obj_ = XSDataString.factory()
            obj_.build(child_)
            self.setPluginName(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'startOfExecution':
            obj_ = XSDataDate.factory()
            obj_.build(child_)
            self.setStartOfExecution(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'systeminfo':
            obj_ = XSDataSysteminfo.factory()
            obj_.build(child_)
            self.setSysteminfo(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'workingDirectory':
            obj_ = XSDataFile.factory()
            obj_.build(child_)
            self.setWorkingDirectory(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'configuration':
            obj_ = XSConfiguration.factory()
            obj_.build(child_)
            self.setConfiguration(obj_)
# end class XSDataExecutionInfo


class XSDataFile(XSData):
    subclass = None
    def __init__(self, path=None):
        XSData.__init__(self)
        self.path = path
    def factory(*args_, **kwargs_):
        if XSDataFile.subclass:
            return XSDataFile.subclass(*args_, **kwargs_)
        else:
            return XSDataFile(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getPath(self): return self.path
    def setPath(self, path): self.path = path
    def export(self, outfile, level, name_='XSDataFile'):
        showIndent(outfile, level)
        outfile.write('<%s>\n' % name_)
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='XSDataFile'):
        XSData.exportAttributes(self, outfile, level, name_='XSDataFile')
    def exportChildren(self, outfile, level, name_='XSDataFile'):
        if self.path:
            self.path.export(outfile, level, name_='path')
        XSData.exportChildren(self, outfile, level, name_)

    #Only to export the entire XML tree to a file stream on disk
    def outputFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write("<?xml version=\"1.0\" ?>\n")
        self.export( outfile, 0, name_='XSDataFile' )
        outfile.close()


    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataFile.factory()
        rootObj.build(rootNode)
        return rootObj
    parseString = staticmethod( parseString ) 


    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataFile.factory()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile ) 


    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO.StringIO()
        oStreamString.write('<?xml version="1.0" ?>\n')
        self.export( oStreamString, 0, name_="XSDataFile" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    def exportLiteral(self, outfile, level, name_='XSDataFile'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        pass
        XSData.exportLiteralAttributes(self, outfile, level, name_)
    def exportLiteralChildren(self, outfile, level, name_):
        if self.path:
            showIndent(outfile, level)
            outfile.write('path=XSDataString(\n')
            self.path.exportLiteral(outfile, level, name_='path')
            showIndent(outfile, level)
            outfile.write('),\n')
        XSData.exportLiteralChildren(self, outfile, level, name_)
    def build(self, node_):
        attrs = node_.attributes
        self.buildAttributes(attrs)
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildAttributes(self, attrs):
        XSData.buildAttributes(self, attrs)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'path':
            obj_ = XSDataString.factory()
            obj_.build(child_)
            self.setPath(obj_)
# end class XSDataFile


class XSDataFloat(XSData):
    subclass = None
    def __init__(self, value=0.0):
        XSData.__init__(self)
        self.value = value
    def factory(*args_, **kwargs_):
        if XSDataFloat.subclass:
            return XSDataFloat.subclass(*args_, **kwargs_)
        else:
            return XSDataFloat(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getValue(self): return self.value
    def setValue(self, value): self.value = value
    def export(self, outfile, level, name_='XSDataFloat'):
        showIndent(outfile, level)
        outfile.write('<%s>\n' % name_)
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='XSDataFloat'):
        XSData.exportAttributes(self, outfile, level, name_='XSDataFloat')
    def exportChildren(self, outfile, level, name_='XSDataFloat'):
        showIndent(outfile, level)
        outfile.write('<value>%e</value>\n' % self.getValue())
        XSData.exportChildren(self, outfile, level, name_)

    #Only to export the entire XML tree to a file stream on disk
    def outputFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write("<?xml version=\"1.0\" ?>\n")
        self.export( outfile, 0, name_='XSDataFloat' )
        outfile.close()


    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataFloat.factory()
        rootObj.build(rootNode)
        return rootObj
    parseString = staticmethod( parseString ) 


    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataFloat.factory()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile ) 


    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO.StringIO()
        oStreamString.write('<?xml version="1.0" ?>\n')
        self.export( oStreamString, 0, name_="XSDataFloat" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    def exportLiteral(self, outfile, level, name_='XSDataFloat'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        pass
        XSData.exportLiteralAttributes(self, outfile, level, name_)
    def exportLiteralChildren(self, outfile, level, name_):
        showIndent(outfile, level)
        outfile.write('value=%e,\n' % self.getValue())
        XSData.exportLiteralChildren(self, outfile, level, name_)
    def build(self, node_):
        attrs = node_.attributes
        self.buildAttributes(attrs)
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildAttributes(self, attrs):
        XSData.buildAttributes(self, attrs)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'value':
            if child_.firstChild:
                sval_ = child_.firstChild.nodeValue
                try:
                    fval_ = float(sval_)
                except ValueError:
                    raise ValueError('requires float (or double) -- %s' % child_.toxml())
                self.value = fval_
# end class XSDataFloat


class XSDataFlux(XSDataDoubleWithUnit):
    subclass = None
    def __init__(self, value=0.0, unit=None, error=None, valueOf_=''):
        XSDataDoubleWithUnit.__init__(self, value, unit, error)
        self.valueOf_ = valueOf_
    def factory(*args_, **kwargs_):
        if XSDataFlux.subclass:
            return XSDataFlux.subclass(*args_, **kwargs_)
        else:
            return XSDataFlux(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getValueOf_(self): return self.valueOf_
    def setValueOf_(self, valueOf_): self.valueOf_ = valueOf_
    def export(self, outfile, level, name_='XSDataFlux'):
        showIndent(outfile, level)
        outfile.write('<%s>\n' % name_)
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='XSDataFlux'):
        XSDataDoubleWithUnit.exportAttributes(self, outfile, level, name_='XSDataFlux')
    def exportChildren(self, outfile, level, name_='XSDataFlux'):
        XSDataDoubleWithUnit.exportChildren(self, outfile, level, name_)

    #Only to export the entire XML tree to a file stream on disk
    def outputFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write("<?xml version=\"1.0\" ?>\n")
        self.export( outfile, 0, name_='XSDataFlux' )
        outfile.close()


    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataFlux.factory()
        rootObj.build(rootNode)
        return rootObj
    parseString = staticmethod( parseString ) 


    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataFlux.factory()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile ) 


    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO.StringIO()
        oStreamString.write('<?xml version="1.0" ?>\n')
        self.export( oStreamString, 0, name_="XSDataFlux" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    def exportLiteral(self, outfile, level, name_='XSDataFlux'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        pass
        XSDataDoubleWithUnit.exportLiteralAttributes(self, outfile, level, name_)
    def exportLiteralChildren(self, outfile, level, name_):
        showIndent(outfile, level)
        outfile.write('valueOf_ = "%s",\n' % (self.valueOf_,))
        XSDataDoubleWithUnit.exportLiteralChildren(self, outfile, level, name_)
    def build(self, node_):
        attrs = node_.attributes
        self.buildAttributes(attrs)
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildAttributes(self, attrs):
        XSDataDoubleWithUnit.buildAttributes(self, attrs)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.TEXT_NODE:
            self.valueOf_ += child_.nodeValue
        XSDataDoubleWithUnit.buildChildren(self, child_, nodeName_)
# end class XSDataFlux


class XSDataImage(XSDataFile):
    subclass = None
    def __init__(self, path=None, date=None, number=None):
        XSDataFile.__init__(self, path)
        self.date = date
        self.number = number
    def factory(*args_, **kwargs_):
        if XSDataImage.subclass:
            return XSDataImage.subclass(*args_, **kwargs_)
        else:
            return XSDataImage(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getDate(self): return self.date
    def setDate(self, date): self.date = date
    def getNumber(self): return self.number
    def setNumber(self, number): self.number = number
    def export(self, outfile, level, name_='XSDataImage'):
        showIndent(outfile, level)
        outfile.write('<%s>\n' % name_)
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='XSDataImage'):
        XSDataFile.exportAttributes(self, outfile, level, name_='XSDataImage')
    def exportChildren(self, outfile, level, name_='XSDataImage'):
        if self.getDate() != None :
            if self.date:
                self.date.export(outfile, level, name_='date')
        if self.getNumber() != None :
            if self.number:
                self.number.export(outfile, level, name_='number')
        XSDataFile.exportChildren(self, outfile, level, name_)

    #Only to export the entire XML tree to a file stream on disk
    def outputFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write("<?xml version=\"1.0\" ?>\n")
        self.export( outfile, 0, name_='XSDataImage' )
        outfile.close()


    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataImage.factory()
        rootObj.build(rootNode)
        return rootObj
    parseString = staticmethod( parseString ) 


    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataImage.factory()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile ) 


    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO.StringIO()
        oStreamString.write('<?xml version="1.0" ?>\n')
        self.export( oStreamString, 0, name_="XSDataImage" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    def exportLiteral(self, outfile, level, name_='XSDataImage'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        pass
        XSDataFile.exportLiteralAttributes(self, outfile, level, name_)
    def exportLiteralChildren(self, outfile, level, name_):
        if self.date:
            showIndent(outfile, level)
            outfile.write('date=XSDataString(\n')
            self.date.exportLiteral(outfile, level, name_='date')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.number:
            showIndent(outfile, level)
            outfile.write('number=XSDataInteger(\n')
            self.number.exportLiteral(outfile, level, name_='number')
            showIndent(outfile, level)
            outfile.write('),\n')
        XSDataFile.exportLiteralChildren(self, outfile, level, name_)
    def build(self, node_):
        attrs = node_.attributes
        self.buildAttributes(attrs)
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildAttributes(self, attrs):
        XSDataFile.buildAttributes(self, attrs)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'date':
            obj_ = XSDataString.factory()
            obj_.build(child_)
            self.setDate(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'number':
            obj_ = XSDataInteger.factory()
            obj_.build(child_)
            self.setNumber(obj_)
        XSDataFile.buildChildren(self, child_, nodeName_)
# end class XSDataImage


class XSDataInput(XSData):
    subclass = None
    def __init__(self, configuration=None):
        XSData.__init__(self)
        self.configuration = configuration
    def factory(*args_, **kwargs_):
        if XSDataInput.subclass:
            return XSDataInput.subclass(*args_, **kwargs_)
        else:
            return XSDataInput(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getConfiguration(self): return self.configuration
    def setConfiguration(self, configuration): self.configuration = configuration
    def export(self, outfile, level, name_='XSDataInput'):
        showIndent(outfile, level)
        outfile.write('<%s>\n' % name_)
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='XSDataInput'):
        XSData.exportAttributes(self, outfile, level, name_='XSDataInput')
    def exportChildren(self, outfile, level, name_='XSDataInput'):
        if self.configuration:
            self.configuration.export(outfile, level, name_='configuration')
        XSData.exportChildren(self, outfile, level, name_)

    #Only to export the entire XML tree to a file stream on disk
    def outputFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write("<?xml version=\"1.0\" ?>\n")
        self.export( outfile, 0, name_='XSDataInput' )
        outfile.close()


    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataInput.factory()
        rootObj.build(rootNode)
        return rootObj
    parseString = staticmethod( parseString ) 


    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataInput.factory()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile ) 


    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO.StringIO()
        oStreamString.write('<?xml version="1.0" ?>\n')
        self.export( oStreamString, 0, name_="XSDataInput" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    def exportLiteral(self, outfile, level, name_='XSDataInput'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        pass
        XSData.exportLiteralAttributes(self, outfile, level, name_)
    def exportLiteralChildren(self, outfile, level, name_):
        if self.configuration:
            showIndent(outfile, level)
            outfile.write('configuration=XSConfiguration(\n')
            self.configuration.exportLiteral(outfile, level, name_='configuration')
            showIndent(outfile, level)
            outfile.write('),\n')
        XSData.exportLiteralChildren(self, outfile, level, name_)
    def build(self, node_):
        attrs = node_.attributes
        self.buildAttributes(attrs)
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildAttributes(self, attrs):
        XSData.buildAttributes(self, attrs)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'configuration':
            obj_ = XSConfiguration.factory()
            obj_.build(child_)
            self.setConfiguration(obj_)
# end class XSDataInput


class XSDataInteger(XSData):
    subclass = None
    def __init__(self, value=-1):
        XSData.__init__(self)
        self.value = value
    def factory(*args_, **kwargs_):
        if XSDataInteger.subclass:
            return XSDataInteger.subclass(*args_, **kwargs_)
        else:
            return XSDataInteger(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getValue(self): return self.value
    def setValue(self, value): self.value = value
    def export(self, outfile, level, name_='XSDataInteger'):
        showIndent(outfile, level)
        outfile.write('<%s>\n' % name_)
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='XSDataInteger'):
        XSData.exportAttributes(self, outfile, level, name_='XSDataInteger')
    def exportChildren(self, outfile, level, name_='XSDataInteger'):
        showIndent(outfile, level)
        outfile.write('<value>%d</value>\n' % self.getValue())
        XSData.exportChildren(self, outfile, level, name_)

    #Only to export the entire XML tree to a file stream on disk
    def outputFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write("<?xml version=\"1.0\" ?>\n")
        self.export( outfile, 0, name_='XSDataInteger' )
        outfile.close()


    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataInteger.factory()
        rootObj.build(rootNode)
        return rootObj
    parseString = staticmethod( parseString ) 


    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataInteger.factory()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile ) 


    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO.StringIO()
        oStreamString.write('<?xml version="1.0" ?>\n')
        self.export( oStreamString, 0, name_="XSDataInteger" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    def exportLiteral(self, outfile, level, name_='XSDataInteger'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        pass
        XSData.exportLiteralAttributes(self, outfile, level, name_)
    def exportLiteralChildren(self, outfile, level, name_):
        showIndent(outfile, level)
        outfile.write('value=%d,\n' % self.getValue())
        XSData.exportLiteralChildren(self, outfile, level, name_)
    def build(self, node_):
        attrs = node_.attributes
        self.buildAttributes(attrs)
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildAttributes(self, attrs):
        XSData.buildAttributes(self, attrs)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'value':
            if child_.firstChild:
                sval_ = child_.firstChild.nodeValue
                try:
                    ival_ = int(sval_)
                except ValueError:
                    raise ValueError('requires integer -- %s' % child_.toxml())
                self.value = ival_
# end class XSDataInteger


class XSDataKeyValuePair:
    subclass = None
    def __init__(self, value=None, key=None):
        self.value = value
        self.key = key
    def factory(*args_, **kwargs_):
        if XSDataKeyValuePair.subclass:
            return XSDataKeyValuePair.subclass(*args_, **kwargs_)
        else:
            return XSDataKeyValuePair(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getValue(self): return self.value
    def setValue(self, value): self.value = value
    def getKey(self): return self.key
    def setKey(self, key): self.key = key
    def export(self, outfile, level, name_='XSDataKeyValuePair'):
        showIndent(outfile, level)
        outfile.write('<%s>\n' % name_)
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='XSDataKeyValuePair'):
        pass
    def exportChildren(self, outfile, level, name_='XSDataKeyValuePair'):
        if self.value:
            self.value.export(outfile, level, name_='value')
        if self.key:
            self.key.export(outfile, level, name_='key')

    #Only to export the entire XML tree to a file stream on disk
    def outputFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write("<?xml version=\"1.0\" ?>\n")
        self.export( outfile, 0, name_='XSDataKeyValuePair' )
        outfile.close()


    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataKeyValuePair.factory()
        rootObj.build(rootNode)
        return rootObj
    parseString = staticmethod( parseString ) 


    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataKeyValuePair.factory()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile ) 


    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO.StringIO()
        oStreamString.write('<?xml version="1.0" ?>\n')
        self.export( oStreamString, 0, name_="XSDataKeyValuePair" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    def exportLiteral(self, outfile, level, name_='XSDataKeyValuePair'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        pass
    def exportLiteralChildren(self, outfile, level, name_):
        if self.value:
            showIndent(outfile, level)
            outfile.write('value=XSDataString(\n')
            self.value.exportLiteral(outfile, level, name_='value')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.key:
            showIndent(outfile, level)
            outfile.write('key=XSDataString(\n')
            self.key.exportLiteral(outfile, level, name_='key')
            showIndent(outfile, level)
            outfile.write('),\n')
    def build(self, node_):
        attrs = node_.attributes
        self.buildAttributes(attrs)
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildAttributes(self, attrs):
        pass
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'value':
            obj_ = XSDataString.factory()
            obj_.build(child_)
            self.setValue(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'key':
            obj_ = XSDataString.factory()
            obj_.build(child_)
            self.setKey(obj_)
# end class XSDataKeyValuePair


class XSDataLength(XSDataDoubleWithUnit):
    subclass = None
    def __init__(self, value=0.0, unit=None, error=None, valueOf_=''):
        XSDataDoubleWithUnit.__init__(self, value, unit, error)
        self.valueOf_ = valueOf_
    def factory(*args_, **kwargs_):
        if XSDataLength.subclass:
            return XSDataLength.subclass(*args_, **kwargs_)
        else:
            return XSDataLength(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getValueOf_(self): return self.valueOf_
    def setValueOf_(self, valueOf_): self.valueOf_ = valueOf_
    def export(self, outfile, level, name_='XSDataLength'):
        showIndent(outfile, level)
        outfile.write('<%s>\n' % name_)
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='XSDataLength'):
        XSDataDoubleWithUnit.exportAttributes(self, outfile, level, name_='XSDataLength')
    def exportChildren(self, outfile, level, name_='XSDataLength'):
        XSDataDoubleWithUnit.exportChildren(self, outfile, level, name_)

    #Only to export the entire XML tree to a file stream on disk
    def outputFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write("<?xml version=\"1.0\" ?>\n")
        self.export( outfile, 0, name_='XSDataLength' )
        outfile.close()


    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataLength.factory()
        rootObj.build(rootNode)
        return rootObj
    parseString = staticmethod( parseString ) 


    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataLength.factory()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile ) 


    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO.StringIO()
        oStreamString.write('<?xml version="1.0" ?>\n')
        self.export( oStreamString, 0, name_="XSDataLength" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    def exportLiteral(self, outfile, level, name_='XSDataLength'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        pass
        XSDataDoubleWithUnit.exportLiteralAttributes(self, outfile, level, name_)
    def exportLiteralChildren(self, outfile, level, name_):
        showIndent(outfile, level)
        outfile.write('valueOf_ = "%s",\n' % (self.valueOf_,))
        XSDataDoubleWithUnit.exportLiteralChildren(self, outfile, level, name_)
    def build(self, node_):
        attrs = node_.attributes
        self.buildAttributes(attrs)
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildAttributes(self, attrs):
        XSDataDoubleWithUnit.buildAttributes(self, attrs)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.TEXT_NODE:
            self.valueOf_ += child_.nodeValue
        XSDataDoubleWithUnit.buildChildren(self, child_, nodeName_)
# end class XSDataLength


class XSDataLinearDisplacement(XSDataDisplacement):
    subclass = None
    def __init__(self, value=0.0, unit=None, error=None, valueOf_=''):
        XSDataDisplacement.__init__(self, value, unit, error)
        self.valueOf_ = valueOf_
    def factory(*args_, **kwargs_):
        if XSDataLinearDisplacement.subclass:
            return XSDataLinearDisplacement.subclass(*args_, **kwargs_)
        else:
            return XSDataLinearDisplacement(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getValueOf_(self): return self.valueOf_
    def setValueOf_(self, valueOf_): self.valueOf_ = valueOf_
    def export(self, outfile, level, name_='XSDataLinearDisplacement'):
        showIndent(outfile, level)
        outfile.write('<%s>\n' % name_)
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='XSDataLinearDisplacement'):
        XSDataDisplacement.exportAttributes(self, outfile, level, name_='XSDataLinearDisplacement')
    def exportChildren(self, outfile, level, name_='XSDataLinearDisplacement'):
        XSDataDisplacement.exportChildren(self, outfile, level, name_)

    #Only to export the entire XML tree to a file stream on disk
    def outputFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write("<?xml version=\"1.0\" ?>\n")
        self.export( outfile, 0, name_='XSDataLinearDisplacement' )
        outfile.close()


    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataLinearDisplacement.factory()
        rootObj.build(rootNode)
        return rootObj
    parseString = staticmethod( parseString ) 


    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataLinearDisplacement.factory()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile ) 


    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO.StringIO()
        oStreamString.write('<?xml version="1.0" ?>\n')
        self.export( oStreamString, 0, name_="XSDataLinearDisplacement" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    def exportLiteral(self, outfile, level, name_='XSDataLinearDisplacement'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        pass
        XSDataDisplacement.exportLiteralAttributes(self, outfile, level, name_)
    def exportLiteralChildren(self, outfile, level, name_):
        showIndent(outfile, level)
        outfile.write('valueOf_ = "%s",\n' % (self.valueOf_,))
        XSDataDisplacement.exportLiteralChildren(self, outfile, level, name_)
    def build(self, node_):
        attrs = node_.attributes
        self.buildAttributes(attrs)
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildAttributes(self, attrs):
        XSDataDisplacement.buildAttributes(self, attrs)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.TEXT_NODE:
            self.valueOf_ += child_.nodeValue
        XSDataDisplacement.buildChildren(self, child_, nodeName_)
# end class XSDataLinearDisplacement


class XSDataMatrixDouble(XSData):
    subclass = None
    def __init__(self, m11=0.0, m12=0.0, m13=0.0, m21=0.0, m22=0.0, m23=0.0, m31=0.0, m32=0.0, m33=0.0):
        XSData.__init__(self)
        self.m11 = m11
        self.m12 = m12
        self.m13 = m13
        self.m21 = m21
        self.m22 = m22
        self.m23 = m23
        self.m31 = m31
        self.m32 = m32
        self.m33 = m33
    def factory(*args_, **kwargs_):
        if XSDataMatrixDouble.subclass:
            return XSDataMatrixDouble.subclass(*args_, **kwargs_)
        else:
            return XSDataMatrixDouble(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getM11(self): return self.m11
    def setM11(self, m11): self.m11 = m11
    def getM12(self): return self.m12
    def setM12(self, m12): self.m12 = m12
    def getM13(self): return self.m13
    def setM13(self, m13): self.m13 = m13
    def getM21(self): return self.m21
    def setM21(self, m21): self.m21 = m21
    def getM22(self): return self.m22
    def setM22(self, m22): self.m22 = m22
    def getM23(self): return self.m23
    def setM23(self, m23): self.m23 = m23
    def getM31(self): return self.m31
    def setM31(self, m31): self.m31 = m31
    def getM32(self): return self.m32
    def setM32(self, m32): self.m32 = m32
    def getM33(self): return self.m33
    def setM33(self, m33): self.m33 = m33
    def export(self, outfile, level, name_='XSDataMatrixDouble'):
        showIndent(outfile, level)
        outfile.write('<%s>\n' % name_)
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='XSDataMatrixDouble'):
        XSData.exportAttributes(self, outfile, level, name_='XSDataMatrixDouble')
    def exportChildren(self, outfile, level, name_='XSDataMatrixDouble'):
        showIndent(outfile, level)
        outfile.write('<m11>%e</m11>\n' % self.getM11())
        showIndent(outfile, level)
        outfile.write('<m12>%e</m12>\n' % self.getM12())
        showIndent(outfile, level)
        outfile.write('<m13>%e</m13>\n' % self.getM13())
        showIndent(outfile, level)
        outfile.write('<m21>%e</m21>\n' % self.getM21())
        showIndent(outfile, level)
        outfile.write('<m22>%e</m22>\n' % self.getM22())
        showIndent(outfile, level)
        outfile.write('<m23>%e</m23>\n' % self.getM23())
        showIndent(outfile, level)
        outfile.write('<m31>%e</m31>\n' % self.getM31())
        showIndent(outfile, level)
        outfile.write('<m32>%e</m32>\n' % self.getM32())
        showIndent(outfile, level)
        outfile.write('<m33>%e</m33>\n' % self.getM33())
        XSData.exportChildren(self, outfile, level, name_)

    #Only to export the entire XML tree to a file stream on disk
    def outputFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write("<?xml version=\"1.0\" ?>\n")
        self.export( outfile, 0, name_='XSDataMatrixDouble' )
        outfile.close()


    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataMatrixDouble.factory()
        rootObj.build(rootNode)
        return rootObj
    parseString = staticmethod( parseString ) 


    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataMatrixDouble.factory()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile ) 


    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO.StringIO()
        oStreamString.write('<?xml version="1.0" ?>\n')
        self.export( oStreamString, 0, name_="XSDataMatrixDouble" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    def exportLiteral(self, outfile, level, name_='XSDataMatrixDouble'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        pass
        XSData.exportLiteralAttributes(self, outfile, level, name_)
    def exportLiteralChildren(self, outfile, level, name_):
        showIndent(outfile, level)
        outfile.write('m11=%e,\n' % self.getM11())
        showIndent(outfile, level)
        outfile.write('m12=%e,\n' % self.getM12())
        showIndent(outfile, level)
        outfile.write('m13=%e,\n' % self.getM13())
        showIndent(outfile, level)
        outfile.write('m21=%e,\n' % self.getM21())
        showIndent(outfile, level)
        outfile.write('m22=%e,\n' % self.getM22())
        showIndent(outfile, level)
        outfile.write('m23=%e,\n' % self.getM23())
        showIndent(outfile, level)
        outfile.write('m31=%e,\n' % self.getM31())
        showIndent(outfile, level)
        outfile.write('m32=%e,\n' % self.getM32())
        showIndent(outfile, level)
        outfile.write('m33=%e,\n' % self.getM33())
        XSData.exportLiteralChildren(self, outfile, level, name_)
    def build(self, node_):
        attrs = node_.attributes
        self.buildAttributes(attrs)
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildAttributes(self, attrs):
        XSData.buildAttributes(self, attrs)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'm11':
            if child_.firstChild:
                sval_ = child_.firstChild.nodeValue
                try:
                    fval_ = float(sval_)
                except ValueError:
                    raise ValueError('requires float (or double) -- %s' % child_.toxml())
                self.m11 = fval_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'm12':
            if child_.firstChild:
                sval_ = child_.firstChild.nodeValue
                try:
                    fval_ = float(sval_)
                except ValueError:
                    raise ValueError('requires float (or double) -- %s' % child_.toxml())
                self.m12 = fval_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'm13':
            if child_.firstChild:
                sval_ = child_.firstChild.nodeValue
                try:
                    fval_ = float(sval_)
                except ValueError:
                    raise ValueError('requires float (or double) -- %s' % child_.toxml())
                self.m13 = fval_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'm21':
            if child_.firstChild:
                sval_ = child_.firstChild.nodeValue
                try:
                    fval_ = float(sval_)
                except ValueError:
                    raise ValueError('requires float (or double) -- %s' % child_.toxml())
                self.m21 = fval_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'm22':
            if child_.firstChild:
                sval_ = child_.firstChild.nodeValue
                try:
                    fval_ = float(sval_)
                except ValueError:
                    raise ValueError('requires float (or double) -- %s' % child_.toxml())
                self.m22 = fval_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'm23':
            if child_.firstChild:
                sval_ = child_.firstChild.nodeValue
                try:
                    fval_ = float(sval_)
                except ValueError:
                    raise ValueError('requires float (or double) -- %s' % child_.toxml())
                self.m23 = fval_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'm31':
            if child_.firstChild:
                sval_ = child_.firstChild.nodeValue
                try:
                    fval_ = float(sval_)
                except ValueError:
                    raise ValueError('requires float (or double) -- %s' % child_.toxml())
                self.m31 = fval_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'm32':
            if child_.firstChild:
                sval_ = child_.firstChild.nodeValue
                try:
                    fval_ = float(sval_)
                except ValueError:
                    raise ValueError('requires float (or double) -- %s' % child_.toxml())
                self.m32 = fval_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'm33':
            if child_.firstChild:
                sval_ = child_.firstChild.nodeValue
                try:
                    fval_ = float(sval_)
                except ValueError:
                    raise ValueError('requires float (or double) -- %s' % child_.toxml())
                self.m33 = fval_
# end class XSDataMatrixDouble


class XSDataMatrixInteger(XSData):
    subclass = None
    def __init__(self, m11=-1, m12=-1, m13=-1, m21=-1, m22=-1, m23=-1, m31=-1, m32=-1, m33=-1):
        XSData.__init__(self)
        self.m11 = m11
        self.m12 = m12
        self.m13 = m13
        self.m21 = m21
        self.m22 = m22
        self.m23 = m23
        self.m31 = m31
        self.m32 = m32
        self.m33 = m33
    def factory(*args_, **kwargs_):
        if XSDataMatrixInteger.subclass:
            return XSDataMatrixInteger.subclass(*args_, **kwargs_)
        else:
            return XSDataMatrixInteger(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getM11(self): return self.m11
    def setM11(self, m11): self.m11 = m11
    def getM12(self): return self.m12
    def setM12(self, m12): self.m12 = m12
    def getM13(self): return self.m13
    def setM13(self, m13): self.m13 = m13
    def getM21(self): return self.m21
    def setM21(self, m21): self.m21 = m21
    def getM22(self): return self.m22
    def setM22(self, m22): self.m22 = m22
    def getM23(self): return self.m23
    def setM23(self, m23): self.m23 = m23
    def getM31(self): return self.m31
    def setM31(self, m31): self.m31 = m31
    def getM32(self): return self.m32
    def setM32(self, m32): self.m32 = m32
    def getM33(self): return self.m33
    def setM33(self, m33): self.m33 = m33
    def export(self, outfile, level, name_='XSDataMatrixInteger'):
        showIndent(outfile, level)
        outfile.write('<%s>\n' % name_)
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='XSDataMatrixInteger'):
        XSData.exportAttributes(self, outfile, level, name_='XSDataMatrixInteger')
    def exportChildren(self, outfile, level, name_='XSDataMatrixInteger'):
        showIndent(outfile, level)
        outfile.write('<m11>%d</m11>\n' % self.getM11())
        showIndent(outfile, level)
        outfile.write('<m12>%d</m12>\n' % self.getM12())
        showIndent(outfile, level)
        outfile.write('<m13>%d</m13>\n' % self.getM13())
        showIndent(outfile, level)
        outfile.write('<m21>%d</m21>\n' % self.getM21())
        showIndent(outfile, level)
        outfile.write('<m22>%d</m22>\n' % self.getM22())
        showIndent(outfile, level)
        outfile.write('<m23>%d</m23>\n' % self.getM23())
        showIndent(outfile, level)
        outfile.write('<m31>%d</m31>\n' % self.getM31())
        showIndent(outfile, level)
        outfile.write('<m32>%d</m32>\n' % self.getM32())
        showIndent(outfile, level)
        outfile.write('<m33>%d</m33>\n' % self.getM33())
        XSData.exportChildren(self, outfile, level, name_)

    #Only to export the entire XML tree to a file stream on disk
    def outputFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write("<?xml version=\"1.0\" ?>\n")
        self.export( outfile, 0, name_='XSDataMatrixInteger' )
        outfile.close()


    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataMatrixInteger.factory()
        rootObj.build(rootNode)
        return rootObj
    parseString = staticmethod( parseString ) 


    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataMatrixInteger.factory()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile ) 


    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO.StringIO()
        oStreamString.write('<?xml version="1.0" ?>\n')
        self.export( oStreamString, 0, name_="XSDataMatrixInteger" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    def exportLiteral(self, outfile, level, name_='XSDataMatrixInteger'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        pass
        XSData.exportLiteralAttributes(self, outfile, level, name_)
    def exportLiteralChildren(self, outfile, level, name_):
        showIndent(outfile, level)
        outfile.write('m11=%d,\n' % self.getM11())
        showIndent(outfile, level)
        outfile.write('m12=%d,\n' % self.getM12())
        showIndent(outfile, level)
        outfile.write('m13=%d,\n' % self.getM13())
        showIndent(outfile, level)
        outfile.write('m21=%d,\n' % self.getM21())
        showIndent(outfile, level)
        outfile.write('m22=%d,\n' % self.getM22())
        showIndent(outfile, level)
        outfile.write('m23=%d,\n' % self.getM23())
        showIndent(outfile, level)
        outfile.write('m31=%d,\n' % self.getM31())
        showIndent(outfile, level)
        outfile.write('m32=%d,\n' % self.getM32())
        showIndent(outfile, level)
        outfile.write('m33=%d,\n' % self.getM33())
        XSData.exportLiteralChildren(self, outfile, level, name_)
    def build(self, node_):
        attrs = node_.attributes
        self.buildAttributes(attrs)
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildAttributes(self, attrs):
        XSData.buildAttributes(self, attrs)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'm11':
            if child_.firstChild:
                sval_ = child_.firstChild.nodeValue
                try:
                    ival_ = int(sval_)
                except ValueError:
                    raise ValueError('requires integer -- %s' % child_.toxml())
                self.m11 = ival_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'm12':
            if child_.firstChild:
                sval_ = child_.firstChild.nodeValue
                try:
                    ival_ = int(sval_)
                except ValueError:
                    raise ValueError('requires integer -- %s' % child_.toxml())
                self.m12 = ival_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'm13':
            if child_.firstChild:
                sval_ = child_.firstChild.nodeValue
                try:
                    ival_ = int(sval_)
                except ValueError:
                    raise ValueError('requires integer -- %s' % child_.toxml())
                self.m13 = ival_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'm21':
            if child_.firstChild:
                sval_ = child_.firstChild.nodeValue
                try:
                    ival_ = int(sval_)
                except ValueError:
                    raise ValueError('requires integer -- %s' % child_.toxml())
                self.m21 = ival_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'm22':
            if child_.firstChild:
                sval_ = child_.firstChild.nodeValue
                try:
                    ival_ = int(sval_)
                except ValueError:
                    raise ValueError('requires integer -- %s' % child_.toxml())
                self.m22 = ival_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'm23':
            if child_.firstChild:
                sval_ = child_.firstChild.nodeValue
                try:
                    ival_ = int(sval_)
                except ValueError:
                    raise ValueError('requires integer -- %s' % child_.toxml())
                self.m23 = ival_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'm31':
            if child_.firstChild:
                sval_ = child_.firstChild.nodeValue
                try:
                    ival_ = int(sval_)
                except ValueError:
                    raise ValueError('requires integer -- %s' % child_.toxml())
                self.m31 = ival_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'm32':
            if child_.firstChild:
                sval_ = child_.firstChild.nodeValue
                try:
                    ival_ = int(sval_)
                except ValueError:
                    raise ValueError('requires integer -- %s' % child_.toxml())
                self.m32 = ival_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'm33':
            if child_.firstChild:
                sval_ = child_.firstChild.nodeValue
                try:
                    ival_ = int(sval_)
                except ValueError:
                    raise ValueError('requires integer -- %s' % child_.toxml())
                self.m33 = ival_
# end class XSDataMatrixInteger


class XSDataMessage(XSData):
    subclass = None
    def __init__(self, debuginfo=None, level=None, text=None, typexx=None):
        XSData.__init__(self)
        self.debuginfo = debuginfo
        self.level = level
        self.text = text
        self.typexx = typexx
    def factory(*args_, **kwargs_):
        if XSDataMessage.subclass:
            return XSDataMessage.subclass(*args_, **kwargs_)
        else:
            return XSDataMessage(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getDebuginfo(self): return self.debuginfo
    def setDebuginfo(self, debuginfo): self.debuginfo = debuginfo
    def getLevel(self): return self.level
    def setLevel(self, level): self.level = level
    def getText(self): return self.text
    def setText(self, text): self.text = text
    def getType(self): return self.typexx
    def setType(self, typexx): self.typexx = typexx
    def export(self, outfile, level, name_='XSDataMessage'):
        showIndent(outfile, level)
        outfile.write('<%s>\n' % name_)
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='XSDataMessage'):
        XSData.exportAttributes(self, outfile, level, name_='XSDataMessage')
    def exportChildren(self, outfile, level, name_='XSDataMessage'):
        if self.debuginfo:
            self.debuginfo.export(outfile, level, name_='debuginfo')
        if self.level:
            self.level.export(outfile, level, name_='level')
        if self.text:
            self.text.export(outfile, level, name_='text')
        if self.typexx:
            self.typexx.export(outfile, level, name_='type')
        XSData.exportChildren(self, outfile, level, name_)

    #Only to export the entire XML tree to a file stream on disk
    def outputFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write("<?xml version=\"1.0\" ?>\n")
        self.export( outfile, 0, name_='XSDataMessage' )
        outfile.close()


    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataMessage.factory()
        rootObj.build(rootNode)
        return rootObj
    parseString = staticmethod( parseString ) 


    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataMessage.factory()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile ) 


    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO.StringIO()
        oStreamString.write('<?xml version="1.0" ?>\n')
        self.export( oStreamString, 0, name_="XSDataMessage" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    def exportLiteral(self, outfile, level, name_='XSDataMessage'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        pass
        XSData.exportLiteralAttributes(self, outfile, level, name_)
    def exportLiteralChildren(self, outfile, level, name_):
        if self.debuginfo:
            showIndent(outfile, level)
            outfile.write('debuginfo=XSDataString(\n')
            self.debuginfo.exportLiteral(outfile, level, name_='debuginfo')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.level:
            showIndent(outfile, level)
            outfile.write('level=XSDataString(\n')
            self.level.exportLiteral(outfile, level, name_='level')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.text:
            showIndent(outfile, level)
            outfile.write('text=XSDataString(\n')
            self.text.exportLiteral(outfile, level, name_='text')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.typexx:
            showIndent(outfile, level)
            outfile.write('typexx=XSDataString(\n')
            self.typexx.exportLiteral(outfile, level, name_='type')
            showIndent(outfile, level)
            outfile.write('),\n')
        XSData.exportLiteralChildren(self, outfile, level, name_)
    def build(self, node_):
        attrs = node_.attributes
        self.buildAttributes(attrs)
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildAttributes(self, attrs):
        XSData.buildAttributes(self, attrs)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'debuginfo':
            obj_ = XSDataString.factory()
            obj_.build(child_)
            self.setDebuginfo(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'level':
            obj_ = XSDataString.factory()
            obj_.build(child_)
            self.setLevel(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'text':
            obj_ = XSDataString.factory()
            obj_.build(child_)
            self.setText(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'type':
            obj_ = XSDataString.factory()
            obj_.build(child_)
            self.setType(obj_)
# end class XSDataMessage


class XSDataResult(XSData):
    subclass = None
    def __init__(self, valueOf_=''):
        XSData.__init__(self)
        self.valueOf_ = valueOf_
    def factory(*args_, **kwargs_):
        if XSDataResult.subclass:
            return XSDataResult.subclass(*args_, **kwargs_)
        else:
            return XSDataResult(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getValueOf_(self): return self.valueOf_
    def setValueOf_(self, valueOf_): self.valueOf_ = valueOf_
    def export(self, outfile, level, name_='XSDataResult'):
        showIndent(outfile, level)
        outfile.write('<%s>' % name_)
        self.exportChildren(outfile, level + 1, name_)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='XSDataResult'):
        XSData.exportAttributes(self, outfile, level, name_='XSDataResult')
    def exportChildren(self, outfile, level, name_='XSDataResult'):
        XSData.exportChildren(self, outfile, level, name_)
        outfile.write(self.valueOf_)

    #Only to export the entire XML tree to a file stream on disk
    def outputFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write("<?xml version=\"1.0\" ?>\n")
        self.export( outfile, 0, name_='XSDataResult' )
        outfile.close()


    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataResult.factory()
        rootObj.build(rootNode)
        return rootObj
    parseString = staticmethod( parseString ) 


    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataResult.factory()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile ) 


    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO.StringIO()
        oStreamString.write('<?xml version="1.0" ?>\n')
        self.export( oStreamString, 0, name_="XSDataResult" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    def exportLiteral(self, outfile, level, name_='XSDataResult'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        pass
        XSData.exportLiteralAttributes(self, outfile, level, name_)
    def exportLiteralChildren(self, outfile, level, name_):
        showIndent(outfile, level)
        outfile.write('valueOf_ = "%s",\n' % (self.valueOf_,))
        XSData.exportLiteralChildren(self, outfile, level, name_)
    def build(self, node_):
        attrs = node_.attributes
        self.buildAttributes(attrs)
        self.valueOf_ = ''
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildAttributes(self, attrs):
        XSData.buildAttributes(self, attrs)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.TEXT_NODE:
            self.valueOf_ += child_.nodeValue
# end class XSDataResult


class XSDataRotation(XSData):
    subclass = None
    def __init__(self, q0=0.0, q1=0.0, q2=0.0, q3=0.0):
        XSData.__init__(self)
        self.q0 = q0
        self.q1 = q1
        self.q2 = q2
        self.q3 = q3
    def factory(*args_, **kwargs_):
        if XSDataRotation.subclass:
            return XSDataRotation.subclass(*args_, **kwargs_)
        else:
            return XSDataRotation(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getQ0(self): return self.q0
    def setQ0(self, q0): self.q0 = q0
    def getQ1(self): return self.q1
    def setQ1(self, q1): self.q1 = q1
    def getQ2(self): return self.q2
    def setQ2(self, q2): self.q2 = q2
    def getQ3(self): return self.q3
    def setQ3(self, q3): self.q3 = q3
    def export(self, outfile, level, name_='XSDataRotation'):
        showIndent(outfile, level)
        outfile.write('<%s>\n' % name_)
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='XSDataRotation'):
        XSData.exportAttributes(self, outfile, level, name_='XSDataRotation')
    def exportChildren(self, outfile, level, name_='XSDataRotation'):
        showIndent(outfile, level)
        outfile.write('<q0>%e</q0>\n' % self.getQ0())
        showIndent(outfile, level)
        outfile.write('<q1>%e</q1>\n' % self.getQ1())
        showIndent(outfile, level)
        outfile.write('<q2>%e</q2>\n' % self.getQ2())
        showIndent(outfile, level)
        outfile.write('<q3>%e</q3>\n' % self.getQ3())
        XSData.exportChildren(self, outfile, level, name_)

    #Only to export the entire XML tree to a file stream on disk
    def outputFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write("<?xml version=\"1.0\" ?>\n")
        self.export( outfile, 0, name_='XSDataRotation' )
        outfile.close()


    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataRotation.factory()
        rootObj.build(rootNode)
        return rootObj
    parseString = staticmethod( parseString ) 


    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataRotation.factory()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile ) 


    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO.StringIO()
        oStreamString.write('<?xml version="1.0" ?>\n')
        self.export( oStreamString, 0, name_="XSDataRotation" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    def exportLiteral(self, outfile, level, name_='XSDataRotation'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        pass
        XSData.exportLiteralAttributes(self, outfile, level, name_)
    def exportLiteralChildren(self, outfile, level, name_):
        showIndent(outfile, level)
        outfile.write('q0=%e,\n' % self.getQ0())
        showIndent(outfile, level)
        outfile.write('q1=%e,\n' % self.getQ1())
        showIndent(outfile, level)
        outfile.write('q2=%e,\n' % self.getQ2())
        showIndent(outfile, level)
        outfile.write('q3=%e,\n' % self.getQ3())
        XSData.exportLiteralChildren(self, outfile, level, name_)
    def build(self, node_):
        attrs = node_.attributes
        self.buildAttributes(attrs)
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildAttributes(self, attrs):
        XSData.buildAttributes(self, attrs)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'q0':
            if child_.firstChild:
                sval_ = child_.firstChild.nodeValue
                try:
                    fval_ = float(sval_)
                except ValueError:
                    raise ValueError('requires float (or double) -- %s' % child_.toxml())
                self.q0 = fval_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'q1':
            if child_.firstChild:
                sval_ = child_.firstChild.nodeValue
                try:
                    fval_ = float(sval_)
                except ValueError:
                    raise ValueError('requires float (or double) -- %s' % child_.toxml())
                self.q1 = fval_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'q2':
            if child_.firstChild:
                sval_ = child_.firstChild.nodeValue
                try:
                    fval_ = float(sval_)
                except ValueError:
                    raise ValueError('requires float (or double) -- %s' % child_.toxml())
                self.q2 = fval_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'q3':
            if child_.firstChild:
                sval_ = child_.firstChild.nodeValue
                try:
                    fval_ = float(sval_)
                except ValueError:
                    raise ValueError('requires float (or double) -- %s' % child_.toxml())
                self.q3 = fval_
# end class XSDataRotation


class XSDataSize(XSData):
    subclass = None
    def __init__(self, x=None, y=None, z=None):
        XSData.__init__(self)
        self.x = x
        self.y = y
        self.z = z
    def factory(*args_, **kwargs_):
        if XSDataSize.subclass:
            return XSDataSize.subclass(*args_, **kwargs_)
        else:
            return XSDataSize(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getX(self): return self.x
    def setX(self, x): self.x = x
    def getY(self): return self.y
    def setY(self, y): self.y = y
    def getZ(self): return self.z
    def setZ(self, z): self.z = z
    def export(self, outfile, level, name_='XSDataSize'):
        showIndent(outfile, level)
        outfile.write('<%s>\n' % name_)
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='XSDataSize'):
        XSData.exportAttributes(self, outfile, level, name_='XSDataSize')
    def exportChildren(self, outfile, level, name_='XSDataSize'):
        if self.x:
            self.x.export(outfile, level, name_='x')
        if self.y:
            self.y.export(outfile, level, name_='y')
        if self.z:
            self.z.export(outfile, level, name_='z')
        XSData.exportChildren(self, outfile, level, name_)

    #Only to export the entire XML tree to a file stream on disk
    def outputFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write("<?xml version=\"1.0\" ?>\n")
        self.export( outfile, 0, name_='XSDataSize' )
        outfile.close()


    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataSize.factory()
        rootObj.build(rootNode)
        return rootObj
    parseString = staticmethod( parseString ) 


    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataSize.factory()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile ) 


    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO.StringIO()
        oStreamString.write('<?xml version="1.0" ?>\n')
        self.export( oStreamString, 0, name_="XSDataSize" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    def exportLiteral(self, outfile, level, name_='XSDataSize'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        pass
        XSData.exportLiteralAttributes(self, outfile, level, name_)
    def exportLiteralChildren(self, outfile, level, name_):
        if self.x:
            showIndent(outfile, level)
            outfile.write('x=XSDataLength(\n')
            self.x.exportLiteral(outfile, level, name_='x')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.y:
            showIndent(outfile, level)
            outfile.write('y=XSDataLength(\n')
            self.y.exportLiteral(outfile, level, name_='y')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.z:
            showIndent(outfile, level)
            outfile.write('z=XSDataLength(\n')
            self.z.exportLiteral(outfile, level, name_='z')
            showIndent(outfile, level)
            outfile.write('),\n')
        XSData.exportLiteralChildren(self, outfile, level, name_)
    def build(self, node_):
        attrs = node_.attributes
        self.buildAttributes(attrs)
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildAttributes(self, attrs):
        XSData.buildAttributes(self, attrs)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'x':
            obj_ = XSDataLength.factory()
            obj_.build(child_)
            self.setX(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'y':
            obj_ = XSDataLength.factory()
            obj_.build(child_)
            self.setY(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'z':
            obj_ = XSDataLength.factory()
            obj_.build(child_)
            self.setZ(obj_)
# end class XSDataSize


class XSDataSpeed(XSDataDoubleWithUnit):
    subclass = None
    def __init__(self, value=0.0, unit=None, error=None, valueOf_=''):
        XSDataDoubleWithUnit.__init__(self, value, unit, error)
        self.valueOf_ = valueOf_
    def factory(*args_, **kwargs_):
        if XSDataSpeed.subclass:
            return XSDataSpeed.subclass(*args_, **kwargs_)
        else:
            return XSDataSpeed(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getValueOf_(self): return self.valueOf_
    def setValueOf_(self, valueOf_): self.valueOf_ = valueOf_
    def export(self, outfile, level, name_='XSDataSpeed'):
        showIndent(outfile, level)
        outfile.write('<%s>\n' % name_)
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='XSDataSpeed'):
        XSDataDoubleWithUnit.exportAttributes(self, outfile, level, name_='XSDataSpeed')
    def exportChildren(self, outfile, level, name_='XSDataSpeed'):
        XSDataDoubleWithUnit.exportChildren(self, outfile, level, name_)

    #Only to export the entire XML tree to a file stream on disk
    def outputFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write("<?xml version=\"1.0\" ?>\n")
        self.export( outfile, 0, name_='XSDataSpeed' )
        outfile.close()


    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataSpeed.factory()
        rootObj.build(rootNode)
        return rootObj
    parseString = staticmethod( parseString ) 


    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataSpeed.factory()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile ) 


    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO.StringIO()
        oStreamString.write('<?xml version="1.0" ?>\n')
        self.export( oStreamString, 0, name_="XSDataSpeed" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    def exportLiteral(self, outfile, level, name_='XSDataSpeed'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        pass
        XSDataDoubleWithUnit.exportLiteralAttributes(self, outfile, level, name_)
    def exportLiteralChildren(self, outfile, level, name_):
        showIndent(outfile, level)
        outfile.write('valueOf_ = "%s",\n' % (self.valueOf_,))
        XSDataDoubleWithUnit.exportLiteralChildren(self, outfile, level, name_)
    def build(self, node_):
        attrs = node_.attributes
        self.buildAttributes(attrs)
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildAttributes(self, attrs):
        XSDataDoubleWithUnit.buildAttributes(self, attrs)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.TEXT_NODE:
            self.valueOf_ += child_.nodeValue
        XSDataDoubleWithUnit.buildChildren(self, child_, nodeName_)
# end class XSDataSpeed


class XSDataStatus(XSData):
    subclass = None
    def __init__(self, executiveSummary=None, isSuccess=None, executionInfo=None):
        XSData.__init__(self)
        self.executiveSummary = executiveSummary
        self.isSuccess = isSuccess
        self.executionInfo = executionInfo
    def factory(*args_, **kwargs_):
        if XSDataStatus.subclass:
            return XSDataStatus.subclass(*args_, **kwargs_)
        else:
            return XSDataStatus(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getExecutiveSummary(self): return self.executiveSummary
    def setExecutiveSummary(self, executiveSummary): self.executiveSummary = executiveSummary
    def getIsSuccess(self): return self.isSuccess
    def setIsSuccess(self, isSuccess): self.isSuccess = isSuccess
    def getExecutionInfo(self): return self.executionInfo
    def setExecutionInfo(self, executionInfo): self.executionInfo = executionInfo
    def export(self, outfile, level, name_='XSDataStatus'):
        showIndent(outfile, level)
        outfile.write('<%s>\n' % name_)
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='XSDataStatus'):
        XSData.exportAttributes(self, outfile, level, name_='XSDataStatus')
    def exportChildren(self, outfile, level, name_='XSDataStatus'):
        if self.getExecutiveSummary() != None :
            if self.executiveSummary:
                self.executiveSummary.export(outfile, level, name_='executiveSummary')
        if self.isSuccess:
            self.isSuccess.export(outfile, level, name_='isSuccess')
        if self.getExecutionInfo() != None :
            if self.executionInfo:
                self.executionInfo.export(outfile, level, name_='executionInfo')
        XSData.exportChildren(self, outfile, level, name_)

    #Only to export the entire XML tree to a file stream on disk
    def outputFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write("<?xml version=\"1.0\" ?>\n")
        self.export( outfile, 0, name_='XSDataStatus' )
        outfile.close()


    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataStatus.factory()
        rootObj.build(rootNode)
        return rootObj
    parseString = staticmethod( parseString ) 


    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataStatus.factory()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile ) 


    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO.StringIO()
        oStreamString.write('<?xml version="1.0" ?>\n')
        self.export( oStreamString, 0, name_="XSDataStatus" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    def exportLiteral(self, outfile, level, name_='XSDataStatus'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        pass
        XSData.exportLiteralAttributes(self, outfile, level, name_)
    def exportLiteralChildren(self, outfile, level, name_):
        if self.executiveSummary:
            showIndent(outfile, level)
            outfile.write('executiveSummary=XSDataString(\n')
            self.executiveSummary.exportLiteral(outfile, level, name_='executiveSummary')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.isSuccess:
            showIndent(outfile, level)
            outfile.write('isSuccess=XSDataBoolean(\n')
            self.isSuccess.exportLiteral(outfile, level, name_='isSuccess')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.executionInfo:
            showIndent(outfile, level)
            outfile.write('executionInfo=XSDataExecutionInfo(\n')
            self.executionInfo.exportLiteral(outfile, level, name_='executionInfo')
            showIndent(outfile, level)
            outfile.write('),\n')
        XSData.exportLiteralChildren(self, outfile, level, name_)
    def build(self, node_):
        attrs = node_.attributes
        self.buildAttributes(attrs)
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildAttributes(self, attrs):
        XSData.buildAttributes(self, attrs)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'executiveSummary':
            obj_ = XSDataString.factory()
            obj_.build(child_)
            self.setExecutiveSummary(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'isSuccess':
            obj_ = XSDataBoolean.factory()
            obj_.build(child_)
            self.setIsSuccess(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'executionInfo':
            obj_ = XSDataExecutionInfo.factory()
            obj_.build(child_)
            self.setExecutionInfo(obj_)
# end class XSDataStatus


class XSDataString(XSData):
    subclass = None
    def __init__(self, value=''):
        XSData.__init__(self)
        self.value = value
    def factory(*args_, **kwargs_):
        if XSDataString.subclass:
            return XSDataString.subclass(*args_, **kwargs_)
        else:
            return XSDataString(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getValue(self): return self.value
    def setValue(self, value): self.value = value
    def export(self, outfile, level, name_='XSDataString'):
        showIndent(outfile, level)
        outfile.write('<%s>\n' % name_)
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='XSDataString'):
        XSData.exportAttributes(self, outfile, level, name_='XSDataString')
    def exportChildren(self, outfile, level, name_='XSDataString'):
        showIndent(outfile, level)
        outfile.write('<value>%s</value>\n' % quote_xml(self.getValue()))
        XSData.exportChildren(self, outfile, level, name_)

    #Only to export the entire XML tree to a file stream on disk
    def outputFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write("<?xml version=\"1.0\" ?>\n")
        self.export( outfile, 0, name_='XSDataString' )
        outfile.close()


    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataString.factory()
        rootObj.build(rootNode)
        return rootObj
    parseString = staticmethod( parseString ) 


    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataString.factory()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile ) 


    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO.StringIO()
        oStreamString.write('<?xml version="1.0" ?>\n')
        self.export( oStreamString, 0, name_="XSDataString" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    def exportLiteral(self, outfile, level, name_='XSDataString'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        pass
        XSData.exportLiteralAttributes(self, outfile, level, name_)
    def exportLiteralChildren(self, outfile, level, name_):
        showIndent(outfile, level)
        outfile.write('value=%s,\n' % quote_python(self.getValue()))
        XSData.exportLiteralChildren(self, outfile, level, name_)
    def build(self, node_):
        attrs = node_.attributes
        self.buildAttributes(attrs)
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildAttributes(self, attrs):
        XSData.buildAttributes(self, attrs)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'value':
            value_ = ''
            for text__content_ in child_.childNodes:
                value_ += text__content_.nodeValue
            self.value = value_
# end class XSDataString


class XSDataSysteminfo(XSData):
    subclass = None
    def __init__(self, compiler=None, hostIP=None, hostName=None, operatingSystem=None, operatingSystemType=None, userName=None, virtualMachine=None):
        XSData.__init__(self)
        self.compiler = compiler
        self.hostIP = hostIP
        self.hostName = hostName
        self.operatingSystem = operatingSystem
        self.operatingSystemType = operatingSystemType
        self.userName = userName
        self.virtualMachine = virtualMachine
    def factory(*args_, **kwargs_):
        if XSDataSysteminfo.subclass:
            return XSDataSysteminfo.subclass(*args_, **kwargs_)
        else:
            return XSDataSysteminfo(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getCompiler(self): return self.compiler
    def setCompiler(self, compiler): self.compiler = compiler
    def getHostIP(self): return self.hostIP
    def setHostIP(self, hostIP): self.hostIP = hostIP
    def getHostName(self): return self.hostName
    def setHostName(self, hostName): self.hostName = hostName
    def getOperatingSystem(self): return self.operatingSystem
    def setOperatingSystem(self, operatingSystem): self.operatingSystem = operatingSystem
    def getOperatingSystemType(self): return self.operatingSystemType
    def setOperatingSystemType(self, operatingSystemType): self.operatingSystemType = operatingSystemType
    def getUserName(self): return self.userName
    def setUserName(self, userName): self.userName = userName
    def getVirtualMachine(self): return self.virtualMachine
    def setVirtualMachine(self, virtualMachine): self.virtualMachine = virtualMachine
    def export(self, outfile, level, name_='XSDataSysteminfo'):
        showIndent(outfile, level)
        outfile.write('<%s>\n' % name_)
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='XSDataSysteminfo'):
        XSData.exportAttributes(self, outfile, level, name_='XSDataSysteminfo')
    def exportChildren(self, outfile, level, name_='XSDataSysteminfo'):
        if self.compiler:
            self.compiler.export(outfile, level, name_='compiler')
        if self.hostIP:
            self.hostIP.export(outfile, level, name_='hostIP')
        if self.hostName:
            self.hostName.export(outfile, level, name_='hostName')
        if self.operatingSystem:
            self.operatingSystem.export(outfile, level, name_='operatingSystem')
        if self.operatingSystemType:
            self.operatingSystemType.export(outfile, level, name_='operatingSystemType')
        if self.userName:
            self.userName.export(outfile, level, name_='userName')
        if self.virtualMachine:
            self.virtualMachine.export(outfile, level, name_='virtualMachine')
        XSData.exportChildren(self, outfile, level, name_)

    #Only to export the entire XML tree to a file stream on disk
    def outputFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write("<?xml version=\"1.0\" ?>\n")
        self.export( outfile, 0, name_='XSDataSysteminfo' )
        outfile.close()


    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataSysteminfo.factory()
        rootObj.build(rootNode)
        return rootObj
    parseString = staticmethod( parseString ) 


    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataSysteminfo.factory()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile ) 


    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO.StringIO()
        oStreamString.write('<?xml version="1.0" ?>\n')
        self.export( oStreamString, 0, name_="XSDataSysteminfo" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    def exportLiteral(self, outfile, level, name_='XSDataSysteminfo'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        pass
        XSData.exportLiteralAttributes(self, outfile, level, name_)
    def exportLiteralChildren(self, outfile, level, name_):
        if self.compiler:
            showIndent(outfile, level)
            outfile.write('compiler=XSDataString(\n')
            self.compiler.exportLiteral(outfile, level, name_='compiler')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.hostIP:
            showIndent(outfile, level)
            outfile.write('hostIP=XSDataString(\n')
            self.hostIP.exportLiteral(outfile, level, name_='hostIP')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.hostName:
            showIndent(outfile, level)
            outfile.write('hostName=XSDataString(\n')
            self.hostName.exportLiteral(outfile, level, name_='hostName')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.operatingSystem:
            showIndent(outfile, level)
            outfile.write('operatingSystem=XSDataString(\n')
            self.operatingSystem.exportLiteral(outfile, level, name_='operatingSystem')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.operatingSystemType:
            showIndent(outfile, level)
            outfile.write('operatingSystemType=XSDataString(\n')
            self.operatingSystemType.exportLiteral(outfile, level, name_='operatingSystemType')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.userName:
            showIndent(outfile, level)
            outfile.write('userName=XSDataString(\n')
            self.userName.exportLiteral(outfile, level, name_='userName')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.virtualMachine:
            showIndent(outfile, level)
            outfile.write('virtualMachine=XSDataString(\n')
            self.virtualMachine.exportLiteral(outfile, level, name_='virtualMachine')
            showIndent(outfile, level)
            outfile.write('),\n')
        XSData.exportLiteralChildren(self, outfile, level, name_)
    def build(self, node_):
        attrs = node_.attributes
        self.buildAttributes(attrs)
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildAttributes(self, attrs):
        XSData.buildAttributes(self, attrs)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'compiler':
            obj_ = XSDataString.factory()
            obj_.build(child_)
            self.setCompiler(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'hostIP':
            obj_ = XSDataString.factory()
            obj_.build(child_)
            self.setHostIP(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'hostName':
            obj_ = XSDataString.factory()
            obj_.build(child_)
            self.setHostName(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'operatingSystem':
            obj_ = XSDataString.factory()
            obj_.build(child_)
            self.setOperatingSystem(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'operatingSystemType':
            obj_ = XSDataString.factory()
            obj_.build(child_)
            self.setOperatingSystemType(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'userName':
            obj_ = XSDataString.factory()
            obj_.build(child_)
            self.setUserName(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'virtualMachine':
            obj_ = XSDataString.factory()
            obj_.build(child_)
            self.setVirtualMachine(obj_)
# end class XSDataSysteminfo


class XSDataTime(XSDataDoubleWithUnit):
    subclass = None
    def __init__(self, value=0.0, unit=None, error=None, valueOf_=''):
        XSDataDoubleWithUnit.__init__(self, value, unit, error)
        self.valueOf_ = valueOf_
    def factory(*args_, **kwargs_):
        if XSDataTime.subclass:
            return XSDataTime.subclass(*args_, **kwargs_)
        else:
            return XSDataTime(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getValueOf_(self): return self.valueOf_
    def setValueOf_(self, valueOf_): self.valueOf_ = valueOf_
    def export(self, outfile, level, name_='XSDataTime'):
        showIndent(outfile, level)
        outfile.write('<%s>\n' % name_)
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='XSDataTime'):
        XSDataDoubleWithUnit.exportAttributes(self, outfile, level, name_='XSDataTime')
    def exportChildren(self, outfile, level, name_='XSDataTime'):
        XSDataDoubleWithUnit.exportChildren(self, outfile, level, name_)

    #Only to export the entire XML tree to a file stream on disk
    def outputFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write("<?xml version=\"1.0\" ?>\n")
        self.export( outfile, 0, name_='XSDataTime' )
        outfile.close()


    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataTime.factory()
        rootObj.build(rootNode)
        return rootObj
    parseString = staticmethod( parseString ) 


    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataTime.factory()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile ) 


    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO.StringIO()
        oStreamString.write('<?xml version="1.0" ?>\n')
        self.export( oStreamString, 0, name_="XSDataTime" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    def exportLiteral(self, outfile, level, name_='XSDataTime'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        pass
        XSDataDoubleWithUnit.exportLiteralAttributes(self, outfile, level, name_)
    def exportLiteralChildren(self, outfile, level, name_):
        showIndent(outfile, level)
        outfile.write('valueOf_ = "%s",\n' % (self.valueOf_,))
        XSDataDoubleWithUnit.exportLiteralChildren(self, outfile, level, name_)
    def build(self, node_):
        attrs = node_.attributes
        self.buildAttributes(attrs)
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildAttributes(self, attrs):
        XSDataDoubleWithUnit.buildAttributes(self, attrs)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.TEXT_NODE:
            self.valueOf_ += child_.nodeValue
        XSDataDoubleWithUnit.buildChildren(self, child_, nodeName_)
# end class XSDataTime


class XSDataVectorDouble(XSData):
    subclass = None
    def __init__(self, v1=0.0, v2=0.0, v3=0.0):
        XSData.__init__(self)
        self.v1 = v1
        self.v2 = v2
        self.v3 = v3
    def factory(*args_, **kwargs_):
        if XSDataVectorDouble.subclass:
            return XSDataVectorDouble.subclass(*args_, **kwargs_)
        else:
            return XSDataVectorDouble(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getV1(self): return self.v1
    def setV1(self, v1): self.v1 = v1
    def getV2(self): return self.v2
    def setV2(self, v2): self.v2 = v2
    def getV3(self): return self.v3
    def setV3(self, v3): self.v3 = v3
    def export(self, outfile, level, name_='XSDataVectorDouble'):
        showIndent(outfile, level)
        outfile.write('<%s>\n' % name_)
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='XSDataVectorDouble'):
        XSData.exportAttributes(self, outfile, level, name_='XSDataVectorDouble')
    def exportChildren(self, outfile, level, name_='XSDataVectorDouble'):
        showIndent(outfile, level)
        outfile.write('<v1>%e</v1>\n' % self.getV1())
        showIndent(outfile, level)
        outfile.write('<v2>%e</v2>\n' % self.getV2())
        showIndent(outfile, level)
        outfile.write('<v3>%e</v3>\n' % self.getV3())
        XSData.exportChildren(self, outfile, level, name_)

    #Only to export the entire XML tree to a file stream on disk
    def outputFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write("<?xml version=\"1.0\" ?>\n")
        self.export( outfile, 0, name_='XSDataVectorDouble' )
        outfile.close()


    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataVectorDouble.factory()
        rootObj.build(rootNode)
        return rootObj
    parseString = staticmethod( parseString ) 


    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataVectorDouble.factory()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile ) 


    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO.StringIO()
        oStreamString.write('<?xml version="1.0" ?>\n')
        self.export( oStreamString, 0, name_="XSDataVectorDouble" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    def exportLiteral(self, outfile, level, name_='XSDataVectorDouble'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        pass
        XSData.exportLiteralAttributes(self, outfile, level, name_)
    def exportLiteralChildren(self, outfile, level, name_):
        showIndent(outfile, level)
        outfile.write('v1=%e,\n' % self.getV1())
        showIndent(outfile, level)
        outfile.write('v2=%e,\n' % self.getV2())
        showIndent(outfile, level)
        outfile.write('v3=%e,\n' % self.getV3())
        XSData.exportLiteralChildren(self, outfile, level, name_)
    def build(self, node_):
        attrs = node_.attributes
        self.buildAttributes(attrs)
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildAttributes(self, attrs):
        XSData.buildAttributes(self, attrs)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'v1':
            if child_.firstChild:
                sval_ = child_.firstChild.nodeValue
                try:
                    fval_ = float(sval_)
                except ValueError:
                    raise ValueError('requires float (or double) -- %s' % child_.toxml())
                self.v1 = fval_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'v2':
            if child_.firstChild:
                sval_ = child_.firstChild.nodeValue
                try:
                    fval_ = float(sval_)
                except ValueError:
                    raise ValueError('requires float (or double) -- %s' % child_.toxml())
                self.v2 = fval_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'v3':
            if child_.firstChild:
                sval_ = child_.firstChild.nodeValue
                try:
                    fval_ = float(sval_)
                except ValueError:
                    raise ValueError('requires float (or double) -- %s' % child_.toxml())
                self.v3 = fval_
# end class XSDataVectorDouble


class XSDataVectorInteger(XSData):
    subclass = None
    def __init__(self, v1=-1, v2=-1, v3=-1):
        XSData.__init__(self)
        self.v1 = v1
        self.v2 = v2
        self.v3 = v3
    def factory(*args_, **kwargs_):
        if XSDataVectorInteger.subclass:
            return XSDataVectorInteger.subclass(*args_, **kwargs_)
        else:
            return XSDataVectorInteger(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getV1(self): return self.v1
    def setV1(self, v1): self.v1 = v1
    def getV2(self): return self.v2
    def setV2(self, v2): self.v2 = v2
    def getV3(self): return self.v3
    def setV3(self, v3): self.v3 = v3
    def export(self, outfile, level, name_='XSDataVectorInteger'):
        showIndent(outfile, level)
        outfile.write('<%s>\n' % name_)
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='XSDataVectorInteger'):
        XSData.exportAttributes(self, outfile, level, name_='XSDataVectorInteger')
    def exportChildren(self, outfile, level, name_='XSDataVectorInteger'):
        showIndent(outfile, level)
        outfile.write('<v1>%d</v1>\n' % self.getV1())
        showIndent(outfile, level)
        outfile.write('<v2>%d</v2>\n' % self.getV2())
        showIndent(outfile, level)
        outfile.write('<v3>%d</v3>\n' % self.getV3())
        XSData.exportChildren(self, outfile, level, name_)

    #Only to export the entire XML tree to a file stream on disk
    def outputFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write("<?xml version=\"1.0\" ?>\n")
        self.export( outfile, 0, name_='XSDataVectorInteger' )
        outfile.close()


    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataVectorInteger.factory()
        rootObj.build(rootNode)
        return rootObj
    parseString = staticmethod( parseString ) 


    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataVectorInteger.factory()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile ) 


    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO.StringIO()
        oStreamString.write('<?xml version="1.0" ?>\n')
        self.export( oStreamString, 0, name_="XSDataVectorInteger" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    def exportLiteral(self, outfile, level, name_='XSDataVectorInteger'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        pass
        XSData.exportLiteralAttributes(self, outfile, level, name_)
    def exportLiteralChildren(self, outfile, level, name_):
        showIndent(outfile, level)
        outfile.write('v1=%d,\n' % self.getV1())
        showIndent(outfile, level)
        outfile.write('v2=%d,\n' % self.getV2())
        showIndent(outfile, level)
        outfile.write('v3=%d,\n' % self.getV3())
        XSData.exportLiteralChildren(self, outfile, level, name_)
    def build(self, node_):
        attrs = node_.attributes
        self.buildAttributes(attrs)
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildAttributes(self, attrs):
        XSData.buildAttributes(self, attrs)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'v1':
            if child_.firstChild:
                sval_ = child_.firstChild.nodeValue
                try:
                    ival_ = int(sval_)
                except ValueError:
                    raise ValueError('requires integer -- %s' % child_.toxml())
                self.v1 = ival_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'v2':
            if child_.firstChild:
                sval_ = child_.firstChild.nodeValue
                try:
                    ival_ = int(sval_)
                except ValueError:
                    raise ValueError('requires integer -- %s' % child_.toxml())
                self.v2 = ival_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'v3':
            if child_.firstChild:
                sval_ = child_.firstChild.nodeValue
                try:
                    ival_ = int(sval_)
                except ValueError:
                    raise ValueError('requires integer -- %s' % child_.toxml())
                self.v3 = ival_
# end class XSDataVectorInteger


class XSDataWavelength(XSDataDoubleWithUnit):
    subclass = None
    def __init__(self, value=0.0, unit=None, error=None, valueOf_=''):
        XSDataDoubleWithUnit.__init__(self, value, unit, error)
        self.valueOf_ = valueOf_
    def factory(*args_, **kwargs_):
        if XSDataWavelength.subclass:
            return XSDataWavelength.subclass(*args_, **kwargs_)
        else:
            return XSDataWavelength(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getValueOf_(self): return self.valueOf_
    def setValueOf_(self, valueOf_): self.valueOf_ = valueOf_
    def export(self, outfile, level, name_='XSDataWavelength'):
        showIndent(outfile, level)
        outfile.write('<%s>\n' % name_)
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='XSDataWavelength'):
        XSDataDoubleWithUnit.exportAttributes(self, outfile, level, name_='XSDataWavelength')
    def exportChildren(self, outfile, level, name_='XSDataWavelength'):
        XSDataDoubleWithUnit.exportChildren(self, outfile, level, name_)

    #Only to export the entire XML tree to a file stream on disk
    def outputFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write("<?xml version=\"1.0\" ?>\n")
        self.export( outfile, 0, name_='XSDataWavelength' )
        outfile.close()


    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataWavelength.factory()
        rootObj.build(rootNode)
        return rootObj
    parseString = staticmethod( parseString ) 


    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataWavelength.factory()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile ) 


    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO.StringIO()
        oStreamString.write('<?xml version="1.0" ?>\n')
        self.export( oStreamString, 0, name_="XSDataWavelength" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    def exportLiteral(self, outfile, level, name_='XSDataWavelength'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        pass
        XSDataDoubleWithUnit.exportLiteralAttributes(self, outfile, level, name_)
    def exportLiteralChildren(self, outfile, level, name_):
        showIndent(outfile, level)
        outfile.write('valueOf_ = "%s",\n' % (self.valueOf_,))
        XSDataDoubleWithUnit.exportLiteralChildren(self, outfile, level, name_)
    def build(self, node_):
        attrs = node_.attributes
        self.buildAttributes(attrs)
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildAttributes(self, attrs):
        XSDataDoubleWithUnit.buildAttributes(self, attrs)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.TEXT_NODE:
            self.valueOf_ += child_.nodeValue
        XSDataDoubleWithUnit.buildChildren(self, child_, nodeName_)
# end class XSDataWavelength


class XSOptionItem:
    subclass = None
    def __init__(self, enabled=0, name=''):
        self.enabled = enabled
        self.name = name
    def factory(*args_, **kwargs_):
        if XSOptionItem.subclass:
            return XSOptionItem.subclass(*args_, **kwargs_)
        else:
            return XSOptionItem(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getEnabled(self): return self.enabled
    def setEnabled(self, enabled): self.enabled = enabled
    def getName(self): return self.name
    def setName(self, name): self.name = name
    def export(self, outfile, level, name_='XSOptionItem'):
        showIndent(outfile, level)
        outfile.write('<%s>\n' % name_)
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='XSOptionItem'):
        pass
    def exportChildren(self, outfile, level, name_='XSOptionItem'):
        showIndent(outfile, level)
        outfile.write('<enabled>%d</enabled>\n' % self.getEnabled())
        showIndent(outfile, level)
        outfile.write('<name>%s</name>\n' % quote_xml(self.getName()))

    #Only to export the entire XML tree to a file stream on disk
    def outputFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write("<?xml version=\"1.0\" ?>\n")
        self.export( outfile, 0, name_='XSOptionItem' )
        outfile.close()


    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSOptionItem.factory()
        rootObj.build(rootNode)
        return rootObj
    parseString = staticmethod( parseString ) 


    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSOptionItem.factory()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile ) 


    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO.StringIO()
        oStreamString.write('<?xml version="1.0" ?>\n')
        self.export( oStreamString, 0, name_="XSOptionItem" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    def exportLiteral(self, outfile, level, name_='XSOptionItem'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        pass
    def exportLiteralChildren(self, outfile, level, name_):
        showIndent(outfile, level)
        outfile.write('enabled=%d,\n' % self.getEnabled())
        showIndent(outfile, level)
        outfile.write('name=%s,\n' % quote_python(self.getName()))
    def build(self, node_):
        attrs = node_.attributes
        self.buildAttributes(attrs)
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildAttributes(self, attrs):
        pass
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'enabled':
            if child_.firstChild:
                sval_ = child_.firstChild.nodeValue
                if sval_ in ('true', '1'):
                    ival_ = 1
                elif sval_ in ('false', '0'):
                    ival_ = 0
                else:
                    raise ValueError('requires boolean -- %s' % child_.toxml())
                self.enabled = ival_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'name':
            name_ = ''
            for text__content_ in child_.childNodes:
                name_ += text__content_.nodeValue
            self.name = name_
# end class XSOptionItem


class XSOptionList:
    subclass = None
    def __init__(self, XSOptionItem=None):
        if XSOptionItem is None:
            self.XSOptionItem = []
        else:
            self.XSOptionItem = XSOptionItem
    def factory(*args_, **kwargs_):
        if XSOptionList.subclass:
            return XSOptionList.subclass(*args_, **kwargs_)
        else:
            return XSOptionList(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getXSOptionItem(self): return self.XSOptionItem
    def setXSOptionItem(self, XSOptionItem): self.XSOptionItem = XSOptionItem
    def addXSOptionItem(self, value): self.XSOptionItem.append(value)
    def insertXSOptionItem(self, index, value): self.XSOptionItem[index] = value
    def export(self, outfile, level, name_='XSOptionList'):
        showIndent(outfile, level)
        outfile.write('<%s>\n' % name_)
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='XSOptionList'):
        pass
    def exportChildren(self, outfile, level, name_='XSOptionList'):
        for XSOptionItem_ in self.getXSOptionItem():
            XSOptionItem_.export(outfile, level)

    #Only to export the entire XML tree to a file stream on disk
    def outputFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write("<?xml version=\"1.0\" ?>\n")
        self.export( outfile, 0, name_='XSOptionList' )
        outfile.close()


    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSOptionList.factory()
        rootObj.build(rootNode)
        return rootObj
    parseString = staticmethod( parseString ) 


    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSOptionList.factory()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile ) 


    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO.StringIO()
        oStreamString.write('<?xml version="1.0" ?>\n')
        self.export( oStreamString, 0, name_="XSOptionList" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    def exportLiteral(self, outfile, level, name_='XSOptionList'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        pass
    def exportLiteralChildren(self, outfile, level, name_):
        showIndent(outfile, level)
        outfile.write('XSOptionItem=[\n')
        level += 1
        for XSOptionItem in self.XSOptionItem:
            showIndent(outfile, level)
            outfile.write('XSOptionItem(\n')
            XSOptionItem.exportLiteral(outfile, level)
            showIndent(outfile, level)
            outfile.write('),\n')
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
    def build(self, node_):
        attrs = node_.attributes
        self.buildAttributes(attrs)
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildAttributes(self, attrs):
        pass
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'XSOptionItem':
            obj_ = XSOptionItem.factory()
            obj_.build(child_)
            self.XSOptionItem.append(obj_)
# end class XSOptionList


class XSParamItem:
    subclass = None
    def __init__(self, name='', value=''):
        self.name = name
        self.value = value
    def factory(*args_, **kwargs_):
        if XSParamItem.subclass:
            return XSParamItem.subclass(*args_, **kwargs_)
        else:
            return XSParamItem(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getName(self): return self.name
    def setName(self, name): self.name = name
    def getValue(self): return self.value
    def setValue(self, value): self.value = value
    def export(self, outfile, level, name_='XSParamItem'):
        showIndent(outfile, level)
        outfile.write('<%s>\n' % name_)
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='XSParamItem'):
        pass
    def exportChildren(self, outfile, level, name_='XSParamItem'):
        showIndent(outfile, level)
        outfile.write('<name>%s</name>\n' % quote_xml(self.getName()))
        showIndent(outfile, level)
        outfile.write('<value>%s</value>\n' % quote_xml(self.getValue()))

    #Only to export the entire XML tree to a file stream on disk
    def outputFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write("<?xml version=\"1.0\" ?>\n")
        self.export( outfile, 0, name_='XSParamItem' )
        outfile.close()


    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSParamItem.factory()
        rootObj.build(rootNode)
        return rootObj
    parseString = staticmethod( parseString ) 


    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSParamItem.factory()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile ) 


    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO.StringIO()
        oStreamString.write('<?xml version="1.0" ?>\n')
        self.export( oStreamString, 0, name_="XSParamItem" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    def exportLiteral(self, outfile, level, name_='XSParamItem'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        pass
    def exportLiteralChildren(self, outfile, level, name_):
        showIndent(outfile, level)
        outfile.write('name=%s,\n' % quote_python(self.getName()))
        showIndent(outfile, level)
        outfile.write('value=%s,\n' % quote_python(self.getValue()))
    def build(self, node_):
        attrs = node_.attributes
        self.buildAttributes(attrs)
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildAttributes(self, attrs):
        pass
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'name':
            name_ = ''
            for text__content_ in child_.childNodes:
                name_ += text__content_.nodeValue
            self.name = name_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'value':
            value_ = ''
            for text__content_ in child_.childNodes:
                value_ += text__content_.nodeValue
            self.value = value_
# end class XSParamItem


class XSParamList:
    subclass = None
    def __init__(self, XSParamItem=None):
        if XSParamItem is None:
            self.XSParamItem = []
        else:
            self.XSParamItem = XSParamItem
    def factory(*args_, **kwargs_):
        if XSParamList.subclass:
            return XSParamList.subclass(*args_, **kwargs_)
        else:
            return XSParamList(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getXSParamItem(self): return self.XSParamItem
    def setXSParamItem(self, XSParamItem): self.XSParamItem = XSParamItem
    def addXSParamItem(self, value): self.XSParamItem.append(value)
    def insertXSParamItem(self, index, value): self.XSParamItem[index] = value
    def export(self, outfile, level, name_='XSParamList'):
        showIndent(outfile, level)
        outfile.write('<%s>\n' % name_)
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='XSParamList'):
        pass
    def exportChildren(self, outfile, level, name_='XSParamList'):
        for XSParamItem_ in self.getXSParamItem():
            XSParamItem_.export(outfile, level)

    #Only to export the entire XML tree to a file stream on disk
    def outputFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write("<?xml version=\"1.0\" ?>\n")
        self.export( outfile, 0, name_='XSParamList' )
        outfile.close()


    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSParamList.factory()
        rootObj.build(rootNode)
        return rootObj
    parseString = staticmethod( parseString ) 


    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSParamList.factory()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile ) 


    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO.StringIO()
        oStreamString.write('<?xml version="1.0" ?>\n')
        self.export( oStreamString, 0, name_="XSParamList" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    def exportLiteral(self, outfile, level, name_='XSParamList'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        pass
    def exportLiteralChildren(self, outfile, level, name_):
        showIndent(outfile, level)
        outfile.write('XSParamItem=[\n')
        level += 1
        for XSParamItem in self.XSParamItem:
            showIndent(outfile, level)
            outfile.write('XSParamItem(\n')
            XSParamItem.exportLiteral(outfile, level)
            showIndent(outfile, level)
            outfile.write('),\n')
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
    def build(self, node_):
        attrs = node_.attributes
        self.buildAttributes(attrs)
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildAttributes(self, attrs):
        pass
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'XSParamItem':
            obj_ = XSParamItem.factory()
            obj_.build(child_)
            self.XSParamItem.append(obj_)
# end class XSParamList


class XSPluginItem:
    subclass = None
    def __init__(self, name='', XSParamList=None, XSOptionList=None):
        self.name = name
        self.XSParamList = XSParamList
        self.XSOptionList = XSOptionList
    def factory(*args_, **kwargs_):
        if XSPluginItem.subclass:
            return XSPluginItem.subclass(*args_, **kwargs_)
        else:
            return XSPluginItem(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getName(self): return self.name
    def setName(self, name): self.name = name
    def getXSParamList(self): return self.XSParamList
    def setXSParamList(self, XSParamList): self.XSParamList = XSParamList
    def getXSOptionList(self): return self.XSOptionList
    def setXSOptionList(self, XSOptionList): self.XSOptionList = XSOptionList
    def export(self, outfile, level, name_='XSPluginItem'):
        showIndent(outfile, level)
        outfile.write('<%s>\n' % name_)
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='XSPluginItem'):
        pass
    def exportChildren(self, outfile, level, name_='XSPluginItem'):
        showIndent(outfile, level)
        outfile.write('<name>%s</name>\n' % quote_xml(self.getName()))
        if self.getXSParamList() != None :
            if self.XSParamList:
                self.XSParamList.export(outfile, level)
        if self.getXSOptionList() != None :
            if self.XSOptionList:
                self.XSOptionList.export(outfile, level)

    #Only to export the entire XML tree to a file stream on disk
    def outputFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write("<?xml version=\"1.0\" ?>\n")
        self.export( outfile, 0, name_='XSPluginItem' )
        outfile.close()


    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSPluginItem.factory()
        rootObj.build(rootNode)
        return rootObj
    parseString = staticmethod( parseString ) 


    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSPluginItem.factory()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile ) 


    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO.StringIO()
        oStreamString.write('<?xml version="1.0" ?>\n')
        self.export( oStreamString, 0, name_="XSPluginItem" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    def exportLiteral(self, outfile, level, name_='XSPluginItem'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        pass
    def exportLiteralChildren(self, outfile, level, name_):
        showIndent(outfile, level)
        outfile.write('name=%s,\n' % quote_python(self.getName()))
        if self.XSParamList:
            showIndent(outfile, level)
            outfile.write('XSParamList=XSParamList(\n')
            self.XSParamList.exportLiteral(outfile, level)
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.XSOptionList:
            showIndent(outfile, level)
            outfile.write('XSOptionList=XSOptionList(\n')
            self.XSOptionList.exportLiteral(outfile, level)
            showIndent(outfile, level)
            outfile.write('),\n')
    def build(self, node_):
        attrs = node_.attributes
        self.buildAttributes(attrs)
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildAttributes(self, attrs):
        pass
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'name':
            name_ = ''
            for text__content_ in child_.childNodes:
                name_ += text__content_.nodeValue
            self.name = name_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'XSParamList':
            obj_ = XSParamList.factory()
            obj_.build(child_)
            self.setXSParamList(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'XSOptionList':
            obj_ = XSOptionList.factory()
            obj_.build(child_)
            self.setXSOptionList(obj_)
# end class XSPluginItem


class XSPluginList:
    subclass = None
    def __init__(self, XSPluginItem=None):
        if XSPluginItem is None:
            self.XSPluginItem = []
        else:
            self.XSPluginItem = XSPluginItem
    def factory(*args_, **kwargs_):
        if XSPluginList.subclass:
            return XSPluginList.subclass(*args_, **kwargs_)
        else:
            return XSPluginList(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getXSPluginItem(self): return self.XSPluginItem
    def setXSPluginItem(self, XSPluginItem): self.XSPluginItem = XSPluginItem
    def addXSPluginItem(self, value): self.XSPluginItem.append(value)
    def insertXSPluginItem(self, index, value): self.XSPluginItem[index] = value
    def export(self, outfile, level, name_='XSPluginList'):
        showIndent(outfile, level)
        outfile.write('<%s>\n' % name_)
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='XSPluginList'):
        pass
    def exportChildren(self, outfile, level, name_='XSPluginList'):
        for XSPluginItem_ in self.getXSPluginItem():
            XSPluginItem_.export(outfile, level)

    #Only to export the entire XML tree to a file stream on disk
    def outputFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write("<?xml version=\"1.0\" ?>\n")
        self.export( outfile, 0, name_='XSPluginList' )
        outfile.close()


    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSPluginList.factory()
        rootObj.build(rootNode)
        return rootObj
    parseString = staticmethod( parseString ) 


    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSPluginList.factory()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile ) 


    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO.StringIO()
        oStreamString.write('<?xml version="1.0" ?>\n')
        self.export( oStreamString, 0, name_="XSPluginList" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    def exportLiteral(self, outfile, level, name_='XSPluginList'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        pass
    def exportLiteralChildren(self, outfile, level, name_):
        showIndent(outfile, level)
        outfile.write('XSPluginItem=[\n')
        level += 1
        for XSPluginItem in self.XSPluginItem:
            showIndent(outfile, level)
            outfile.write('XSPluginItem(\n')
            XSPluginItem.exportLiteral(outfile, level)
            showIndent(outfile, level)
            outfile.write('),\n')
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
    def build(self, node_):
        attrs = node_.attributes
        self.buildAttributes(attrs)
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildAttributes(self, attrs):
        pass
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'XSPluginItem':
            obj_ = XSPluginItem.factory()
            obj_.build(child_)
            self.XSPluginItem.append(obj_)
# end class XSPluginList


class XSDataAtom(XSData):
    subclass = None
    def __init__(self, concentration=None, numberOf=None, symbol=None):
        XSData.__init__(self)
        self.concentration = concentration
        self.numberOf = numberOf
        self.symbol = symbol
    def factory(*args_, **kwargs_):
        if XSDataAtom.subclass:
            return XSDataAtom.subclass(*args_, **kwargs_)
        else:
            return XSDataAtom(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getConcentration(self): return self.concentration
    def setConcentration(self, concentration): self.concentration = concentration
    def getNumberOf(self): return self.numberOf
    def setNumberOf(self, numberOf): self.numberOf = numberOf
    def getSymbol(self): return self.symbol
    def setSymbol(self, symbol): self.symbol = symbol
    def export(self, outfile, level, name_='XSDataAtom'):
        showIndent(outfile, level)
        outfile.write('<%s>\n' % name_)
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='XSDataAtom'):
        XSData.exportAttributes(self, outfile, level, name_='XSDataAtom')
    def exportChildren(self, outfile, level, name_='XSDataAtom'):
        if self.concentration:
            self.concentration.export(outfile, level, name_='concentration')
        if self.numberOf:
            self.numberOf.export(outfile, level, name_='numberOf')
        if self.symbol:
            self.symbol.export(outfile, level, name_='symbol')
        XSData.exportChildren(self, outfile, level, name_)

    #Only to export the entire XML tree to a file stream on disk
    def outputFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write("<?xml version=\"1.0\" ?>\n")
        self.export( outfile, 0, name_='XSDataAtom' )
        outfile.close()


    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataAtom.factory()
        rootObj.build(rootNode)
        return rootObj
    parseString = staticmethod( parseString ) 


    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataAtom.factory()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile ) 


    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO.StringIO()
        oStreamString.write('<?xml version="1.0" ?>\n')
        self.export( oStreamString, 0, name_="XSDataAtom" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    def exportLiteral(self, outfile, level, name_='XSDataAtom'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        pass
        XSData.exportLiteralAttributes(self, outfile, level, name_)
    def exportLiteralChildren(self, outfile, level, name_):
        if self.concentration:
            showIndent(outfile, level)
            outfile.write('concentration=XSDataFloat(\n')
            self.concentration.exportLiteral(outfile, level, name_='concentration')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.numberOf:
            showIndent(outfile, level)
            outfile.write('numberOf=XSDataFloat(\n')
            self.numberOf.exportLiteral(outfile, level, name_='numberOf')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.symbol:
            showIndent(outfile, level)
            outfile.write('symbol=XSDataString(\n')
            self.symbol.exportLiteral(outfile, level, name_='symbol')
            showIndent(outfile, level)
            outfile.write('),\n')
        XSData.exportLiteralChildren(self, outfile, level, name_)
    def build(self, node_):
        attrs = node_.attributes
        self.buildAttributes(attrs)
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildAttributes(self, attrs):
        XSData.buildAttributes(self, attrs)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'concentration':
            obj_ = XSDataFloat.factory()
            obj_.build(child_)
            self.setConcentration(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'numberOf':
            obj_ = XSDataFloat.factory()
            obj_.build(child_)
            self.setNumberOf(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'symbol':
            obj_ = XSDataString.factory()
            obj_.build(child_)
            self.setSymbol(obj_)
# end class XSDataAtom


class XSDataAtomicComposition(XSData):
    subclass = None
    def __init__(self, atom=None):
        XSData.__init__(self)
        if atom is None:
            self.atom = []
        else:
            self.atom = atom
    def factory(*args_, **kwargs_):
        if XSDataAtomicComposition.subclass:
            return XSDataAtomicComposition.subclass(*args_, **kwargs_)
        else:
            return XSDataAtomicComposition(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getAtom(self): return self.atom
    def setAtom(self, atom): self.atom = atom
    def addAtom(self, value): self.atom.append(value)
    def insertAtom(self, index, value): self.atom[index] = value
    def export(self, outfile, level, name_='XSDataAtomicComposition'):
        showIndent(outfile, level)
        outfile.write('<%s>\n' % name_)
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='XSDataAtomicComposition'):
        XSData.exportAttributes(self, outfile, level, name_='XSDataAtomicComposition')
    def exportChildren(self, outfile, level, name_='XSDataAtomicComposition'):
        for atom_ in self.getAtom():
            atom_.export(outfile, level, name_='atom')
        XSData.exportChildren(self, outfile, level, name_)

    #Only to export the entire XML tree to a file stream on disk
    def outputFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write("<?xml version=\"1.0\" ?>\n")
        self.export( outfile, 0, name_='XSDataAtomicComposition' )
        outfile.close()


    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataAtomicComposition.factory()
        rootObj.build(rootNode)
        return rootObj
    parseString = staticmethod( parseString ) 


    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataAtomicComposition.factory()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile ) 


    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO.StringIO()
        oStreamString.write('<?xml version="1.0" ?>\n')
        self.export( oStreamString, 0, name_="XSDataAtomicComposition" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    def exportLiteral(self, outfile, level, name_='XSDataAtomicComposition'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        pass
        XSData.exportLiteralAttributes(self, outfile, level, name_)
    def exportLiteralChildren(self, outfile, level, name_):
        showIndent(outfile, level)
        outfile.write('atom=[\n')
        level += 1
        for atom in self.atom:
            showIndent(outfile, level)
            outfile.write('XSDataAtom(\n')
            atom.exportLiteral(outfile, level, name_='atom')
            showIndent(outfile, level)
            outfile.write('),\n')
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
        XSData.exportLiteralChildren(self, outfile, level, name_)
    def build(self, node_):
        attrs = node_.attributes
        self.buildAttributes(attrs)
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildAttributes(self, attrs):
        XSData.buildAttributes(self, attrs)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'atom':
            obj_ = XSDataAtom.factory()
            obj_.build(child_)
            self.atom.append(obj_)
# end class XSDataAtomicComposition


class XSDataBeam(XSData):
    subclass = None
    def __init__(self, exposureTime=None, flux=None, minExposureTimePerImage=None, size=None, transmission=None, wavelength=None):
        XSData.__init__(self)
        self.exposureTime = exposureTime
        self.flux = flux
        self.minExposureTimePerImage = minExposureTimePerImage
        self.size = size
        self.transmission = transmission
        self.wavelength = wavelength
    def factory(*args_, **kwargs_):
        if XSDataBeam.subclass:
            return XSDataBeam.subclass(*args_, **kwargs_)
        else:
            return XSDataBeam(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getExposureTime(self): return self.exposureTime
    def setExposureTime(self, exposureTime): self.exposureTime = exposureTime
    def getFlux(self): return self.flux
    def setFlux(self, flux): self.flux = flux
    def getMinExposureTimePerImage(self): return self.minExposureTimePerImage
    def setMinExposureTimePerImage(self, minExposureTimePerImage): self.minExposureTimePerImage = minExposureTimePerImage
    def getSize(self): return self.size
    def setSize(self, size): self.size = size
    def getTransmission(self): return self.transmission
    def setTransmission(self, transmission): self.transmission = transmission
    def getWavelength(self): return self.wavelength
    def setWavelength(self, wavelength): self.wavelength = wavelength
    def export(self, outfile, level, name_='XSDataBeam'):
        showIndent(outfile, level)
        outfile.write('<%s>\n' % name_)
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='XSDataBeam'):
        XSData.exportAttributes(self, outfile, level, name_='XSDataBeam')
    def exportChildren(self, outfile, level, name_='XSDataBeam'):
        if self.getExposureTime() != None :
            if self.exposureTime:
                self.exposureTime.export(outfile, level, name_='exposureTime')
        if self.getFlux() != None :
            if self.flux:
                self.flux.export(outfile, level, name_='flux')
        if self.getMinExposureTimePerImage() != None :
            if self.minExposureTimePerImage:
                self.minExposureTimePerImage.export(outfile, level, name_='minExposureTimePerImage')
        if self.getSize() != None :
            if self.size:
                self.size.export(outfile, level, name_='size')
        if self.getTransmission() != None :
            if self.transmission:
                self.transmission.export(outfile, level, name_='transmission')
        if self.getWavelength() != None :
            if self.wavelength:
                self.wavelength.export(outfile, level, name_='wavelength')
        XSData.exportChildren(self, outfile, level, name_)

    #Only to export the entire XML tree to a file stream on disk
    def outputFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write("<?xml version=\"1.0\" ?>\n")
        self.export( outfile, 0, name_='XSDataBeam' )
        outfile.close()


    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataBeam.factory()
        rootObj.build(rootNode)
        return rootObj
    parseString = staticmethod( parseString ) 


    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataBeam.factory()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile ) 


    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO.StringIO()
        oStreamString.write('<?xml version="1.0" ?>\n')
        self.export( oStreamString, 0, name_="XSDataBeam" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    def exportLiteral(self, outfile, level, name_='XSDataBeam'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        pass
        XSData.exportLiteralAttributes(self, outfile, level, name_)
    def exportLiteralChildren(self, outfile, level, name_):
        if self.exposureTime:
            showIndent(outfile, level)
            outfile.write('exposureTime=XSDataTime(\n')
            self.exposureTime.exportLiteral(outfile, level, name_='exposureTime')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.flux:
            showIndent(outfile, level)
            outfile.write('flux=XSDataFlux(\n')
            self.flux.exportLiteral(outfile, level, name_='flux')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.minExposureTimePerImage:
            showIndent(outfile, level)
            outfile.write('minExposureTimePerImage=XSDataTime(\n')
            self.minExposureTimePerImage.exportLiteral(outfile, level, name_='minExposureTimePerImage')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.size:
            showIndent(outfile, level)
            outfile.write('size=XSDataSize(\n')
            self.size.exportLiteral(outfile, level, name_='size')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.transmission:
            showIndent(outfile, level)
            outfile.write('transmission=XSDataDouble(\n')
            self.transmission.exportLiteral(outfile, level, name_='transmission')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.wavelength:
            showIndent(outfile, level)
            outfile.write('wavelength=XSDataWavelength(\n')
            self.wavelength.exportLiteral(outfile, level, name_='wavelength')
            showIndent(outfile, level)
            outfile.write('),\n')
        XSData.exportLiteralChildren(self, outfile, level, name_)
    def build(self, node_):
        attrs = node_.attributes
        self.buildAttributes(attrs)
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildAttributes(self, attrs):
        XSData.buildAttributes(self, attrs)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'exposureTime':
            obj_ = XSDataTime.factory()
            obj_.build(child_)
            self.setExposureTime(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'flux':
            obj_ = XSDataFlux.factory()
            obj_.build(child_)
            self.setFlux(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'minExposureTimePerImage':
            obj_ = XSDataTime.factory()
            obj_.build(child_)
            self.setMinExposureTimePerImage(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'size':
            obj_ = XSDataSize.factory()
            obj_.build(child_)
            self.setSize(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'transmission':
            obj_ = XSDataDouble.factory()
            obj_.build(child_)
            self.setTransmission(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'wavelength':
            obj_ = XSDataWavelength.factory()
            obj_.build(child_)
            self.setWavelength(obj_)
# end class XSDataBeam


class XSDataCell(XSData):
    subclass = None
    def __init__(self, angle_alpha=None, angle_beta=None, angle_gamma=None, length_a=None, length_b=None, length_c=None):
        XSData.__init__(self)
        self.angle_alpha = angle_alpha
        self.angle_beta = angle_beta
        self.angle_gamma = angle_gamma
        self.length_a = length_a
        self.length_b = length_b
        self.length_c = length_c
    def factory(*args_, **kwargs_):
        if XSDataCell.subclass:
            return XSDataCell.subclass(*args_, **kwargs_)
        else:
            return XSDataCell(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getAngle_alpha(self): return self.angle_alpha
    def setAngle_alpha(self, angle_alpha): self.angle_alpha = angle_alpha
    def getAngle_beta(self): return self.angle_beta
    def setAngle_beta(self, angle_beta): self.angle_beta = angle_beta
    def getAngle_gamma(self): return self.angle_gamma
    def setAngle_gamma(self, angle_gamma): self.angle_gamma = angle_gamma
    def getLength_a(self): return self.length_a
    def setLength_a(self, length_a): self.length_a = length_a
    def getLength_b(self): return self.length_b
    def setLength_b(self, length_b): self.length_b = length_b
    def getLength_c(self): return self.length_c
    def setLength_c(self, length_c): self.length_c = length_c
    def export(self, outfile, level, name_='XSDataCell'):
        showIndent(outfile, level)
        outfile.write('<%s>\n' % name_)
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='XSDataCell'):
        XSData.exportAttributes(self, outfile, level, name_='XSDataCell')
    def exportChildren(self, outfile, level, name_='XSDataCell'):
        if self.angle_alpha:
            self.angle_alpha.export(outfile, level, name_='angle_alpha')
        if self.angle_beta:
            self.angle_beta.export(outfile, level, name_='angle_beta')
        if self.angle_gamma:
            self.angle_gamma.export(outfile, level, name_='angle_gamma')
        if self.length_a:
            self.length_a.export(outfile, level, name_='length_a')
        if self.length_b:
            self.length_b.export(outfile, level, name_='length_b')
        if self.length_c:
            self.length_c.export(outfile, level, name_='length_c')
        XSData.exportChildren(self, outfile, level, name_)

    #Only to export the entire XML tree to a file stream on disk
    def outputFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write("<?xml version=\"1.0\" ?>\n")
        self.export( outfile, 0, name_='XSDataCell' )
        outfile.close()


    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataCell.factory()
        rootObj.build(rootNode)
        return rootObj
    parseString = staticmethod( parseString ) 


    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataCell.factory()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile ) 


    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO.StringIO()
        oStreamString.write('<?xml version="1.0" ?>\n')
        self.export( oStreamString, 0, name_="XSDataCell" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    def exportLiteral(self, outfile, level, name_='XSDataCell'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        pass
        XSData.exportLiteralAttributes(self, outfile, level, name_)
    def exportLiteralChildren(self, outfile, level, name_):
        if self.angle_alpha:
            showIndent(outfile, level)
            outfile.write('angle_alpha=XSDataAngle(\n')
            self.angle_alpha.exportLiteral(outfile, level, name_='angle_alpha')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.angle_beta:
            showIndent(outfile, level)
            outfile.write('angle_beta=XSDataAngle(\n')
            self.angle_beta.exportLiteral(outfile, level, name_='angle_beta')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.angle_gamma:
            showIndent(outfile, level)
            outfile.write('angle_gamma=XSDataAngle(\n')
            self.angle_gamma.exportLiteral(outfile, level, name_='angle_gamma')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.length_a:
            showIndent(outfile, level)
            outfile.write('length_a=XSDataLength(\n')
            self.length_a.exportLiteral(outfile, level, name_='length_a')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.length_b:
            showIndent(outfile, level)
            outfile.write('length_b=XSDataLength(\n')
            self.length_b.exportLiteral(outfile, level, name_='length_b')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.length_c:
            showIndent(outfile, level)
            outfile.write('length_c=XSDataLength(\n')
            self.length_c.exportLiteral(outfile, level, name_='length_c')
            showIndent(outfile, level)
            outfile.write('),\n')
        XSData.exportLiteralChildren(self, outfile, level, name_)
    def build(self, node_):
        attrs = node_.attributes
        self.buildAttributes(attrs)
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildAttributes(self, attrs):
        XSData.buildAttributes(self, attrs)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'angle_alpha':
            obj_ = XSDataAngle.factory()
            obj_.build(child_)
            self.setAngle_alpha(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'angle_beta':
            obj_ = XSDataAngle.factory()
            obj_.build(child_)
            self.setAngle_beta(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'angle_gamma':
            obj_ = XSDataAngle.factory()
            obj_.build(child_)
            self.setAngle_gamma(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'length_a':
            obj_ = XSDataLength.factory()
            obj_.build(child_)
            self.setLength_a(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'length_b':
            obj_ = XSDataLength.factory()
            obj_.build(child_)
            self.setLength_b(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'length_c':
            obj_ = XSDataLength.factory()
            obj_.build(child_)
            self.setLength_c(obj_)
# end class XSDataCell


class XSDataChain(XSData):
    subclass = None
    def __init__(self, numberOfCopies=None, numberOfMonomers=None, typexx=None, heavyAtoms=None):
        XSData.__init__(self)
        self.numberOfCopies = numberOfCopies
        self.numberOfMonomers = numberOfMonomers
        self.typexx = typexx
        self.heavyAtoms = heavyAtoms
    def factory(*args_, **kwargs_):
        if XSDataChain.subclass:
            return XSDataChain.subclass(*args_, **kwargs_)
        else:
            return XSDataChain(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getNumberOfCopies(self): return self.numberOfCopies
    def setNumberOfCopies(self, numberOfCopies): self.numberOfCopies = numberOfCopies
    def getNumberOfMonomers(self): return self.numberOfMonomers
    def setNumberOfMonomers(self, numberOfMonomers): self.numberOfMonomers = numberOfMonomers
    def getType(self): return self.typexx
    def setType(self, typexx): self.typexx = typexx
    def getHeavyAtoms(self): return self.heavyAtoms
    def setHeavyAtoms(self, heavyAtoms): self.heavyAtoms = heavyAtoms
    def export(self, outfile, level, name_='XSDataChain'):
        showIndent(outfile, level)
        outfile.write('<%s>\n' % name_)
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='XSDataChain'):
        XSData.exportAttributes(self, outfile, level, name_='XSDataChain')
    def exportChildren(self, outfile, level, name_='XSDataChain'):
        if self.numberOfCopies:
            self.numberOfCopies.export(outfile, level, name_='numberOfCopies')
        if self.numberOfMonomers:
            self.numberOfMonomers.export(outfile, level, name_='numberOfMonomers')
        if self.typexx:
            self.typexx.export(outfile, level, name_='type')
        if self.heavyAtoms:
            self.heavyAtoms.export(outfile, level, name_='heavyAtoms')
        XSData.exportChildren(self, outfile, level, name_)

    #Only to export the entire XML tree to a file stream on disk
    def outputFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write("<?xml version=\"1.0\" ?>\n")
        self.export( outfile, 0, name_='XSDataChain' )
        outfile.close()


    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataChain.factory()
        rootObj.build(rootNode)
        return rootObj
    parseString = staticmethod( parseString ) 


    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataChain.factory()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile ) 


    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO.StringIO()
        oStreamString.write('<?xml version="1.0" ?>\n')
        self.export( oStreamString, 0, name_="XSDataChain" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    def exportLiteral(self, outfile, level, name_='XSDataChain'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        pass
        XSData.exportLiteralAttributes(self, outfile, level, name_)
    def exportLiteralChildren(self, outfile, level, name_):
        if self.numberOfCopies:
            showIndent(outfile, level)
            outfile.write('numberOfCopies=XSDataFloat(\n')
            self.numberOfCopies.exportLiteral(outfile, level, name_='numberOfCopies')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.numberOfMonomers:
            showIndent(outfile, level)
            outfile.write('numberOfMonomers=XSDataFloat(\n')
            self.numberOfMonomers.exportLiteral(outfile, level, name_='numberOfMonomers')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.typexx:
            showIndent(outfile, level)
            outfile.write('typexx=XSDataString(\n')
            self.typexx.exportLiteral(outfile, level, name_='type')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.heavyAtoms:
            showIndent(outfile, level)
            outfile.write('heavyAtoms=XSDataAtomicComposition(\n')
            self.heavyAtoms.exportLiteral(outfile, level, name_='heavyAtoms')
            showIndent(outfile, level)
            outfile.write('),\n')
        XSData.exportLiteralChildren(self, outfile, level, name_)
    def build(self, node_):
        attrs = node_.attributes
        self.buildAttributes(attrs)
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildAttributes(self, attrs):
        XSData.buildAttributes(self, attrs)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'numberOfCopies':
            obj_ = XSDataFloat.factory()
            obj_.build(child_)
            self.setNumberOfCopies(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'numberOfMonomers':
            obj_ = XSDataFloat.factory()
            obj_.build(child_)
            self.setNumberOfMonomers(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'type':
            obj_ = XSDataString.factory()
            obj_.build(child_)
            self.setType(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'heavyAtoms':
            obj_ = XSDataAtomicComposition.factory()
            obj_.build(child_)
            self.setHeavyAtoms(obj_)
# end class XSDataChain


class XSDataCharacterisation(XSData):
    subclass = None
    def __init__(self, dataCollection=None, indexingResult=None, integrationResult=None, strategyResult=None):
        XSData.__init__(self)
        self.dataCollection = dataCollection
        self.indexingResult = indexingResult
        self.integrationResult = integrationResult
        self.strategyResult = strategyResult
    def factory(*args_, **kwargs_):
        if XSDataCharacterisation.subclass:
            return XSDataCharacterisation.subclass(*args_, **kwargs_)
        else:
            return XSDataCharacterisation(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getDataCollection(self): return self.dataCollection
    def setDataCollection(self, dataCollection): self.dataCollection = dataCollection
    def getIndexingResult(self): return self.indexingResult
    def setIndexingResult(self, indexingResult): self.indexingResult = indexingResult
    def getIntegrationResult(self): return self.integrationResult
    def setIntegrationResult(self, integrationResult): self.integrationResult = integrationResult
    def getStrategyResult(self): return self.strategyResult
    def setStrategyResult(self, strategyResult): self.strategyResult = strategyResult
    def export(self, outfile, level, name_='XSDataCharacterisation'):
        showIndent(outfile, level)
        outfile.write('<%s>\n' % name_)
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='XSDataCharacterisation'):
        XSData.exportAttributes(self, outfile, level, name_='XSDataCharacterisation')
    def exportChildren(self, outfile, level, name_='XSDataCharacterisation'):
        if self.dataCollection:
            self.dataCollection.export(outfile, level, name_='dataCollection')
        if self.getIndexingResult() != None :
            if self.indexingResult:
                self.indexingResult.export(outfile, level, name_='indexingResult')
        if self.getIntegrationResult() != None :
            if self.integrationResult:
                self.integrationResult.export(outfile, level, name_='integrationResult')
        if self.getStrategyResult() != None :
            if self.strategyResult:
                self.strategyResult.export(outfile, level, name_='strategyResult')
        XSData.exportChildren(self, outfile, level, name_)

    #Only to export the entire XML tree to a file stream on disk
    def outputFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write("<?xml version=\"1.0\" ?>\n")
        self.export( outfile, 0, name_='XSDataCharacterisation' )
        outfile.close()


    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataCharacterisation.factory()
        rootObj.build(rootNode)
        return rootObj
    parseString = staticmethod( parseString ) 


    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataCharacterisation.factory()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile ) 


    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO.StringIO()
        oStreamString.write('<?xml version="1.0" ?>\n')
        self.export( oStreamString, 0, name_="XSDataCharacterisation" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    def exportLiteral(self, outfile, level, name_='XSDataCharacterisation'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        pass
        XSData.exportLiteralAttributes(self, outfile, level, name_)
    def exportLiteralChildren(self, outfile, level, name_):
        if self.dataCollection:
            showIndent(outfile, level)
            outfile.write('dataCollection=XSDataCollection(\n')
            self.dataCollection.exportLiteral(outfile, level, name_='dataCollection')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.indexingResult:
            showIndent(outfile, level)
            outfile.write('indexingResult=XSDataIndexingResult(\n')
            self.indexingResult.exportLiteral(outfile, level, name_='indexingResult')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.integrationResult:
            showIndent(outfile, level)
            outfile.write('integrationResult=XSDataIntegrationResult(\n')
            self.integrationResult.exportLiteral(outfile, level, name_='integrationResult')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.strategyResult:
            showIndent(outfile, level)
            outfile.write('strategyResult=XSDataStrategyResult(\n')
            self.strategyResult.exportLiteral(outfile, level, name_='strategyResult')
            showIndent(outfile, level)
            outfile.write('),\n')
        XSData.exportLiteralChildren(self, outfile, level, name_)
    def build(self, node_):
        attrs = node_.attributes
        self.buildAttributes(attrs)
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildAttributes(self, attrs):
        XSData.buildAttributes(self, attrs)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'dataCollection':
            obj_ = XSDataCollection.factory()
            obj_.build(child_)
            self.setDataCollection(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'indexingResult':
            obj_ = XSDataIndexingResult.factory()
            obj_.build(child_)
            self.setIndexingResult(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'integrationResult':
            obj_ = XSDataIntegrationResult.factory()
            obj_.build(child_)
            self.setIntegrationResult(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'strategyResult':
            obj_ = XSDataStrategyResult.factory()
            obj_.build(child_)
            self.setStrategyResult(obj_)
# end class XSDataCharacterisation


class XSDataChemicalCompositionMM(XSData):
    subclass = None
    def __init__(self, solvent=None, structure=None):
        XSData.__init__(self)
        self.solvent = solvent
        self.structure = structure
    def factory(*args_, **kwargs_):
        if XSDataChemicalCompositionMM.subclass:
            return XSDataChemicalCompositionMM.subclass(*args_, **kwargs_)
        else:
            return XSDataChemicalCompositionMM(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getSolvent(self): return self.solvent
    def setSolvent(self, solvent): self.solvent = solvent
    def getStructure(self): return self.structure
    def setStructure(self, structure): self.structure = structure
    def export(self, outfile, level, name_='XSDataChemicalCompositionMM'):
        showIndent(outfile, level)
        outfile.write('<%s>\n' % name_)
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='XSDataChemicalCompositionMM'):
        XSData.exportAttributes(self, outfile, level, name_='XSDataChemicalCompositionMM')
    def exportChildren(self, outfile, level, name_='XSDataChemicalCompositionMM'):
        if self.solvent:
            self.solvent.export(outfile, level, name_='solvent')
        if self.structure:
            self.structure.export(outfile, level, name_='structure')
        XSData.exportChildren(self, outfile, level, name_)

    #Only to export the entire XML tree to a file stream on disk
    def outputFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write("<?xml version=\"1.0\" ?>\n")
        self.export( outfile, 0, name_='XSDataChemicalCompositionMM' )
        outfile.close()


    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataChemicalCompositionMM.factory()
        rootObj.build(rootNode)
        return rootObj
    parseString = staticmethod( parseString ) 


    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataChemicalCompositionMM.factory()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile ) 


    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO.StringIO()
        oStreamString.write('<?xml version="1.0" ?>\n')
        self.export( oStreamString, 0, name_="XSDataChemicalCompositionMM" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    def exportLiteral(self, outfile, level, name_='XSDataChemicalCompositionMM'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        pass
        XSData.exportLiteralAttributes(self, outfile, level, name_)
    def exportLiteralChildren(self, outfile, level, name_):
        if self.solvent:
            showIndent(outfile, level)
            outfile.write('solvent=XSDataSolvent(\n')
            self.solvent.exportLiteral(outfile, level, name_='solvent')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.structure:
            showIndent(outfile, level)
            outfile.write('structure=XSDataStructure(\n')
            self.structure.exportLiteral(outfile, level, name_='structure')
            showIndent(outfile, level)
            outfile.write('),\n')
        XSData.exportLiteralChildren(self, outfile, level, name_)
    def build(self, node_):
        attrs = node_.attributes
        self.buildAttributes(attrs)
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildAttributes(self, attrs):
        XSData.buildAttributes(self, attrs)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'solvent':
            obj_ = XSDataSolvent.factory()
            obj_.build(child_)
            self.setSolvent(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'structure':
            obj_ = XSDataStructure.factory()
            obj_.build(child_)
            self.setStructure(obj_)
# end class XSDataChemicalCompositionMM


class XSDataCollection(XSData):
    subclass = None
    def __init__(self, diffractionPlan=None, sample=None, subWedge=None):
        XSData.__init__(self)
        self.diffractionPlan = diffractionPlan
        self.sample = sample
        if subWedge is None:
            self.subWedge = []
        else:
            self.subWedge = subWedge
    def factory(*args_, **kwargs_):
        if XSDataCollection.subclass:
            return XSDataCollection.subclass(*args_, **kwargs_)
        else:
            return XSDataCollection(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getDiffractionPlan(self): return self.diffractionPlan
    def setDiffractionPlan(self, diffractionPlan): self.diffractionPlan = diffractionPlan
    def getSample(self): return self.sample
    def setSample(self, sample): self.sample = sample
    def getSubWedge(self): return self.subWedge
    def setSubWedge(self, subWedge): self.subWedge = subWedge
    def addSubWedge(self, value): self.subWedge.append(value)
    def insertSubWedge(self, index, value): self.subWedge[index] = value
    def export(self, outfile, level, name_='XSDataCollection'):
        showIndent(outfile, level)
        outfile.write('<%s>\n' % name_)
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='XSDataCollection'):
        XSData.exportAttributes(self, outfile, level, name_='XSDataCollection')
    def exportChildren(self, outfile, level, name_='XSDataCollection'):
        if self.getDiffractionPlan() != None :
            if self.diffractionPlan:
                self.diffractionPlan.export(outfile, level, name_='diffractionPlan')
        if self.getSample() != None :
            if self.sample:
                self.sample.export(outfile, level, name_='sample')
        for subWedge_ in self.getSubWedge():
            subWedge_.export(outfile, level, name_='subWedge')
        XSData.exportChildren(self, outfile, level, name_)

    #Only to export the entire XML tree to a file stream on disk
    def outputFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write("<?xml version=\"1.0\" ?>\n")
        self.export( outfile, 0, name_='XSDataCollection' )
        outfile.close()


    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataCollection.factory()
        rootObj.build(rootNode)
        return rootObj
    parseString = staticmethod( parseString ) 


    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataCollection.factory()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile ) 


    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO.StringIO()
        oStreamString.write('<?xml version="1.0" ?>\n')
        self.export( oStreamString, 0, name_="XSDataCollection" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    def exportLiteral(self, outfile, level, name_='XSDataCollection'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        pass
        XSData.exportLiteralAttributes(self, outfile, level, name_)
    def exportLiteralChildren(self, outfile, level, name_):
        if self.diffractionPlan:
            showIndent(outfile, level)
            outfile.write('diffractionPlan=XSDataDiffractionPlan(\n')
            self.diffractionPlan.exportLiteral(outfile, level, name_='diffractionPlan')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.sample:
            showIndent(outfile, level)
            outfile.write('sample=XSDataSampleCrystalMM(\n')
            self.sample.exportLiteral(outfile, level, name_='sample')
            showIndent(outfile, level)
            outfile.write('),\n')
        showIndent(outfile, level)
        outfile.write('subWedge=[\n')
        level += 1
        for subWedge in self.subWedge:
            showIndent(outfile, level)
            outfile.write('XSDataSubWedge(\n')
            subWedge.exportLiteral(outfile, level, name_='subWedge')
            showIndent(outfile, level)
            outfile.write('),\n')
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
        XSData.exportLiteralChildren(self, outfile, level, name_)
    def build(self, node_):
        attrs = node_.attributes
        self.buildAttributes(attrs)
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildAttributes(self, attrs):
        XSData.buildAttributes(self, attrs)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'diffractionPlan':
            obj_ = XSDataDiffractionPlan.factory()
            obj_.build(child_)
            self.setDiffractionPlan(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'sample':
            obj_ = XSDataSampleCrystalMM.factory()
            obj_.build(child_)
            self.setSample(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'subWedge':
            obj_ = XSDataSubWedge.factory()
            obj_.build(child_)
            self.subWedge.append(obj_)
# end class XSDataCollection


class XSDataCollectionPlan(XSData):
    subclass = None
    def __init__(self, collectionPlanNumber=None, collectionStrategy=None, comment=None, strategySummary=None, statistics=None):
        XSData.__init__(self)
        self.collectionPlanNumber = collectionPlanNumber
        self.collectionStrategy = collectionStrategy
        self.comment = comment
        self.strategySummary = strategySummary
        self.statistics = statistics
    def factory(*args_, **kwargs_):
        if XSDataCollectionPlan.subclass:
            return XSDataCollectionPlan.subclass(*args_, **kwargs_)
        else:
            return XSDataCollectionPlan(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getCollectionPlanNumber(self): return self.collectionPlanNumber
    def setCollectionPlanNumber(self, collectionPlanNumber): self.collectionPlanNumber = collectionPlanNumber
    def getCollectionStrategy(self): return self.collectionStrategy
    def setCollectionStrategy(self, collectionStrategy): self.collectionStrategy = collectionStrategy
    def getComment(self): return self.comment
    def setComment(self, comment): self.comment = comment
    def getStrategySummary(self): return self.strategySummary
    def setStrategySummary(self, strategySummary): self.strategySummary = strategySummary
    def getStatistics(self): return self.statistics
    def setStatistics(self, statistics): self.statistics = statistics
    def export(self, outfile, level, name_='XSDataCollectionPlan'):
        showIndent(outfile, level)
        outfile.write('<%s>\n' % name_)
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='XSDataCollectionPlan'):
        XSData.exportAttributes(self, outfile, level, name_='XSDataCollectionPlan')
    def exportChildren(self, outfile, level, name_='XSDataCollectionPlan'):
        if self.collectionPlanNumber:
            self.collectionPlanNumber.export(outfile, level, name_='collectionPlanNumber')
        if self.collectionStrategy:
            self.collectionStrategy.export(outfile, level, name_='collectionStrategy')
        if self.comment:
            self.comment.export(outfile, level, name_='comment')
        if self.strategySummary:
            self.strategySummary.export(outfile, level, name_='strategySummary')
        if self.statistics:
            self.statistics.export(outfile, level, name_='statistics')
        XSData.exportChildren(self, outfile, level, name_)

    #Only to export the entire XML tree to a file stream on disk
    def outputFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write("<?xml version=\"1.0\" ?>\n")
        self.export( outfile, 0, name_='XSDataCollectionPlan' )
        outfile.close()


    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataCollectionPlan.factory()
        rootObj.build(rootNode)
        return rootObj
    parseString = staticmethod( parseString ) 


    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataCollectionPlan.factory()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile ) 


    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO.StringIO()
        oStreamString.write('<?xml version="1.0" ?>\n')
        self.export( oStreamString, 0, name_="XSDataCollectionPlan" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    def exportLiteral(self, outfile, level, name_='XSDataCollectionPlan'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        pass
        XSData.exportLiteralAttributes(self, outfile, level, name_)
    def exportLiteralChildren(self, outfile, level, name_):
        if self.collectionPlanNumber:
            showIndent(outfile, level)
            outfile.write('collectionPlanNumber=XSDataInteger(\n')
            self.collectionPlanNumber.exportLiteral(outfile, level, name_='collectionPlanNumber')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.collectionStrategy:
            showIndent(outfile, level)
            outfile.write('collectionStrategy=XSDataCollection(\n')
            self.collectionStrategy.exportLiteral(outfile, level, name_='collectionStrategy')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.comment:
            showIndent(outfile, level)
            outfile.write('comment=XSDataString(\n')
            self.comment.exportLiteral(outfile, level, name_='comment')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.strategySummary:
            showIndent(outfile, level)
            outfile.write('strategySummary=XSDataStrategySummary(\n')
            self.strategySummary.exportLiteral(outfile, level, name_='strategySummary')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.statistics:
            showIndent(outfile, level)
            outfile.write('statistics=XSDataStatisticsStrategy(\n')
            self.statistics.exportLiteral(outfile, level, name_='statistics')
            showIndent(outfile, level)
            outfile.write('),\n')
        XSData.exportLiteralChildren(self, outfile, level, name_)
    def build(self, node_):
        attrs = node_.attributes
        self.buildAttributes(attrs)
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildAttributes(self, attrs):
        XSData.buildAttributes(self, attrs)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'collectionPlanNumber':
            obj_ = XSDataInteger.factory()
            obj_.build(child_)
            self.setCollectionPlanNumber(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'collectionStrategy':
            obj_ = XSDataCollection.factory()
            obj_.build(child_)
            self.setCollectionStrategy(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'comment':
            obj_ = XSDataString.factory()
            obj_.build(child_)
            self.setComment(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'strategySummary':
            obj_ = XSDataStrategySummary.factory()
            obj_.build(child_)
            self.setStrategySummary(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'statistics':
            obj_ = XSDataStatisticsStrategy.factory()
            obj_.build(child_)
            self.setStatistics(obj_)
# end class XSDataCollectionPlan


class XSDataCrystal(XSData):
    subclass = None
    def __init__(self, mosaicity=None, spaceGroup=None, cell=None):
        XSData.__init__(self)
        self.mosaicity = mosaicity
        self.spaceGroup = spaceGroup
        self.cell = cell
    def factory(*args_, **kwargs_):
        if XSDataCrystal.subclass:
            return XSDataCrystal.subclass(*args_, **kwargs_)
        else:
            return XSDataCrystal(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getMosaicity(self): return self.mosaicity
    def setMosaicity(self, mosaicity): self.mosaicity = mosaicity
    def getSpaceGroup(self): return self.spaceGroup
    def setSpaceGroup(self, spaceGroup): self.spaceGroup = spaceGroup
    def getCell(self): return self.cell
    def setCell(self, cell): self.cell = cell
    def export(self, outfile, level, name_='XSDataCrystal'):
        showIndent(outfile, level)
        outfile.write('<%s>\n' % name_)
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='XSDataCrystal'):
        XSData.exportAttributes(self, outfile, level, name_='XSDataCrystal')
    def exportChildren(self, outfile, level, name_='XSDataCrystal'):
        if self.mosaicity:
            self.mosaicity.export(outfile, level, name_='mosaicity')
        if self.spaceGroup:
            self.spaceGroup.export(outfile, level, name_='spaceGroup')
        if self.cell:
            self.cell.export(outfile, level, name_='cell')
        XSData.exportChildren(self, outfile, level, name_)

    #Only to export the entire XML tree to a file stream on disk
    def outputFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write("<?xml version=\"1.0\" ?>\n")
        self.export( outfile, 0, name_='XSDataCrystal' )
        outfile.close()


    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataCrystal.factory()
        rootObj.build(rootNode)
        return rootObj
    parseString = staticmethod( parseString ) 


    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataCrystal.factory()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile ) 


    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO.StringIO()
        oStreamString.write('<?xml version="1.0" ?>\n')
        self.export( oStreamString, 0, name_="XSDataCrystal" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    def exportLiteral(self, outfile, level, name_='XSDataCrystal'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        pass
        XSData.exportLiteralAttributes(self, outfile, level, name_)
    def exportLiteralChildren(self, outfile, level, name_):
        if self.mosaicity:
            showIndent(outfile, level)
            outfile.write('mosaicity=XSDataFloat(\n')
            self.mosaicity.exportLiteral(outfile, level, name_='mosaicity')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.spaceGroup:
            showIndent(outfile, level)
            outfile.write('spaceGroup=XSDataSpaceGroup(\n')
            self.spaceGroup.exportLiteral(outfile, level, name_='spaceGroup')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.cell:
            showIndent(outfile, level)
            outfile.write('cell=XSDataCell(\n')
            self.cell.exportLiteral(outfile, level, name_='cell')
            showIndent(outfile, level)
            outfile.write('),\n')
        XSData.exportLiteralChildren(self, outfile, level, name_)
    def build(self, node_):
        attrs = node_.attributes
        self.buildAttributes(attrs)
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildAttributes(self, attrs):
        XSData.buildAttributes(self, attrs)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'mosaicity':
            obj_ = XSDataFloat.factory()
            obj_.build(child_)
            self.setMosaicity(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'spaceGroup':
            obj_ = XSDataSpaceGroup.factory()
            obj_.build(child_)
            self.setSpaceGroup(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'cell':
            obj_ = XSDataCell.factory()
            obj_.build(child_)
            self.setCell(obj_)
# end class XSDataCrystal


class XSDataDetector(XSData):
    subclass = None
    def __init__(self, beamPositionX=None, beamPositionY=None, bin=None, byteOrder=None, dataType=None, distance=None, gain=None, imageSaturation=None, name=None, numberBytesInHeader=None, numberPixelX=None, numberPixelY=None, pixelSizeX=None, pixelSizeY=None, serialNumber=None, twoTheta=None, typexx=None):
        XSData.__init__(self)
        self.beamPositionX = beamPositionX
        self.beamPositionY = beamPositionY
        self.bin = bin
        self.byteOrder = byteOrder
        self.dataType = dataType
        self.distance = distance
        self.gain = gain
        self.imageSaturation = imageSaturation
        self.name = name
        self.numberBytesInHeader = numberBytesInHeader
        self.numberPixelX = numberPixelX
        self.numberPixelY = numberPixelY
        self.pixelSizeX = pixelSizeX
        self.pixelSizeY = pixelSizeY
        self.serialNumber = serialNumber
        self.twoTheta = twoTheta
        self.typexx = typexx
    def factory(*args_, **kwargs_):
        if XSDataDetector.subclass:
            return XSDataDetector.subclass(*args_, **kwargs_)
        else:
            return XSDataDetector(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getBeamPositionX(self): return self.beamPositionX
    def setBeamPositionX(self, beamPositionX): self.beamPositionX = beamPositionX
    def getBeamPositionY(self): return self.beamPositionY
    def setBeamPositionY(self, beamPositionY): self.beamPositionY = beamPositionY
    def getBin(self): return self.bin
    def setBin(self, bin): self.bin = bin
    def getByteOrder(self): return self.byteOrder
    def setByteOrder(self, byteOrder): self.byteOrder = byteOrder
    def getDataType(self): return self.dataType
    def setDataType(self, dataType): self.dataType = dataType
    def getDistance(self): return self.distance
    def setDistance(self, distance): self.distance = distance
    def getGain(self): return self.gain
    def setGain(self, gain): self.gain = gain
    def getImageSaturation(self): return self.imageSaturation
    def setImageSaturation(self, imageSaturation): self.imageSaturation = imageSaturation
    def getName(self): return self.name
    def setName(self, name): self.name = name
    def getNumberBytesInHeader(self): return self.numberBytesInHeader
    def setNumberBytesInHeader(self, numberBytesInHeader): self.numberBytesInHeader = numberBytesInHeader
    def getNumberPixelX(self): return self.numberPixelX
    def setNumberPixelX(self, numberPixelX): self.numberPixelX = numberPixelX
    def getNumberPixelY(self): return self.numberPixelY
    def setNumberPixelY(self, numberPixelY): self.numberPixelY = numberPixelY
    def getPixelSizeX(self): return self.pixelSizeX
    def setPixelSizeX(self, pixelSizeX): self.pixelSizeX = pixelSizeX
    def getPixelSizeY(self): return self.pixelSizeY
    def setPixelSizeY(self, pixelSizeY): self.pixelSizeY = pixelSizeY
    def getSerialNumber(self): return self.serialNumber
    def setSerialNumber(self, serialNumber): self.serialNumber = serialNumber
    def getTwoTheta(self): return self.twoTheta
    def setTwoTheta(self, twoTheta): self.twoTheta = twoTheta
    def getType(self): return self.typexx
    def setType(self, typexx): self.typexx = typexx
    def export(self, outfile, level, name_='XSDataDetector'):
        showIndent(outfile, level)
        outfile.write('<%s>\n' % name_)
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='XSDataDetector'):
        XSData.exportAttributes(self, outfile, level, name_='XSDataDetector')
    def exportChildren(self, outfile, level, name_='XSDataDetector'):
        if self.beamPositionX:
            self.beamPositionX.export(outfile, level, name_='beamPositionX')
        if self.beamPositionY:
            self.beamPositionY.export(outfile, level, name_='beamPositionY')
        if self.bin:
            self.bin.export(outfile, level, name_='bin')
        if self.byteOrder:
            self.byteOrder.export(outfile, level, name_='byteOrder')
        if self.dataType:
            self.dataType.export(outfile, level, name_='dataType')
        if self.distance:
            self.distance.export(outfile, level, name_='distance')
        if self.gain:
            self.gain.export(outfile, level, name_='gain')
        if self.imageSaturation:
            self.imageSaturation.export(outfile, level, name_='imageSaturation')
        if self.name:
            self.name.export(outfile, level, name_='name')
        if self.numberBytesInHeader:
            self.numberBytesInHeader.export(outfile, level, name_='numberBytesInHeader')
        if self.numberPixelX:
            self.numberPixelX.export(outfile, level, name_='numberPixelX')
        if self.numberPixelY:
            self.numberPixelY.export(outfile, level, name_='numberPixelY')
        if self.pixelSizeX:
            self.pixelSizeX.export(outfile, level, name_='pixelSizeX')
        if self.pixelSizeY:
            self.pixelSizeY.export(outfile, level, name_='pixelSizeY')
        if self.serialNumber:
            self.serialNumber.export(outfile, level, name_='serialNumber')
        if self.twoTheta:
            self.twoTheta.export(outfile, level, name_='twoTheta')
        if self.typexx:
            self.typexx.export(outfile, level, name_='type')
        XSData.exportChildren(self, outfile, level, name_)

    #Only to export the entire XML tree to a file stream on disk
    def outputFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write("<?xml version=\"1.0\" ?>\n")
        self.export( outfile, 0, name_='XSDataDetector' )
        outfile.close()


    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataDetector.factory()
        rootObj.build(rootNode)
        return rootObj
    parseString = staticmethod( parseString ) 


    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataDetector.factory()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile ) 


    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO.StringIO()
        oStreamString.write('<?xml version="1.0" ?>\n')
        self.export( oStreamString, 0, name_="XSDataDetector" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    def exportLiteral(self, outfile, level, name_='XSDataDetector'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        pass
        XSData.exportLiteralAttributes(self, outfile, level, name_)
    def exportLiteralChildren(self, outfile, level, name_):
        if self.beamPositionX:
            showIndent(outfile, level)
            outfile.write('beamPositionX=XSDataLength(\n')
            self.beamPositionX.exportLiteral(outfile, level, name_='beamPositionX')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.beamPositionY:
            showIndent(outfile, level)
            outfile.write('beamPositionY=XSDataLength(\n')
            self.beamPositionY.exportLiteral(outfile, level, name_='beamPositionY')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.bin:
            showIndent(outfile, level)
            outfile.write('bin=XSDataString(\n')
            self.bin.exportLiteral(outfile, level, name_='bin')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.byteOrder:
            showIndent(outfile, level)
            outfile.write('byteOrder=XSDataString(\n')
            self.byteOrder.exportLiteral(outfile, level, name_='byteOrder')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.dataType:
            showIndent(outfile, level)
            outfile.write('dataType=XSDataString(\n')
            self.dataType.exportLiteral(outfile, level, name_='dataType')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.distance:
            showIndent(outfile, level)
            outfile.write('distance=XSDataLength(\n')
            self.distance.exportLiteral(outfile, level, name_='distance')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.gain:
            showIndent(outfile, level)
            outfile.write('gain=XSDataFloat(\n')
            self.gain.exportLiteral(outfile, level, name_='gain')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.imageSaturation:
            showIndent(outfile, level)
            outfile.write('imageSaturation=XSDataInteger(\n')
            self.imageSaturation.exportLiteral(outfile, level, name_='imageSaturation')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.name:
            showIndent(outfile, level)
            outfile.write('name=XSDataString(\n')
            self.name.exportLiteral(outfile, level, name_='name')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.numberBytesInHeader:
            showIndent(outfile, level)
            outfile.write('numberBytesInHeader=XSDataInteger(\n')
            self.numberBytesInHeader.exportLiteral(outfile, level, name_='numberBytesInHeader')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.numberPixelX:
            showIndent(outfile, level)
            outfile.write('numberPixelX=XSDataInteger(\n')
            self.numberPixelX.exportLiteral(outfile, level, name_='numberPixelX')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.numberPixelY:
            showIndent(outfile, level)
            outfile.write('numberPixelY=XSDataInteger(\n')
            self.numberPixelY.exportLiteral(outfile, level, name_='numberPixelY')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.pixelSizeX:
            showIndent(outfile, level)
            outfile.write('pixelSizeX=XSDataFloat(\n')
            self.pixelSizeX.exportLiteral(outfile, level, name_='pixelSizeX')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.pixelSizeY:
            showIndent(outfile, level)
            outfile.write('pixelSizeY=XSDataFloat(\n')
            self.pixelSizeY.exportLiteral(outfile, level, name_='pixelSizeY')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.serialNumber:
            showIndent(outfile, level)
            outfile.write('serialNumber=XSDataString(\n')
            self.serialNumber.exportLiteral(outfile, level, name_='serialNumber')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.twoTheta:
            showIndent(outfile, level)
            outfile.write('twoTheta=XSDataAngle(\n')
            self.twoTheta.exportLiteral(outfile, level, name_='twoTheta')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.typexx:
            showIndent(outfile, level)
            outfile.write('typexx=XSDataString(\n')
            self.typexx.exportLiteral(outfile, level, name_='type')
            showIndent(outfile, level)
            outfile.write('),\n')
        XSData.exportLiteralChildren(self, outfile, level, name_)
    def build(self, node_):
        attrs = node_.attributes
        self.buildAttributes(attrs)
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildAttributes(self, attrs):
        XSData.buildAttributes(self, attrs)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'beamPositionX':
            obj_ = XSDataLength.factory()
            obj_.build(child_)
            self.setBeamPositionX(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'beamPositionY':
            obj_ = XSDataLength.factory()
            obj_.build(child_)
            self.setBeamPositionY(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'bin':
            obj_ = XSDataString.factory()
            obj_.build(child_)
            self.setBin(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'byteOrder':
            obj_ = XSDataString.factory()
            obj_.build(child_)
            self.setByteOrder(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'dataType':
            obj_ = XSDataString.factory()
            obj_.build(child_)
            self.setDataType(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'distance':
            obj_ = XSDataLength.factory()
            obj_.build(child_)
            self.setDistance(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'gain':
            obj_ = XSDataFloat.factory()
            obj_.build(child_)
            self.setGain(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'imageSaturation':
            obj_ = XSDataInteger.factory()
            obj_.build(child_)
            self.setImageSaturation(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'name':
            obj_ = XSDataString.factory()
            obj_.build(child_)
            self.setName(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'numberBytesInHeader':
            obj_ = XSDataInteger.factory()
            obj_.build(child_)
            self.setNumberBytesInHeader(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'numberPixelX':
            obj_ = XSDataInteger.factory()
            obj_.build(child_)
            self.setNumberPixelX(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'numberPixelY':
            obj_ = XSDataInteger.factory()
            obj_.build(child_)
            self.setNumberPixelY(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'pixelSizeX':
            obj_ = XSDataFloat.factory()
            obj_.build(child_)
            self.setPixelSizeX(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'pixelSizeY':
            obj_ = XSDataFloat.factory()
            obj_.build(child_)
            self.setPixelSizeY(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'serialNumber':
            obj_ = XSDataString.factory()
            obj_.build(child_)
            self.setSerialNumber(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'twoTheta':
            obj_ = XSDataAngle.factory()
            obj_.build(child_)
            self.setTwoTheta(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'type':
            obj_ = XSDataString.factory()
            obj_.build(child_)
            self.setType(obj_)
# end class XSDataDetector


class XSDataDiffractionPlan(XSData):
    subclass = None
    def __init__(self, aimedCompleteness=None, aimedIOverSigmaAtHighestResolution=None, aimedMultiplicity=None, aimedResolution=None, anomalousData=None, complexity=None, detectorMaxResolution=None, detectorMinResolution=None, estimateRadiationDamage=None, forcedSpaceGroup=None, maxExposureTimePerDataCollection=None, requiredCompleteness=None, requiredMultiplicity=None, requiredResolution=None, strategyOption=None, minExposureTimePerImage=None, goniostatMaxOscillationSpeed=None, goniostatMinOscillationWidth=None, minTransmission=None):
        XSData.__init__(self)
        self.aimedCompleteness = aimedCompleteness
        self.aimedIOverSigmaAtHighestResolution = aimedIOverSigmaAtHighestResolution
        self.aimedMultiplicity = aimedMultiplicity
        self.aimedResolution = aimedResolution
        self.anomalousData = anomalousData
        self.complexity = complexity
        self.detectorMaxResolution = detectorMaxResolution
        self.detectorMinResolution = detectorMinResolution
        self.estimateRadiationDamage = estimateRadiationDamage
        self.forcedSpaceGroup = forcedSpaceGroup
        self.maxExposureTimePerDataCollection = maxExposureTimePerDataCollection
        self.requiredCompleteness = requiredCompleteness
        self.requiredMultiplicity = requiredMultiplicity
        self.requiredResolution = requiredResolution
        self.strategyOption = strategyOption
        self.minExposureTimePerImage = minExposureTimePerImage
        self.goniostatMaxOscillationSpeed = goniostatMaxOscillationSpeed
        self.goniostatMinOscillationWidth = goniostatMinOscillationWidth
        self.minTransmission = minTransmission
    def factory(*args_, **kwargs_):
        if XSDataDiffractionPlan.subclass:
            return XSDataDiffractionPlan.subclass(*args_, **kwargs_)
        else:
            return XSDataDiffractionPlan(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getAimedCompleteness(self): return self.aimedCompleteness
    def setAimedCompleteness(self, aimedCompleteness): self.aimedCompleteness = aimedCompleteness
    def getAimedIOverSigmaAtHighestResolution(self): return self.aimedIOverSigmaAtHighestResolution
    def setAimedIOverSigmaAtHighestResolution(self, aimedIOverSigmaAtHighestResolution): self.aimedIOverSigmaAtHighestResolution = aimedIOverSigmaAtHighestResolution
    def getAimedMultiplicity(self): return self.aimedMultiplicity
    def setAimedMultiplicity(self, aimedMultiplicity): self.aimedMultiplicity = aimedMultiplicity
    def getAimedResolution(self): return self.aimedResolution
    def setAimedResolution(self, aimedResolution): self.aimedResolution = aimedResolution
    def getAnomalousData(self): return self.anomalousData
    def setAnomalousData(self, anomalousData): self.anomalousData = anomalousData
    def getComplexity(self): return self.complexity
    def setComplexity(self, complexity): self.complexity = complexity
    def getDetectorMaxResolution(self): return self.detectorMaxResolution
    def setDetectorMaxResolution(self, detectorMaxResolution): self.detectorMaxResolution = detectorMaxResolution
    def getDetectorMinResolution(self): return self.detectorMinResolution
    def setDetectorMinResolution(self, detectorMinResolution): self.detectorMinResolution = detectorMinResolution
    def getEstimateRadiationDamage(self): return self.estimateRadiationDamage
    def setEstimateRadiationDamage(self, estimateRadiationDamage): self.estimateRadiationDamage = estimateRadiationDamage
    def getForcedSpaceGroup(self): return self.forcedSpaceGroup
    def setForcedSpaceGroup(self, forcedSpaceGroup): self.forcedSpaceGroup = forcedSpaceGroup
    def getMaxExposureTimePerDataCollection(self): return self.maxExposureTimePerDataCollection
    def setMaxExposureTimePerDataCollection(self, maxExposureTimePerDataCollection): self.maxExposureTimePerDataCollection = maxExposureTimePerDataCollection
    def getRequiredCompleteness(self): return self.requiredCompleteness
    def setRequiredCompleteness(self, requiredCompleteness): self.requiredCompleteness = requiredCompleteness
    def getRequiredMultiplicity(self): return self.requiredMultiplicity
    def setRequiredMultiplicity(self, requiredMultiplicity): self.requiredMultiplicity = requiredMultiplicity
    def getRequiredResolution(self): return self.requiredResolution
    def setRequiredResolution(self, requiredResolution): self.requiredResolution = requiredResolution
    def getStrategyOption(self): return self.strategyOption
    def setStrategyOption(self, strategyOption): self.strategyOption = strategyOption
    def getMinExposureTimePerImage(self): return self.minExposureTimePerImage
    def setMinExposureTimePerImage(self, minExposureTimePerImage): self.minExposureTimePerImage = minExposureTimePerImage
    def getGoniostatMaxOscillationSpeed(self): return self.goniostatMaxOscillationSpeed
    def setGoniostatMaxOscillationSpeed(self, goniostatMaxOscillationSpeed): self.goniostatMaxOscillationSpeed = goniostatMaxOscillationSpeed
    def getGoniostatMinOscillationWidth(self): return self.goniostatMinOscillationWidth
    def setGoniostatMinOscillationWidth(self, goniostatMinOscillationWidth): self.goniostatMinOscillationWidth = goniostatMinOscillationWidth
    def getMinTransmission(self): return self.minTransmission
    def setMinTransmission(self, minTransmission): self.minTransmission = minTransmission
    def export(self, outfile, level, name_='XSDataDiffractionPlan'):
        showIndent(outfile, level)
        outfile.write('<%s>\n' % name_)
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='XSDataDiffractionPlan'):
        XSData.exportAttributes(self, outfile, level, name_='XSDataDiffractionPlan')
    def exportChildren(self, outfile, level, name_='XSDataDiffractionPlan'):
        if self.aimedCompleteness:
            self.aimedCompleteness.export(outfile, level, name_='aimedCompleteness')
        if self.aimedIOverSigmaAtHighestResolution:
            self.aimedIOverSigmaAtHighestResolution.export(outfile, level, name_='aimedIOverSigmaAtHighestResolution')
        if self.aimedMultiplicity:
            self.aimedMultiplicity.export(outfile, level, name_='aimedMultiplicity')
        if self.aimedResolution:
            self.aimedResolution.export(outfile, level, name_='aimedResolution')
        if self.anomalousData:
            self.anomalousData.export(outfile, level, name_='anomalousData')
        if self.complexity:
            self.complexity.export(outfile, level, name_='complexity')
        if self.detectorMaxResolution:
            self.detectorMaxResolution.export(outfile, level, name_='detectorMaxResolution')
        if self.detectorMinResolution:
            self.detectorMinResolution.export(outfile, level, name_='detectorMinResolution')
        if self.estimateRadiationDamage:
            self.estimateRadiationDamage.export(outfile, level, name_='estimateRadiationDamage')
        if self.forcedSpaceGroup:
            self.forcedSpaceGroup.export(outfile, level, name_='forcedSpaceGroup')
        if self.maxExposureTimePerDataCollection:
            self.maxExposureTimePerDataCollection.export(outfile, level, name_='maxExposureTimePerDataCollection')
        if self.requiredCompleteness:
            self.requiredCompleteness.export(outfile, level, name_='requiredCompleteness')
        if self.requiredMultiplicity:
            self.requiredMultiplicity.export(outfile, level, name_='requiredMultiplicity')
        if self.requiredResolution:
            self.requiredResolution.export(outfile, level, name_='requiredResolution')
        if self.strategyOption:
            self.strategyOption.export(outfile, level, name_='strategyOption')
        if self.minExposureTimePerImage:
            self.minExposureTimePerImage.export(outfile, level, name_='minExposureTimePerImage')
        if self.goniostatMaxOscillationSpeed:
            self.goniostatMaxOscillationSpeed.export(outfile, level, name_='goniostatMaxOscillationSpeed')
        if self.goniostatMinOscillationWidth:
            self.goniostatMinOscillationWidth.export(outfile, level, name_='goniostatMinOscillationWidth')
        if self.minTransmission:
            self.minTransmission.export(outfile, level, name_='minTransmission')
        XSData.exportChildren(self, outfile, level, name_)

    #Only to export the entire XML tree to a file stream on disk
    def outputFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write("<?xml version=\"1.0\" ?>\n")
        self.export( outfile, 0, name_='XSDataDiffractionPlan' )
        outfile.close()


    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataDiffractionPlan.factory()
        rootObj.build(rootNode)
        return rootObj
    parseString = staticmethod( parseString ) 


    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataDiffractionPlan.factory()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile ) 


    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO.StringIO()
        oStreamString.write('<?xml version="1.0" ?>\n')
        self.export( oStreamString, 0, name_="XSDataDiffractionPlan" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    def exportLiteral(self, outfile, level, name_='XSDataDiffractionPlan'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        pass
        XSData.exportLiteralAttributes(self, outfile, level, name_)
    def exportLiteralChildren(self, outfile, level, name_):
        if self.aimedCompleteness:
            showIndent(outfile, level)
            outfile.write('aimedCompleteness=XSDataDouble(\n')
            self.aimedCompleteness.exportLiteral(outfile, level, name_='aimedCompleteness')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.aimedIOverSigmaAtHighestResolution:
            showIndent(outfile, level)
            outfile.write('aimedIOverSigmaAtHighestResolution=XSDataDouble(\n')
            self.aimedIOverSigmaAtHighestResolution.exportLiteral(outfile, level, name_='aimedIOverSigmaAtHighestResolution')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.aimedMultiplicity:
            showIndent(outfile, level)
            outfile.write('aimedMultiplicity=XSDataDouble(\n')
            self.aimedMultiplicity.exportLiteral(outfile, level, name_='aimedMultiplicity')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.aimedResolution:
            showIndent(outfile, level)
            outfile.write('aimedResolution=XSDataDouble(\n')
            self.aimedResolution.exportLiteral(outfile, level, name_='aimedResolution')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.anomalousData:
            showIndent(outfile, level)
            outfile.write('anomalousData=XSDataBoolean(\n')
            self.anomalousData.exportLiteral(outfile, level, name_='anomalousData')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.complexity:
            showIndent(outfile, level)
            outfile.write('complexity=XSDataString(\n')
            self.complexity.exportLiteral(outfile, level, name_='complexity')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.detectorMaxResolution:
            showIndent(outfile, level)
            outfile.write('detectorMaxResolution=XSDataDouble(\n')
            self.detectorMaxResolution.exportLiteral(outfile, level, name_='detectorMaxResolution')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.detectorMinResolution:
            showIndent(outfile, level)
            outfile.write('detectorMinResolution=XSDataDouble(\n')
            self.detectorMinResolution.exportLiteral(outfile, level, name_='detectorMinResolution')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.estimateRadiationDamage:
            showIndent(outfile, level)
            outfile.write('estimateRadiationDamage=XSDataBoolean(\n')
            self.estimateRadiationDamage.exportLiteral(outfile, level, name_='estimateRadiationDamage')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.forcedSpaceGroup:
            showIndent(outfile, level)
            outfile.write('forcedSpaceGroup=XSDataString(\n')
            self.forcedSpaceGroup.exportLiteral(outfile, level, name_='forcedSpaceGroup')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.maxExposureTimePerDataCollection:
            showIndent(outfile, level)
            outfile.write('maxExposureTimePerDataCollection=XSDataTime(\n')
            self.maxExposureTimePerDataCollection.exportLiteral(outfile, level, name_='maxExposureTimePerDataCollection')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.requiredCompleteness:
            showIndent(outfile, level)
            outfile.write('requiredCompleteness=XSDataDouble(\n')
            self.requiredCompleteness.exportLiteral(outfile, level, name_='requiredCompleteness')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.requiredMultiplicity:
            showIndent(outfile, level)
            outfile.write('requiredMultiplicity=XSDataDouble(\n')
            self.requiredMultiplicity.exportLiteral(outfile, level, name_='requiredMultiplicity')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.requiredResolution:
            showIndent(outfile, level)
            outfile.write('requiredResolution=XSDataDouble(\n')
            self.requiredResolution.exportLiteral(outfile, level, name_='requiredResolution')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.strategyOption:
            showIndent(outfile, level)
            outfile.write('strategyOption=XSDataString(\n')
            self.strategyOption.exportLiteral(outfile, level, name_='strategyOption')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.minExposureTimePerImage:
            showIndent(outfile, level)
            outfile.write('minExposureTimePerImage=XSDataTime(\n')
            self.minExposureTimePerImage.exportLiteral(outfile, level, name_='minExposureTimePerImage')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.goniostatMaxOscillationSpeed:
            showIndent(outfile, level)
            outfile.write('goniostatMaxOscillationSpeed=XSDataAngularSpeed(\n')
            self.goniostatMaxOscillationSpeed.exportLiteral(outfile, level, name_='goniostatMaxOscillationSpeed')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.goniostatMinOscillationWidth:
            showIndent(outfile, level)
            outfile.write('goniostatMinOscillationWidth=XSDataAngle(\n')
            self.goniostatMinOscillationWidth.exportLiteral(outfile, level, name_='goniostatMinOscillationWidth')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.minTransmission:
            showIndent(outfile, level)
            outfile.write('minTransmission=XSDataDouble(\n')
            self.minTransmission.exportLiteral(outfile, level, name_='minTransmission')
            showIndent(outfile, level)
            outfile.write('),\n')
        XSData.exportLiteralChildren(self, outfile, level, name_)
    def build(self, node_):
        attrs = node_.attributes
        self.buildAttributes(attrs)
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildAttributes(self, attrs):
        XSData.buildAttributes(self, attrs)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'aimedCompleteness':
            obj_ = XSDataDouble.factory()
            obj_.build(child_)
            self.setAimedCompleteness(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'aimedIOverSigmaAtHighestResolution':
            obj_ = XSDataDouble.factory()
            obj_.build(child_)
            self.setAimedIOverSigmaAtHighestResolution(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'aimedMultiplicity':
            obj_ = XSDataDouble.factory()
            obj_.build(child_)
            self.setAimedMultiplicity(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'aimedResolution':
            obj_ = XSDataDouble.factory()
            obj_.build(child_)
            self.setAimedResolution(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'anomalousData':
            obj_ = XSDataBoolean.factory()
            obj_.build(child_)
            self.setAnomalousData(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'complexity':
            obj_ = XSDataString.factory()
            obj_.build(child_)
            self.setComplexity(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'detectorMaxResolution':
            obj_ = XSDataDouble.factory()
            obj_.build(child_)
            self.setDetectorMaxResolution(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'detectorMinResolution':
            obj_ = XSDataDouble.factory()
            obj_.build(child_)
            self.setDetectorMinResolution(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'estimateRadiationDamage':
            obj_ = XSDataBoolean.factory()
            obj_.build(child_)
            self.setEstimateRadiationDamage(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'forcedSpaceGroup':
            obj_ = XSDataString.factory()
            obj_.build(child_)
            self.setForcedSpaceGroup(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'maxExposureTimePerDataCollection':
            obj_ = XSDataTime.factory()
            obj_.build(child_)
            self.setMaxExposureTimePerDataCollection(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'requiredCompleteness':
            obj_ = XSDataDouble.factory()
            obj_.build(child_)
            self.setRequiredCompleteness(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'requiredMultiplicity':
            obj_ = XSDataDouble.factory()
            obj_.build(child_)
            self.setRequiredMultiplicity(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'requiredResolution':
            obj_ = XSDataDouble.factory()
            obj_.build(child_)
            self.setRequiredResolution(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'strategyOption':
            obj_ = XSDataString.factory()
            obj_.build(child_)
            self.setStrategyOption(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'minExposureTimePerImage':
            obj_ = XSDataTime.factory()
            obj_.build(child_)
            self.setMinExposureTimePerImage(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'goniostatMaxOscillationSpeed':
            obj_ = XSDataAngularSpeed.factory()
            obj_.build(child_)
            self.setGoniostatMaxOscillationSpeed(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'goniostatMinOscillationWidth':
            obj_ = XSDataAngle.factory()
            obj_.build(child_)
            self.setGoniostatMinOscillationWidth(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'minTransmission':
            obj_ = XSDataDouble.factory()
            obj_.build(child_)
            self.setMinTransmission(obj_)
# end class XSDataDiffractionPlan


class XSDataExperimentalCondition(XSData):
    subclass = None
    def __init__(self, beam=None, detector=None, goniostat=None):
        XSData.__init__(self)
        self.beam = beam
        self.detector = detector
        self.goniostat = goniostat
    def factory(*args_, **kwargs_):
        if XSDataExperimentalCondition.subclass:
            return XSDataExperimentalCondition.subclass(*args_, **kwargs_)
        else:
            return XSDataExperimentalCondition(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getBeam(self): return self.beam
    def setBeam(self, beam): self.beam = beam
    def getDetector(self): return self.detector
    def setDetector(self, detector): self.detector = detector
    def getGoniostat(self): return self.goniostat
    def setGoniostat(self, goniostat): self.goniostat = goniostat
    def export(self, outfile, level, name_='XSDataExperimentalCondition'):
        showIndent(outfile, level)
        outfile.write('<%s>\n' % name_)
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='XSDataExperimentalCondition'):
        XSData.exportAttributes(self, outfile, level, name_='XSDataExperimentalCondition')
    def exportChildren(self, outfile, level, name_='XSDataExperimentalCondition'):
        if self.getBeam() != None :
            if self.beam:
                self.beam.export(outfile, level, name_='beam')
        if self.getDetector() != None :
            if self.detector:
                self.detector.export(outfile, level, name_='detector')
        if self.getGoniostat() != None :
            if self.goniostat:
                self.goniostat.export(outfile, level, name_='goniostat')
        XSData.exportChildren(self, outfile, level, name_)

    #Only to export the entire XML tree to a file stream on disk
    def outputFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write("<?xml version=\"1.0\" ?>\n")
        self.export( outfile, 0, name_='XSDataExperimentalCondition' )
        outfile.close()


    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataExperimentalCondition.factory()
        rootObj.build(rootNode)
        return rootObj
    parseString = staticmethod( parseString ) 


    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataExperimentalCondition.factory()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile ) 


    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO.StringIO()
        oStreamString.write('<?xml version="1.0" ?>\n')
        self.export( oStreamString, 0, name_="XSDataExperimentalCondition" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    def exportLiteral(self, outfile, level, name_='XSDataExperimentalCondition'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        pass
        XSData.exportLiteralAttributes(self, outfile, level, name_)
    def exportLiteralChildren(self, outfile, level, name_):
        if self.beam:
            showIndent(outfile, level)
            outfile.write('beam=XSDataBeam(\n')
            self.beam.exportLiteral(outfile, level, name_='beam')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.detector:
            showIndent(outfile, level)
            outfile.write('detector=XSDataDetector(\n')
            self.detector.exportLiteral(outfile, level, name_='detector')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.goniostat:
            showIndent(outfile, level)
            outfile.write('goniostat=XSDataGoniostat(\n')
            self.goniostat.exportLiteral(outfile, level, name_='goniostat')
            showIndent(outfile, level)
            outfile.write('),\n')
        XSData.exportLiteralChildren(self, outfile, level, name_)
    def build(self, node_):
        attrs = node_.attributes
        self.buildAttributes(attrs)
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildAttributes(self, attrs):
        XSData.buildAttributes(self, attrs)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'beam':
            obj_ = XSDataBeam.factory()
            obj_.build(child_)
            self.setBeam(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'detector':
            obj_ = XSDataDetector.factory()
            obj_.build(child_)
            self.setDetector(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'goniostat':
            obj_ = XSDataGoniostat.factory()
            obj_.build(child_)
            self.setGoniostat(obj_)
# end class XSDataExperimentalCondition


class XSDataGeneratePredictionInput(XSDataInput):
    subclass = None
    def __init__(self, configuration=None, dataCollection=None, selectedIndexingSolution=None):
        XSDataInput.__init__(self, configuration)
        self.dataCollection = dataCollection
        self.selectedIndexingSolution = selectedIndexingSolution
    def factory(*args_, **kwargs_):
        if XSDataGeneratePredictionInput.subclass:
            return XSDataGeneratePredictionInput.subclass(*args_, **kwargs_)
        else:
            return XSDataGeneratePredictionInput(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getDataCollection(self): return self.dataCollection
    def setDataCollection(self, dataCollection): self.dataCollection = dataCollection
    def getSelectedIndexingSolution(self): return self.selectedIndexingSolution
    def setSelectedIndexingSolution(self, selectedIndexingSolution): self.selectedIndexingSolution = selectedIndexingSolution
    def export(self, outfile, level, name_='XSDataGeneratePredictionInput'):
        showIndent(outfile, level)
        outfile.write('<%s>\n' % name_)
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='XSDataGeneratePredictionInput'):
        XSDataInput.exportAttributes(self, outfile, level, name_='XSDataGeneratePredictionInput')
    def exportChildren(self, outfile, level, name_='XSDataGeneratePredictionInput'):
        if self.dataCollection:
            self.dataCollection.export(outfile, level, name_='dataCollection')
        if self.selectedIndexingSolution:
            self.selectedIndexingSolution.export(outfile, level, name_='selectedIndexingSolution')
        XSDataInput.exportChildren(self, outfile, level, name_)

    #Only to export the entire XML tree to a file stream on disk
    def outputFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write("<?xml version=\"1.0\" ?>\n")
        self.export( outfile, 0, name_='XSDataGeneratePredictionInput' )
        outfile.close()


    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataGeneratePredictionInput.factory()
        rootObj.build(rootNode)
        return rootObj
    parseString = staticmethod( parseString ) 


    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataGeneratePredictionInput.factory()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile ) 


    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO.StringIO()
        oStreamString.write('<?xml version="1.0" ?>\n')
        self.export( oStreamString, 0, name_="XSDataGeneratePredictionInput" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    def exportLiteral(self, outfile, level, name_='XSDataGeneratePredictionInput'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        pass
        XSDataInput.exportLiteralAttributes(self, outfile, level, name_)
    def exportLiteralChildren(self, outfile, level, name_):
        if self.dataCollection:
            showIndent(outfile, level)
            outfile.write('dataCollection=XSDataCollection(\n')
            self.dataCollection.exportLiteral(outfile, level, name_='dataCollection')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.selectedIndexingSolution:
            showIndent(outfile, level)
            outfile.write('selectedIndexingSolution=XSDataIndexingSolutionSelected(\n')
            self.selectedIndexingSolution.exportLiteral(outfile, level, name_='selectedIndexingSolution')
            showIndent(outfile, level)
            outfile.write('),\n')
        XSDataInput.exportLiteralChildren(self, outfile, level, name_)
    def build(self, node_):
        attrs = node_.attributes
        self.buildAttributes(attrs)
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildAttributes(self, attrs):
        XSDataInput.buildAttributes(self, attrs)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'dataCollection':
            obj_ = XSDataCollection.factory()
            obj_.build(child_)
            self.setDataCollection(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'selectedIndexingSolution':
            obj_ = XSDataIndexingSolutionSelected.factory()
            obj_.build(child_)
            self.setSelectedIndexingSolution(obj_)
        XSDataInput.buildChildren(self, child_, nodeName_)
# end class XSDataGeneratePredictionInput


class XSDataGeneratePredictionResult(XSDataResult):
    subclass = None
    def __init__(self, predictionImage=None):
        XSDataResult.__init__(self)
        if predictionImage is None:
            self.predictionImage = []
        else:
            self.predictionImage = predictionImage
    def factory(*args_, **kwargs_):
        if XSDataGeneratePredictionResult.subclass:
            return XSDataGeneratePredictionResult.subclass(*args_, **kwargs_)
        else:
            return XSDataGeneratePredictionResult(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getPredictionImage(self): return self.predictionImage
    def setPredictionImage(self, predictionImage): self.predictionImage = predictionImage
    def addPredictionImage(self, value): self.predictionImage.append(value)
    def insertPredictionImage(self, index, value): self.predictionImage[index] = value
    def export(self, outfile, level, name_='XSDataGeneratePredictionResult'):
        showIndent(outfile, level)
        outfile.write('<%s>\n' % name_)
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='XSDataGeneratePredictionResult'):
        XSDataResult.exportAttributes(self, outfile, level, name_='XSDataGeneratePredictionResult')
    def exportChildren(self, outfile, level, name_='XSDataGeneratePredictionResult'):
        for predictionImage_ in self.getPredictionImage():
            predictionImage_.export(outfile, level, name_='predictionImage')
        XSDataResult.exportChildren(self, outfile, level, name_)

    #Only to export the entire XML tree to a file stream on disk
    def outputFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write("<?xml version=\"1.0\" ?>\n")
        self.export( outfile, 0, name_='XSDataGeneratePredictionResult' )
        outfile.close()


    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataGeneratePredictionResult.factory()
        rootObj.build(rootNode)
        return rootObj
    parseString = staticmethod( parseString ) 


    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataGeneratePredictionResult.factory()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile ) 


    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO.StringIO()
        oStreamString.write('<?xml version="1.0" ?>\n')
        self.export( oStreamString, 0, name_="XSDataGeneratePredictionResult" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    def exportLiteral(self, outfile, level, name_='XSDataGeneratePredictionResult'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        pass
        XSDataResult.exportLiteralAttributes(self, outfile, level, name_)
    def exportLiteralChildren(self, outfile, level, name_):
        showIndent(outfile, level)
        outfile.write('predictionImage=[\n')
        level += 1
        for predictionImage in self.predictionImage:
            showIndent(outfile, level)
            outfile.write('XSDataImage(\n')
            predictionImage.exportLiteral(outfile, level, name_='predictionImage')
            showIndent(outfile, level)
            outfile.write('),\n')
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
        XSDataResult.exportLiteralChildren(self, outfile, level, name_)
    def build(self, node_):
        attrs = node_.attributes
        self.buildAttributes(attrs)
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildAttributes(self, attrs):
        XSDataResult.buildAttributes(self, attrs)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'predictionImage':
            obj_ = XSDataImage.factory()
            obj_.build(child_)
            self.predictionImage.append(obj_)
# end class XSDataGeneratePredictionResult


class XSDataGoniostat(XSData):
    subclass = None
    def __init__(self, maxOscillationSpeed=None, minOscillationWidth=None, oscillationWidth=None, rotationAxis=None, rotationAxisEnd=None, rotationAxisStart=None):
        XSData.__init__(self)
        self.maxOscillationSpeed = maxOscillationSpeed
        self.minOscillationWidth = minOscillationWidth
        self.oscillationWidth = oscillationWidth
        self.rotationAxis = rotationAxis
        self.rotationAxisEnd = rotationAxisEnd
        self.rotationAxisStart = rotationAxisStart
    def factory(*args_, **kwargs_):
        if XSDataGoniostat.subclass:
            return XSDataGoniostat.subclass(*args_, **kwargs_)
        else:
            return XSDataGoniostat(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getMaxOscillationSpeed(self): return self.maxOscillationSpeed
    def setMaxOscillationSpeed(self, maxOscillationSpeed): self.maxOscillationSpeed = maxOscillationSpeed
    def getMinOscillationWidth(self): return self.minOscillationWidth
    def setMinOscillationWidth(self, minOscillationWidth): self.minOscillationWidth = minOscillationWidth
    def getOscillationWidth(self): return self.oscillationWidth
    def setOscillationWidth(self, oscillationWidth): self.oscillationWidth = oscillationWidth
    def getRotationAxis(self): return self.rotationAxis
    def setRotationAxis(self, rotationAxis): self.rotationAxis = rotationAxis
    def getRotationAxisEnd(self): return self.rotationAxisEnd
    def setRotationAxisEnd(self, rotationAxisEnd): self.rotationAxisEnd = rotationAxisEnd
    def getRotationAxisStart(self): return self.rotationAxisStart
    def setRotationAxisStart(self, rotationAxisStart): self.rotationAxisStart = rotationAxisStart
    def export(self, outfile, level, name_='XSDataGoniostat'):
        showIndent(outfile, level)
        outfile.write('<%s>\n' % name_)
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='XSDataGoniostat'):
        XSData.exportAttributes(self, outfile, level, name_='XSDataGoniostat')
    def exportChildren(self, outfile, level, name_='XSDataGoniostat'):
        if self.maxOscillationSpeed:
            self.maxOscillationSpeed.export(outfile, level, name_='maxOscillationSpeed')
        if self.minOscillationWidth:
            self.minOscillationWidth.export(outfile, level, name_='minOscillationWidth')
        if self.oscillationWidth:
            self.oscillationWidth.export(outfile, level, name_='oscillationWidth')
        if self.rotationAxis:
            self.rotationAxis.export(outfile, level, name_='rotationAxis')
        if self.rotationAxisEnd:
            self.rotationAxisEnd.export(outfile, level, name_='rotationAxisEnd')
        if self.rotationAxisStart:
            self.rotationAxisStart.export(outfile, level, name_='rotationAxisStart')
        XSData.exportChildren(self, outfile, level, name_)

    #Only to export the entire XML tree to a file stream on disk
    def outputFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write("<?xml version=\"1.0\" ?>\n")
        self.export( outfile, 0, name_='XSDataGoniostat' )
        outfile.close()


    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataGoniostat.factory()
        rootObj.build(rootNode)
        return rootObj
    parseString = staticmethod( parseString ) 


    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataGoniostat.factory()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile ) 


    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO.StringIO()
        oStreamString.write('<?xml version="1.0" ?>\n')
        self.export( oStreamString, 0, name_="XSDataGoniostat" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    def exportLiteral(self, outfile, level, name_='XSDataGoniostat'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        pass
        XSData.exportLiteralAttributes(self, outfile, level, name_)
    def exportLiteralChildren(self, outfile, level, name_):
        if self.maxOscillationSpeed:
            showIndent(outfile, level)
            outfile.write('maxOscillationSpeed=XSDataAngularSpeed(\n')
            self.maxOscillationSpeed.exportLiteral(outfile, level, name_='maxOscillationSpeed')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.minOscillationWidth:
            showIndent(outfile, level)
            outfile.write('minOscillationWidth=XSDataAngle(\n')
            self.minOscillationWidth.exportLiteral(outfile, level, name_='minOscillationWidth')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.oscillationWidth:
            showIndent(outfile, level)
            outfile.write('oscillationWidth=XSDataAngle(\n')
            self.oscillationWidth.exportLiteral(outfile, level, name_='oscillationWidth')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.rotationAxis:
            showIndent(outfile, level)
            outfile.write('rotationAxis=XSDataString(\n')
            self.rotationAxis.exportLiteral(outfile, level, name_='rotationAxis')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.rotationAxisEnd:
            showIndent(outfile, level)
            outfile.write('rotationAxisEnd=XSDataAngle(\n')
            self.rotationAxisEnd.exportLiteral(outfile, level, name_='rotationAxisEnd')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.rotationAxisStart:
            showIndent(outfile, level)
            outfile.write('rotationAxisStart=XSDataAngle(\n')
            self.rotationAxisStart.exportLiteral(outfile, level, name_='rotationAxisStart')
            showIndent(outfile, level)
            outfile.write('),\n')
        XSData.exportLiteralChildren(self, outfile, level, name_)
    def build(self, node_):
        attrs = node_.attributes
        self.buildAttributes(attrs)
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildAttributes(self, attrs):
        XSData.buildAttributes(self, attrs)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'maxOscillationSpeed':
            obj_ = XSDataAngularSpeed.factory()
            obj_.build(child_)
            self.setMaxOscillationSpeed(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'minOscillationWidth':
            obj_ = XSDataAngle.factory()
            obj_.build(child_)
            self.setMinOscillationWidth(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'oscillationWidth':
            obj_ = XSDataAngle.factory()
            obj_.build(child_)
            self.setOscillationWidth(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'rotationAxis':
            obj_ = XSDataString.factory()
            obj_.build(child_)
            self.setRotationAxis(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'rotationAxisEnd':
            obj_ = XSDataAngle.factory()
            obj_.build(child_)
            self.setRotationAxisEnd(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'rotationAxisStart':
            obj_ = XSDataAngle.factory()
            obj_.build(child_)
            self.setRotationAxisStart(obj_)
# end class XSDataGoniostat


class XSDataImageQualityIndicators(XSData):
    subclass = None
    def __init__(self, binPopCutOffMethod2Res=None, goodBraggCandidates=None, iceRings=None, image=None, inResolutionOvrlSpots=None, inResTotal=None, maxUnitCell=None, method1Res=None, method2Res=None, pctSaturationTop50Peaks=None, spotTotal=None):
        XSData.__init__(self)
        self.binPopCutOffMethod2Res = binPopCutOffMethod2Res
        self.goodBraggCandidates = goodBraggCandidates
        self.iceRings = iceRings
        self.image = image
        self.inResolutionOvrlSpots = inResolutionOvrlSpots
        self.inResTotal = inResTotal
        self.maxUnitCell = maxUnitCell
        self.method1Res = method1Res
        self.method2Res = method2Res
        self.pctSaturationTop50Peaks = pctSaturationTop50Peaks
        self.spotTotal = spotTotal
    def factory(*args_, **kwargs_):
        if XSDataImageQualityIndicators.subclass:
            return XSDataImageQualityIndicators.subclass(*args_, **kwargs_)
        else:
            return XSDataImageQualityIndicators(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getBinPopCutOffMethod2Res(self): return self.binPopCutOffMethod2Res
    def setBinPopCutOffMethod2Res(self, binPopCutOffMethod2Res): self.binPopCutOffMethod2Res = binPopCutOffMethod2Res
    def getGoodBraggCandidates(self): return self.goodBraggCandidates
    def setGoodBraggCandidates(self, goodBraggCandidates): self.goodBraggCandidates = goodBraggCandidates
    def getIceRings(self): return self.iceRings
    def setIceRings(self, iceRings): self.iceRings = iceRings
    def getImage(self): return self.image
    def setImage(self, image): self.image = image
    def getInResolutionOvrlSpots(self): return self.inResolutionOvrlSpots
    def setInResolutionOvrlSpots(self, inResolutionOvrlSpots): self.inResolutionOvrlSpots = inResolutionOvrlSpots
    def getInResTotal(self): return self.inResTotal
    def setInResTotal(self, inResTotal): self.inResTotal = inResTotal
    def getMaxUnitCell(self): return self.maxUnitCell
    def setMaxUnitCell(self, maxUnitCell): self.maxUnitCell = maxUnitCell
    def getMethod1Res(self): return self.method1Res
    def setMethod1Res(self, method1Res): self.method1Res = method1Res
    def getMethod2Res(self): return self.method2Res
    def setMethod2Res(self, method2Res): self.method2Res = method2Res
    def getPctSaturationTop50Peaks(self): return self.pctSaturationTop50Peaks
    def setPctSaturationTop50Peaks(self, pctSaturationTop50Peaks): self.pctSaturationTop50Peaks = pctSaturationTop50Peaks
    def getSpotTotal(self): return self.spotTotal
    def setSpotTotal(self, spotTotal): self.spotTotal = spotTotal
    def export(self, outfile, level, name_='XSDataImageQualityIndicators'):
        showIndent(outfile, level)
        outfile.write('<%s>\n' % name_)
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='XSDataImageQualityIndicators'):
        XSData.exportAttributes(self, outfile, level, name_='XSDataImageQualityIndicators')
    def exportChildren(self, outfile, level, name_='XSDataImageQualityIndicators'):
        if self.binPopCutOffMethod2Res:
            self.binPopCutOffMethod2Res.export(outfile, level, name_='binPopCutOffMethod2Res')
        if self.goodBraggCandidates:
            self.goodBraggCandidates.export(outfile, level, name_='goodBraggCandidates')
        if self.iceRings:
            self.iceRings.export(outfile, level, name_='iceRings')
        if self.image:
            self.image.export(outfile, level, name_='image')
        if self.inResolutionOvrlSpots:
            self.inResolutionOvrlSpots.export(outfile, level, name_='inResolutionOvrlSpots')
        if self.inResTotal:
            self.inResTotal.export(outfile, level, name_='inResTotal')
        if self.maxUnitCell:
            self.maxUnitCell.export(outfile, level, name_='maxUnitCell')
        if self.method1Res:
            self.method1Res.export(outfile, level, name_='method1Res')
        if self.method2Res:
            self.method2Res.export(outfile, level, name_='method2Res')
        if self.pctSaturationTop50Peaks:
            self.pctSaturationTop50Peaks.export(outfile, level, name_='pctSaturationTop50Peaks')
        if self.spotTotal:
            self.spotTotal.export(outfile, level, name_='spotTotal')
        XSData.exportChildren(self, outfile, level, name_)

    #Only to export the entire XML tree to a file stream on disk
    def outputFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write("<?xml version=\"1.0\" ?>\n")
        self.export( outfile, 0, name_='XSDataImageQualityIndicators' )
        outfile.close()


    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataImageQualityIndicators.factory()
        rootObj.build(rootNode)
        return rootObj
    parseString = staticmethod( parseString ) 


    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataImageQualityIndicators.factory()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile ) 


    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO.StringIO()
        oStreamString.write('<?xml version="1.0" ?>\n')
        self.export( oStreamString, 0, name_="XSDataImageQualityIndicators" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    def exportLiteral(self, outfile, level, name_='XSDataImageQualityIndicators'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        pass
        XSData.exportLiteralAttributes(self, outfile, level, name_)
    def exportLiteralChildren(self, outfile, level, name_):
        if self.binPopCutOffMethod2Res:
            showIndent(outfile, level)
            outfile.write('binPopCutOffMethod2Res=XSDataDouble(\n')
            self.binPopCutOffMethod2Res.exportLiteral(outfile, level, name_='binPopCutOffMethod2Res')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.goodBraggCandidates:
            showIndent(outfile, level)
            outfile.write('goodBraggCandidates=XSDataInteger(\n')
            self.goodBraggCandidates.exportLiteral(outfile, level, name_='goodBraggCandidates')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.iceRings:
            showIndent(outfile, level)
            outfile.write('iceRings=XSDataInteger(\n')
            self.iceRings.exportLiteral(outfile, level, name_='iceRings')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.image:
            showIndent(outfile, level)
            outfile.write('image=XSDataImage(\n')
            self.image.exportLiteral(outfile, level, name_='image')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.inResolutionOvrlSpots:
            showIndent(outfile, level)
            outfile.write('inResolutionOvrlSpots=XSDataInteger(\n')
            self.inResolutionOvrlSpots.exportLiteral(outfile, level, name_='inResolutionOvrlSpots')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.inResTotal:
            showIndent(outfile, level)
            outfile.write('inResTotal=XSDataInteger(\n')
            self.inResTotal.exportLiteral(outfile, level, name_='inResTotal')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.maxUnitCell:
            showIndent(outfile, level)
            outfile.write('maxUnitCell=XSDataDouble(\n')
            self.maxUnitCell.exportLiteral(outfile, level, name_='maxUnitCell')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.method1Res:
            showIndent(outfile, level)
            outfile.write('method1Res=XSDataDouble(\n')
            self.method1Res.exportLiteral(outfile, level, name_='method1Res')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.method2Res:
            showIndent(outfile, level)
            outfile.write('method2Res=XSDataDouble(\n')
            self.method2Res.exportLiteral(outfile, level, name_='method2Res')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.pctSaturationTop50Peaks:
            showIndent(outfile, level)
            outfile.write('pctSaturationTop50Peaks=XSDataDouble(\n')
            self.pctSaturationTop50Peaks.exportLiteral(outfile, level, name_='pctSaturationTop50Peaks')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.spotTotal:
            showIndent(outfile, level)
            outfile.write('spotTotal=XSDataInteger(\n')
            self.spotTotal.exportLiteral(outfile, level, name_='spotTotal')
            showIndent(outfile, level)
            outfile.write('),\n')
        XSData.exportLiteralChildren(self, outfile, level, name_)
    def build(self, node_):
        attrs = node_.attributes
        self.buildAttributes(attrs)
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildAttributes(self, attrs):
        XSData.buildAttributes(self, attrs)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'binPopCutOffMethod2Res':
            obj_ = XSDataDouble.factory()
            obj_.build(child_)
            self.setBinPopCutOffMethod2Res(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'goodBraggCandidates':
            obj_ = XSDataInteger.factory()
            obj_.build(child_)
            self.setGoodBraggCandidates(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'iceRings':
            obj_ = XSDataInteger.factory()
            obj_.build(child_)
            self.setIceRings(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'image':
            obj_ = XSDataImage.factory()
            obj_.build(child_)
            self.setImage(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'inResolutionOvrlSpots':
            obj_ = XSDataInteger.factory()
            obj_.build(child_)
            self.setInResolutionOvrlSpots(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'inResTotal':
            obj_ = XSDataInteger.factory()
            obj_.build(child_)
            self.setInResTotal(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'maxUnitCell':
            obj_ = XSDataDouble.factory()
            obj_.build(child_)
            self.setMaxUnitCell(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'method1Res':
            obj_ = XSDataDouble.factory()
            obj_.build(child_)
            self.setMethod1Res(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'method2Res':
            obj_ = XSDataDouble.factory()
            obj_.build(child_)
            self.setMethod2Res(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'pctSaturationTop50Peaks':
            obj_ = XSDataDouble.factory()
            obj_.build(child_)
            self.setPctSaturationTop50Peaks(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'spotTotal':
            obj_ = XSDataInteger.factory()
            obj_.build(child_)
            self.setSpotTotal(obj_)
# end class XSDataImageQualityIndicators


class XSDataIndexingInput(XSDataInput):
    subclass = None
    def __init__(self, configuration=None, crystal=None, dataCollection=None, experimentalCondition=None):
        XSDataInput.__init__(self, configuration)
        self.crystal = crystal
        self.dataCollection = dataCollection
        self.experimentalCondition = experimentalCondition
    def factory(*args_, **kwargs_):
        if XSDataIndexingInput.subclass:
            return XSDataIndexingInput.subclass(*args_, **kwargs_)
        else:
            return XSDataIndexingInput(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getCrystal(self): return self.crystal
    def setCrystal(self, crystal): self.crystal = crystal
    def getDataCollection(self): return self.dataCollection
    def setDataCollection(self, dataCollection): self.dataCollection = dataCollection
    def getExperimentalCondition(self): return self.experimentalCondition
    def setExperimentalCondition(self, experimentalCondition): self.experimentalCondition = experimentalCondition
    def export(self, outfile, level, name_='XSDataIndexingInput'):
        showIndent(outfile, level)
        outfile.write('<%s>\n' % name_)
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='XSDataIndexingInput'):
        XSDataInput.exportAttributes(self, outfile, level, name_='XSDataIndexingInput')
    def exportChildren(self, outfile, level, name_='XSDataIndexingInput'):
        if self.getCrystal() != None :
            if self.crystal:
                self.crystal.export(outfile, level, name_='crystal')
        if self.dataCollection:
            self.dataCollection.export(outfile, level, name_='dataCollection')
        if self.getExperimentalCondition() != None :
            if self.experimentalCondition:
                self.experimentalCondition.export(outfile, level, name_='experimentalCondition')
        XSDataInput.exportChildren(self, outfile, level, name_)

    #Only to export the entire XML tree to a file stream on disk
    def outputFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write("<?xml version=\"1.0\" ?>\n")
        self.export( outfile, 0, name_='XSDataIndexingInput' )
        outfile.close()


    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataIndexingInput.factory()
        rootObj.build(rootNode)
        return rootObj
    parseString = staticmethod( parseString ) 


    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataIndexingInput.factory()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile ) 


    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO.StringIO()
        oStreamString.write('<?xml version="1.0" ?>\n')
        self.export( oStreamString, 0, name_="XSDataIndexingInput" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    def exportLiteral(self, outfile, level, name_='XSDataIndexingInput'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        pass
        XSDataInput.exportLiteralAttributes(self, outfile, level, name_)
    def exportLiteralChildren(self, outfile, level, name_):
        if self.crystal:
            showIndent(outfile, level)
            outfile.write('crystal=XSDataCrystal(\n')
            self.crystal.exportLiteral(outfile, level, name_='crystal')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.dataCollection:
            showIndent(outfile, level)
            outfile.write('dataCollection=XSDataCollection(\n')
            self.dataCollection.exportLiteral(outfile, level, name_='dataCollection')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.experimentalCondition:
            showIndent(outfile, level)
            outfile.write('experimentalCondition=XSDataExperimentalCondition(\n')
            self.experimentalCondition.exportLiteral(outfile, level, name_='experimentalCondition')
            showIndent(outfile, level)
            outfile.write('),\n')
        XSDataInput.exportLiteralChildren(self, outfile, level, name_)
    def build(self, node_):
        attrs = node_.attributes
        self.buildAttributes(attrs)
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildAttributes(self, attrs):
        XSDataInput.buildAttributes(self, attrs)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'crystal':
            obj_ = XSDataCrystal.factory()
            obj_.build(child_)
            self.setCrystal(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'dataCollection':
            obj_ = XSDataCollection.factory()
            obj_.build(child_)
            self.setDataCollection(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'experimentalCondition':
            obj_ = XSDataExperimentalCondition.factory()
            obj_.build(child_)
            self.setExperimentalCondition(obj_)
        XSDataInput.buildChildren(self, child_, nodeName_)
# end class XSDataIndexingInput


class XSDataIndexingResult(XSDataResult):
    subclass = None
    def __init__(self, image=None, indexingLogFile=None, predictionResult=None, solution=None, selectedSolution=None):
        XSDataResult.__init__(self)
        if image is None:
            self.image = []
        else:
            self.image = image
        self.indexingLogFile = indexingLogFile
        self.predictionResult = predictionResult
        if solution is None:
            self.solution = []
        else:
            self.solution = solution
        self.selectedSolution = selectedSolution
    def factory(*args_, **kwargs_):
        if XSDataIndexingResult.subclass:
            return XSDataIndexingResult.subclass(*args_, **kwargs_)
        else:
            return XSDataIndexingResult(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getImage(self): return self.image
    def setImage(self, image): self.image = image
    def addImage(self, value): self.image.append(value)
    def insertImage(self, index, value): self.image[index] = value
    def getIndexingLogFile(self): return self.indexingLogFile
    def setIndexingLogFile(self, indexingLogFile): self.indexingLogFile = indexingLogFile
    def getPredictionResult(self): return self.predictionResult
    def setPredictionResult(self, predictionResult): self.predictionResult = predictionResult
    def getSolution(self): return self.solution
    def setSolution(self, solution): self.solution = solution
    def addSolution(self, value): self.solution.append(value)
    def insertSolution(self, index, value): self.solution[index] = value
    def getSelectedSolution(self): return self.selectedSolution
    def setSelectedSolution(self, selectedSolution): self.selectedSolution = selectedSolution
    def export(self, outfile, level, name_='XSDataIndexingResult'):
        showIndent(outfile, level)
        outfile.write('<%s>\n' % name_)
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='XSDataIndexingResult'):
        XSDataResult.exportAttributes(self, outfile, level, name_='XSDataIndexingResult')
    def exportChildren(self, outfile, level, name_='XSDataIndexingResult'):
        for image_ in self.getImage():
            image_.export(outfile, level, name_='image')
        if self.getIndexingLogFile() != None :
            if self.indexingLogFile:
                self.indexingLogFile.export(outfile, level, name_='indexingLogFile')
        if self.getPredictionResult() != None :
            if self.predictionResult:
                self.predictionResult.export(outfile, level, name_='predictionResult')
        for solution_ in self.getSolution():
            solution_.export(outfile, level, name_='solution')
        if self.getSelectedSolution() != None :
            if self.selectedSolution:
                self.selectedSolution.export(outfile, level, name_='selectedSolution')
        XSDataResult.exportChildren(self, outfile, level, name_)

    #Only to export the entire XML tree to a file stream on disk
    def outputFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write("<?xml version=\"1.0\" ?>\n")
        self.export( outfile, 0, name_='XSDataIndexingResult' )
        outfile.close()


    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataIndexingResult.factory()
        rootObj.build(rootNode)
        return rootObj
    parseString = staticmethod( parseString ) 


    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataIndexingResult.factory()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile ) 


    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO.StringIO()
        oStreamString.write('<?xml version="1.0" ?>\n')
        self.export( oStreamString, 0, name_="XSDataIndexingResult" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    def exportLiteral(self, outfile, level, name_='XSDataIndexingResult'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        pass
        XSDataResult.exportLiteralAttributes(self, outfile, level, name_)
    def exportLiteralChildren(self, outfile, level, name_):
        showIndent(outfile, level)
        outfile.write('image=[\n')
        level += 1
        for image in self.image:
            showIndent(outfile, level)
            outfile.write('XSDataImage(\n')
            image.exportLiteral(outfile, level, name_='image')
            showIndent(outfile, level)
            outfile.write('),\n')
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
        if self.indexingLogFile:
            showIndent(outfile, level)
            outfile.write('indexingLogFile=XSDataFile(\n')
            self.indexingLogFile.exportLiteral(outfile, level, name_='indexingLogFile')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.predictionResult:
            showIndent(outfile, level)
            outfile.write('predictionResult=XSDataGeneratePredictionResult(\n')
            self.predictionResult.exportLiteral(outfile, level, name_='predictionResult')
            showIndent(outfile, level)
            outfile.write('),\n')
        showIndent(outfile, level)
        outfile.write('solution=[\n')
        level += 1
        for solution in self.solution:
            showIndent(outfile, level)
            outfile.write('XSDataIndexingSolution(\n')
            solution.exportLiteral(outfile, level, name_='solution')
            showIndent(outfile, level)
            outfile.write('),\n')
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
        if self.selectedSolution:
            showIndent(outfile, level)
            outfile.write('selectedSolution=XSDataIndexingSolutionSelected(\n')
            self.selectedSolution.exportLiteral(outfile, level, name_='selectedSolution')
            showIndent(outfile, level)
            outfile.write('),\n')
        XSDataResult.exportLiteralChildren(self, outfile, level, name_)
    def build(self, node_):
        attrs = node_.attributes
        self.buildAttributes(attrs)
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildAttributes(self, attrs):
        XSDataResult.buildAttributes(self, attrs)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'image':
            obj_ = XSDataImage.factory()
            obj_.build(child_)
            self.image.append(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'indexingLogFile':
            obj_ = XSDataFile.factory()
            obj_.build(child_)
            self.setIndexingLogFile(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'predictionResult':
            obj_ = XSDataGeneratePredictionResult.factory()
            obj_.build(child_)
            self.setPredictionResult(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'solution':
            obj_ = XSDataIndexingSolution.factory()
            obj_.build(child_)
            self.solution.append(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'selectedSolution':
            obj_ = XSDataIndexingSolutionSelected.factory()
            obj_.build(child_)
            self.setSelectedSolution(obj_)
# end class XSDataIndexingResult


class XSDataIndexingSolution(XSData):
    subclass = None
    def __init__(self, crystal=None, number=None, penalty=None):
        XSData.__init__(self)
        self.crystal = crystal
        self.number = number
        self.penalty = penalty
    def factory(*args_, **kwargs_):
        if XSDataIndexingSolution.subclass:
            return XSDataIndexingSolution.subclass(*args_, **kwargs_)
        else:
            return XSDataIndexingSolution(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getCrystal(self): return self.crystal
    def setCrystal(self, crystal): self.crystal = crystal
    def getNumber(self): return self.number
    def setNumber(self, number): self.number = number
    def getPenalty(self): return self.penalty
    def setPenalty(self, penalty): self.penalty = penalty
    def export(self, outfile, level, name_='XSDataIndexingSolution'):
        showIndent(outfile, level)
        outfile.write('<%s>\n' % name_)
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='XSDataIndexingSolution'):
        XSData.exportAttributes(self, outfile, level, name_='XSDataIndexingSolution')
    def exportChildren(self, outfile, level, name_='XSDataIndexingSolution'):
        if self.crystal:
            self.crystal.export(outfile, level, name_='crystal')
        if self.number:
            self.number.export(outfile, level, name_='number')
        if self.penalty:
            self.penalty.export(outfile, level, name_='penalty')
        XSData.exportChildren(self, outfile, level, name_)

    #Only to export the entire XML tree to a file stream on disk
    def outputFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write("<?xml version=\"1.0\" ?>\n")
        self.export( outfile, 0, name_='XSDataIndexingSolution' )
        outfile.close()


    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataIndexingSolution.factory()
        rootObj.build(rootNode)
        return rootObj
    parseString = staticmethod( parseString ) 


    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataIndexingSolution.factory()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile ) 


    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO.StringIO()
        oStreamString.write('<?xml version="1.0" ?>\n')
        self.export( oStreamString, 0, name_="XSDataIndexingSolution" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    def exportLiteral(self, outfile, level, name_='XSDataIndexingSolution'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        pass
        XSData.exportLiteralAttributes(self, outfile, level, name_)
    def exportLiteralChildren(self, outfile, level, name_):
        if self.crystal:
            showIndent(outfile, level)
            outfile.write('crystal=XSDataCrystal(\n')
            self.crystal.exportLiteral(outfile, level, name_='crystal')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.number:
            showIndent(outfile, level)
            outfile.write('number=XSDataInteger(\n')
            self.number.exportLiteral(outfile, level, name_='number')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.penalty:
            showIndent(outfile, level)
            outfile.write('penalty=XSDataFloat(\n')
            self.penalty.exportLiteral(outfile, level, name_='penalty')
            showIndent(outfile, level)
            outfile.write('),\n')
        XSData.exportLiteralChildren(self, outfile, level, name_)
    def build(self, node_):
        attrs = node_.attributes
        self.buildAttributes(attrs)
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildAttributes(self, attrs):
        XSData.buildAttributes(self, attrs)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'crystal':
            obj_ = XSDataCrystal.factory()
            obj_.build(child_)
            self.setCrystal(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'number':
            obj_ = XSDataInteger.factory()
            obj_.build(child_)
            self.setNumber(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'penalty':
            obj_ = XSDataFloat.factory()
            obj_.build(child_)
            self.setPenalty(obj_)
# end class XSDataIndexingSolution


class XSDataIndexingSolutionSelected(XSDataIndexingSolution):
    subclass = None
    def __init__(self, crystal=None, number=None, penalty=None, experimentalConditionRefined=None, mosaicityEstimation=None, statistics=None, orientation=None):
        XSDataIndexingSolution.__init__(self, crystal, number, penalty)
        self.experimentalConditionRefined = experimentalConditionRefined
        self.mosaicityEstimation = mosaicityEstimation
        self.statistics = statistics
        self.orientation = orientation
    def factory(*args_, **kwargs_):
        if XSDataIndexingSolutionSelected.subclass:
            return XSDataIndexingSolutionSelected.subclass(*args_, **kwargs_)
        else:
            return XSDataIndexingSolutionSelected(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getExperimentalConditionRefined(self): return self.experimentalConditionRefined
    def setExperimentalConditionRefined(self, experimentalConditionRefined): self.experimentalConditionRefined = experimentalConditionRefined
    def getMosaicityEstimation(self): return self.mosaicityEstimation
    def setMosaicityEstimation(self, mosaicityEstimation): self.mosaicityEstimation = mosaicityEstimation
    def getStatistics(self): return self.statistics
    def setStatistics(self, statistics): self.statistics = statistics
    def getOrientation(self): return self.orientation
    def setOrientation(self, orientation): self.orientation = orientation
    def export(self, outfile, level, name_='XSDataIndexingSolutionSelected'):
        showIndent(outfile, level)
        outfile.write('<%s>\n' % name_)
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='XSDataIndexingSolutionSelected'):
        XSDataIndexingSolution.exportAttributes(self, outfile, level, name_='XSDataIndexingSolutionSelected')
    def exportChildren(self, outfile, level, name_='XSDataIndexingSolutionSelected'):
        if self.experimentalConditionRefined:
            self.experimentalConditionRefined.export(outfile, level, name_='experimentalConditionRefined')
        if self.mosaicityEstimation:
            self.mosaicityEstimation.export(outfile, level, name_='mosaicityEstimation')
        if self.statistics:
            self.statistics.export(outfile, level, name_='statistics')
        if self.orientation:
            self.orientation.export(outfile, level, name_='orientation')
        XSDataIndexingSolution.exportChildren(self, outfile, level, name_)

    #Only to export the entire XML tree to a file stream on disk
    def outputFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write("<?xml version=\"1.0\" ?>\n")
        self.export( outfile, 0, name_='XSDataIndexingSolutionSelected' )
        outfile.close()


    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataIndexingSolutionSelected.factory()
        rootObj.build(rootNode)
        return rootObj
    parseString = staticmethod( parseString ) 


    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataIndexingSolutionSelected.factory()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile ) 


    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO.StringIO()
        oStreamString.write('<?xml version="1.0" ?>\n')
        self.export( oStreamString, 0, name_="XSDataIndexingSolutionSelected" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    def exportLiteral(self, outfile, level, name_='XSDataIndexingSolutionSelected'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        pass
        XSDataIndexingSolution.exportLiteralAttributes(self, outfile, level, name_)
    def exportLiteralChildren(self, outfile, level, name_):
        if self.experimentalConditionRefined:
            showIndent(outfile, level)
            outfile.write('experimentalConditionRefined=XSDataExperimentalCondition(\n')
            self.experimentalConditionRefined.exportLiteral(outfile, level, name_='experimentalConditionRefined')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.mosaicityEstimation:
            showIndent(outfile, level)
            outfile.write('mosaicityEstimation=XSDataFloat(\n')
            self.mosaicityEstimation.exportLiteral(outfile, level, name_='mosaicityEstimation')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.statistics:
            showIndent(outfile, level)
            outfile.write('statistics=XSDataStatisticsIndexing(\n')
            self.statistics.exportLiteral(outfile, level, name_='statistics')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.orientation:
            showIndent(outfile, level)
            outfile.write('orientation=XSDataOrientation(\n')
            self.orientation.exportLiteral(outfile, level, name_='orientation')
            showIndent(outfile, level)
            outfile.write('),\n')
        XSDataIndexingSolution.exportLiteralChildren(self, outfile, level, name_)
    def build(self, node_):
        attrs = node_.attributes
        self.buildAttributes(attrs)
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildAttributes(self, attrs):
        XSDataIndexingSolution.buildAttributes(self, attrs)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'experimentalConditionRefined':
            obj_ = XSDataExperimentalCondition.factory()
            obj_.build(child_)
            self.setExperimentalConditionRefined(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'mosaicityEstimation':
            obj_ = XSDataFloat.factory()
            obj_.build(child_)
            self.setMosaicityEstimation(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'statistics':
            obj_ = XSDataStatisticsIndexing.factory()
            obj_.build(child_)
            self.setStatistics(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'orientation':
            obj_ = XSDataOrientation.factory()
            obj_.build(child_)
            self.setOrientation(obj_)
        XSDataIndexingSolution.buildChildren(self, child_, nodeName_)
# end class XSDataIndexingSolutionSelected


class XSDataInputCharacterisation(XSDataInput):
    subclass = None
    def __init__(self, configuration=None, dataCollection=None):
        XSDataInput.__init__(self, configuration)
        self.dataCollection = dataCollection
    def factory(*args_, **kwargs_):
        if XSDataInputCharacterisation.subclass:
            return XSDataInputCharacterisation.subclass(*args_, **kwargs_)
        else:
            return XSDataInputCharacterisation(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getDataCollection(self): return self.dataCollection
    def setDataCollection(self, dataCollection): self.dataCollection = dataCollection
    def export(self, outfile, level, name_='XSDataInputCharacterisation'):
        showIndent(outfile, level)
        outfile.write('<%s>\n' % name_)
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='XSDataInputCharacterisation'):
        XSDataInput.exportAttributes(self, outfile, level, name_='XSDataInputCharacterisation')
    def exportChildren(self, outfile, level, name_='XSDataInputCharacterisation'):
        if self.dataCollection:
            self.dataCollection.export(outfile, level, name_='dataCollection')
        XSDataInput.exportChildren(self, outfile, level, name_)

    #Only to export the entire XML tree to a file stream on disk
    def outputFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write("<?xml version=\"1.0\" ?>\n")
        self.export( outfile, 0, name_='XSDataInputCharacterisation' )
        outfile.close()


    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataInputCharacterisation.factory()
        rootObj.build(rootNode)
        return rootObj
    parseString = staticmethod( parseString ) 


    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataInputCharacterisation.factory()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile ) 


    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO.StringIO()
        oStreamString.write('<?xml version="1.0" ?>\n')
        self.export( oStreamString, 0, name_="XSDataInputCharacterisation" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    def exportLiteral(self, outfile, level, name_='XSDataInputCharacterisation'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        pass
        XSDataInput.exportLiteralAttributes(self, outfile, level, name_)
    def exportLiteralChildren(self, outfile, level, name_):
        if self.dataCollection:
            showIndent(outfile, level)
            outfile.write('dataCollection=XSDataCollection(\n')
            self.dataCollection.exportLiteral(outfile, level, name_='dataCollection')
            showIndent(outfile, level)
            outfile.write('),\n')
        XSDataInput.exportLiteralChildren(self, outfile, level, name_)
    def build(self, node_):
        attrs = node_.attributes
        self.buildAttributes(attrs)
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildAttributes(self, attrs):
        XSDataInput.buildAttributes(self, attrs)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'dataCollection':
            obj_ = XSDataCollection.factory()
            obj_.build(child_)
            self.setDataCollection(obj_)
        XSDataInput.buildChildren(self, child_, nodeName_)
# end class XSDataInputCharacterisation


class XSDataInputControlISPyB(XSDataInput):
    subclass = None
    def __init__(self, configuration=None, characterisationResult=None, dataCollectionId=None):
        XSDataInput.__init__(self, configuration)
        self.characterisationResult = characterisationResult
        self.dataCollectionId = dataCollectionId
    def factory(*args_, **kwargs_):
        if XSDataInputControlISPyB.subclass:
            return XSDataInputControlISPyB.subclass(*args_, **kwargs_)
        else:
            return XSDataInputControlISPyB(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getCharacterisationResult(self): return self.characterisationResult
    def setCharacterisationResult(self, characterisationResult): self.characterisationResult = characterisationResult
    def getDataCollectionId(self): return self.dataCollectionId
    def setDataCollectionId(self, dataCollectionId): self.dataCollectionId = dataCollectionId
    def export(self, outfile, level, name_='XSDataInputControlISPyB'):
        showIndent(outfile, level)
        outfile.write('<%s>\n' % name_)
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='XSDataInputControlISPyB'):
        XSDataInput.exportAttributes(self, outfile, level, name_='XSDataInputControlISPyB')
    def exportChildren(self, outfile, level, name_='XSDataInputControlISPyB'):
        if self.characterisationResult:
            self.characterisationResult.export(outfile, level, name_='characterisationResult')
        if self.getDataCollectionId() != None :
            if self.dataCollectionId:
                self.dataCollectionId.export(outfile, level, name_='dataCollectionId')
        XSDataInput.exportChildren(self, outfile, level, name_)

    #Only to export the entire XML tree to a file stream on disk
    def outputFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write("<?xml version=\"1.0\" ?>\n")
        self.export( outfile, 0, name_='XSDataInputControlISPyB' )
        outfile.close()


    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataInputControlISPyB.factory()
        rootObj.build(rootNode)
        return rootObj
    parseString = staticmethod( parseString ) 


    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataInputControlISPyB.factory()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile ) 


    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO.StringIO()
        oStreamString.write('<?xml version="1.0" ?>\n')
        self.export( oStreamString, 0, name_="XSDataInputControlISPyB" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    def exportLiteral(self, outfile, level, name_='XSDataInputControlISPyB'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        pass
        XSDataInput.exportLiteralAttributes(self, outfile, level, name_)
    def exportLiteralChildren(self, outfile, level, name_):
        if self.characterisationResult:
            showIndent(outfile, level)
            outfile.write('characterisationResult=XSDataResultCharacterisation(\n')
            self.characterisationResult.exportLiteral(outfile, level, name_='characterisationResult')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.dataCollectionId:
            showIndent(outfile, level)
            outfile.write('dataCollectionId=XSDataInteger(\n')
            self.dataCollectionId.exportLiteral(outfile, level, name_='dataCollectionId')
            showIndent(outfile, level)
            outfile.write('),\n')
        XSDataInput.exportLiteralChildren(self, outfile, level, name_)
    def build(self, node_):
        attrs = node_.attributes
        self.buildAttributes(attrs)
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildAttributes(self, attrs):
        XSDataInput.buildAttributes(self, attrs)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'characterisationResult':
            obj_ = XSDataResultCharacterisation.factory()
            obj_.build(child_)
            self.setCharacterisationResult(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'dataCollectionId':
            obj_ = XSDataInteger.factory()
            obj_.build(child_)
            self.setDataCollectionId(obj_)
        XSDataInput.buildChildren(self, child_, nodeName_)
# end class XSDataInputControlISPyB


class XSDataInputInducedRadiationProcess(XSDataInput):
    subclass = None
    def __init__(self, configuration=None, characterisationResult=None):
        XSDataInput.__init__(self, configuration)
        self.characterisationResult = characterisationResult
    def factory(*args_, **kwargs_):
        if XSDataInputInducedRadiationProcess.subclass:
            return XSDataInputInducedRadiationProcess.subclass(*args_, **kwargs_)
        else:
            return XSDataInputInducedRadiationProcess(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getCharacterisationResult(self): return self.characterisationResult
    def setCharacterisationResult(self, characterisationResult): self.characterisationResult = characterisationResult
    def export(self, outfile, level, name_='XSDataInputInducedRadiationProcess'):
        showIndent(outfile, level)
        outfile.write('<%s>\n' % name_)
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='XSDataInputInducedRadiationProcess'):
        XSDataInput.exportAttributes(self, outfile, level, name_='XSDataInputInducedRadiationProcess')
    def exportChildren(self, outfile, level, name_='XSDataInputInducedRadiationProcess'):
        if self.characterisationResult:
            self.characterisationResult.export(outfile, level, name_='characterisationResult')
        XSDataInput.exportChildren(self, outfile, level, name_)

    #Only to export the entire XML tree to a file stream on disk
    def outputFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write("<?xml version=\"1.0\" ?>\n")
        self.export( outfile, 0, name_='XSDataInputInducedRadiationProcess' )
        outfile.close()


    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataInputInducedRadiationProcess.factory()
        rootObj.build(rootNode)
        return rootObj
    parseString = staticmethod( parseString ) 


    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataInputInducedRadiationProcess.factory()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile ) 


    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO.StringIO()
        oStreamString.write('<?xml version="1.0" ?>\n')
        self.export( oStreamString, 0, name_="XSDataInputInducedRadiationProcess" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    def exportLiteral(self, outfile, level, name_='XSDataInputInducedRadiationProcess'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        pass
        XSDataInput.exportLiteralAttributes(self, outfile, level, name_)
    def exportLiteralChildren(self, outfile, level, name_):
        if self.characterisationResult:
            showIndent(outfile, level)
            outfile.write('characterisationResult=XSDataResultCharacterisation(\n')
            self.characterisationResult.exportLiteral(outfile, level, name_='characterisationResult')
            showIndent(outfile, level)
            outfile.write('),\n')
        XSDataInput.exportLiteralChildren(self, outfile, level, name_)
    def build(self, node_):
        attrs = node_.attributes
        self.buildAttributes(attrs)
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildAttributes(self, attrs):
        XSDataInput.buildAttributes(self, attrs)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'characterisationResult':
            obj_ = XSDataResultCharacterisation.factory()
            obj_.build(child_)
            self.setCharacterisationResult(obj_)
        XSDataInput.buildChildren(self, child_, nodeName_)
# end class XSDataInputInducedRadiationProcess


class XSDataInputReadImageHeader(XSDataInput):
    subclass = None
    def __init__(self, configuration=None, image=None):
        XSDataInput.__init__(self, configuration)
        self.image = image
    def factory(*args_, **kwargs_):
        if XSDataInputReadImageHeader.subclass:
            return XSDataInputReadImageHeader.subclass(*args_, **kwargs_)
        else:
            return XSDataInputReadImageHeader(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getImage(self): return self.image
    def setImage(self, image): self.image = image
    def export(self, outfile, level, name_='XSDataInputReadImageHeader'):
        showIndent(outfile, level)
        outfile.write('<%s>\n' % name_)
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='XSDataInputReadImageHeader'):
        XSDataInput.exportAttributes(self, outfile, level, name_='XSDataInputReadImageHeader')
    def exportChildren(self, outfile, level, name_='XSDataInputReadImageHeader'):
        if self.image:
            self.image.export(outfile, level, name_='image')
        XSDataInput.exportChildren(self, outfile, level, name_)

    #Only to export the entire XML tree to a file stream on disk
    def outputFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write("<?xml version=\"1.0\" ?>\n")
        self.export( outfile, 0, name_='XSDataInputReadImageHeader' )
        outfile.close()


    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataInputReadImageHeader.factory()
        rootObj.build(rootNode)
        return rootObj
    parseString = staticmethod( parseString ) 


    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataInputReadImageHeader.factory()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile ) 


    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO.StringIO()
        oStreamString.write('<?xml version="1.0" ?>\n')
        self.export( oStreamString, 0, name_="XSDataInputReadImageHeader" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    def exportLiteral(self, outfile, level, name_='XSDataInputReadImageHeader'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        pass
        XSDataInput.exportLiteralAttributes(self, outfile, level, name_)
    def exportLiteralChildren(self, outfile, level, name_):
        if self.image:
            showIndent(outfile, level)
            outfile.write('image=XSDataFile(\n')
            self.image.exportLiteral(outfile, level, name_='image')
            showIndent(outfile, level)
            outfile.write('),\n')
        XSDataInput.exportLiteralChildren(self, outfile, level, name_)
    def build(self, node_):
        attrs = node_.attributes
        self.buildAttributes(attrs)
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildAttributes(self, attrs):
        XSDataInput.buildAttributes(self, attrs)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'image':
            obj_ = XSDataFile.factory()
            obj_.build(child_)
            self.setImage(obj_)
        XSDataInput.buildChildren(self, child_, nodeName_)
# end class XSDataInputReadImageHeader


class XSDataInputStrategy(XSDataInput):
    subclass = None
    def __init__(self, configuration=None, bestFileContentDat=None, bestFileContentHKL=None, bestFileContentPar=None, crystalRefined=None, diffractionPlan=None, experimentalCondition=None, sample=None):
        XSDataInput.__init__(self, configuration)
        self.bestFileContentDat = bestFileContentDat
        if bestFileContentHKL is None:
            self.bestFileContentHKL = []
        else:
            self.bestFileContentHKL = bestFileContentHKL
        self.bestFileContentPar = bestFileContentPar
        self.crystalRefined = crystalRefined
        self.diffractionPlan = diffractionPlan
        self.experimentalCondition = experimentalCondition
        self.sample = sample
    def factory(*args_, **kwargs_):
        if XSDataInputStrategy.subclass:
            return XSDataInputStrategy.subclass(*args_, **kwargs_)
        else:
            return XSDataInputStrategy(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getBestFileContentDat(self): return self.bestFileContentDat
    def setBestFileContentDat(self, bestFileContentDat): self.bestFileContentDat = bestFileContentDat
    def getBestFileContentHKL(self): return self.bestFileContentHKL
    def setBestFileContentHKL(self, bestFileContentHKL): self.bestFileContentHKL = bestFileContentHKL
    def addBestFileContentHKL(self, value): self.bestFileContentHKL.append(value)
    def insertBestFileContentHKL(self, index, value): self.bestFileContentHKL[index] = value
    def getBestFileContentPar(self): return self.bestFileContentPar
    def setBestFileContentPar(self, bestFileContentPar): self.bestFileContentPar = bestFileContentPar
    def getCrystalRefined(self): return self.crystalRefined
    def setCrystalRefined(self, crystalRefined): self.crystalRefined = crystalRefined
    def getDiffractionPlan(self): return self.diffractionPlan
    def setDiffractionPlan(self, diffractionPlan): self.diffractionPlan = diffractionPlan
    def getExperimentalCondition(self): return self.experimentalCondition
    def setExperimentalCondition(self, experimentalCondition): self.experimentalCondition = experimentalCondition
    def getSample(self): return self.sample
    def setSample(self, sample): self.sample = sample
    def export(self, outfile, level, name_='XSDataInputStrategy'):
        showIndent(outfile, level)
        outfile.write('<%s>\n' % name_)
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='XSDataInputStrategy'):
        XSDataInput.exportAttributes(self, outfile, level, name_='XSDataInputStrategy')
    def exportChildren(self, outfile, level, name_='XSDataInputStrategy'):
        if self.bestFileContentDat:
            self.bestFileContentDat.export(outfile, level, name_='bestFileContentDat')
        for bestFileContentHKL_ in self.getBestFileContentHKL():
            bestFileContentHKL_.export(outfile, level, name_='bestFileContentHKL')
        if self.bestFileContentPar:
            self.bestFileContentPar.export(outfile, level, name_='bestFileContentPar')
        if self.crystalRefined:
            self.crystalRefined.export(outfile, level, name_='crystalRefined')
        if self.diffractionPlan:
            self.diffractionPlan.export(outfile, level, name_='diffractionPlan')
        if self.experimentalCondition:
            self.experimentalCondition.export(outfile, level, name_='experimentalCondition')
        if self.sample:
            self.sample.export(outfile, level, name_='sample')
        XSDataInput.exportChildren(self, outfile, level, name_)

    #Only to export the entire XML tree to a file stream on disk
    def outputFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write("<?xml version=\"1.0\" ?>\n")
        self.export( outfile, 0, name_='XSDataInputStrategy' )
        outfile.close()


    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataInputStrategy.factory()
        rootObj.build(rootNode)
        return rootObj
    parseString = staticmethod( parseString ) 


    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataInputStrategy.factory()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile ) 


    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO.StringIO()
        oStreamString.write('<?xml version="1.0" ?>\n')
        self.export( oStreamString, 0, name_="XSDataInputStrategy" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    def exportLiteral(self, outfile, level, name_='XSDataInputStrategy'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        pass
        XSDataInput.exportLiteralAttributes(self, outfile, level, name_)
    def exportLiteralChildren(self, outfile, level, name_):
        if self.bestFileContentDat:
            showIndent(outfile, level)
            outfile.write('bestFileContentDat=XSDataString(\n')
            self.bestFileContentDat.exportLiteral(outfile, level, name_='bestFileContentDat')
            showIndent(outfile, level)
            outfile.write('),\n')
        showIndent(outfile, level)
        outfile.write('bestFileContentHKL=[\n')
        level += 1
        for bestFileContentHKL in self.bestFileContentHKL:
            showIndent(outfile, level)
            outfile.write('XSDataString(\n')
            bestFileContentHKL.exportLiteral(outfile, level, name_='bestFileContentHKL')
            showIndent(outfile, level)
            outfile.write('),\n')
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
        if self.bestFileContentPar:
            showIndent(outfile, level)
            outfile.write('bestFileContentPar=XSDataString(\n')
            self.bestFileContentPar.exportLiteral(outfile, level, name_='bestFileContentPar')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.crystalRefined:
            showIndent(outfile, level)
            outfile.write('crystalRefined=XSDataCrystal(\n')
            self.crystalRefined.exportLiteral(outfile, level, name_='crystalRefined')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.diffractionPlan:
            showIndent(outfile, level)
            outfile.write('diffractionPlan=XSDataDiffractionPlan(\n')
            self.diffractionPlan.exportLiteral(outfile, level, name_='diffractionPlan')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.experimentalCondition:
            showIndent(outfile, level)
            outfile.write('experimentalCondition=XSDataExperimentalCondition(\n')
            self.experimentalCondition.exportLiteral(outfile, level, name_='experimentalCondition')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.sample:
            showIndent(outfile, level)
            outfile.write('sample=XSDataSampleCrystalMM(\n')
            self.sample.exportLiteral(outfile, level, name_='sample')
            showIndent(outfile, level)
            outfile.write('),\n')
        XSDataInput.exportLiteralChildren(self, outfile, level, name_)
    def build(self, node_):
        attrs = node_.attributes
        self.buildAttributes(attrs)
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildAttributes(self, attrs):
        XSDataInput.buildAttributes(self, attrs)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'bestFileContentDat':
            obj_ = XSDataString.factory()
            obj_.build(child_)
            self.setBestFileContentDat(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'bestFileContentHKL':
            obj_ = XSDataString.factory()
            obj_.build(child_)
            self.bestFileContentHKL.append(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'bestFileContentPar':
            obj_ = XSDataString.factory()
            obj_.build(child_)
            self.setBestFileContentPar(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'crystalRefined':
            obj_ = XSDataCrystal.factory()
            obj_.build(child_)
            self.setCrystalRefined(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'diffractionPlan':
            obj_ = XSDataDiffractionPlan.factory()
            obj_.build(child_)
            self.setDiffractionPlan(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'experimentalCondition':
            obj_ = XSDataExperimentalCondition.factory()
            obj_.build(child_)
            self.setExperimentalCondition(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'sample':
            obj_ = XSDataSampleCrystalMM.factory()
            obj_.build(child_)
            self.setSample(obj_)
        XSDataInput.buildChildren(self, child_, nodeName_)
# end class XSDataInputStrategy


class XSDataInputSubWedgeAssemble(XSDataInput):
    subclass = None
    def __init__(self, configuration=None, file=None):
        XSDataInput.__init__(self, configuration)
        if file is None:
            self.file = []
        else:
            self.file = file
    def factory(*args_, **kwargs_):
        if XSDataInputSubWedgeAssemble.subclass:
            return XSDataInputSubWedgeAssemble.subclass(*args_, **kwargs_)
        else:
            return XSDataInputSubWedgeAssemble(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getFile(self): return self.file
    def setFile(self, file): self.file = file
    def addFile(self, value): self.file.append(value)
    def insertFile(self, index, value): self.file[index] = value
    def export(self, outfile, level, name_='XSDataInputSubWedgeAssemble'):
        showIndent(outfile, level)
        outfile.write('<%s>\n' % name_)
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='XSDataInputSubWedgeAssemble'):
        XSDataInput.exportAttributes(self, outfile, level, name_='XSDataInputSubWedgeAssemble')
    def exportChildren(self, outfile, level, name_='XSDataInputSubWedgeAssemble'):
        for file_ in self.getFile():
            file_.export(outfile, level, name_='file')
        XSDataInput.exportChildren(self, outfile, level, name_)

    #Only to export the entire XML tree to a file stream on disk
    def outputFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write("<?xml version=\"1.0\" ?>\n")
        self.export( outfile, 0, name_='XSDataInputSubWedgeAssemble' )
        outfile.close()


    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataInputSubWedgeAssemble.factory()
        rootObj.build(rootNode)
        return rootObj
    parseString = staticmethod( parseString ) 


    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataInputSubWedgeAssemble.factory()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile ) 


    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO.StringIO()
        oStreamString.write('<?xml version="1.0" ?>\n')
        self.export( oStreamString, 0, name_="XSDataInputSubWedgeAssemble" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    def exportLiteral(self, outfile, level, name_='XSDataInputSubWedgeAssemble'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        pass
        XSDataInput.exportLiteralAttributes(self, outfile, level, name_)
    def exportLiteralChildren(self, outfile, level, name_):
        showIndent(outfile, level)
        outfile.write('file=[\n')
        level += 1
        for file in self.file:
            showIndent(outfile, level)
            outfile.write('XSDataFile(\n')
            file.exportLiteral(outfile, level, name_='file')
            showIndent(outfile, level)
            outfile.write('),\n')
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
        XSDataInput.exportLiteralChildren(self, outfile, level, name_)
    def build(self, node_):
        attrs = node_.attributes
        self.buildAttributes(attrs)
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildAttributes(self, attrs):
        XSDataInput.buildAttributes(self, attrs)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'file':
            obj_ = XSDataFile.factory()
            obj_.build(child_)
            self.file.append(obj_)
        XSDataInput.buildChildren(self, child_, nodeName_)
# end class XSDataInputSubWedgeAssemble


class XSDataInputSubWedgeMerge(XSDataInput):
    subclass = None
    def __init__(self, configuration=None, subWedge=None):
        XSDataInput.__init__(self, configuration)
        if subWedge is None:
            self.subWedge = []
        else:
            self.subWedge = subWedge
    def factory(*args_, **kwargs_):
        if XSDataInputSubWedgeMerge.subclass:
            return XSDataInputSubWedgeMerge.subclass(*args_, **kwargs_)
        else:
            return XSDataInputSubWedgeMerge(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getSubWedge(self): return self.subWedge
    def setSubWedge(self, subWedge): self.subWedge = subWedge
    def addSubWedge(self, value): self.subWedge.append(value)
    def insertSubWedge(self, index, value): self.subWedge[index] = value
    def export(self, outfile, level, name_='XSDataInputSubWedgeMerge'):
        showIndent(outfile, level)
        outfile.write('<%s>\n' % name_)
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='XSDataInputSubWedgeMerge'):
        XSDataInput.exportAttributes(self, outfile, level, name_='XSDataInputSubWedgeMerge')
    def exportChildren(self, outfile, level, name_='XSDataInputSubWedgeMerge'):
        for subWedge_ in self.getSubWedge():
            subWedge_.export(outfile, level, name_='subWedge')
        XSDataInput.exportChildren(self, outfile, level, name_)

    #Only to export the entire XML tree to a file stream on disk
    def outputFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write("<?xml version=\"1.0\" ?>\n")
        self.export( outfile, 0, name_='XSDataInputSubWedgeMerge' )
        outfile.close()


    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataInputSubWedgeMerge.factory()
        rootObj.build(rootNode)
        return rootObj
    parseString = staticmethod( parseString ) 


    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataInputSubWedgeMerge.factory()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile ) 


    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO.StringIO()
        oStreamString.write('<?xml version="1.0" ?>\n')
        self.export( oStreamString, 0, name_="XSDataInputSubWedgeMerge" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    def exportLiteral(self, outfile, level, name_='XSDataInputSubWedgeMerge'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        pass
        XSDataInput.exportLiteralAttributes(self, outfile, level, name_)
    def exportLiteralChildren(self, outfile, level, name_):
        showIndent(outfile, level)
        outfile.write('subWedge=[\n')
        level += 1
        for subWedge in self.subWedge:
            showIndent(outfile, level)
            outfile.write('XSDataSubWedge(\n')
            subWedge.exportLiteral(outfile, level, name_='subWedge')
            showIndent(outfile, level)
            outfile.write('),\n')
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
        XSDataInput.exportLiteralChildren(self, outfile, level, name_)
    def build(self, node_):
        attrs = node_.attributes
        self.buildAttributes(attrs)
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildAttributes(self, attrs):
        XSDataInput.buildAttributes(self, attrs)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'subWedge':
            obj_ = XSDataSubWedge.factory()
            obj_.build(child_)
            self.subWedge.append(obj_)
        XSDataInput.buildChildren(self, child_, nodeName_)
# end class XSDataInputSubWedgeMerge


class XSDataIntegrationInput(XSDataGeneratePredictionInput):
    subclass = None
    def __init__(self, configuration=None, dataCollection=None, selectedIndexingSolution=None, crystalRefined=None, experimentalConditionRefined=None):
        XSDataGeneratePredictionInput.__init__(self, configuration, dataCollection, selectedIndexingSolution)
        self.crystalRefined = crystalRefined
        self.experimentalConditionRefined = experimentalConditionRefined
    def factory(*args_, **kwargs_):
        if XSDataIntegrationInput.subclass:
            return XSDataIntegrationInput.subclass(*args_, **kwargs_)
        else:
            return XSDataIntegrationInput(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getCrystalRefined(self): return self.crystalRefined
    def setCrystalRefined(self, crystalRefined): self.crystalRefined = crystalRefined
    def getExperimentalConditionRefined(self): return self.experimentalConditionRefined
    def setExperimentalConditionRefined(self, experimentalConditionRefined): self.experimentalConditionRefined = experimentalConditionRefined
    def export(self, outfile, level, name_='XSDataIntegrationInput'):
        showIndent(outfile, level)
        outfile.write('<%s>\n' % name_)
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='XSDataIntegrationInput'):
        XSDataGeneratePredictionInput.exportAttributes(self, outfile, level, name_='XSDataIntegrationInput')
    def exportChildren(self, outfile, level, name_='XSDataIntegrationInput'):
        if self.getCrystalRefined() != None :
            if self.crystalRefined:
                self.crystalRefined.export(outfile, level, name_='crystalRefined')
        if self.getExperimentalConditionRefined() != None :
            if self.experimentalConditionRefined:
                self.experimentalConditionRefined.export(outfile, level, name_='experimentalConditionRefined')
        XSDataGeneratePredictionInput.exportChildren(self, outfile, level, name_)

    #Only to export the entire XML tree to a file stream on disk
    def outputFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write("<?xml version=\"1.0\" ?>\n")
        self.export( outfile, 0, name_='XSDataIntegrationInput' )
        outfile.close()


    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataIntegrationInput.factory()
        rootObj.build(rootNode)
        return rootObj
    parseString = staticmethod( parseString ) 


    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataIntegrationInput.factory()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile ) 


    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO.StringIO()
        oStreamString.write('<?xml version="1.0" ?>\n')
        self.export( oStreamString, 0, name_="XSDataIntegrationInput" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    def exportLiteral(self, outfile, level, name_='XSDataIntegrationInput'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        pass
        XSDataGeneratePredictionInput.exportLiteralAttributes(self, outfile, level, name_)
    def exportLiteralChildren(self, outfile, level, name_):
        if self.crystalRefined:
            showIndent(outfile, level)
            outfile.write('crystalRefined=XSDataCrystal(\n')
            self.crystalRefined.exportLiteral(outfile, level, name_='crystalRefined')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.experimentalConditionRefined:
            showIndent(outfile, level)
            outfile.write('experimentalConditionRefined=XSDataExperimentalCondition(\n')
            self.experimentalConditionRefined.exportLiteral(outfile, level, name_='experimentalConditionRefined')
            showIndent(outfile, level)
            outfile.write('),\n')
        XSDataGeneratePredictionInput.exportLiteralChildren(self, outfile, level, name_)
    def build(self, node_):
        attrs = node_.attributes
        self.buildAttributes(attrs)
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildAttributes(self, attrs):
        XSDataGeneratePredictionInput.buildAttributes(self, attrs)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'crystalRefined':
            obj_ = XSDataCrystal.factory()
            obj_.build(child_)
            self.setCrystalRefined(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'experimentalConditionRefined':
            obj_ = XSDataExperimentalCondition.factory()
            obj_.build(child_)
            self.setExperimentalConditionRefined(obj_)
        XSDataGeneratePredictionInput.buildChildren(self, child_, nodeName_)
# end class XSDataIntegrationInput


class XSDataIntegrationResult(XSDataResult):
    subclass = None
    def __init__(self, integrationSubWedgeResult=None):
        XSDataResult.__init__(self)
        if integrationSubWedgeResult is None:
            self.integrationSubWedgeResult = []
        else:
            self.integrationSubWedgeResult = integrationSubWedgeResult
    def factory(*args_, **kwargs_):
        if XSDataIntegrationResult.subclass:
            return XSDataIntegrationResult.subclass(*args_, **kwargs_)
        else:
            return XSDataIntegrationResult(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getIntegrationSubWedgeResult(self): return self.integrationSubWedgeResult
    def setIntegrationSubWedgeResult(self, integrationSubWedgeResult): self.integrationSubWedgeResult = integrationSubWedgeResult
    def addIntegrationSubWedgeResult(self, value): self.integrationSubWedgeResult.append(value)
    def insertIntegrationSubWedgeResult(self, index, value): self.integrationSubWedgeResult[index] = value
    def export(self, outfile, level, name_='XSDataIntegrationResult'):
        showIndent(outfile, level)
        outfile.write('<%s>\n' % name_)
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='XSDataIntegrationResult'):
        XSDataResult.exportAttributes(self, outfile, level, name_='XSDataIntegrationResult')
    def exportChildren(self, outfile, level, name_='XSDataIntegrationResult'):
        for integrationSubWedgeResult_ in self.getIntegrationSubWedgeResult():
            integrationSubWedgeResult_.export(outfile, level, name_='integrationSubWedgeResult')
        XSDataResult.exportChildren(self, outfile, level, name_)

    #Only to export the entire XML tree to a file stream on disk
    def outputFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write("<?xml version=\"1.0\" ?>\n")
        self.export( outfile, 0, name_='XSDataIntegrationResult' )
        outfile.close()


    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataIntegrationResult.factory()
        rootObj.build(rootNode)
        return rootObj
    parseString = staticmethod( parseString ) 


    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataIntegrationResult.factory()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile ) 


    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO.StringIO()
        oStreamString.write('<?xml version="1.0" ?>\n')
        self.export( oStreamString, 0, name_="XSDataIntegrationResult" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    def exportLiteral(self, outfile, level, name_='XSDataIntegrationResult'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        pass
        XSDataResult.exportLiteralAttributes(self, outfile, level, name_)
    def exportLiteralChildren(self, outfile, level, name_):
        showIndent(outfile, level)
        outfile.write('integrationSubWedgeResult=[\n')
        level += 1
        for integrationSubWedgeResult in self.integrationSubWedgeResult:
            showIndent(outfile, level)
            outfile.write('XSDataIntegrationSubWedgeResult(\n')
            integrationSubWedgeResult.exportLiteral(outfile, level, name_='integrationSubWedgeResult')
            showIndent(outfile, level)
            outfile.write('),\n')
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
        XSDataResult.exportLiteralChildren(self, outfile, level, name_)
    def build(self, node_):
        attrs = node_.attributes
        self.buildAttributes(attrs)
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildAttributes(self, attrs):
        XSDataResult.buildAttributes(self, attrs)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'integrationSubWedgeResult':
            obj_ = XSDataIntegrationSubWedgeResult.factory()
            obj_.build(child_)
            self.integrationSubWedgeResult.append(obj_)
# end class XSDataIntegrationResult


class XSDataIntegrationSubWedgeResult(XSData):
    subclass = None
    def __init__(self, bestfileDat=None, bestfileHKL=None, bestfilePar=None, experimentalConditionRefined=None, generatedMTZFile=None, integrationLogFile=None, subWedgeNumber=None, statistics=None, statisticsPerResolutionBin=None):
        XSData.__init__(self)
        self.bestfileDat = bestfileDat
        self.bestfileHKL = bestfileHKL
        self.bestfilePar = bestfilePar
        self.experimentalConditionRefined = experimentalConditionRefined
        self.generatedMTZFile = generatedMTZFile
        self.integrationLogFile = integrationLogFile
        self.subWedgeNumber = subWedgeNumber
        self.statistics = statistics
        if statisticsPerResolutionBin is None:
            self.statisticsPerResolutionBin = []
        else:
            self.statisticsPerResolutionBin = statisticsPerResolutionBin
    def factory(*args_, **kwargs_):
        if XSDataIntegrationSubWedgeResult.subclass:
            return XSDataIntegrationSubWedgeResult.subclass(*args_, **kwargs_)
        else:
            return XSDataIntegrationSubWedgeResult(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getBestfileDat(self): return self.bestfileDat
    def setBestfileDat(self, bestfileDat): self.bestfileDat = bestfileDat
    def getBestfileHKL(self): return self.bestfileHKL
    def setBestfileHKL(self, bestfileHKL): self.bestfileHKL = bestfileHKL
    def getBestfilePar(self): return self.bestfilePar
    def setBestfilePar(self, bestfilePar): self.bestfilePar = bestfilePar
    def getExperimentalConditionRefined(self): return self.experimentalConditionRefined
    def setExperimentalConditionRefined(self, experimentalConditionRefined): self.experimentalConditionRefined = experimentalConditionRefined
    def getGeneratedMTZFile(self): return self.generatedMTZFile
    def setGeneratedMTZFile(self, generatedMTZFile): self.generatedMTZFile = generatedMTZFile
    def getIntegrationLogFile(self): return self.integrationLogFile
    def setIntegrationLogFile(self, integrationLogFile): self.integrationLogFile = integrationLogFile
    def getSubWedgeNumber(self): return self.subWedgeNumber
    def setSubWedgeNumber(self, subWedgeNumber): self.subWedgeNumber = subWedgeNumber
    def getStatistics(self): return self.statistics
    def setStatistics(self, statistics): self.statistics = statistics
    def getStatisticsPerResolutionBin(self): return self.statisticsPerResolutionBin
    def setStatisticsPerResolutionBin(self, statisticsPerResolutionBin): self.statisticsPerResolutionBin = statisticsPerResolutionBin
    def addStatisticsPerResolutionBin(self, value): self.statisticsPerResolutionBin.append(value)
    def insertStatisticsPerResolutionBin(self, index, value): self.statisticsPerResolutionBin[index] = value
    def export(self, outfile, level, name_='XSDataIntegrationSubWedgeResult'):
        showIndent(outfile, level)
        outfile.write('<%s>\n' % name_)
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='XSDataIntegrationSubWedgeResult'):
        XSData.exportAttributes(self, outfile, level, name_='XSDataIntegrationSubWedgeResult')
    def exportChildren(self, outfile, level, name_='XSDataIntegrationSubWedgeResult'):
        if self.bestfileDat:
            self.bestfileDat.export(outfile, level, name_='bestfileDat')
        if self.bestfileHKL:
            self.bestfileHKL.export(outfile, level, name_='bestfileHKL')
        if self.bestfilePar:
            self.bestfilePar.export(outfile, level, name_='bestfilePar')
        if self.experimentalConditionRefined:
            self.experimentalConditionRefined.export(outfile, level, name_='experimentalConditionRefined')
        if self.generatedMTZFile:
            self.generatedMTZFile.export(outfile, level, name_='generatedMTZFile')
        if self.integrationLogFile:
            self.integrationLogFile.export(outfile, level, name_='integrationLogFile')
        if self.subWedgeNumber:
            self.subWedgeNumber.export(outfile, level, name_='subWedgeNumber')
        if self.statistics:
            self.statistics.export(outfile, level, name_='statistics')
        for statisticsPerResolutionBin_ in self.getStatisticsPerResolutionBin():
            statisticsPerResolutionBin_.export(outfile, level, name_='statisticsPerResolutionBin')
        XSData.exportChildren(self, outfile, level, name_)

    #Only to export the entire XML tree to a file stream on disk
    def outputFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write("<?xml version=\"1.0\" ?>\n")
        self.export( outfile, 0, name_='XSDataIntegrationSubWedgeResult' )
        outfile.close()


    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataIntegrationSubWedgeResult.factory()
        rootObj.build(rootNode)
        return rootObj
    parseString = staticmethod( parseString ) 


    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataIntegrationSubWedgeResult.factory()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile ) 


    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO.StringIO()
        oStreamString.write('<?xml version="1.0" ?>\n')
        self.export( oStreamString, 0, name_="XSDataIntegrationSubWedgeResult" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    def exportLiteral(self, outfile, level, name_='XSDataIntegrationSubWedgeResult'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        pass
        XSData.exportLiteralAttributes(self, outfile, level, name_)
    def exportLiteralChildren(self, outfile, level, name_):
        if self.bestfileDat:
            showIndent(outfile, level)
            outfile.write('bestfileDat=XSDataString(\n')
            self.bestfileDat.exportLiteral(outfile, level, name_='bestfileDat')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.bestfileHKL:
            showIndent(outfile, level)
            outfile.write('bestfileHKL=XSDataString(\n')
            self.bestfileHKL.exportLiteral(outfile, level, name_='bestfileHKL')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.bestfilePar:
            showIndent(outfile, level)
            outfile.write('bestfilePar=XSDataString(\n')
            self.bestfilePar.exportLiteral(outfile, level, name_='bestfilePar')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.experimentalConditionRefined:
            showIndent(outfile, level)
            outfile.write('experimentalConditionRefined=XSDataExperimentalCondition(\n')
            self.experimentalConditionRefined.exportLiteral(outfile, level, name_='experimentalConditionRefined')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.generatedMTZFile:
            showIndent(outfile, level)
            outfile.write('generatedMTZFile=XSDataFile(\n')
            self.generatedMTZFile.exportLiteral(outfile, level, name_='generatedMTZFile')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.integrationLogFile:
            showIndent(outfile, level)
            outfile.write('integrationLogFile=XSDataFile(\n')
            self.integrationLogFile.exportLiteral(outfile, level, name_='integrationLogFile')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.subWedgeNumber:
            showIndent(outfile, level)
            outfile.write('subWedgeNumber=XSDataInteger(\n')
            self.subWedgeNumber.exportLiteral(outfile, level, name_='subWedgeNumber')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.statistics:
            showIndent(outfile, level)
            outfile.write('statistics=XSDataStatisticsIntegration(\n')
            self.statistics.exportLiteral(outfile, level, name_='statistics')
            showIndent(outfile, level)
            outfile.write('),\n')
        showIndent(outfile, level)
        outfile.write('statisticsPerResolutionBin=[\n')
        level += 1
        for statisticsPerResolutionBin in self.statisticsPerResolutionBin:
            showIndent(outfile, level)
            outfile.write('XSDataStatisticsIntegrationPerResolutionBin(\n')
            statisticsPerResolutionBin.exportLiteral(outfile, level, name_='statisticsPerResolutionBin')
            showIndent(outfile, level)
            outfile.write('),\n')
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
        XSData.exportLiteralChildren(self, outfile, level, name_)
    def build(self, node_):
        attrs = node_.attributes
        self.buildAttributes(attrs)
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildAttributes(self, attrs):
        XSData.buildAttributes(self, attrs)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'bestfileDat':
            obj_ = XSDataString.factory()
            obj_.build(child_)
            self.setBestfileDat(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'bestfileHKL':
            obj_ = XSDataString.factory()
            obj_.build(child_)
            self.setBestfileHKL(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'bestfilePar':
            obj_ = XSDataString.factory()
            obj_.build(child_)
            self.setBestfilePar(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'experimentalConditionRefined':
            obj_ = XSDataExperimentalCondition.factory()
            obj_.build(child_)
            self.setExperimentalConditionRefined(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'generatedMTZFile':
            obj_ = XSDataFile.factory()
            obj_.build(child_)
            self.setGeneratedMTZFile(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'integrationLogFile':
            obj_ = XSDataFile.factory()
            obj_.build(child_)
            self.setIntegrationLogFile(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'subWedgeNumber':
            obj_ = XSDataInteger.factory()
            obj_.build(child_)
            self.setSubWedgeNumber(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'statistics':
            obj_ = XSDataStatisticsIntegration.factory()
            obj_.build(child_)
            self.setStatistics(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'statisticsPerResolutionBin':
            obj_ = XSDataStatisticsIntegrationPerResolutionBin.factory()
            obj_.build(child_)
            self.statisticsPerResolutionBin.append(obj_)
# end class XSDataIntegrationSubWedgeResult


class XSDataLigand(XSData):
    subclass = None
    def __init__(self, numberOfCopies=None, numberOfLightAtoms=None, heavyAtoms=None):
        XSData.__init__(self)
        self.numberOfCopies = numberOfCopies
        self.numberOfLightAtoms = numberOfLightAtoms
        self.heavyAtoms = heavyAtoms
    def factory(*args_, **kwargs_):
        if XSDataLigand.subclass:
            return XSDataLigand.subclass(*args_, **kwargs_)
        else:
            return XSDataLigand(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getNumberOfCopies(self): return self.numberOfCopies
    def setNumberOfCopies(self, numberOfCopies): self.numberOfCopies = numberOfCopies
    def getNumberOfLightAtoms(self): return self.numberOfLightAtoms
    def setNumberOfLightAtoms(self, numberOfLightAtoms): self.numberOfLightAtoms = numberOfLightAtoms
    def getHeavyAtoms(self): return self.heavyAtoms
    def setHeavyAtoms(self, heavyAtoms): self.heavyAtoms = heavyAtoms
    def export(self, outfile, level, name_='XSDataLigand'):
        showIndent(outfile, level)
        outfile.write('<%s>\n' % name_)
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='XSDataLigand'):
        XSData.exportAttributes(self, outfile, level, name_='XSDataLigand')
    def exportChildren(self, outfile, level, name_='XSDataLigand'):
        if self.numberOfCopies:
            self.numberOfCopies.export(outfile, level, name_='numberOfCopies')
        if self.numberOfLightAtoms:
            self.numberOfLightAtoms.export(outfile, level, name_='numberOfLightAtoms')
        if self.heavyAtoms:
            self.heavyAtoms.export(outfile, level, name_='heavyAtoms')
        XSData.exportChildren(self, outfile, level, name_)

    #Only to export the entire XML tree to a file stream on disk
    def outputFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write("<?xml version=\"1.0\" ?>\n")
        self.export( outfile, 0, name_='XSDataLigand' )
        outfile.close()


    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataLigand.factory()
        rootObj.build(rootNode)
        return rootObj
    parseString = staticmethod( parseString ) 


    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataLigand.factory()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile ) 


    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO.StringIO()
        oStreamString.write('<?xml version="1.0" ?>\n')
        self.export( oStreamString, 0, name_="XSDataLigand" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    def exportLiteral(self, outfile, level, name_='XSDataLigand'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        pass
        XSData.exportLiteralAttributes(self, outfile, level, name_)
    def exportLiteralChildren(self, outfile, level, name_):
        if self.numberOfCopies:
            showIndent(outfile, level)
            outfile.write('numberOfCopies=XSDataFloat(\n')
            self.numberOfCopies.exportLiteral(outfile, level, name_='numberOfCopies')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.numberOfLightAtoms:
            showIndent(outfile, level)
            outfile.write('numberOfLightAtoms=XSDataFloat(\n')
            self.numberOfLightAtoms.exportLiteral(outfile, level, name_='numberOfLightAtoms')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.heavyAtoms:
            showIndent(outfile, level)
            outfile.write('heavyAtoms=XSDataAtomicComposition(\n')
            self.heavyAtoms.exportLiteral(outfile, level, name_='heavyAtoms')
            showIndent(outfile, level)
            outfile.write('),\n')
        XSData.exportLiteralChildren(self, outfile, level, name_)
    def build(self, node_):
        attrs = node_.attributes
        self.buildAttributes(attrs)
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildAttributes(self, attrs):
        XSData.buildAttributes(self, attrs)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'numberOfCopies':
            obj_ = XSDataFloat.factory()
            obj_.build(child_)
            self.setNumberOfCopies(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'numberOfLightAtoms':
            obj_ = XSDataFloat.factory()
            obj_.build(child_)
            self.setNumberOfLightAtoms(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'heavyAtoms':
            obj_ = XSDataAtomicComposition.factory()
            obj_.build(child_)
            self.setHeavyAtoms(obj_)
# end class XSDataLigand


class XSDataOrientation(XSData):
    subclass = None
    def __init__(self, matrixA=None, matrixU=None):
        XSData.__init__(self)
        self.matrixA = matrixA
        self.matrixU = matrixU
    def factory(*args_, **kwargs_):
        if XSDataOrientation.subclass:
            return XSDataOrientation.subclass(*args_, **kwargs_)
        else:
            return XSDataOrientation(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getMatrixA(self): return self.matrixA
    def setMatrixA(self, matrixA): self.matrixA = matrixA
    def getMatrixU(self): return self.matrixU
    def setMatrixU(self, matrixU): self.matrixU = matrixU
    def export(self, outfile, level, name_='XSDataOrientation'):
        showIndent(outfile, level)
        outfile.write('<%s>\n' % name_)
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='XSDataOrientation'):
        XSData.exportAttributes(self, outfile, level, name_='XSDataOrientation')
    def exportChildren(self, outfile, level, name_='XSDataOrientation'):
        if self.matrixA:
            self.matrixA.export(outfile, level, name_='matrixA')
        if self.matrixU:
            self.matrixU.export(outfile, level, name_='matrixU')
        XSData.exportChildren(self, outfile, level, name_)

    #Only to export the entire XML tree to a file stream on disk
    def outputFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write("<?xml version=\"1.0\" ?>\n")
        self.export( outfile, 0, name_='XSDataOrientation' )
        outfile.close()


    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataOrientation.factory()
        rootObj.build(rootNode)
        return rootObj
    parseString = staticmethod( parseString ) 


    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataOrientation.factory()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile ) 


    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO.StringIO()
        oStreamString.write('<?xml version="1.0" ?>\n')
        self.export( oStreamString, 0, name_="XSDataOrientation" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    def exportLiteral(self, outfile, level, name_='XSDataOrientation'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        pass
        XSData.exportLiteralAttributes(self, outfile, level, name_)
    def exportLiteralChildren(self, outfile, level, name_):
        if self.matrixA:
            showIndent(outfile, level)
            outfile.write('matrixA=XSDataMatrixDouble(\n')
            self.matrixA.exportLiteral(outfile, level, name_='matrixA')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.matrixU:
            showIndent(outfile, level)
            outfile.write('matrixU=XSDataMatrixDouble(\n')
            self.matrixU.exportLiteral(outfile, level, name_='matrixU')
            showIndent(outfile, level)
            outfile.write('),\n')
        XSData.exportLiteralChildren(self, outfile, level, name_)
    def build(self, node_):
        attrs = node_.attributes
        self.buildAttributes(attrs)
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildAttributes(self, attrs):
        XSData.buildAttributes(self, attrs)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'matrixA':
            obj_ = XSDataMatrixDouble.factory()
            obj_.build(child_)
            self.setMatrixA(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'matrixU':
            obj_ = XSDataMatrixDouble.factory()
            obj_.build(child_)
            self.setMatrixU(obj_)
# end class XSDataOrientation


class XSDataResolutionBin(XSData):
    subclass = None
    def __init__(self, averageIntensity=None, averageIntensityOverAverageSigma=None, averageSigma=None, chi2=None, completeness=None, IOverSigma=None, IOverSigmaChi=None, maxResolution=None, minResolution=None, percentageOverload=None, redundancy=None, rFactor=None, rFriedel=None):
        XSData.__init__(self)
        self.averageIntensity = averageIntensity
        self.averageIntensityOverAverageSigma = averageIntensityOverAverageSigma
        self.averageSigma = averageSigma
        self.chi2 = chi2
        self.completeness = completeness
        self.IOverSigma = IOverSigma
        self.IOverSigmaChi = IOverSigmaChi
        self.maxResolution = maxResolution
        self.minResolution = minResolution
        self.percentageOverload = percentageOverload
        self.redundancy = redundancy
        self.rFactor = rFactor
        self.rFriedel = rFriedel
    def factory(*args_, **kwargs_):
        if XSDataResolutionBin.subclass:
            return XSDataResolutionBin.subclass(*args_, **kwargs_)
        else:
            return XSDataResolutionBin(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getAverageIntensity(self): return self.averageIntensity
    def setAverageIntensity(self, averageIntensity): self.averageIntensity = averageIntensity
    def getAverageIntensityOverAverageSigma(self): return self.averageIntensityOverAverageSigma
    def setAverageIntensityOverAverageSigma(self, averageIntensityOverAverageSigma): self.averageIntensityOverAverageSigma = averageIntensityOverAverageSigma
    def getAverageSigma(self): return self.averageSigma
    def setAverageSigma(self, averageSigma): self.averageSigma = averageSigma
    def getChi2(self): return self.chi2
    def setChi2(self, chi2): self.chi2 = chi2
    def getCompleteness(self): return self.completeness
    def setCompleteness(self, completeness): self.completeness = completeness
    def getIOverSigma(self): return self.IOverSigma
    def setIOverSigma(self, IOverSigma): self.IOverSigma = IOverSigma
    def getIOverSigmaChi(self): return self.IOverSigmaChi
    def setIOverSigmaChi(self, IOverSigmaChi): self.IOverSigmaChi = IOverSigmaChi
    def getMaxResolution(self): return self.maxResolution
    def setMaxResolution(self, maxResolution): self.maxResolution = maxResolution
    def getMinResolution(self): return self.minResolution
    def setMinResolution(self, minResolution): self.minResolution = minResolution
    def getPercentageOverload(self): return self.percentageOverload
    def setPercentageOverload(self, percentageOverload): self.percentageOverload = percentageOverload
    def getRedundancy(self): return self.redundancy
    def setRedundancy(self, redundancy): self.redundancy = redundancy
    def getRFactor(self): return self.rFactor
    def setRFactor(self, rFactor): self.rFactor = rFactor
    def getRFriedel(self): return self.rFriedel
    def setRFriedel(self, rFriedel): self.rFriedel = rFriedel
    def export(self, outfile, level, name_='XSDataResolutionBin'):
        showIndent(outfile, level)
        outfile.write('<%s>\n' % name_)
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='XSDataResolutionBin'):
        XSData.exportAttributes(self, outfile, level, name_='XSDataResolutionBin')
    def exportChildren(self, outfile, level, name_='XSDataResolutionBin'):
        if self.averageIntensity:
            self.averageIntensity.export(outfile, level, name_='averageIntensity')
        if self.averageIntensityOverAverageSigma:
            self.averageIntensityOverAverageSigma.export(outfile, level, name_='averageIntensityOverAverageSigma')
        if self.averageSigma:
            self.averageSigma.export(outfile, level, name_='averageSigma')
        if self.chi2:
            self.chi2.export(outfile, level, name_='chi2')
        if self.completeness:
            self.completeness.export(outfile, level, name_='completeness')
        if self.IOverSigma:
            self.IOverSigma.export(outfile, level, name_='IOverSigma')
        if self.IOverSigmaChi:
            self.IOverSigmaChi.export(outfile, level, name_='IOverSigmaChi')
        if self.maxResolution:
            self.maxResolution.export(outfile, level, name_='maxResolution')
        if self.minResolution:
            self.minResolution.export(outfile, level, name_='minResolution')
        if self.percentageOverload:
            self.percentageOverload.export(outfile, level, name_='percentageOverload')
        if self.redundancy:
            self.redundancy.export(outfile, level, name_='redundancy')
        if self.rFactor:
            self.rFactor.export(outfile, level, name_='rFactor')
        if self.rFriedel:
            self.rFriedel.export(outfile, level, name_='rFriedel')
        XSData.exportChildren(self, outfile, level, name_)

    #Only to export the entire XML tree to a file stream on disk
    def outputFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write("<?xml version=\"1.0\" ?>\n")
        self.export( outfile, 0, name_='XSDataResolutionBin' )
        outfile.close()


    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataResolutionBin.factory()
        rootObj.build(rootNode)
        return rootObj
    parseString = staticmethod( parseString ) 


    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataResolutionBin.factory()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile ) 


    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO.StringIO()
        oStreamString.write('<?xml version="1.0" ?>\n')
        self.export( oStreamString, 0, name_="XSDataResolutionBin" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    def exportLiteral(self, outfile, level, name_='XSDataResolutionBin'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        pass
        XSData.exportLiteralAttributes(self, outfile, level, name_)
    def exportLiteralChildren(self, outfile, level, name_):
        if self.averageIntensity:
            showIndent(outfile, level)
            outfile.write('averageIntensity=XSDataFloat(\n')
            self.averageIntensity.exportLiteral(outfile, level, name_='averageIntensity')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.averageIntensityOverAverageSigma:
            showIndent(outfile, level)
            outfile.write('averageIntensityOverAverageSigma=XSDataFloat(\n')
            self.averageIntensityOverAverageSigma.exportLiteral(outfile, level, name_='averageIntensityOverAverageSigma')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.averageSigma:
            showIndent(outfile, level)
            outfile.write('averageSigma=XSDataFloat(\n')
            self.averageSigma.exportLiteral(outfile, level, name_='averageSigma')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.chi2:
            showIndent(outfile, level)
            outfile.write('chi2=XSDataFloat(\n')
            self.chi2.exportLiteral(outfile, level, name_='chi2')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.completeness:
            showIndent(outfile, level)
            outfile.write('completeness=XSDataFloat(\n')
            self.completeness.exportLiteral(outfile, level, name_='completeness')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.IOverSigma:
            showIndent(outfile, level)
            outfile.write('IOverSigma=XSDataFloat(\n')
            self.IOverSigma.exportLiteral(outfile, level, name_='IOverSigma')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.IOverSigmaChi:
            showIndent(outfile, level)
            outfile.write('IOverSigmaChi=XSDataFloat(\n')
            self.IOverSigmaChi.exportLiteral(outfile, level, name_='IOverSigmaChi')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.maxResolution:
            showIndent(outfile, level)
            outfile.write('maxResolution=XSDataFloat(\n')
            self.maxResolution.exportLiteral(outfile, level, name_='maxResolution')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.minResolution:
            showIndent(outfile, level)
            outfile.write('minResolution=XSDataFloat(\n')
            self.minResolution.exportLiteral(outfile, level, name_='minResolution')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.percentageOverload:
            showIndent(outfile, level)
            outfile.write('percentageOverload=XSDataFloat(\n')
            self.percentageOverload.exportLiteral(outfile, level, name_='percentageOverload')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.redundancy:
            showIndent(outfile, level)
            outfile.write('redundancy=XSDataFloat(\n')
            self.redundancy.exportLiteral(outfile, level, name_='redundancy')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.rFactor:
            showIndent(outfile, level)
            outfile.write('rFactor=XSDataFloat(\n')
            self.rFactor.exportLiteral(outfile, level, name_='rFactor')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.rFriedel:
            showIndent(outfile, level)
            outfile.write('rFriedel=XSDataFloat(\n')
            self.rFriedel.exportLiteral(outfile, level, name_='rFriedel')
            showIndent(outfile, level)
            outfile.write('),\n')
        XSData.exportLiteralChildren(self, outfile, level, name_)
    def build(self, node_):
        attrs = node_.attributes
        self.buildAttributes(attrs)
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildAttributes(self, attrs):
        XSData.buildAttributes(self, attrs)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'averageIntensity':
            obj_ = XSDataFloat.factory()
            obj_.build(child_)
            self.setAverageIntensity(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'averageIntensityOverAverageSigma':
            obj_ = XSDataFloat.factory()
            obj_.build(child_)
            self.setAverageIntensityOverAverageSigma(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'averageSigma':
            obj_ = XSDataFloat.factory()
            obj_.build(child_)
            self.setAverageSigma(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'chi2':
            obj_ = XSDataFloat.factory()
            obj_.build(child_)
            self.setChi2(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'completeness':
            obj_ = XSDataFloat.factory()
            obj_.build(child_)
            self.setCompleteness(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'IOverSigma':
            obj_ = XSDataFloat.factory()
            obj_.build(child_)
            self.setIOverSigma(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'IOverSigmaChi':
            obj_ = XSDataFloat.factory()
            obj_.build(child_)
            self.setIOverSigmaChi(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'maxResolution':
            obj_ = XSDataFloat.factory()
            obj_.build(child_)
            self.setMaxResolution(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'minResolution':
            obj_ = XSDataFloat.factory()
            obj_.build(child_)
            self.setMinResolution(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'percentageOverload':
            obj_ = XSDataFloat.factory()
            obj_.build(child_)
            self.setPercentageOverload(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'redundancy':
            obj_ = XSDataFloat.factory()
            obj_.build(child_)
            self.setRedundancy(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'rFactor':
            obj_ = XSDataFloat.factory()
            obj_.build(child_)
            self.setRFactor(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'rFriedel':
            obj_ = XSDataFloat.factory()
            obj_.build(child_)
            self.setRFriedel(obj_)
# end class XSDataResolutionBin


class XSDataResultCharacterisation(XSDataResult):
    subclass = None
    def __init__(self, dataCollection=None, imageQualityIndicators=None, integrationResult=None, strategyResult=None, executiveSummary=None, shortSummary=None, statusMessage=None, indexingResult=None):
        XSDataResult.__init__(self)
        self.dataCollection = dataCollection
        if imageQualityIndicators is None:
            self.imageQualityIndicators = []
        else:
            self.imageQualityIndicators = imageQualityIndicators
        self.integrationResult = integrationResult
        self.strategyResult = strategyResult
        self.executiveSummary = executiveSummary
        self.shortSummary = shortSummary
        self.statusMessage = statusMessage
        self.indexingResult = indexingResult
    def factory(*args_, **kwargs_):
        if XSDataResultCharacterisation.subclass:
            return XSDataResultCharacterisation.subclass(*args_, **kwargs_)
        else:
            return XSDataResultCharacterisation(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getDataCollection(self): return self.dataCollection
    def setDataCollection(self, dataCollection): self.dataCollection = dataCollection
    def getImageQualityIndicators(self): return self.imageQualityIndicators
    def setImageQualityIndicators(self, imageQualityIndicators): self.imageQualityIndicators = imageQualityIndicators
    def addImageQualityIndicators(self, value): self.imageQualityIndicators.append(value)
    def insertImageQualityIndicators(self, index, value): self.imageQualityIndicators[index] = value
    def getIntegrationResult(self): return self.integrationResult
    def setIntegrationResult(self, integrationResult): self.integrationResult = integrationResult
    def getStrategyResult(self): return self.strategyResult
    def setStrategyResult(self, strategyResult): self.strategyResult = strategyResult
    def getExecutiveSummary(self): return self.executiveSummary
    def setExecutiveSummary(self, executiveSummary): self.executiveSummary = executiveSummary
    def getShortSummary(self): return self.shortSummary
    def setShortSummary(self, shortSummary): self.shortSummary = shortSummary
    def getStatusMessage(self): return self.statusMessage
    def setStatusMessage(self, statusMessage): self.statusMessage = statusMessage
    def getIndexingResult(self): return self.indexingResult
    def setIndexingResult(self, indexingResult): self.indexingResult = indexingResult
    def export(self, outfile, level, name_='XSDataResultCharacterisation'):
        showIndent(outfile, level)
        outfile.write('<%s>\n' % name_)
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='XSDataResultCharacterisation'):
        XSDataResult.exportAttributes(self, outfile, level, name_='XSDataResultCharacterisation')
    def exportChildren(self, outfile, level, name_='XSDataResultCharacterisation'):
        if self.dataCollection:
            self.dataCollection.export(outfile, level, name_='dataCollection')
        for imageQualityIndicators_ in self.getImageQualityIndicators():
            imageQualityIndicators_.export(outfile, level, name_='imageQualityIndicators')
        if self.getIntegrationResult() != None :
            if self.integrationResult:
                self.integrationResult.export(outfile, level, name_='integrationResult')
        if self.getStrategyResult() != None :
            if self.strategyResult:
                self.strategyResult.export(outfile, level, name_='strategyResult')
        if self.executiveSummary:
            self.executiveSummary.export(outfile, level, name_='executiveSummary')
        if self.shortSummary:
            self.shortSummary.export(outfile, level, name_='shortSummary')
        if self.statusMessage:
            self.statusMessage.export(outfile, level, name_='statusMessage')
        if self.getIndexingResult() != None :
            if self.indexingResult:
                self.indexingResult.export(outfile, level, name_='indexingResult')
        XSDataResult.exportChildren(self, outfile, level, name_)

    #Only to export the entire XML tree to a file stream on disk
    def outputFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write("<?xml version=\"1.0\" ?>\n")
        self.export( outfile, 0, name_='XSDataResultCharacterisation' )
        outfile.close()


    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataResultCharacterisation.factory()
        rootObj.build(rootNode)
        return rootObj
    parseString = staticmethod( parseString ) 


    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataResultCharacterisation.factory()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile ) 


    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO.StringIO()
        oStreamString.write('<?xml version="1.0" ?>\n')
        self.export( oStreamString, 0, name_="XSDataResultCharacterisation" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    def exportLiteral(self, outfile, level, name_='XSDataResultCharacterisation'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        pass
        XSDataResult.exportLiteralAttributes(self, outfile, level, name_)
    def exportLiteralChildren(self, outfile, level, name_):
        if self.dataCollection:
            showIndent(outfile, level)
            outfile.write('dataCollection=XSDataCollection(\n')
            self.dataCollection.exportLiteral(outfile, level, name_='dataCollection')
            showIndent(outfile, level)
            outfile.write('),\n')
        showIndent(outfile, level)
        outfile.write('imageQualityIndicators=[\n')
        level += 1
        for imageQualityIndicators in self.imageQualityIndicators:
            showIndent(outfile, level)
            outfile.write('XSDataImageQualityIndicators(\n')
            imageQualityIndicators.exportLiteral(outfile, level, name_='imageQualityIndicators')
            showIndent(outfile, level)
            outfile.write('),\n')
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
        if self.integrationResult:
            showIndent(outfile, level)
            outfile.write('integrationResult=XSDataIntegrationResult(\n')
            self.integrationResult.exportLiteral(outfile, level, name_='integrationResult')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.strategyResult:
            showIndent(outfile, level)
            outfile.write('strategyResult=XSDataResultStrategy(\n')
            self.strategyResult.exportLiteral(outfile, level, name_='strategyResult')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.executiveSummary:
            showIndent(outfile, level)
            outfile.write('executiveSummary=XSDataString(\n')
            self.executiveSummary.exportLiteral(outfile, level, name_='executiveSummary')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.shortSummary:
            showIndent(outfile, level)
            outfile.write('shortSummary=XSDataString(\n')
            self.shortSummary.exportLiteral(outfile, level, name_='shortSummary')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.statusMessage:
            showIndent(outfile, level)
            outfile.write('statusMessage=XSDataString(\n')
            self.statusMessage.exportLiteral(outfile, level, name_='statusMessage')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.indexingResult:
            showIndent(outfile, level)
            outfile.write('indexingResult=XSDataIndexingResult(\n')
            self.indexingResult.exportLiteral(outfile, level, name_='indexingResult')
            showIndent(outfile, level)
            outfile.write('),\n')
        XSDataResult.exportLiteralChildren(self, outfile, level, name_)
    def build(self, node_):
        attrs = node_.attributes
        self.buildAttributes(attrs)
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildAttributes(self, attrs):
        XSDataResult.buildAttributes(self, attrs)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'dataCollection':
            obj_ = XSDataCollection.factory()
            obj_.build(child_)
            self.setDataCollection(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'imageQualityIndicators':
            obj_ = XSDataImageQualityIndicators.factory()
            obj_.build(child_)
            self.imageQualityIndicators.append(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'integrationResult':
            obj_ = XSDataIntegrationResult.factory()
            obj_.build(child_)
            self.setIntegrationResult(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'strategyResult':
            obj_ = XSDataResultStrategy.factory()
            obj_.build(child_)
            self.setStrategyResult(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'executiveSummary':
            obj_ = XSDataString.factory()
            obj_.build(child_)
            self.setExecutiveSummary(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'shortSummary':
            obj_ = XSDataString.factory()
            obj_.build(child_)
            self.setShortSummary(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'statusMessage':
            obj_ = XSDataString.factory()
            obj_.build(child_)
            self.setStatusMessage(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'indexingResult':
            obj_ = XSDataIndexingResult.factory()
            obj_.build(child_)
            self.setIndexingResult(obj_)
# end class XSDataResultCharacterisation


class XSDataResultControlISPyB(XSDataResult):
    subclass = None
    def __init__(self, valueOf_=''):
        XSDataResult.__init__(self)
        self.valueOf_ = valueOf_
    def factory(*args_, **kwargs_):
        if XSDataResultControlISPyB.subclass:
            return XSDataResultControlISPyB.subclass(*args_, **kwargs_)
        else:
            return XSDataResultControlISPyB(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getValueOf_(self): return self.valueOf_
    def setValueOf_(self, valueOf_): self.valueOf_ = valueOf_
    def export(self, outfile, level, name_='XSDataResultControlISPyB'):
        showIndent(outfile, level)
        outfile.write('<%s>' % name_)
        self.exportChildren(outfile, level + 1, name_)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='XSDataResultControlISPyB'):
        XSDataResult.exportAttributes(self, outfile, level, name_='XSDataResultControlISPyB')
    def exportChildren(self, outfile, level, name_='XSDataResultControlISPyB'):
        XSDataResult.exportChildren(self, outfile, level, name_)
        outfile.write(self.valueOf_)

    #Only to export the entire XML tree to a file stream on disk
    def outputFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write("<?xml version=\"1.0\" ?>\n")
        self.export( outfile, 0, name_='XSDataResultControlISPyB' )
        outfile.close()


    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataResultControlISPyB.factory()
        rootObj.build(rootNode)
        return rootObj
    parseString = staticmethod( parseString ) 


    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataResultControlISPyB.factory()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile ) 


    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO.StringIO()
        oStreamString.write('<?xml version="1.0" ?>\n')
        self.export( oStreamString, 0, name_="XSDataResultControlISPyB" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    def exportLiteral(self, outfile, level, name_='XSDataResultControlISPyB'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        pass
        XSDataResult.exportLiteralAttributes(self, outfile, level, name_)
    def exportLiteralChildren(self, outfile, level, name_):
        showIndent(outfile, level)
        outfile.write('valueOf_ = "%s",\n' % (self.valueOf_,))
        XSDataResult.exportLiteralChildren(self, outfile, level, name_)
    def build(self, node_):
        attrs = node_.attributes
        self.buildAttributes(attrs)
        self.valueOf_ = ''
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildAttributes(self, attrs):
        XSDataResult.buildAttributes(self, attrs)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.TEXT_NODE:
            self.valueOf_ += child_.nodeValue
# end class XSDataResultControlISPyB


class XSDataResultInducedRadiationProcess(XSDataResult):
    subclass = None
    def __init__(self, bFactor=None, crystal=None, scale=None):
        XSDataResult.__init__(self)
        self.bFactor = bFactor
        self.crystal = crystal
        self.scale = scale
    def factory(*args_, **kwargs_):
        if XSDataResultInducedRadiationProcess.subclass:
            return XSDataResultInducedRadiationProcess.subclass(*args_, **kwargs_)
        else:
            return XSDataResultInducedRadiationProcess(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getBFactor(self): return self.bFactor
    def setBFactor(self, bFactor): self.bFactor = bFactor
    def getCrystal(self): return self.crystal
    def setCrystal(self, crystal): self.crystal = crystal
    def getScale(self): return self.scale
    def setScale(self, scale): self.scale = scale
    def export(self, outfile, level, name_='XSDataResultInducedRadiationProcess'):
        showIndent(outfile, level)
        outfile.write('<%s>\n' % name_)
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='XSDataResultInducedRadiationProcess'):
        XSDataResult.exportAttributes(self, outfile, level, name_='XSDataResultInducedRadiationProcess')
    def exportChildren(self, outfile, level, name_='XSDataResultInducedRadiationProcess'):
        if self.bFactor:
            self.bFactor.export(outfile, level, name_='bFactor')
        if self.crystal:
            self.crystal.export(outfile, level, name_='crystal')
        if self.scale:
            self.scale.export(outfile, level, name_='scale')
        XSDataResult.exportChildren(self, outfile, level, name_)

    #Only to export the entire XML tree to a file stream on disk
    def outputFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write("<?xml version=\"1.0\" ?>\n")
        self.export( outfile, 0, name_='XSDataResultInducedRadiationProcess' )
        outfile.close()


    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataResultInducedRadiationProcess.factory()
        rootObj.build(rootNode)
        return rootObj
    parseString = staticmethod( parseString ) 


    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataResultInducedRadiationProcess.factory()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile ) 


    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO.StringIO()
        oStreamString.write('<?xml version="1.0" ?>\n')
        self.export( oStreamString, 0, name_="XSDataResultInducedRadiationProcess" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    def exportLiteral(self, outfile, level, name_='XSDataResultInducedRadiationProcess'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        pass
        XSDataResult.exportLiteralAttributes(self, outfile, level, name_)
    def exportLiteralChildren(self, outfile, level, name_):
        if self.bFactor:
            showIndent(outfile, level)
            outfile.write('bFactor=XSDataDouble(\n')
            self.bFactor.exportLiteral(outfile, level, name_='bFactor')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.crystal:
            showIndent(outfile, level)
            outfile.write('crystal=XSDataCrystal(\n')
            self.crystal.exportLiteral(outfile, level, name_='crystal')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.scale:
            showIndent(outfile, level)
            outfile.write('scale=XSDataDouble(\n')
            self.scale.exportLiteral(outfile, level, name_='scale')
            showIndent(outfile, level)
            outfile.write('),\n')
        XSDataResult.exportLiteralChildren(self, outfile, level, name_)
    def build(self, node_):
        attrs = node_.attributes
        self.buildAttributes(attrs)
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildAttributes(self, attrs):
        XSDataResult.buildAttributes(self, attrs)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'bFactor':
            obj_ = XSDataDouble.factory()
            obj_.build(child_)
            self.setBFactor(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'crystal':
            obj_ = XSDataCrystal.factory()
            obj_.build(child_)
            self.setCrystal(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'scale':
            obj_ = XSDataDouble.factory()
            obj_.build(child_)
            self.setScale(obj_)
# end class XSDataResultInducedRadiationProcess


class XSDataResultReadImageHeader(XSDataResult):
    subclass = None
    def __init__(self, subWedge=None):
        XSDataResult.__init__(self)
        self.subWedge = subWedge
    def factory(*args_, **kwargs_):
        if XSDataResultReadImageHeader.subclass:
            return XSDataResultReadImageHeader.subclass(*args_, **kwargs_)
        else:
            return XSDataResultReadImageHeader(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getSubWedge(self): return self.subWedge
    def setSubWedge(self, subWedge): self.subWedge = subWedge
    def export(self, outfile, level, name_='XSDataResultReadImageHeader'):
        showIndent(outfile, level)
        outfile.write('<%s>\n' % name_)
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='XSDataResultReadImageHeader'):
        XSDataResult.exportAttributes(self, outfile, level, name_='XSDataResultReadImageHeader')
    def exportChildren(self, outfile, level, name_='XSDataResultReadImageHeader'):
        if self.subWedge:
            self.subWedge.export(outfile, level, name_='subWedge')
        XSDataResult.exportChildren(self, outfile, level, name_)

    #Only to export the entire XML tree to a file stream on disk
    def outputFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write("<?xml version=\"1.0\" ?>\n")
        self.export( outfile, 0, name_='XSDataResultReadImageHeader' )
        outfile.close()


    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataResultReadImageHeader.factory()
        rootObj.build(rootNode)
        return rootObj
    parseString = staticmethod( parseString ) 


    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataResultReadImageHeader.factory()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile ) 


    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO.StringIO()
        oStreamString.write('<?xml version="1.0" ?>\n')
        self.export( oStreamString, 0, name_="XSDataResultReadImageHeader" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    def exportLiteral(self, outfile, level, name_='XSDataResultReadImageHeader'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        pass
        XSDataResult.exportLiteralAttributes(self, outfile, level, name_)
    def exportLiteralChildren(self, outfile, level, name_):
        if self.subWedge:
            showIndent(outfile, level)
            outfile.write('subWedge=XSDataSubWedge(\n')
            self.subWedge.exportLiteral(outfile, level, name_='subWedge')
            showIndent(outfile, level)
            outfile.write('),\n')
        XSDataResult.exportLiteralChildren(self, outfile, level, name_)
    def build(self, node_):
        attrs = node_.attributes
        self.buildAttributes(attrs)
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildAttributes(self, attrs):
        XSDataResult.buildAttributes(self, attrs)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'subWedge':
            obj_ = XSDataSubWedge.factory()
            obj_.build(child_)
            self.setSubWedge(obj_)
# end class XSDataResultReadImageHeader


class XSDataResultStrategy(XSDataResult):
    subclass = None
    def __init__(self, bestLogFile=None, raddoseLogFile=None, collectionPlan=None):
        XSDataResult.__init__(self)
        self.bestLogFile = bestLogFile
        self.raddoseLogFile = raddoseLogFile
        if collectionPlan is None:
            self.collectionPlan = []
        else:
            self.collectionPlan = collectionPlan
    def factory(*args_, **kwargs_):
        if XSDataResultStrategy.subclass:
            return XSDataResultStrategy.subclass(*args_, **kwargs_)
        else:
            return XSDataResultStrategy(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getBestLogFile(self): return self.bestLogFile
    def setBestLogFile(self, bestLogFile): self.bestLogFile = bestLogFile
    def getRaddoseLogFile(self): return self.raddoseLogFile
    def setRaddoseLogFile(self, raddoseLogFile): self.raddoseLogFile = raddoseLogFile
    def getCollectionPlan(self): return self.collectionPlan
    def setCollectionPlan(self, collectionPlan): self.collectionPlan = collectionPlan
    def addCollectionPlan(self, value): self.collectionPlan.append(value)
    def insertCollectionPlan(self, index, value): self.collectionPlan[index] = value
    def export(self, outfile, level, name_='XSDataResultStrategy'):
        showIndent(outfile, level)
        outfile.write('<%s>\n' % name_)
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='XSDataResultStrategy'):
        XSDataResult.exportAttributes(self, outfile, level, name_='XSDataResultStrategy')
    def exportChildren(self, outfile, level, name_='XSDataResultStrategy'):
        if self.getBestLogFile() != None :
            if self.bestLogFile:
                self.bestLogFile.export(outfile, level, name_='bestLogFile')
        if self.getRaddoseLogFile() != None :
            if self.raddoseLogFile:
                self.raddoseLogFile.export(outfile, level, name_='raddoseLogFile')
        for collectionPlan_ in self.getCollectionPlan():
            collectionPlan_.export(outfile, level, name_='collectionPlan')
        XSDataResult.exportChildren(self, outfile, level, name_)

    #Only to export the entire XML tree to a file stream on disk
    def outputFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write("<?xml version=\"1.0\" ?>\n")
        self.export( outfile, 0, name_='XSDataResultStrategy' )
        outfile.close()


    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataResultStrategy.factory()
        rootObj.build(rootNode)
        return rootObj
    parseString = staticmethod( parseString ) 


    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataResultStrategy.factory()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile ) 


    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO.StringIO()
        oStreamString.write('<?xml version="1.0" ?>\n')
        self.export( oStreamString, 0, name_="XSDataResultStrategy" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    def exportLiteral(self, outfile, level, name_='XSDataResultStrategy'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        pass
        XSDataResult.exportLiteralAttributes(self, outfile, level, name_)
    def exportLiteralChildren(self, outfile, level, name_):
        if self.bestLogFile:
            showIndent(outfile, level)
            outfile.write('bestLogFile=XSDataFile(\n')
            self.bestLogFile.exportLiteral(outfile, level, name_='bestLogFile')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.raddoseLogFile:
            showIndent(outfile, level)
            outfile.write('raddoseLogFile=XSDataFile(\n')
            self.raddoseLogFile.exportLiteral(outfile, level, name_='raddoseLogFile')
            showIndent(outfile, level)
            outfile.write('),\n')
        showIndent(outfile, level)
        outfile.write('collectionPlan=[\n')
        level += 1
        for collectionPlan in self.collectionPlan:
            showIndent(outfile, level)
            outfile.write('XSDataCollectionPlan(\n')
            collectionPlan.exportLiteral(outfile, level, name_='collectionPlan')
            showIndent(outfile, level)
            outfile.write('),\n')
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
        XSDataResult.exportLiteralChildren(self, outfile, level, name_)
    def build(self, node_):
        attrs = node_.attributes
        self.buildAttributes(attrs)
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildAttributes(self, attrs):
        XSDataResult.buildAttributes(self, attrs)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'bestLogFile':
            obj_ = XSDataFile.factory()
            obj_.build(child_)
            self.setBestLogFile(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'raddoseLogFile':
            obj_ = XSDataFile.factory()
            obj_.build(child_)
            self.setRaddoseLogFile(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'collectionPlan':
            obj_ = XSDataCollectionPlan.factory()
            obj_.build(child_)
            self.collectionPlan.append(obj_)
# end class XSDataResultStrategy


class XSDataResultSubWedgeAssemble(XSDataResult):
    subclass = None
    def __init__(self, subWedge=None):
        XSDataResult.__init__(self)
        if subWedge is None:
            self.subWedge = []
        else:
            self.subWedge = subWedge
    def factory(*args_, **kwargs_):
        if XSDataResultSubWedgeAssemble.subclass:
            return XSDataResultSubWedgeAssemble.subclass(*args_, **kwargs_)
        else:
            return XSDataResultSubWedgeAssemble(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getSubWedge(self): return self.subWedge
    def setSubWedge(self, subWedge): self.subWedge = subWedge
    def addSubWedge(self, value): self.subWedge.append(value)
    def insertSubWedge(self, index, value): self.subWedge[index] = value
    def export(self, outfile, level, name_='XSDataResultSubWedgeAssemble'):
        showIndent(outfile, level)
        outfile.write('<%s>\n' % name_)
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='XSDataResultSubWedgeAssemble'):
        XSDataResult.exportAttributes(self, outfile, level, name_='XSDataResultSubWedgeAssemble')
    def exportChildren(self, outfile, level, name_='XSDataResultSubWedgeAssemble'):
        for subWedge_ in self.getSubWedge():
            subWedge_.export(outfile, level, name_='subWedge')
        XSDataResult.exportChildren(self, outfile, level, name_)

    #Only to export the entire XML tree to a file stream on disk
    def outputFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write("<?xml version=\"1.0\" ?>\n")
        self.export( outfile, 0, name_='XSDataResultSubWedgeAssemble' )
        outfile.close()


    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataResultSubWedgeAssemble.factory()
        rootObj.build(rootNode)
        return rootObj
    parseString = staticmethod( parseString ) 


    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataResultSubWedgeAssemble.factory()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile ) 


    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO.StringIO()
        oStreamString.write('<?xml version="1.0" ?>\n')
        self.export( oStreamString, 0, name_="XSDataResultSubWedgeAssemble" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    def exportLiteral(self, outfile, level, name_='XSDataResultSubWedgeAssemble'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        pass
        XSDataResult.exportLiteralAttributes(self, outfile, level, name_)
    def exportLiteralChildren(self, outfile, level, name_):
        showIndent(outfile, level)
        outfile.write('subWedge=[\n')
        level += 1
        for subWedge in self.subWedge:
            showIndent(outfile, level)
            outfile.write('XSDataSubWedge(\n')
            subWedge.exportLiteral(outfile, level, name_='subWedge')
            showIndent(outfile, level)
            outfile.write('),\n')
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
        XSDataResult.exportLiteralChildren(self, outfile, level, name_)
    def build(self, node_):
        attrs = node_.attributes
        self.buildAttributes(attrs)
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildAttributes(self, attrs):
        XSDataResult.buildAttributes(self, attrs)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'subWedge':
            obj_ = XSDataSubWedge.factory()
            obj_.build(child_)
            self.subWedge.append(obj_)
# end class XSDataResultSubWedgeAssemble


class XSDataResultSubWedgeMerge(XSDataResult):
    subclass = None
    def __init__(self, subWedge=None):
        XSDataResult.__init__(self)
        if subWedge is None:
            self.subWedge = []
        else:
            self.subWedge = subWedge
    def factory(*args_, **kwargs_):
        if XSDataResultSubWedgeMerge.subclass:
            return XSDataResultSubWedgeMerge.subclass(*args_, **kwargs_)
        else:
            return XSDataResultSubWedgeMerge(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getSubWedge(self): return self.subWedge
    def setSubWedge(self, subWedge): self.subWedge = subWedge
    def addSubWedge(self, value): self.subWedge.append(value)
    def insertSubWedge(self, index, value): self.subWedge[index] = value
    def export(self, outfile, level, name_='XSDataResultSubWedgeMerge'):
        showIndent(outfile, level)
        outfile.write('<%s>\n' % name_)
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='XSDataResultSubWedgeMerge'):
        XSDataResult.exportAttributes(self, outfile, level, name_='XSDataResultSubWedgeMerge')
    def exportChildren(self, outfile, level, name_='XSDataResultSubWedgeMerge'):
        for subWedge_ in self.getSubWedge():
            subWedge_.export(outfile, level, name_='subWedge')
        XSDataResult.exportChildren(self, outfile, level, name_)

    #Only to export the entire XML tree to a file stream on disk
    def outputFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write("<?xml version=\"1.0\" ?>\n")
        self.export( outfile, 0, name_='XSDataResultSubWedgeMerge' )
        outfile.close()


    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataResultSubWedgeMerge.factory()
        rootObj.build(rootNode)
        return rootObj
    parseString = staticmethod( parseString ) 


    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataResultSubWedgeMerge.factory()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile ) 


    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO.StringIO()
        oStreamString.write('<?xml version="1.0" ?>\n')
        self.export( oStreamString, 0, name_="XSDataResultSubWedgeMerge" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    def exportLiteral(self, outfile, level, name_='XSDataResultSubWedgeMerge'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        pass
        XSDataResult.exportLiteralAttributes(self, outfile, level, name_)
    def exportLiteralChildren(self, outfile, level, name_):
        showIndent(outfile, level)
        outfile.write('subWedge=[\n')
        level += 1
        for subWedge in self.subWedge:
            showIndent(outfile, level)
            outfile.write('XSDataSubWedge(\n')
            subWedge.exportLiteral(outfile, level, name_='subWedge')
            showIndent(outfile, level)
            outfile.write('),\n')
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
        XSDataResult.exportLiteralChildren(self, outfile, level, name_)
    def build(self, node_):
        attrs = node_.attributes
        self.buildAttributes(attrs)
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildAttributes(self, attrs):
        XSDataResult.buildAttributes(self, attrs)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'subWedge':
            obj_ = XSDataSubWedge.factory()
            obj_.build(child_)
            self.subWedge.append(obj_)
# end class XSDataResultSubWedgeMerge


class XSDataSample(XSData):
    subclass = None
    def __init__(self, absorbedDoseRate=None, shape=None, size=None, susceptibility=None):
        XSData.__init__(self)
        self.absorbedDoseRate = absorbedDoseRate
        self.shape = shape
        self.size = size
        self.susceptibility = susceptibility
    def factory(*args_, **kwargs_):
        if XSDataSample.subclass:
            return XSDataSample.subclass(*args_, **kwargs_)
        else:
            return XSDataSample(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getAbsorbedDoseRate(self): return self.absorbedDoseRate
    def setAbsorbedDoseRate(self, absorbedDoseRate): self.absorbedDoseRate = absorbedDoseRate
    def getShape(self): return self.shape
    def setShape(self, shape): self.shape = shape
    def getSize(self): return self.size
    def setSize(self, size): self.size = size
    def getSusceptibility(self): return self.susceptibility
    def setSusceptibility(self, susceptibility): self.susceptibility = susceptibility
    def export(self, outfile, level, name_='XSDataSample'):
        showIndent(outfile, level)
        outfile.write('<%s>\n' % name_)
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='XSDataSample'):
        XSData.exportAttributes(self, outfile, level, name_='XSDataSample')
    def exportChildren(self, outfile, level, name_='XSDataSample'):
        if self.getAbsorbedDoseRate() != None :
            if self.absorbedDoseRate:
                self.absorbedDoseRate.export(outfile, level, name_='absorbedDoseRate')
        if self.getShape() != None :
            if self.shape:
                self.shape.export(outfile, level, name_='shape')
        if self.getSize() != None :
            if self.size:
                self.size.export(outfile, level, name_='size')
        if self.getSusceptibility() != None :
            if self.susceptibility:
                self.susceptibility.export(outfile, level, name_='susceptibility')
        XSData.exportChildren(self, outfile, level, name_)

    #Only to export the entire XML tree to a file stream on disk
    def outputFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write("<?xml version=\"1.0\" ?>\n")
        self.export( outfile, 0, name_='XSDataSample' )
        outfile.close()


    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataSample.factory()
        rootObj.build(rootNode)
        return rootObj
    parseString = staticmethod( parseString ) 


    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataSample.factory()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile ) 


    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO.StringIO()
        oStreamString.write('<?xml version="1.0" ?>\n')
        self.export( oStreamString, 0, name_="XSDataSample" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    def exportLiteral(self, outfile, level, name_='XSDataSample'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        pass
        XSData.exportLiteralAttributes(self, outfile, level, name_)
    def exportLiteralChildren(self, outfile, level, name_):
        if self.absorbedDoseRate:
            showIndent(outfile, level)
            outfile.write('absorbedDoseRate=XSDataAbsorbedDoseRate(\n')
            self.absorbedDoseRate.exportLiteral(outfile, level, name_='absorbedDoseRate')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.shape:
            showIndent(outfile, level)
            outfile.write('shape=XSDataFloat(\n')
            self.shape.exportLiteral(outfile, level, name_='shape')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.size:
            showIndent(outfile, level)
            outfile.write('size=XSDataSize(\n')
            self.size.exportLiteral(outfile, level, name_='size')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.susceptibility:
            showIndent(outfile, level)
            outfile.write('susceptibility=XSDataFloat(\n')
            self.susceptibility.exportLiteral(outfile, level, name_='susceptibility')
            showIndent(outfile, level)
            outfile.write('),\n')
        XSData.exportLiteralChildren(self, outfile, level, name_)
    def build(self, node_):
        attrs = node_.attributes
        self.buildAttributes(attrs)
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildAttributes(self, attrs):
        XSData.buildAttributes(self, attrs)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'absorbedDoseRate':
            obj_ = XSDataAbsorbedDoseRate.factory()
            obj_.build(child_)
            self.setAbsorbedDoseRate(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'shape':
            obj_ = XSDataFloat.factory()
            obj_.build(child_)
            self.setShape(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'size':
            obj_ = XSDataSize.factory()
            obj_.build(child_)
            self.setSize(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'susceptibility':
            obj_ = XSDataFloat.factory()
            obj_.build(child_)
            self.setSusceptibility(obj_)
# end class XSDataSample


class XSDataSampleCrystal(XSDataSample):
    subclass = None
    def __init__(self, absorbedDoseRate=None, shape=None, size=None, susceptibility=None, crystal=None):
        XSDataSample.__init__(self, absorbedDoseRate, shape, size, susceptibility)
        self.crystal = crystal
    def factory(*args_, **kwargs_):
        if XSDataSampleCrystal.subclass:
            return XSDataSampleCrystal.subclass(*args_, **kwargs_)
        else:
            return XSDataSampleCrystal(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getCrystal(self): return self.crystal
    def setCrystal(self, crystal): self.crystal = crystal
    def export(self, outfile, level, name_='XSDataSampleCrystal'):
        showIndent(outfile, level)
        outfile.write('<%s>\n' % name_)
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='XSDataSampleCrystal'):
        XSDataSample.exportAttributes(self, outfile, level, name_='XSDataSampleCrystal')
    def exportChildren(self, outfile, level, name_='XSDataSampleCrystal'):
        if self.crystal:
            self.crystal.export(outfile, level, name_='crystal')
        XSDataSample.exportChildren(self, outfile, level, name_)

    #Only to export the entire XML tree to a file stream on disk
    def outputFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write("<?xml version=\"1.0\" ?>\n")
        self.export( outfile, 0, name_='XSDataSampleCrystal' )
        outfile.close()


    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataSampleCrystal.factory()
        rootObj.build(rootNode)
        return rootObj
    parseString = staticmethod( parseString ) 


    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataSampleCrystal.factory()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile ) 


    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO.StringIO()
        oStreamString.write('<?xml version="1.0" ?>\n')
        self.export( oStreamString, 0, name_="XSDataSampleCrystal" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    def exportLiteral(self, outfile, level, name_='XSDataSampleCrystal'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        pass
        XSDataSample.exportLiteralAttributes(self, outfile, level, name_)
    def exportLiteralChildren(self, outfile, level, name_):
        if self.crystal:
            showIndent(outfile, level)
            outfile.write('crystal=XSDataCrystal(\n')
            self.crystal.exportLiteral(outfile, level, name_='crystal')
            showIndent(outfile, level)
            outfile.write('),\n')
        XSDataSample.exportLiteralChildren(self, outfile, level, name_)
    def build(self, node_):
        attrs = node_.attributes
        self.buildAttributes(attrs)
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildAttributes(self, attrs):
        XSDataSample.buildAttributes(self, attrs)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'crystal':
            obj_ = XSDataCrystal.factory()
            obj_.build(child_)
            self.setCrystal(obj_)
        XSDataSample.buildChildren(self, child_, nodeName_)
# end class XSDataSampleCrystal


class XSDataSampleCrystalMM(XSDataSampleCrystal):
    subclass = None
    def __init__(self, absorbedDoseRate=None, shape=None, size=None, susceptibility=None, crystal=None, chemicalComposition=None):
        XSDataSampleCrystal.__init__(self, absorbedDoseRate, shape, size, susceptibility, crystal)
        self.chemicalComposition = chemicalComposition
    def factory(*args_, **kwargs_):
        if XSDataSampleCrystalMM.subclass:
            return XSDataSampleCrystalMM.subclass(*args_, **kwargs_)
        else:
            return XSDataSampleCrystalMM(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getChemicalComposition(self): return self.chemicalComposition
    def setChemicalComposition(self, chemicalComposition): self.chemicalComposition = chemicalComposition
    def export(self, outfile, level, name_='XSDataSampleCrystalMM'):
        showIndent(outfile, level)
        outfile.write('<%s>\n' % name_)
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='XSDataSampleCrystalMM'):
        XSDataSampleCrystal.exportAttributes(self, outfile, level, name_='XSDataSampleCrystalMM')
    def exportChildren(self, outfile, level, name_='XSDataSampleCrystalMM'):
        if self.chemicalComposition:
            self.chemicalComposition.export(outfile, level, name_='chemicalComposition')
        XSDataSampleCrystal.exportChildren(self, outfile, level, name_)

    #Only to export the entire XML tree to a file stream on disk
    def outputFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write("<?xml version=\"1.0\" ?>\n")
        self.export( outfile, 0, name_='XSDataSampleCrystalMM' )
        outfile.close()


    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataSampleCrystalMM.factory()
        rootObj.build(rootNode)
        return rootObj
    parseString = staticmethod( parseString ) 


    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataSampleCrystalMM.factory()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile ) 


    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO.StringIO()
        oStreamString.write('<?xml version="1.0" ?>\n')
        self.export( oStreamString, 0, name_="XSDataSampleCrystalMM" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    def exportLiteral(self, outfile, level, name_='XSDataSampleCrystalMM'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        pass
        XSDataSampleCrystal.exportLiteralAttributes(self, outfile, level, name_)
    def exportLiteralChildren(self, outfile, level, name_):
        if self.chemicalComposition:
            showIndent(outfile, level)
            outfile.write('chemicalComposition=XSDataChemicalCompositionMM(\n')
            self.chemicalComposition.exportLiteral(outfile, level, name_='chemicalComposition')
            showIndent(outfile, level)
            outfile.write('),\n')
        XSDataSampleCrystal.exportLiteralChildren(self, outfile, level, name_)
    def build(self, node_):
        attrs = node_.attributes
        self.buildAttributes(attrs)
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildAttributes(self, attrs):
        XSDataSampleCrystal.buildAttributes(self, attrs)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'chemicalComposition':
            obj_ = XSDataChemicalCompositionMM.factory()
            obj_.build(child_)
            self.setChemicalComposition(obj_)
        XSDataSampleCrystal.buildChildren(self, child_, nodeName_)
# end class XSDataSampleCrystalMM


class XSDataSolvent(XSData):
    subclass = None
    def __init__(self, atoms=None):
        XSData.__init__(self)
        self.atoms = atoms
    def factory(*args_, **kwargs_):
        if XSDataSolvent.subclass:
            return XSDataSolvent.subclass(*args_, **kwargs_)
        else:
            return XSDataSolvent(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getAtoms(self): return self.atoms
    def setAtoms(self, atoms): self.atoms = atoms
    def export(self, outfile, level, name_='XSDataSolvent'):
        showIndent(outfile, level)
        outfile.write('<%s>\n' % name_)
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='XSDataSolvent'):
        XSData.exportAttributes(self, outfile, level, name_='XSDataSolvent')
    def exportChildren(self, outfile, level, name_='XSDataSolvent'):
        if self.atoms:
            self.atoms.export(outfile, level, name_='atoms')
        XSData.exportChildren(self, outfile, level, name_)

    #Only to export the entire XML tree to a file stream on disk
    def outputFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write("<?xml version=\"1.0\" ?>\n")
        self.export( outfile, 0, name_='XSDataSolvent' )
        outfile.close()


    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataSolvent.factory()
        rootObj.build(rootNode)
        return rootObj
    parseString = staticmethod( parseString ) 


    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataSolvent.factory()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile ) 


    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO.StringIO()
        oStreamString.write('<?xml version="1.0" ?>\n')
        self.export( oStreamString, 0, name_="XSDataSolvent" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    def exportLiteral(self, outfile, level, name_='XSDataSolvent'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        pass
        XSData.exportLiteralAttributes(self, outfile, level, name_)
    def exportLiteralChildren(self, outfile, level, name_):
        if self.atoms:
            showIndent(outfile, level)
            outfile.write('atoms=XSDataAtomicComposition(\n')
            self.atoms.exportLiteral(outfile, level, name_='atoms')
            showIndent(outfile, level)
            outfile.write('),\n')
        XSData.exportLiteralChildren(self, outfile, level, name_)
    def build(self, node_):
        attrs = node_.attributes
        self.buildAttributes(attrs)
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildAttributes(self, attrs):
        XSData.buildAttributes(self, attrs)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'atoms':
            obj_ = XSDataAtomicComposition.factory()
            obj_.build(child_)
            self.setAtoms(obj_)
# end class XSDataSolvent


class XSDataSpaceGroup(XSData):
    subclass = None
    def __init__(self, ITNumber=None, name=None):
        XSData.__init__(self)
        self.ITNumber = ITNumber
        self.name = name
    def factory(*args_, **kwargs_):
        if XSDataSpaceGroup.subclass:
            return XSDataSpaceGroup.subclass(*args_, **kwargs_)
        else:
            return XSDataSpaceGroup(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getITNumber(self): return self.ITNumber
    def setITNumber(self, ITNumber): self.ITNumber = ITNumber
    def getName(self): return self.name
    def setName(self, name): self.name = name
    def export(self, outfile, level, name_='XSDataSpaceGroup'):
        showIndent(outfile, level)
        outfile.write('<%s>\n' % name_)
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='XSDataSpaceGroup'):
        XSData.exportAttributes(self, outfile, level, name_='XSDataSpaceGroup')
    def exportChildren(self, outfile, level, name_='XSDataSpaceGroup'):
        if self.ITNumber:
            self.ITNumber.export(outfile, level, name_='ITNumber')
        if self.name:
            self.name.export(outfile, level, name_='name')
        XSData.exportChildren(self, outfile, level, name_)

    #Only to export the entire XML tree to a file stream on disk
    def outputFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write("<?xml version=\"1.0\" ?>\n")
        self.export( outfile, 0, name_='XSDataSpaceGroup' )
        outfile.close()


    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataSpaceGroup.factory()
        rootObj.build(rootNode)
        return rootObj
    parseString = staticmethod( parseString ) 


    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataSpaceGroup.factory()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile ) 


    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO.StringIO()
        oStreamString.write('<?xml version="1.0" ?>\n')
        self.export( oStreamString, 0, name_="XSDataSpaceGroup" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    def exportLiteral(self, outfile, level, name_='XSDataSpaceGroup'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        pass
        XSData.exportLiteralAttributes(self, outfile, level, name_)
    def exportLiteralChildren(self, outfile, level, name_):
        if self.ITNumber:
            showIndent(outfile, level)
            outfile.write('ITNumber=XSDataInteger(\n')
            self.ITNumber.exportLiteral(outfile, level, name_='ITNumber')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.name:
            showIndent(outfile, level)
            outfile.write('name=XSDataString(\n')
            self.name.exportLiteral(outfile, level, name_='name')
            showIndent(outfile, level)
            outfile.write('),\n')
        XSData.exportLiteralChildren(self, outfile, level, name_)
    def build(self, node_):
        attrs = node_.attributes
        self.buildAttributes(attrs)
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildAttributes(self, attrs):
        XSData.buildAttributes(self, attrs)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'ITNumber':
            obj_ = XSDataInteger.factory()
            obj_.build(child_)
            self.setITNumber(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'name':
            obj_ = XSDataString.factory()
            obj_.build(child_)
            self.setName(obj_)
# end class XSDataSpaceGroup


class XSDataStatisticsIndexing(XSData):
    subclass = None
    def __init__(self, beamPositionShiftX=None, beamPositionShiftY=None, spotDeviationAngular=None, spotDeviationPositional=None, spotsTotal=None, spotsUsed=None):
        XSData.__init__(self)
        self.beamPositionShiftX = beamPositionShiftX
        self.beamPositionShiftY = beamPositionShiftY
        self.spotDeviationAngular = spotDeviationAngular
        self.spotDeviationPositional = spotDeviationPositional
        self.spotsTotal = spotsTotal
        self.spotsUsed = spotsUsed
    def factory(*args_, **kwargs_):
        if XSDataStatisticsIndexing.subclass:
            return XSDataStatisticsIndexing.subclass(*args_, **kwargs_)
        else:
            return XSDataStatisticsIndexing(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getBeamPositionShiftX(self): return self.beamPositionShiftX
    def setBeamPositionShiftX(self, beamPositionShiftX): self.beamPositionShiftX = beamPositionShiftX
    def getBeamPositionShiftY(self): return self.beamPositionShiftY
    def setBeamPositionShiftY(self, beamPositionShiftY): self.beamPositionShiftY = beamPositionShiftY
    def getSpotDeviationAngular(self): return self.spotDeviationAngular
    def setSpotDeviationAngular(self, spotDeviationAngular): self.spotDeviationAngular = spotDeviationAngular
    def getSpotDeviationPositional(self): return self.spotDeviationPositional
    def setSpotDeviationPositional(self, spotDeviationPositional): self.spotDeviationPositional = spotDeviationPositional
    def getSpotsTotal(self): return self.spotsTotal
    def setSpotsTotal(self, spotsTotal): self.spotsTotal = spotsTotal
    def getSpotsUsed(self): return self.spotsUsed
    def setSpotsUsed(self, spotsUsed): self.spotsUsed = spotsUsed
    def export(self, outfile, level, name_='XSDataStatisticsIndexing'):
        showIndent(outfile, level)
        outfile.write('<%s>\n' % name_)
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='XSDataStatisticsIndexing'):
        XSData.exportAttributes(self, outfile, level, name_='XSDataStatisticsIndexing')
    def exportChildren(self, outfile, level, name_='XSDataStatisticsIndexing'):
        if self.beamPositionShiftX:
            self.beamPositionShiftX.export(outfile, level, name_='beamPositionShiftX')
        if self.beamPositionShiftY:
            self.beamPositionShiftY.export(outfile, level, name_='beamPositionShiftY')
        if self.spotDeviationAngular:
            self.spotDeviationAngular.export(outfile, level, name_='spotDeviationAngular')
        if self.spotDeviationPositional:
            self.spotDeviationPositional.export(outfile, level, name_='spotDeviationPositional')
        if self.spotsTotal:
            self.spotsTotal.export(outfile, level, name_='spotsTotal')
        if self.spotsUsed:
            self.spotsUsed.export(outfile, level, name_='spotsUsed')
        XSData.exportChildren(self, outfile, level, name_)

    #Only to export the entire XML tree to a file stream on disk
    def outputFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write("<?xml version=\"1.0\" ?>\n")
        self.export( outfile, 0, name_='XSDataStatisticsIndexing' )
        outfile.close()


    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataStatisticsIndexing.factory()
        rootObj.build(rootNode)
        return rootObj
    parseString = staticmethod( parseString ) 


    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataStatisticsIndexing.factory()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile ) 


    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO.StringIO()
        oStreamString.write('<?xml version="1.0" ?>\n')
        self.export( oStreamString, 0, name_="XSDataStatisticsIndexing" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    def exportLiteral(self, outfile, level, name_='XSDataStatisticsIndexing'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        pass
        XSData.exportLiteralAttributes(self, outfile, level, name_)
    def exportLiteralChildren(self, outfile, level, name_):
        if self.beamPositionShiftX:
            showIndent(outfile, level)
            outfile.write('beamPositionShiftX=XSDataLength(\n')
            self.beamPositionShiftX.exportLiteral(outfile, level, name_='beamPositionShiftX')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.beamPositionShiftY:
            showIndent(outfile, level)
            outfile.write('beamPositionShiftY=XSDataLength(\n')
            self.beamPositionShiftY.exportLiteral(outfile, level, name_='beamPositionShiftY')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.spotDeviationAngular:
            showIndent(outfile, level)
            outfile.write('spotDeviationAngular=XSDataAngle(\n')
            self.spotDeviationAngular.exportLiteral(outfile, level, name_='spotDeviationAngular')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.spotDeviationPositional:
            showIndent(outfile, level)
            outfile.write('spotDeviationPositional=XSDataLength(\n')
            self.spotDeviationPositional.exportLiteral(outfile, level, name_='spotDeviationPositional')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.spotsTotal:
            showIndent(outfile, level)
            outfile.write('spotsTotal=XSDataInteger(\n')
            self.spotsTotal.exportLiteral(outfile, level, name_='spotsTotal')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.spotsUsed:
            showIndent(outfile, level)
            outfile.write('spotsUsed=XSDataInteger(\n')
            self.spotsUsed.exportLiteral(outfile, level, name_='spotsUsed')
            showIndent(outfile, level)
            outfile.write('),\n')
        XSData.exportLiteralChildren(self, outfile, level, name_)
    def build(self, node_):
        attrs = node_.attributes
        self.buildAttributes(attrs)
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildAttributes(self, attrs):
        XSData.buildAttributes(self, attrs)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'beamPositionShiftX':
            obj_ = XSDataLength.factory()
            obj_.build(child_)
            self.setBeamPositionShiftX(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'beamPositionShiftY':
            obj_ = XSDataLength.factory()
            obj_.build(child_)
            self.setBeamPositionShiftY(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'spotDeviationAngular':
            obj_ = XSDataAngle.factory()
            obj_.build(child_)
            self.setSpotDeviationAngular(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'spotDeviationPositional':
            obj_ = XSDataLength.factory()
            obj_.build(child_)
            self.setSpotDeviationPositional(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'spotsTotal':
            obj_ = XSDataInteger.factory()
            obj_.build(child_)
            self.setSpotsTotal(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'spotsUsed':
            obj_ = XSDataInteger.factory()
            obj_.build(child_)
            self.setSpotsUsed(obj_)
# end class XSDataStatisticsIndexing


class XSDataStatisticsIntegration(XSData):
    subclass = None
    def __init__(self, iOverSigmaAtHighestResolution=None, iOverSigmaOverall=None, numberOfBadReflections=None, numberOfFullyRecordedReflections=None, numberOfNegativeReflections=None, numberOfOverlappedReflections=None, numberOfPartialReflections=None, numberOfReflectionsGenerated=None, RMSSpotDeviation=None):
        XSData.__init__(self)
        self.iOverSigmaAtHighestResolution = iOverSigmaAtHighestResolution
        self.iOverSigmaOverall = iOverSigmaOverall
        self.numberOfBadReflections = numberOfBadReflections
        self.numberOfFullyRecordedReflections = numberOfFullyRecordedReflections
        self.numberOfNegativeReflections = numberOfNegativeReflections
        self.numberOfOverlappedReflections = numberOfOverlappedReflections
        self.numberOfPartialReflections = numberOfPartialReflections
        self.numberOfReflectionsGenerated = numberOfReflectionsGenerated
        self.RMSSpotDeviation = RMSSpotDeviation
    def factory(*args_, **kwargs_):
        if XSDataStatisticsIntegration.subclass:
            return XSDataStatisticsIntegration.subclass(*args_, **kwargs_)
        else:
            return XSDataStatisticsIntegration(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getIOverSigmaAtHighestResolution(self): return self.iOverSigmaAtHighestResolution
    def setIOverSigmaAtHighestResolution(self, iOverSigmaAtHighestResolution): self.iOverSigmaAtHighestResolution = iOverSigmaAtHighestResolution
    def getIOverSigmaOverall(self): return self.iOverSigmaOverall
    def setIOverSigmaOverall(self, iOverSigmaOverall): self.iOverSigmaOverall = iOverSigmaOverall
    def getNumberOfBadReflections(self): return self.numberOfBadReflections
    def setNumberOfBadReflections(self, numberOfBadReflections): self.numberOfBadReflections = numberOfBadReflections
    def getNumberOfFullyRecordedReflections(self): return self.numberOfFullyRecordedReflections
    def setNumberOfFullyRecordedReflections(self, numberOfFullyRecordedReflections): self.numberOfFullyRecordedReflections = numberOfFullyRecordedReflections
    def getNumberOfNegativeReflections(self): return self.numberOfNegativeReflections
    def setNumberOfNegativeReflections(self, numberOfNegativeReflections): self.numberOfNegativeReflections = numberOfNegativeReflections
    def getNumberOfOverlappedReflections(self): return self.numberOfOverlappedReflections
    def setNumberOfOverlappedReflections(self, numberOfOverlappedReflections): self.numberOfOverlappedReflections = numberOfOverlappedReflections
    def getNumberOfPartialReflections(self): return self.numberOfPartialReflections
    def setNumberOfPartialReflections(self, numberOfPartialReflections): self.numberOfPartialReflections = numberOfPartialReflections
    def getNumberOfReflectionsGenerated(self): return self.numberOfReflectionsGenerated
    def setNumberOfReflectionsGenerated(self, numberOfReflectionsGenerated): self.numberOfReflectionsGenerated = numberOfReflectionsGenerated
    def getRMSSpotDeviation(self): return self.RMSSpotDeviation
    def setRMSSpotDeviation(self, RMSSpotDeviation): self.RMSSpotDeviation = RMSSpotDeviation
    def export(self, outfile, level, name_='XSDataStatisticsIntegration'):
        showIndent(outfile, level)
        outfile.write('<%s>\n' % name_)
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='XSDataStatisticsIntegration'):
        XSData.exportAttributes(self, outfile, level, name_='XSDataStatisticsIntegration')
    def exportChildren(self, outfile, level, name_='XSDataStatisticsIntegration'):
        if self.iOverSigmaAtHighestResolution:
            self.iOverSigmaAtHighestResolution.export(outfile, level, name_='iOverSigmaAtHighestResolution')
        if self.iOverSigmaOverall:
            self.iOverSigmaOverall.export(outfile, level, name_='iOverSigmaOverall')
        if self.numberOfBadReflections:
            self.numberOfBadReflections.export(outfile, level, name_='numberOfBadReflections')
        if self.numberOfFullyRecordedReflections:
            self.numberOfFullyRecordedReflections.export(outfile, level, name_='numberOfFullyRecordedReflections')
        if self.numberOfNegativeReflections:
            self.numberOfNegativeReflections.export(outfile, level, name_='numberOfNegativeReflections')
        if self.numberOfOverlappedReflections:
            self.numberOfOverlappedReflections.export(outfile, level, name_='numberOfOverlappedReflections')
        if self.numberOfPartialReflections:
            self.numberOfPartialReflections.export(outfile, level, name_='numberOfPartialReflections')
        if self.numberOfReflectionsGenerated:
            self.numberOfReflectionsGenerated.export(outfile, level, name_='numberOfReflectionsGenerated')
        if self.RMSSpotDeviation:
            self.RMSSpotDeviation.export(outfile, level, name_='RMSSpotDeviation')
        XSData.exportChildren(self, outfile, level, name_)

    #Only to export the entire XML tree to a file stream on disk
    def outputFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write("<?xml version=\"1.0\" ?>\n")
        self.export( outfile, 0, name_='XSDataStatisticsIntegration' )
        outfile.close()


    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataStatisticsIntegration.factory()
        rootObj.build(rootNode)
        return rootObj
    parseString = staticmethod( parseString ) 


    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataStatisticsIntegration.factory()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile ) 


    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO.StringIO()
        oStreamString.write('<?xml version="1.0" ?>\n')
        self.export( oStreamString, 0, name_="XSDataStatisticsIntegration" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    def exportLiteral(self, outfile, level, name_='XSDataStatisticsIntegration'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        pass
        XSData.exportLiteralAttributes(self, outfile, level, name_)
    def exportLiteralChildren(self, outfile, level, name_):
        if self.iOverSigmaAtHighestResolution:
            showIndent(outfile, level)
            outfile.write('iOverSigmaAtHighestResolution=XSDataDouble(\n')
            self.iOverSigmaAtHighestResolution.exportLiteral(outfile, level, name_='iOverSigmaAtHighestResolution')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.iOverSigmaOverall:
            showIndent(outfile, level)
            outfile.write('iOverSigmaOverall=XSDataDouble(\n')
            self.iOverSigmaOverall.exportLiteral(outfile, level, name_='iOverSigmaOverall')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.numberOfBadReflections:
            showIndent(outfile, level)
            outfile.write('numberOfBadReflections=XSDataInteger(\n')
            self.numberOfBadReflections.exportLiteral(outfile, level, name_='numberOfBadReflections')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.numberOfFullyRecordedReflections:
            showIndent(outfile, level)
            outfile.write('numberOfFullyRecordedReflections=XSDataInteger(\n')
            self.numberOfFullyRecordedReflections.exportLiteral(outfile, level, name_='numberOfFullyRecordedReflections')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.numberOfNegativeReflections:
            showIndent(outfile, level)
            outfile.write('numberOfNegativeReflections=XSDataInteger(\n')
            self.numberOfNegativeReflections.exportLiteral(outfile, level, name_='numberOfNegativeReflections')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.numberOfOverlappedReflections:
            showIndent(outfile, level)
            outfile.write('numberOfOverlappedReflections=XSDataInteger(\n')
            self.numberOfOverlappedReflections.exportLiteral(outfile, level, name_='numberOfOverlappedReflections')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.numberOfPartialReflections:
            showIndent(outfile, level)
            outfile.write('numberOfPartialReflections=XSDataInteger(\n')
            self.numberOfPartialReflections.exportLiteral(outfile, level, name_='numberOfPartialReflections')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.numberOfReflectionsGenerated:
            showIndent(outfile, level)
            outfile.write('numberOfReflectionsGenerated=XSDataInteger(\n')
            self.numberOfReflectionsGenerated.exportLiteral(outfile, level, name_='numberOfReflectionsGenerated')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.RMSSpotDeviation:
            showIndent(outfile, level)
            outfile.write('RMSSpotDeviation=XSDataLength(\n')
            self.RMSSpotDeviation.exportLiteral(outfile, level, name_='RMSSpotDeviation')
            showIndent(outfile, level)
            outfile.write('),\n')
        XSData.exportLiteralChildren(self, outfile, level, name_)
    def build(self, node_):
        attrs = node_.attributes
        self.buildAttributes(attrs)
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildAttributes(self, attrs):
        XSData.buildAttributes(self, attrs)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'iOverSigmaAtHighestResolution':
            obj_ = XSDataDouble.factory()
            obj_.build(child_)
            self.setIOverSigmaAtHighestResolution(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'iOverSigmaOverall':
            obj_ = XSDataDouble.factory()
            obj_.build(child_)
            self.setIOverSigmaOverall(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'numberOfBadReflections':
            obj_ = XSDataInteger.factory()
            obj_.build(child_)
            self.setNumberOfBadReflections(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'numberOfFullyRecordedReflections':
            obj_ = XSDataInteger.factory()
            obj_.build(child_)
            self.setNumberOfFullyRecordedReflections(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'numberOfNegativeReflections':
            obj_ = XSDataInteger.factory()
            obj_.build(child_)
            self.setNumberOfNegativeReflections(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'numberOfOverlappedReflections':
            obj_ = XSDataInteger.factory()
            obj_.build(child_)
            self.setNumberOfOverlappedReflections(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'numberOfPartialReflections':
            obj_ = XSDataInteger.factory()
            obj_.build(child_)
            self.setNumberOfPartialReflections(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'numberOfReflectionsGenerated':
            obj_ = XSDataInteger.factory()
            obj_.build(child_)
            self.setNumberOfReflectionsGenerated(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'RMSSpotDeviation':
            obj_ = XSDataLength.factory()
            obj_.build(child_)
            self.setRMSSpotDeviation(obj_)
# end class XSDataStatisticsIntegration


class XSDataStatisticsIntegrationAverageAndNumberOfReflections:
    subclass = None
    def __init__(self, averageIntensity=None, averageIOverSigma=None, averageSigma=None, numberOfReflections=None):
        self.averageIntensity = averageIntensity
        self.averageIOverSigma = averageIOverSigma
        self.averageSigma = averageSigma
        self.numberOfReflections = numberOfReflections
    def factory(*args_, **kwargs_):
        if XSDataStatisticsIntegrationAverageAndNumberOfReflections.subclass:
            return XSDataStatisticsIntegrationAverageAndNumberOfReflections.subclass(*args_, **kwargs_)
        else:
            return XSDataStatisticsIntegrationAverageAndNumberOfReflections(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getAverageIntensity(self): return self.averageIntensity
    def setAverageIntensity(self, averageIntensity): self.averageIntensity = averageIntensity
    def getAverageIOverSigma(self): return self.averageIOverSigma
    def setAverageIOverSigma(self, averageIOverSigma): self.averageIOverSigma = averageIOverSigma
    def getAverageSigma(self): return self.averageSigma
    def setAverageSigma(self, averageSigma): self.averageSigma = averageSigma
    def getNumberOfReflections(self): return self.numberOfReflections
    def setNumberOfReflections(self, numberOfReflections): self.numberOfReflections = numberOfReflections
    def export(self, outfile, level, name_='XSDataStatisticsIntegrationAverageAndNumberOfReflections'):
        showIndent(outfile, level)
        outfile.write('<%s>\n' % name_)
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='XSDataStatisticsIntegrationAverageAndNumberOfReflections'):
        pass
    def exportChildren(self, outfile, level, name_='XSDataStatisticsIntegrationAverageAndNumberOfReflections'):
        if self.averageIntensity:
            self.averageIntensity.export(outfile, level, name_='averageIntensity')
        if self.averageIOverSigma:
            self.averageIOverSigma.export(outfile, level, name_='averageIOverSigma')
        if self.averageSigma:
            self.averageSigma.export(outfile, level, name_='averageSigma')
        if self.numberOfReflections:
            self.numberOfReflections.export(outfile, level, name_='numberOfReflections')

    #Only to export the entire XML tree to a file stream on disk
    def outputFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write("<?xml version=\"1.0\" ?>\n")
        self.export( outfile, 0, name_='XSDataStatisticsIntegrationAverageAndNumberOfReflections' )
        outfile.close()


    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataStatisticsIntegrationAverageAndNumberOfReflections.factory()
        rootObj.build(rootNode)
        return rootObj
    parseString = staticmethod( parseString ) 


    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataStatisticsIntegrationAverageAndNumberOfReflections.factory()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile ) 


    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO.StringIO()
        oStreamString.write('<?xml version="1.0" ?>\n')
        self.export( oStreamString, 0, name_="XSDataStatisticsIntegrationAverageAndNumberOfReflections" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    def exportLiteral(self, outfile, level, name_='XSDataStatisticsIntegrationAverageAndNumberOfReflections'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        pass
    def exportLiteralChildren(self, outfile, level, name_):
        if self.averageIntensity:
            showIndent(outfile, level)
            outfile.write('averageIntensity=XSDataDouble(\n')
            self.averageIntensity.exportLiteral(outfile, level, name_='averageIntensity')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.averageIOverSigma:
            showIndent(outfile, level)
            outfile.write('averageIOverSigma=XSDataDouble(\n')
            self.averageIOverSigma.exportLiteral(outfile, level, name_='averageIOverSigma')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.averageSigma:
            showIndent(outfile, level)
            outfile.write('averageSigma=XSDataDouble(\n')
            self.averageSigma.exportLiteral(outfile, level, name_='averageSigma')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.numberOfReflections:
            showIndent(outfile, level)
            outfile.write('numberOfReflections=XSDataInteger(\n')
            self.numberOfReflections.exportLiteral(outfile, level, name_='numberOfReflections')
            showIndent(outfile, level)
            outfile.write('),\n')
    def build(self, node_):
        attrs = node_.attributes
        self.buildAttributes(attrs)
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildAttributes(self, attrs):
        pass
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'averageIntensity':
            obj_ = XSDataDouble.factory()
            obj_.build(child_)
            self.setAverageIntensity(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'averageIOverSigma':
            obj_ = XSDataDouble.factory()
            obj_.build(child_)
            self.setAverageIOverSigma(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'averageSigma':
            obj_ = XSDataDouble.factory()
            obj_.build(child_)
            self.setAverageSigma(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'numberOfReflections':
            obj_ = XSDataInteger.factory()
            obj_.build(child_)
            self.setNumberOfReflections(obj_)
# end class XSDataStatisticsIntegrationAverageAndNumberOfReflections


class XSDataStatisticsIntegrationPerReflectionType(XSData):
    subclass = None
    def __init__(self, fullyRecorded=None, partials=None):
        XSData.__init__(self)
        self.fullyRecorded = fullyRecorded
        self.partials = partials
    def factory(*args_, **kwargs_):
        if XSDataStatisticsIntegrationPerReflectionType.subclass:
            return XSDataStatisticsIntegrationPerReflectionType.subclass(*args_, **kwargs_)
        else:
            return XSDataStatisticsIntegrationPerReflectionType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getFullyRecorded(self): return self.fullyRecorded
    def setFullyRecorded(self, fullyRecorded): self.fullyRecorded = fullyRecorded
    def getPartials(self): return self.partials
    def setPartials(self, partials): self.partials = partials
    def export(self, outfile, level, name_='XSDataStatisticsIntegrationPerReflectionType'):
        showIndent(outfile, level)
        outfile.write('<%s>\n' % name_)
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='XSDataStatisticsIntegrationPerReflectionType'):
        XSData.exportAttributes(self, outfile, level, name_='XSDataStatisticsIntegrationPerReflectionType')
    def exportChildren(self, outfile, level, name_='XSDataStatisticsIntegrationPerReflectionType'):
        if self.fullyRecorded:
            self.fullyRecorded.export(outfile, level, name_='fullyRecorded')
        if self.partials:
            self.partials.export(outfile, level, name_='partials')
        XSData.exportChildren(self, outfile, level, name_)

    #Only to export the entire XML tree to a file stream on disk
    def outputFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write("<?xml version=\"1.0\" ?>\n")
        self.export( outfile, 0, name_='XSDataStatisticsIntegrationPerReflectionType' )
        outfile.close()


    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataStatisticsIntegrationPerReflectionType.factory()
        rootObj.build(rootNode)
        return rootObj
    parseString = staticmethod( parseString ) 


    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataStatisticsIntegrationPerReflectionType.factory()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile ) 


    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO.StringIO()
        oStreamString.write('<?xml version="1.0" ?>\n')
        self.export( oStreamString, 0, name_="XSDataStatisticsIntegrationPerReflectionType" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    def exportLiteral(self, outfile, level, name_='XSDataStatisticsIntegrationPerReflectionType'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        pass
        XSData.exportLiteralAttributes(self, outfile, level, name_)
    def exportLiteralChildren(self, outfile, level, name_):
        if self.fullyRecorded:
            showIndent(outfile, level)
            outfile.write('fullyRecorded=XSDataStatisticsIntegrationAverageAndNumberOfReflections(\n')
            self.fullyRecorded.exportLiteral(outfile, level, name_='fullyRecorded')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.partials:
            showIndent(outfile, level)
            outfile.write('partials=XSDataStatisticsIntegrationAverageAndNumberOfReflections(\n')
            self.partials.exportLiteral(outfile, level, name_='partials')
            showIndent(outfile, level)
            outfile.write('),\n')
        XSData.exportLiteralChildren(self, outfile, level, name_)
    def build(self, node_):
        attrs = node_.attributes
        self.buildAttributes(attrs)
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildAttributes(self, attrs):
        XSData.buildAttributes(self, attrs)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'fullyRecorded':
            obj_ = XSDataStatisticsIntegrationAverageAndNumberOfReflections.factory()
            obj_.build(child_)
            self.setFullyRecorded(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'partials':
            obj_ = XSDataStatisticsIntegrationAverageAndNumberOfReflections.factory()
            obj_.build(child_)
            self.setPartials(obj_)
# end class XSDataStatisticsIntegrationPerReflectionType


class XSDataStatisticsIntegrationPerResolutionBin(XSData):
    subclass = None
    def __init__(self, maxResolution=None, minResolution=None, profileFitted=None, summation=None):
        XSData.__init__(self)
        self.maxResolution = maxResolution
        self.minResolution = minResolution
        self.profileFitted = profileFitted
        self.summation = summation
    def factory(*args_, **kwargs_):
        if XSDataStatisticsIntegrationPerResolutionBin.subclass:
            return XSDataStatisticsIntegrationPerResolutionBin.subclass(*args_, **kwargs_)
        else:
            return XSDataStatisticsIntegrationPerResolutionBin(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getMaxResolution(self): return self.maxResolution
    def setMaxResolution(self, maxResolution): self.maxResolution = maxResolution
    def getMinResolution(self): return self.minResolution
    def setMinResolution(self, minResolution): self.minResolution = minResolution
    def getProfileFitted(self): return self.profileFitted
    def setProfileFitted(self, profileFitted): self.profileFitted = profileFitted
    def getSummation(self): return self.summation
    def setSummation(self, summation): self.summation = summation
    def export(self, outfile, level, name_='XSDataStatisticsIntegrationPerResolutionBin'):
        showIndent(outfile, level)
        outfile.write('<%s>\n' % name_)
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='XSDataStatisticsIntegrationPerResolutionBin'):
        XSData.exportAttributes(self, outfile, level, name_='XSDataStatisticsIntegrationPerResolutionBin')
    def exportChildren(self, outfile, level, name_='XSDataStatisticsIntegrationPerResolutionBin'):
        if self.maxResolution:
            self.maxResolution.export(outfile, level, name_='maxResolution')
        if self.minResolution:
            self.minResolution.export(outfile, level, name_='minResolution')
        if self.profileFitted:
            self.profileFitted.export(outfile, level, name_='profileFitted')
        if self.summation:
            self.summation.export(outfile, level, name_='summation')
        XSData.exportChildren(self, outfile, level, name_)

    #Only to export the entire XML tree to a file stream on disk
    def outputFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write("<?xml version=\"1.0\" ?>\n")
        self.export( outfile, 0, name_='XSDataStatisticsIntegrationPerResolutionBin' )
        outfile.close()


    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataStatisticsIntegrationPerResolutionBin.factory()
        rootObj.build(rootNode)
        return rootObj
    parseString = staticmethod( parseString ) 


    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataStatisticsIntegrationPerResolutionBin.factory()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile ) 


    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO.StringIO()
        oStreamString.write('<?xml version="1.0" ?>\n')
        self.export( oStreamString, 0, name_="XSDataStatisticsIntegrationPerResolutionBin" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    def exportLiteral(self, outfile, level, name_='XSDataStatisticsIntegrationPerResolutionBin'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        pass
        XSData.exportLiteralAttributes(self, outfile, level, name_)
    def exportLiteralChildren(self, outfile, level, name_):
        if self.maxResolution:
            showIndent(outfile, level)
            outfile.write('maxResolution=XSDataDouble(\n')
            self.maxResolution.exportLiteral(outfile, level, name_='maxResolution')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.minResolution:
            showIndent(outfile, level)
            outfile.write('minResolution=XSDataDouble(\n')
            self.minResolution.exportLiteral(outfile, level, name_='minResolution')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.profileFitted:
            showIndent(outfile, level)
            outfile.write('profileFitted=XSDataStatisticsIntegrationPerReflectionType(\n')
            self.profileFitted.exportLiteral(outfile, level, name_='profileFitted')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.summation:
            showIndent(outfile, level)
            outfile.write('summation=XSDataStatisticsIntegrationPerReflectionType(\n')
            self.summation.exportLiteral(outfile, level, name_='summation')
            showIndent(outfile, level)
            outfile.write('),\n')
        XSData.exportLiteralChildren(self, outfile, level, name_)
    def build(self, node_):
        attrs = node_.attributes
        self.buildAttributes(attrs)
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildAttributes(self, attrs):
        XSData.buildAttributes(self, attrs)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'maxResolution':
            obj_ = XSDataDouble.factory()
            obj_.build(child_)
            self.setMaxResolution(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'minResolution':
            obj_ = XSDataDouble.factory()
            obj_.build(child_)
            self.setMinResolution(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'profileFitted':
            obj_ = XSDataStatisticsIntegrationPerReflectionType.factory()
            obj_.build(child_)
            self.setProfileFitted(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'summation':
            obj_ = XSDataStatisticsIntegrationPerReflectionType.factory()
            obj_.build(child_)
            self.setSummation(obj_)
# end class XSDataStatisticsIntegrationPerResolutionBin


class XSDataStatisticsStrategy(XSData):
    subclass = None
    def __init__(self, resolutionBin=None):
        XSData.__init__(self)
        if resolutionBin is None:
            self.resolutionBin = []
        else:
            self.resolutionBin = resolutionBin
    def factory(*args_, **kwargs_):
        if XSDataStatisticsStrategy.subclass:
            return XSDataStatisticsStrategy.subclass(*args_, **kwargs_)
        else:
            return XSDataStatisticsStrategy(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getResolutionBin(self): return self.resolutionBin
    def setResolutionBin(self, resolutionBin): self.resolutionBin = resolutionBin
    def addResolutionBin(self, value): self.resolutionBin.append(value)
    def insertResolutionBin(self, index, value): self.resolutionBin[index] = value
    def export(self, outfile, level, name_='XSDataStatisticsStrategy'):
        showIndent(outfile, level)
        outfile.write('<%s>\n' % name_)
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='XSDataStatisticsStrategy'):
        XSData.exportAttributes(self, outfile, level, name_='XSDataStatisticsStrategy')
    def exportChildren(self, outfile, level, name_='XSDataStatisticsStrategy'):
        for resolutionBin_ in self.getResolutionBin():
            resolutionBin_.export(outfile, level, name_='resolutionBin')
        XSData.exportChildren(self, outfile, level, name_)

    #Only to export the entire XML tree to a file stream on disk
    def outputFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write("<?xml version=\"1.0\" ?>\n")
        self.export( outfile, 0, name_='XSDataStatisticsStrategy' )
        outfile.close()


    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataStatisticsStrategy.factory()
        rootObj.build(rootNode)
        return rootObj
    parseString = staticmethod( parseString ) 


    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataStatisticsStrategy.factory()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile ) 


    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO.StringIO()
        oStreamString.write('<?xml version="1.0" ?>\n')
        self.export( oStreamString, 0, name_="XSDataStatisticsStrategy" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    def exportLiteral(self, outfile, level, name_='XSDataStatisticsStrategy'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        pass
        XSData.exportLiteralAttributes(self, outfile, level, name_)
    def exportLiteralChildren(self, outfile, level, name_):
        showIndent(outfile, level)
        outfile.write('resolutionBin=[\n')
        level += 1
        for resolutionBin in self.resolutionBin:
            showIndent(outfile, level)
            outfile.write('XSDataResolutionBin(\n')
            resolutionBin.exportLiteral(outfile, level, name_='resolutionBin')
            showIndent(outfile, level)
            outfile.write('),\n')
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
        XSData.exportLiteralChildren(self, outfile, level, name_)
    def build(self, node_):
        attrs = node_.attributes
        self.buildAttributes(attrs)
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildAttributes(self, attrs):
        XSData.buildAttributes(self, attrs)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'resolutionBin':
            obj_ = XSDataResolutionBin.factory()
            obj_.build(child_)
            self.resolutionBin.append(obj_)
# end class XSDataStatisticsStrategy


class XSDataStrategyInput(XSDataInput):
    subclass = None
    def __init__(self, configuration=None, bestFileContentDat=None, bestFileContentHKL=None, bestFileContentPar=None, crystalRefined=None, diffractionPlan=None, experimentalCondition=None, sample=None):
        XSDataInput.__init__(self, configuration)
        self.bestFileContentDat = bestFileContentDat
        if bestFileContentHKL is None:
            self.bestFileContentHKL = []
        else:
            self.bestFileContentHKL = bestFileContentHKL
        self.bestFileContentPar = bestFileContentPar
        self.crystalRefined = crystalRefined
        self.diffractionPlan = diffractionPlan
        self.experimentalCondition = experimentalCondition
        self.sample = sample
    def factory(*args_, **kwargs_):
        if XSDataStrategyInput.subclass:
            return XSDataStrategyInput.subclass(*args_, **kwargs_)
        else:
            return XSDataStrategyInput(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getBestFileContentDat(self): return self.bestFileContentDat
    def setBestFileContentDat(self, bestFileContentDat): self.bestFileContentDat = bestFileContentDat
    def getBestFileContentHKL(self): return self.bestFileContentHKL
    def setBestFileContentHKL(self, bestFileContentHKL): self.bestFileContentHKL = bestFileContentHKL
    def addBestFileContentHKL(self, value): self.bestFileContentHKL.append(value)
    def insertBestFileContentHKL(self, index, value): self.bestFileContentHKL[index] = value
    def getBestFileContentPar(self): return self.bestFileContentPar
    def setBestFileContentPar(self, bestFileContentPar): self.bestFileContentPar = bestFileContentPar
    def getCrystalRefined(self): return self.crystalRefined
    def setCrystalRefined(self, crystalRefined): self.crystalRefined = crystalRefined
    def getDiffractionPlan(self): return self.diffractionPlan
    def setDiffractionPlan(self, diffractionPlan): self.diffractionPlan = diffractionPlan
    def getExperimentalCondition(self): return self.experimentalCondition
    def setExperimentalCondition(self, experimentalCondition): self.experimentalCondition = experimentalCondition
    def getSample(self): return self.sample
    def setSample(self, sample): self.sample = sample
    def export(self, outfile, level, name_='XSDataStrategyInput'):
        showIndent(outfile, level)
        outfile.write('<%s>\n' % name_)
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='XSDataStrategyInput'):
        XSDataInput.exportAttributes(self, outfile, level, name_='XSDataStrategyInput')
    def exportChildren(self, outfile, level, name_='XSDataStrategyInput'):
        if self.bestFileContentDat:
            self.bestFileContentDat.export(outfile, level, name_='bestFileContentDat')
        for bestFileContentHKL_ in self.getBestFileContentHKL():
            bestFileContentHKL_.export(outfile, level, name_='bestFileContentHKL')
        if self.bestFileContentPar:
            self.bestFileContentPar.export(outfile, level, name_='bestFileContentPar')
        if self.crystalRefined:
            self.crystalRefined.export(outfile, level, name_='crystalRefined')
        if self.diffractionPlan:
            self.diffractionPlan.export(outfile, level, name_='diffractionPlan')
        if self.experimentalCondition:
            self.experimentalCondition.export(outfile, level, name_='experimentalCondition')
        if self.sample:
            self.sample.export(outfile, level, name_='sample')
        XSDataInput.exportChildren(self, outfile, level, name_)

    #Only to export the entire XML tree to a file stream on disk
    def outputFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write("<?xml version=\"1.0\" ?>\n")
        self.export( outfile, 0, name_='XSDataStrategyInput' )
        outfile.close()


    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataStrategyInput.factory()
        rootObj.build(rootNode)
        return rootObj
    parseString = staticmethod( parseString ) 


    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataStrategyInput.factory()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile ) 


    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO.StringIO()
        oStreamString.write('<?xml version="1.0" ?>\n')
        self.export( oStreamString, 0, name_="XSDataStrategyInput" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    def exportLiteral(self, outfile, level, name_='XSDataStrategyInput'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        pass
        XSDataInput.exportLiteralAttributes(self, outfile, level, name_)
    def exportLiteralChildren(self, outfile, level, name_):
        if self.bestFileContentDat:
            showIndent(outfile, level)
            outfile.write('bestFileContentDat=XSDataString(\n')
            self.bestFileContentDat.exportLiteral(outfile, level, name_='bestFileContentDat')
            showIndent(outfile, level)
            outfile.write('),\n')
        showIndent(outfile, level)
        outfile.write('bestFileContentHKL=[\n')
        level += 1
        for bestFileContentHKL in self.bestFileContentHKL:
            showIndent(outfile, level)
            outfile.write('XSDataString(\n')
            bestFileContentHKL.exportLiteral(outfile, level, name_='bestFileContentHKL')
            showIndent(outfile, level)
            outfile.write('),\n')
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
        if self.bestFileContentPar:
            showIndent(outfile, level)
            outfile.write('bestFileContentPar=XSDataString(\n')
            self.bestFileContentPar.exportLiteral(outfile, level, name_='bestFileContentPar')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.crystalRefined:
            showIndent(outfile, level)
            outfile.write('crystalRefined=XSDataCrystal(\n')
            self.crystalRefined.exportLiteral(outfile, level, name_='crystalRefined')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.diffractionPlan:
            showIndent(outfile, level)
            outfile.write('diffractionPlan=XSDataDiffractionPlan(\n')
            self.diffractionPlan.exportLiteral(outfile, level, name_='diffractionPlan')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.experimentalCondition:
            showIndent(outfile, level)
            outfile.write('experimentalCondition=XSDataExperimentalCondition(\n')
            self.experimentalCondition.exportLiteral(outfile, level, name_='experimentalCondition')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.sample:
            showIndent(outfile, level)
            outfile.write('sample=XSDataSampleCrystalMM(\n')
            self.sample.exportLiteral(outfile, level, name_='sample')
            showIndent(outfile, level)
            outfile.write('),\n')
        XSDataInput.exportLiteralChildren(self, outfile, level, name_)
    def build(self, node_):
        attrs = node_.attributes
        self.buildAttributes(attrs)
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildAttributes(self, attrs):
        XSDataInput.buildAttributes(self, attrs)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'bestFileContentDat':
            obj_ = XSDataString.factory()
            obj_.build(child_)
            self.setBestFileContentDat(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'bestFileContentHKL':
            obj_ = XSDataString.factory()
            obj_.build(child_)
            self.bestFileContentHKL.append(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'bestFileContentPar':
            obj_ = XSDataString.factory()
            obj_.build(child_)
            self.setBestFileContentPar(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'crystalRefined':
            obj_ = XSDataCrystal.factory()
            obj_.build(child_)
            self.setCrystalRefined(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'diffractionPlan':
            obj_ = XSDataDiffractionPlan.factory()
            obj_.build(child_)
            self.setDiffractionPlan(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'experimentalCondition':
            obj_ = XSDataExperimentalCondition.factory()
            obj_.build(child_)
            self.setExperimentalCondition(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'sample':
            obj_ = XSDataSampleCrystalMM.factory()
            obj_.build(child_)
            self.setSample(obj_)
        XSDataInput.buildChildren(self, child_, nodeName_)
# end class XSDataStrategyInput


class XSDataStrategyResult(XSDataResult):
    subclass = None
    def __init__(self, collectionPlan=None):
        XSDataResult.__init__(self)
        if collectionPlan is None:
            self.collectionPlan = []
        else:
            self.collectionPlan = collectionPlan
    def factory(*args_, **kwargs_):
        if XSDataStrategyResult.subclass:
            return XSDataStrategyResult.subclass(*args_, **kwargs_)
        else:
            return XSDataStrategyResult(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getCollectionPlan(self): return self.collectionPlan
    def setCollectionPlan(self, collectionPlan): self.collectionPlan = collectionPlan
    def addCollectionPlan(self, value): self.collectionPlan.append(value)
    def insertCollectionPlan(self, index, value): self.collectionPlan[index] = value
    def export(self, outfile, level, name_='XSDataStrategyResult'):
        showIndent(outfile, level)
        outfile.write('<%s>\n' % name_)
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='XSDataStrategyResult'):
        XSDataResult.exportAttributes(self, outfile, level, name_='XSDataStrategyResult')
    def exportChildren(self, outfile, level, name_='XSDataStrategyResult'):
        for collectionPlan_ in self.getCollectionPlan():
            collectionPlan_.export(outfile, level, name_='collectionPlan')
        XSDataResult.exportChildren(self, outfile, level, name_)

    #Only to export the entire XML tree to a file stream on disk
    def outputFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write("<?xml version=\"1.0\" ?>\n")
        self.export( outfile, 0, name_='XSDataStrategyResult' )
        outfile.close()


    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataStrategyResult.factory()
        rootObj.build(rootNode)
        return rootObj
    parseString = staticmethod( parseString ) 


    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataStrategyResult.factory()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile ) 


    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO.StringIO()
        oStreamString.write('<?xml version="1.0" ?>\n')
        self.export( oStreamString, 0, name_="XSDataStrategyResult" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    def exportLiteral(self, outfile, level, name_='XSDataStrategyResult'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        pass
        XSDataResult.exportLiteralAttributes(self, outfile, level, name_)
    def exportLiteralChildren(self, outfile, level, name_):
        showIndent(outfile, level)
        outfile.write('collectionPlan=[\n')
        level += 1
        for collectionPlan in self.collectionPlan:
            showIndent(outfile, level)
            outfile.write('XSDataCollectionPlan(\n')
            collectionPlan.exportLiteral(outfile, level, name_='collectionPlan')
            showIndent(outfile, level)
            outfile.write('),\n')
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
        XSDataResult.exportLiteralChildren(self, outfile, level, name_)
    def build(self, node_):
        attrs = node_.attributes
        self.buildAttributes(attrs)
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildAttributes(self, attrs):
        XSDataResult.buildAttributes(self, attrs)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'collectionPlan':
            obj_ = XSDataCollectionPlan.factory()
            obj_.build(child_)
            self.collectionPlan.append(obj_)
# end class XSDataStrategyResult


class XSDataStrategySummary(XSData):
    subclass = None
    def __init__(self, attenuation=None, completeness=None, iSigma=None, rankingResolution=None, redundancy=None, resolution=None, resolutionReasoning=None, totalDataCollectionTime=None, totalExposureTime=None):
        XSData.__init__(self)
        self.attenuation = attenuation
        self.completeness = completeness
        self.iSigma = iSigma
        self.rankingResolution = rankingResolution
        self.redundancy = redundancy
        self.resolution = resolution
        self.resolutionReasoning = resolutionReasoning
        self.totalDataCollectionTime = totalDataCollectionTime
        self.totalExposureTime = totalExposureTime
    def factory(*args_, **kwargs_):
        if XSDataStrategySummary.subclass:
            return XSDataStrategySummary.subclass(*args_, **kwargs_)
        else:
            return XSDataStrategySummary(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getAttenuation(self): return self.attenuation
    def setAttenuation(self, attenuation): self.attenuation = attenuation
    def getCompleteness(self): return self.completeness
    def setCompleteness(self, completeness): self.completeness = completeness
    def getISigma(self): return self.iSigma
    def setISigma(self, iSigma): self.iSigma = iSigma
    def getRankingResolution(self): return self.rankingResolution
    def setRankingResolution(self, rankingResolution): self.rankingResolution = rankingResolution
    def getRedundancy(self): return self.redundancy
    def setRedundancy(self, redundancy): self.redundancy = redundancy
    def getResolution(self): return self.resolution
    def setResolution(self, resolution): self.resolution = resolution
    def getResolutionReasoning(self): return self.resolutionReasoning
    def setResolutionReasoning(self, resolutionReasoning): self.resolutionReasoning = resolutionReasoning
    def getTotalDataCollectionTime(self): return self.totalDataCollectionTime
    def setTotalDataCollectionTime(self, totalDataCollectionTime): self.totalDataCollectionTime = totalDataCollectionTime
    def getTotalExposureTime(self): return self.totalExposureTime
    def setTotalExposureTime(self, totalExposureTime): self.totalExposureTime = totalExposureTime
    def export(self, outfile, level, name_='XSDataStrategySummary'):
        showIndent(outfile, level)
        outfile.write('<%s>\n' % name_)
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='XSDataStrategySummary'):
        XSData.exportAttributes(self, outfile, level, name_='XSDataStrategySummary')
    def exportChildren(self, outfile, level, name_='XSDataStrategySummary'):
        if self.attenuation:
            self.attenuation.export(outfile, level, name_='attenuation')
        if self.completeness:
            self.completeness.export(outfile, level, name_='completeness')
        if self.iSigma:
            self.iSigma.export(outfile, level, name_='iSigma')
        if self.rankingResolution:
            self.rankingResolution.export(outfile, level, name_='rankingResolution')
        if self.redundancy:
            self.redundancy.export(outfile, level, name_='redundancy')
        if self.resolution:
            self.resolution.export(outfile, level, name_='resolution')
        if self.resolutionReasoning:
            self.resolutionReasoning.export(outfile, level, name_='resolutionReasoning')
        if self.totalDataCollectionTime:
            self.totalDataCollectionTime.export(outfile, level, name_='totalDataCollectionTime')
        if self.totalExposureTime:
            self.totalExposureTime.export(outfile, level, name_='totalExposureTime')
        XSData.exportChildren(self, outfile, level, name_)

    #Only to export the entire XML tree to a file stream on disk
    def outputFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write("<?xml version=\"1.0\" ?>\n")
        self.export( outfile, 0, name_='XSDataStrategySummary' )
        outfile.close()


    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataStrategySummary.factory()
        rootObj.build(rootNode)
        return rootObj
    parseString = staticmethod( parseString ) 


    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataStrategySummary.factory()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile ) 


    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO.StringIO()
        oStreamString.write('<?xml version="1.0" ?>\n')
        self.export( oStreamString, 0, name_="XSDataStrategySummary" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    def exportLiteral(self, outfile, level, name_='XSDataStrategySummary'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        pass
        XSData.exportLiteralAttributes(self, outfile, level, name_)
    def exportLiteralChildren(self, outfile, level, name_):
        if self.attenuation:
            showIndent(outfile, level)
            outfile.write('attenuation=XSDataFloat(\n')
            self.attenuation.exportLiteral(outfile, level, name_='attenuation')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.completeness:
            showIndent(outfile, level)
            outfile.write('completeness=XSDataFloat(\n')
            self.completeness.exportLiteral(outfile, level, name_='completeness')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.iSigma:
            showIndent(outfile, level)
            outfile.write('iSigma=XSDataFloat(\n')
            self.iSigma.exportLiteral(outfile, level, name_='iSigma')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.rankingResolution:
            showIndent(outfile, level)
            outfile.write('rankingResolution=XSDataFloat(\n')
            self.rankingResolution.exportLiteral(outfile, level, name_='rankingResolution')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.redundancy:
            showIndent(outfile, level)
            outfile.write('redundancy=XSDataFloat(\n')
            self.redundancy.exportLiteral(outfile, level, name_='redundancy')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.resolution:
            showIndent(outfile, level)
            outfile.write('resolution=XSDataFloat(\n')
            self.resolution.exportLiteral(outfile, level, name_='resolution')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.resolutionReasoning:
            showIndent(outfile, level)
            outfile.write('resolutionReasoning=XSDataString(\n')
            self.resolutionReasoning.exportLiteral(outfile, level, name_='resolutionReasoning')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.totalDataCollectionTime:
            showIndent(outfile, level)
            outfile.write('totalDataCollectionTime=XSDataTime(\n')
            self.totalDataCollectionTime.exportLiteral(outfile, level, name_='totalDataCollectionTime')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.totalExposureTime:
            showIndent(outfile, level)
            outfile.write('totalExposureTime=XSDataTime(\n')
            self.totalExposureTime.exportLiteral(outfile, level, name_='totalExposureTime')
            showIndent(outfile, level)
            outfile.write('),\n')
        XSData.exportLiteralChildren(self, outfile, level, name_)
    def build(self, node_):
        attrs = node_.attributes
        self.buildAttributes(attrs)
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildAttributes(self, attrs):
        XSData.buildAttributes(self, attrs)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'attenuation':
            obj_ = XSDataFloat.factory()
            obj_.build(child_)
            self.setAttenuation(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'completeness':
            obj_ = XSDataFloat.factory()
            obj_.build(child_)
            self.setCompleteness(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'iSigma':
            obj_ = XSDataFloat.factory()
            obj_.build(child_)
            self.setISigma(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'rankingResolution':
            obj_ = XSDataFloat.factory()
            obj_.build(child_)
            self.setRankingResolution(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'redundancy':
            obj_ = XSDataFloat.factory()
            obj_.build(child_)
            self.setRedundancy(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'resolution':
            obj_ = XSDataFloat.factory()
            obj_.build(child_)
            self.setResolution(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'resolutionReasoning':
            obj_ = XSDataString.factory()
            obj_.build(child_)
            self.setResolutionReasoning(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'totalDataCollectionTime':
            obj_ = XSDataTime.factory()
            obj_.build(child_)
            self.setTotalDataCollectionTime(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'totalExposureTime':
            obj_ = XSDataTime.factory()
            obj_.build(child_)
            self.setTotalExposureTime(obj_)
# end class XSDataStrategySummary


class XSDataStructure(XSData):
    subclass = None
    def __init__(self, numberOfCopiesInAsymmetricUnit=None, chain=None, ligand=None):
        XSData.__init__(self)
        self.numberOfCopiesInAsymmetricUnit = numberOfCopiesInAsymmetricUnit
        if chain is None:
            self.chain = []
        else:
            self.chain = chain
        if ligand is None:
            self.ligand = []
        else:
            self.ligand = ligand
    def factory(*args_, **kwargs_):
        if XSDataStructure.subclass:
            return XSDataStructure.subclass(*args_, **kwargs_)
        else:
            return XSDataStructure(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getNumberOfCopiesInAsymmetricUnit(self): return self.numberOfCopiesInAsymmetricUnit
    def setNumberOfCopiesInAsymmetricUnit(self, numberOfCopiesInAsymmetricUnit): self.numberOfCopiesInAsymmetricUnit = numberOfCopiesInAsymmetricUnit
    def getChain(self): return self.chain
    def setChain(self, chain): self.chain = chain
    def addChain(self, value): self.chain.append(value)
    def insertChain(self, index, value): self.chain[index] = value
    def getLigand(self): return self.ligand
    def setLigand(self, ligand): self.ligand = ligand
    def addLigand(self, value): self.ligand.append(value)
    def insertLigand(self, index, value): self.ligand[index] = value
    def export(self, outfile, level, name_='XSDataStructure'):
        showIndent(outfile, level)
        outfile.write('<%s>\n' % name_)
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='XSDataStructure'):
        XSData.exportAttributes(self, outfile, level, name_='XSDataStructure')
    def exportChildren(self, outfile, level, name_='XSDataStructure'):
        if self.numberOfCopiesInAsymmetricUnit:
            self.numberOfCopiesInAsymmetricUnit.export(outfile, level, name_='numberOfCopiesInAsymmetricUnit')
        for chain_ in self.getChain():
            chain_.export(outfile, level, name_='chain')
        for ligand_ in self.getLigand():
            ligand_.export(outfile, level, name_='ligand')
        XSData.exportChildren(self, outfile, level, name_)

    #Only to export the entire XML tree to a file stream on disk
    def outputFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write("<?xml version=\"1.0\" ?>\n")
        self.export( outfile, 0, name_='XSDataStructure' )
        outfile.close()


    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataStructure.factory()
        rootObj.build(rootNode)
        return rootObj
    parseString = staticmethod( parseString ) 


    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataStructure.factory()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile ) 


    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO.StringIO()
        oStreamString.write('<?xml version="1.0" ?>\n')
        self.export( oStreamString, 0, name_="XSDataStructure" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    def exportLiteral(self, outfile, level, name_='XSDataStructure'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        pass
        XSData.exportLiteralAttributes(self, outfile, level, name_)
    def exportLiteralChildren(self, outfile, level, name_):
        if self.numberOfCopiesInAsymmetricUnit:
            showIndent(outfile, level)
            outfile.write('numberOfCopiesInAsymmetricUnit=XSDataFloat(\n')
            self.numberOfCopiesInAsymmetricUnit.exportLiteral(outfile, level, name_='numberOfCopiesInAsymmetricUnit')
            showIndent(outfile, level)
            outfile.write('),\n')
        showIndent(outfile, level)
        outfile.write('chain=[\n')
        level += 1
        for chain in self.chain:
            showIndent(outfile, level)
            outfile.write('XSDataChain(\n')
            chain.exportLiteral(outfile, level, name_='chain')
            showIndent(outfile, level)
            outfile.write('),\n')
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
        showIndent(outfile, level)
        outfile.write('ligand=[\n')
        level += 1
        for ligand in self.ligand:
            showIndent(outfile, level)
            outfile.write('XSDataLigand(\n')
            ligand.exportLiteral(outfile, level, name_='ligand')
            showIndent(outfile, level)
            outfile.write('),\n')
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
        XSData.exportLiteralChildren(self, outfile, level, name_)
    def build(self, node_):
        attrs = node_.attributes
        self.buildAttributes(attrs)
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildAttributes(self, attrs):
        XSData.buildAttributes(self, attrs)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'numberOfCopiesInAsymmetricUnit':
            obj_ = XSDataFloat.factory()
            obj_.build(child_)
            self.setNumberOfCopiesInAsymmetricUnit(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'chain':
            obj_ = XSDataChain.factory()
            obj_.build(child_)
            self.chain.append(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'ligand':
            obj_ = XSDataLigand.factory()
            obj_.build(child_)
            self.ligand.append(obj_)
# end class XSDataStructure


class XSDataSubWedge(XSData):
    subclass = None
    def __init__(self, action=None, image=None, subWedgeNumber=None, experimentalCondition=None):
        XSData.__init__(self)
        self.action = action
        if image is None:
            self.image = []
        else:
            self.image = image
        self.subWedgeNumber = subWedgeNumber
        self.experimentalCondition = experimentalCondition
    def factory(*args_, **kwargs_):
        if XSDataSubWedge.subclass:
            return XSDataSubWedge.subclass(*args_, **kwargs_)
        else:
            return XSDataSubWedge(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getAction(self): return self.action
    def setAction(self, action): self.action = action
    def getImage(self): return self.image
    def setImage(self, image): self.image = image
    def addImage(self, value): self.image.append(value)
    def insertImage(self, index, value): self.image[index] = value
    def getSubWedgeNumber(self): return self.subWedgeNumber
    def setSubWedgeNumber(self, subWedgeNumber): self.subWedgeNumber = subWedgeNumber
    def getExperimentalCondition(self): return self.experimentalCondition
    def setExperimentalCondition(self, experimentalCondition): self.experimentalCondition = experimentalCondition
    def export(self, outfile, level, name_='XSDataSubWedge'):
        showIndent(outfile, level)
        outfile.write('<%s>\n' % name_)
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='XSDataSubWedge'):
        XSData.exportAttributes(self, outfile, level, name_='XSDataSubWedge')
    def exportChildren(self, outfile, level, name_='XSDataSubWedge'):
        if self.getAction() != None :
            if self.action:
                self.action.export(outfile, level, name_='action')
        for image_ in self.getImage():
            image_.export(outfile, level, name_='image')
        if self.getSubWedgeNumber() != None :
            if self.subWedgeNumber:
                self.subWedgeNumber.export(outfile, level, name_='subWedgeNumber')
        if self.experimentalCondition:
            self.experimentalCondition.export(outfile, level, name_='experimentalCondition')
        XSData.exportChildren(self, outfile, level, name_)

    #Only to export the entire XML tree to a file stream on disk
    def outputFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write("<?xml version=\"1.0\" ?>\n")
        self.export( outfile, 0, name_='XSDataSubWedge' )
        outfile.close()


    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataSubWedge.factory()
        rootObj.build(rootNode)
        return rootObj
    parseString = staticmethod( parseString ) 


    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataSubWedge.factory()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile ) 


    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO.StringIO()
        oStreamString.write('<?xml version="1.0" ?>\n')
        self.export( oStreamString, 0, name_="XSDataSubWedge" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    def exportLiteral(self, outfile, level, name_='XSDataSubWedge'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        pass
        XSData.exportLiteralAttributes(self, outfile, level, name_)
    def exportLiteralChildren(self, outfile, level, name_):
        if self.action:
            showIndent(outfile, level)
            outfile.write('action=XSDataString(\n')
            self.action.exportLiteral(outfile, level, name_='action')
            showIndent(outfile, level)
            outfile.write('),\n')
        showIndent(outfile, level)
        outfile.write('image=[\n')
        level += 1
        for image in self.image:
            showIndent(outfile, level)
            outfile.write('XSDataImage(\n')
            image.exportLiteral(outfile, level, name_='image')
            showIndent(outfile, level)
            outfile.write('),\n')
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
        if self.subWedgeNumber:
            showIndent(outfile, level)
            outfile.write('subWedgeNumber=XSDataInteger(\n')
            self.subWedgeNumber.exportLiteral(outfile, level, name_='subWedgeNumber')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.experimentalCondition:
            showIndent(outfile, level)
            outfile.write('experimentalCondition=XSDataExperimentalCondition(\n')
            self.experimentalCondition.exportLiteral(outfile, level, name_='experimentalCondition')
            showIndent(outfile, level)
            outfile.write('),\n')
        XSData.exportLiteralChildren(self, outfile, level, name_)
    def build(self, node_):
        attrs = node_.attributes
        self.buildAttributes(attrs)
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildAttributes(self, attrs):
        XSData.buildAttributes(self, attrs)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'action':
            obj_ = XSDataString.factory()
            obj_.build(child_)
            self.setAction(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'image':
            obj_ = XSDataImage.factory()
            obj_.build(child_)
            self.image.append(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'subWedgeNumber':
            obj_ = XSDataInteger.factory()
            obj_.build(child_)
            self.setSubWedgeNumber(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'experimentalCondition':
            obj_ = XSDataExperimentalCondition.factory()
            obj_.build(child_)
            self.setExperimentalCondition(obj_)
# end class XSDataSubWedge


class XSDataAbsorbedDoseRate(XSDataDoubleWithUnit):
    subclass = None
    def __init__(self, value=0.0, unit=None, error=None, valueOf_=''):
        XSDataDoubleWithUnit.__init__(self, value, unit, error)
        self.valueOf_ = valueOf_
    def factory(*args_, **kwargs_):
        if XSDataAbsorbedDoseRate.subclass:
            return XSDataAbsorbedDoseRate.subclass(*args_, **kwargs_)
        else:
            return XSDataAbsorbedDoseRate(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getValueOf_(self): return self.valueOf_
    def setValueOf_(self, valueOf_): self.valueOf_ = valueOf_
    def export(self, outfile, level, name_='XSDataAbsorbedDoseRate'):
        showIndent(outfile, level)
        outfile.write('<%s>\n' % name_)
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='XSDataAbsorbedDoseRate'):
        XSDataDoubleWithUnit.exportAttributes(self, outfile, level, name_='XSDataAbsorbedDoseRate')
    def exportChildren(self, outfile, level, name_='XSDataAbsorbedDoseRate'):
        XSDataDoubleWithUnit.exportChildren(self, outfile, level, name_)

    #Only to export the entire XML tree to a file stream on disk
    def outputFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write("<?xml version=\"1.0\" ?>\n")
        self.export( outfile, 0, name_='XSDataAbsorbedDoseRate' )
        outfile.close()


    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataAbsorbedDoseRate.factory()
        rootObj.build(rootNode)
        return rootObj
    parseString = staticmethod( parseString ) 


    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataAbsorbedDoseRate.factory()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile ) 


    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO.StringIO()
        oStreamString.write('<?xml version="1.0" ?>\n')
        self.export( oStreamString, 0, name_="XSDataAbsorbedDoseRate" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    def exportLiteral(self, outfile, level, name_='XSDataAbsorbedDoseRate'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        pass
        XSDataDoubleWithUnit.exportLiteralAttributes(self, outfile, level, name_)
    def exportLiteralChildren(self, outfile, level, name_):
        showIndent(outfile, level)
        outfile.write('valueOf_ = "%s",\n' % (self.valueOf_,))
        XSDataDoubleWithUnit.exportLiteralChildren(self, outfile, level, name_)
    def build(self, node_):
        attrs = node_.attributes
        self.buildAttributes(attrs)
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildAttributes(self, attrs):
        XSDataDoubleWithUnit.buildAttributes(self, attrs)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.TEXT_NODE:
            self.valueOf_ += child_.nodeValue
        XSDataDoubleWithUnit.buildChildren(self, child_, nodeName_)
# end class XSDataAbsorbedDoseRate


class XSDataAngle(XSDataDisplacement):
    subclass = None
    def __init__(self, value=0.0, unit=None, error=None, valueOf_=''):
        XSDataDisplacement.__init__(self, value, unit, error)
        self.valueOf_ = valueOf_
    def factory(*args_, **kwargs_):
        if XSDataAngle.subclass:
            return XSDataAngle.subclass(*args_, **kwargs_)
        else:
            return XSDataAngle(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getValueOf_(self): return self.valueOf_
    def setValueOf_(self, valueOf_): self.valueOf_ = valueOf_
    def export(self, outfile, level, name_='XSDataAngle'):
        showIndent(outfile, level)
        outfile.write('<%s>\n' % name_)
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='XSDataAngle'):
        XSDataDisplacement.exportAttributes(self, outfile, level, name_='XSDataAngle')
    def exportChildren(self, outfile, level, name_='XSDataAngle'):
        XSDataDisplacement.exportChildren(self, outfile, level, name_)

    #Only to export the entire XML tree to a file stream on disk
    def outputFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write("<?xml version=\"1.0\" ?>\n")
        self.export( outfile, 0, name_='XSDataAngle' )
        outfile.close()


    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataAngle.factory()
        rootObj.build(rootNode)
        return rootObj
    parseString = staticmethod( parseString ) 


    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataAngle.factory()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile ) 


    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO.StringIO()
        oStreamString.write('<?xml version="1.0" ?>\n')
        self.export( oStreamString, 0, name_="XSDataAngle" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    def exportLiteral(self, outfile, level, name_='XSDataAngle'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        pass
        XSDataDisplacement.exportLiteralAttributes(self, outfile, level, name_)
    def exportLiteralChildren(self, outfile, level, name_):
        showIndent(outfile, level)
        outfile.write('valueOf_ = "%s",\n' % (self.valueOf_,))
        XSDataDisplacement.exportLiteralChildren(self, outfile, level, name_)
    def build(self, node_):
        attrs = node_.attributes
        self.buildAttributes(attrs)
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildAttributes(self, attrs):
        XSDataDisplacement.buildAttributes(self, attrs)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.TEXT_NODE:
            self.valueOf_ += child_.nodeValue
        XSDataDisplacement.buildChildren(self, child_, nodeName_)
# end class XSDataAngle


class XSDataAngularSpeed(XSDataDoubleWithUnit):
    subclass = None
    def __init__(self, value=0.0, unit=None, error=None, valueOf_=''):
        XSDataDoubleWithUnit.__init__(self, value, unit, error)
        self.valueOf_ = valueOf_
    def factory(*args_, **kwargs_):
        if XSDataAngularSpeed.subclass:
            return XSDataAngularSpeed.subclass(*args_, **kwargs_)
        else:
            return XSDataAngularSpeed(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getValueOf_(self): return self.valueOf_
    def setValueOf_(self, valueOf_): self.valueOf_ = valueOf_
    def export(self, outfile, level, name_='XSDataAngularSpeed'):
        showIndent(outfile, level)
        outfile.write('<%s>\n' % name_)
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='XSDataAngularSpeed'):
        XSDataDoubleWithUnit.exportAttributes(self, outfile, level, name_='XSDataAngularSpeed')
    def exportChildren(self, outfile, level, name_='XSDataAngularSpeed'):
        XSDataDoubleWithUnit.exportChildren(self, outfile, level, name_)

    #Only to export the entire XML tree to a file stream on disk
    def outputFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write("<?xml version=\"1.0\" ?>\n")
        self.export( outfile, 0, name_='XSDataAngularSpeed' )
        outfile.close()


    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataAngularSpeed.factory()
        rootObj.build(rootNode)
        return rootObj
    parseString = staticmethod( parseString ) 


    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataAngularSpeed.factory()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile ) 


    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO.StringIO()
        oStreamString.write('<?xml version="1.0" ?>\n')
        self.export( oStreamString, 0, name_="XSDataAngularSpeed" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    def exportLiteral(self, outfile, level, name_='XSDataAngularSpeed'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        pass
        XSDataDoubleWithUnit.exportLiteralAttributes(self, outfile, level, name_)
    def exportLiteralChildren(self, outfile, level, name_):
        showIndent(outfile, level)
        outfile.write('valueOf_ = "%s",\n' % (self.valueOf_,))
        XSDataDoubleWithUnit.exportLiteralChildren(self, outfile, level, name_)
    def build(self, node_):
        attrs = node_.attributes
        self.buildAttributes(attrs)
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildAttributes(self, attrs):
        XSDataDoubleWithUnit.buildAttributes(self, attrs)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.TEXT_NODE:
            self.valueOf_ += child_.nodeValue
        XSDataDoubleWithUnit.buildChildren(self, child_, nodeName_)
# end class XSDataAngularSpeed


class XSDataDate(XSDataString):
    subclass = None
    def __init__(self, value='', valueOf_=''):
        XSDataString.__init__(self, value)
        self.valueOf_ = valueOf_
    def factory(*args_, **kwargs_):
        if XSDataDate.subclass:
            return XSDataDate.subclass(*args_, **kwargs_)
        else:
            return XSDataDate(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getValueOf_(self): return self.valueOf_
    def setValueOf_(self, valueOf_): self.valueOf_ = valueOf_
    def export(self, outfile, level, name_='XSDataDate'):
        showIndent(outfile, level)
        outfile.write('<%s>\n' % name_)
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='XSDataDate'):
        XSDataString.exportAttributes(self, outfile, level, name_='XSDataDate')
    def exportChildren(self, outfile, level, name_='XSDataDate'):
        XSDataString.exportChildren(self, outfile, level, name_)

    #Only to export the entire XML tree to a file stream on disk
    def outputFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write("<?xml version=\"1.0\" ?>\n")
        self.export( outfile, 0, name_='XSDataDate' )
        outfile.close()


    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataDate.factory()
        rootObj.build(rootNode)
        return rootObj
    parseString = staticmethod( parseString ) 


    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataDate.factory()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile ) 


    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO.StringIO()
        oStreamString.write('<?xml version="1.0" ?>\n')
        self.export( oStreamString, 0, name_="XSDataDate" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    def exportLiteral(self, outfile, level, name_='XSDataDate'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        pass
        XSDataString.exportLiteralAttributes(self, outfile, level, name_)
    def exportLiteralChildren(self, outfile, level, name_):
        showIndent(outfile, level)
        outfile.write('valueOf_ = "%s",\n' % (self.valueOf_,))
        XSDataString.exportLiteralChildren(self, outfile, level, name_)
    def build(self, node_):
        attrs = node_.attributes
        self.buildAttributes(attrs)
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildAttributes(self, attrs):
        XSDataString.buildAttributes(self, attrs)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.TEXT_NODE:
            self.valueOf_ += child_.nodeValue
        XSDataString.buildChildren(self, child_, nodeName_)
# end class XSDataDate


class XSDataMatrix(XSDataMatrixDouble):
    subclass = None
    def __init__(self, m11=0.0, m12=0.0, m13=0.0, m21=0.0, m22=0.0, m23=0.0, m31=0.0, m32=0.0, m33=0.0, valueOf_=''):
        XSDataMatrixDouble.__init__(self, m11, m12, m13, m21, m22, m23, m31, m32, m33)
        self.valueOf_ = valueOf_
    def factory(*args_, **kwargs_):
        if XSDataMatrix.subclass:
            return XSDataMatrix.subclass(*args_, **kwargs_)
        else:
            return XSDataMatrix(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getValueOf_(self): return self.valueOf_
    def setValueOf_(self, valueOf_): self.valueOf_ = valueOf_
    def export(self, outfile, level, name_='XSDataMatrix'):
        showIndent(outfile, level)
        outfile.write('<%s>\n' % name_)
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='XSDataMatrix'):
        XSDataMatrixDouble.exportAttributes(self, outfile, level, name_='XSDataMatrix')
    def exportChildren(self, outfile, level, name_='XSDataMatrix'):
        XSDataMatrixDouble.exportChildren(self, outfile, level, name_)

    #Only to export the entire XML tree to a file stream on disk
    def outputFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write("<?xml version=\"1.0\" ?>\n")
        self.export( outfile, 0, name_='XSDataMatrix' )
        outfile.close()


    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataMatrix.factory()
        rootObj.build(rootNode)
        return rootObj
    parseString = staticmethod( parseString ) 


    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataMatrix.factory()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile ) 


    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO.StringIO()
        oStreamString.write('<?xml version="1.0" ?>\n')
        self.export( oStreamString, 0, name_="XSDataMatrix" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    def exportLiteral(self, outfile, level, name_='XSDataMatrix'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        pass
        XSDataMatrixDouble.exportLiteralAttributes(self, outfile, level, name_)
    def exportLiteralChildren(self, outfile, level, name_):
        showIndent(outfile, level)
        outfile.write('valueOf_ = "%s",\n' % (self.valueOf_,))
        XSDataMatrixDouble.exportLiteralChildren(self, outfile, level, name_)
    def build(self, node_):
        attrs = node_.attributes
        self.buildAttributes(attrs)
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildAttributes(self, attrs):
        XSDataMatrixDouble.buildAttributes(self, attrs)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.TEXT_NODE:
            self.valueOf_ += child_.nodeValue
        XSDataMatrixDouble.buildChildren(self, child_, nodeName_)
# end class XSDataMatrix


class XSDataUnitVector(XSDataVectorDouble):
    subclass = None
    def __init__(self, v1=0.0, v2=0.0, v3=0.0, valueOf_=''):
        XSDataVectorDouble.__init__(self, v1, v2, v3)
        self.valueOf_ = valueOf_
    def factory(*args_, **kwargs_):
        if XSDataUnitVector.subclass:
            return XSDataUnitVector.subclass(*args_, **kwargs_)
        else:
            return XSDataUnitVector(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getValueOf_(self): return self.valueOf_
    def setValueOf_(self, valueOf_): self.valueOf_ = valueOf_
    def export(self, outfile, level, name_='XSDataUnitVector'):
        showIndent(outfile, level)
        outfile.write('<%s>\n' % name_)
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='XSDataUnitVector'):
        XSDataVectorDouble.exportAttributes(self, outfile, level, name_='XSDataUnitVector')
    def exportChildren(self, outfile, level, name_='XSDataUnitVector'):
        XSDataVectorDouble.exportChildren(self, outfile, level, name_)

    #Only to export the entire XML tree to a file stream on disk
    def outputFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write("<?xml version=\"1.0\" ?>\n")
        self.export( outfile, 0, name_='XSDataUnitVector' )
        outfile.close()


    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataUnitVector.factory()
        rootObj.build(rootNode)
        return rootObj
    parseString = staticmethod( parseString ) 


    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataUnitVector.factory()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile ) 


    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO.StringIO()
        oStreamString.write('<?xml version="1.0" ?>\n')
        self.export( oStreamString, 0, name_="XSDataUnitVector" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    def exportLiteral(self, outfile, level, name_='XSDataUnitVector'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        pass
        XSDataVectorDouble.exportLiteralAttributes(self, outfile, level, name_)
    def exportLiteralChildren(self, outfile, level, name_):
        showIndent(outfile, level)
        outfile.write('valueOf_ = "%s",\n' % (self.valueOf_,))
        XSDataVectorDouble.exportLiteralChildren(self, outfile, level, name_)
    def build(self, node_):
        attrs = node_.attributes
        self.buildAttributes(attrs)
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildAttributes(self, attrs):
        XSDataVectorDouble.buildAttributes(self, attrs)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.TEXT_NODE:
            self.valueOf_ += child_.nodeValue
        XSDataVectorDouble.buildChildren(self, child_, nodeName_)
# end class XSDataUnitVector


class XSDataInputInterface:
    subclass = None
    def __init__(self, experimentalCondition=None, diffractionPlan=None, sample=None, imagePath=None, flux=None, minExposureTimePerImage=None, beamSize=None, beamSizeX=None, beamSizeY=None, templateMode=None, generatedTemplateFile=None, resultsFilePath=None, beamPosX=None, beamPosY=None, wavelength=None, transmission=None, dataCollectionId=None, shortComments=None, comments=None, inputCharacterisation=None):
        self.experimentalCondition = experimentalCondition
        self.diffractionPlan = diffractionPlan
        self.sample = sample
        if imagePath is None:
            self.imagePath = []
        else:
            self.imagePath = imagePath
        self.flux = flux
        self.minExposureTimePerImage = minExposureTimePerImage
        self.beamSize = beamSize
        self.beamSizeX = beamSizeX
        self.beamSizeY = beamSizeY
        self.templateMode = templateMode
        self.generatedTemplateFile = generatedTemplateFile
        self.resultsFilePath = resultsFilePath
        self.beamPosX = beamPosX
        self.beamPosY = beamPosY
        self.wavelength = wavelength
        self.transmission = transmission
        self.dataCollectionId = dataCollectionId
        self.shortComments = shortComments
        self.comments = comments
        self.inputCharacterisation = inputCharacterisation
    def factory(*args_, **kwargs_):
        if XSDataInputInterface.subclass:
            return XSDataInputInterface.subclass(*args_, **kwargs_)
        else:
            return XSDataInputInterface(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getExperimentalCondition(self): return self.experimentalCondition
    def setExperimentalCondition(self, experimentalCondition): self.experimentalCondition = experimentalCondition
    def getDiffractionPlan(self): return self.diffractionPlan
    def setDiffractionPlan(self, diffractionPlan): self.diffractionPlan = diffractionPlan
    def getSample(self): return self.sample
    def setSample(self, sample): self.sample = sample
    def getImagePath(self): return self.imagePath
    def setImagePath(self, imagePath): self.imagePath = imagePath
    def addImagePath(self, value): self.imagePath.append(value)
    def insertImagePath(self, index, value): self.imagePath[index] = value
    def getFlux(self): return self.flux
    def setFlux(self, flux): self.flux = flux
    def getMinExposureTimePerImage(self): return self.minExposureTimePerImage
    def setMinExposureTimePerImage(self, minExposureTimePerImage): self.minExposureTimePerImage = minExposureTimePerImage
    def getBeamSize(self): return self.beamSize
    def setBeamSize(self, beamSize): self.beamSize = beamSize
    def getBeamSizeX(self): return self.beamSizeX
    def setBeamSizeX(self, beamSizeX): self.beamSizeX = beamSizeX
    def getBeamSizeY(self): return self.beamSizeY
    def setBeamSizeY(self, beamSizeY): self.beamSizeY = beamSizeY
    def getTemplateMode(self): return self.templateMode
    def setTemplateMode(self, templateMode): self.templateMode = templateMode
    def getGeneratedTemplateFile(self): return self.generatedTemplateFile
    def setGeneratedTemplateFile(self, generatedTemplateFile): self.generatedTemplateFile = generatedTemplateFile
    def getResultsFilePath(self): return self.resultsFilePath
    def setResultsFilePath(self, resultsFilePath): self.resultsFilePath = resultsFilePath
    def getBeamPosX(self): return self.beamPosX
    def setBeamPosX(self, beamPosX): self.beamPosX = beamPosX
    def getBeamPosY(self): return self.beamPosY
    def setBeamPosY(self, beamPosY): self.beamPosY = beamPosY
    def getWavelength(self): return self.wavelength
    def setWavelength(self, wavelength): self.wavelength = wavelength
    def getTransmission(self): return self.transmission
    def setTransmission(self, transmission): self.transmission = transmission
    def getDataCollectionId(self): return self.dataCollectionId
    def setDataCollectionId(self, dataCollectionId): self.dataCollectionId = dataCollectionId
    def getShortComments(self): return self.shortComments
    def setShortComments(self, shortComments): self.shortComments = shortComments
    def getComments(self): return self.comments
    def setComments(self, comments): self.comments = comments
    def getInputCharacterisation(self): return self.inputCharacterisation
    def setInputCharacterisation(self, inputCharacterisation): self.inputCharacterisation = inputCharacterisation
    def export(self, outfile, level, name_='XSDataInputInterface'):
        showIndent(outfile, level)
        outfile.write('<%s>\n' % name_)
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='XSDataInputInterface'):
        pass
    def exportChildren(self, outfile, level, name_='XSDataInputInterface'):
        if self.getExperimentalCondition() != None :
            if self.experimentalCondition:
                self.experimentalCondition.export(outfile, level, name_='experimentalCondition')
        if self.getDiffractionPlan() != None :
            if self.diffractionPlan:
                self.diffractionPlan.export(outfile, level, name_='diffractionPlan')
        if self.getSample() != None :
            if self.sample:
                self.sample.export(outfile, level, name_='sample')
        for imagePath_ in self.getImagePath():
            imagePath_.export(outfile, level, name_='imagePath')
        if self.getFlux() != None :
            if self.flux:
                self.flux.export(outfile, level, name_='flux')
        if self.getMinExposureTimePerImage() != None :
            if self.minExposureTimePerImage:
                self.minExposureTimePerImage.export(outfile, level, name_='minExposureTimePerImage')
        if self.getBeamSize() != None :
            if self.beamSize:
                self.beamSize.export(outfile, level, name_='beamSize')
        if self.getBeamSizeX() != None :
            if self.beamSizeX:
                self.beamSizeX.export(outfile, level, name_='beamSizeX')
        if self.getBeamSizeY() != None :
            if self.beamSizeY:
                self.beamSizeY.export(outfile, level, name_='beamSizeY')
        if self.getTemplateMode() != None :
            if self.templateMode:
                self.templateMode.export(outfile, level, name_='templateMode')
        if self.getGeneratedTemplateFile() != None :
            if self.generatedTemplateFile:
                self.generatedTemplateFile.export(outfile, level, name_='generatedTemplateFile')
        if self.getResultsFilePath() != None :
            if self.resultsFilePath:
                self.resultsFilePath.export(outfile, level, name_='resultsFilePath')
        if self.getBeamPosX() != None :
            if self.beamPosX:
                self.beamPosX.export(outfile, level, name_='beamPosX')
        if self.getBeamPosY() != None :
            if self.beamPosY:
                self.beamPosY.export(outfile, level, name_='beamPosY')
        if self.getWavelength() != None :
            if self.wavelength:
                self.wavelength.export(outfile, level, name_='wavelength')
        if self.getTransmission() != None :
            if self.transmission:
                self.transmission.export(outfile, level, name_='transmission')
        if self.getDataCollectionId() != None :
            if self.dataCollectionId:
                self.dataCollectionId.export(outfile, level, name_='dataCollectionId')
        if self.getShortComments() != None :
            if self.shortComments:
                self.shortComments.export(outfile, level, name_='shortComments')
        if self.getComments() != None :
            if self.comments:
                self.comments.export(outfile, level, name_='comments')
        if self.getInputCharacterisation() != None :
            if self.inputCharacterisation:
                self.inputCharacterisation.export(outfile, level, name_='inputCharacterisation')

    #Only to export the entire XML tree to a file stream on disk
    def outputFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write("<?xml version=\"1.0\" ?>\n")
        self.export( outfile, 0, name_='XSDataInputInterface' )
        outfile.close()


    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataInputInterface.factory()
        rootObj.build(rootNode)
        return rootObj
    parseString = staticmethod( parseString ) 


    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataInputInterface.factory()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile ) 


    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO.StringIO()
        oStreamString.write('<?xml version="1.0" ?>\n')
        self.export( oStreamString, 0, name_="XSDataInputInterface" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    def exportLiteral(self, outfile, level, name_='XSDataInputInterface'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        pass
    def exportLiteralChildren(self, outfile, level, name_):
        if self.experimentalCondition:
            showIndent(outfile, level)
            outfile.write('experimentalCondition=XSDataExperimentalCondition(\n')
            self.experimentalCondition.exportLiteral(outfile, level, name_='experimentalCondition')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.diffractionPlan:
            showIndent(outfile, level)
            outfile.write('diffractionPlan=XSDataDiffractionPlan(\n')
            self.diffractionPlan.exportLiteral(outfile, level, name_='diffractionPlan')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.sample:
            showIndent(outfile, level)
            outfile.write('sample=XSDataSample(\n')
            self.sample.exportLiteral(outfile, level, name_='sample')
            showIndent(outfile, level)
            outfile.write('),\n')
        showIndent(outfile, level)
        outfile.write('imagePath=[\n')
        level += 1
        for imagePath in self.imagePath:
            showIndent(outfile, level)
            outfile.write('XSDataFile(\n')
            imagePath.exportLiteral(outfile, level, name_='imagePath')
            showIndent(outfile, level)
            outfile.write('),\n')
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
        if self.flux:
            showIndent(outfile, level)
            outfile.write('flux=XSDataFloat(\n')
            self.flux.exportLiteral(outfile, level, name_='flux')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.minExposureTimePerImage:
            showIndent(outfile, level)
            outfile.write('minExposureTimePerImage=XSDataTime(\n')
            self.minExposureTimePerImage.exportLiteral(outfile, level, name_='minExposureTimePerImage')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.beamSize:
            showIndent(outfile, level)
            outfile.write('beamSize=XSDataLength(\n')
            self.beamSize.exportLiteral(outfile, level, name_='beamSize')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.beamSizeX:
            showIndent(outfile, level)
            outfile.write('beamSizeX=XSDataLength(\n')
            self.beamSizeX.exportLiteral(outfile, level, name_='beamSizeX')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.beamSizeY:
            showIndent(outfile, level)
            outfile.write('beamSizeY=XSDataLength(\n')
            self.beamSizeY.exportLiteral(outfile, level, name_='beamSizeY')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.templateMode:
            showIndent(outfile, level)
            outfile.write('templateMode=XSDataBoolean(\n')
            self.templateMode.exportLiteral(outfile, level, name_='templateMode')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.generatedTemplateFile:
            showIndent(outfile, level)
            outfile.write('generatedTemplateFile=XSDataFile(\n')
            self.generatedTemplateFile.exportLiteral(outfile, level, name_='generatedTemplateFile')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.resultsFilePath:
            showIndent(outfile, level)
            outfile.write('resultsFilePath=XSDataFile(\n')
            self.resultsFilePath.exportLiteral(outfile, level, name_='resultsFilePath')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.beamPosX:
            showIndent(outfile, level)
            outfile.write('beamPosX=XSDataFloat(\n')
            self.beamPosX.exportLiteral(outfile, level, name_='beamPosX')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.beamPosY:
            showIndent(outfile, level)
            outfile.write('beamPosY=XSDataFloat(\n')
            self.beamPosY.exportLiteral(outfile, level, name_='beamPosY')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.wavelength:
            showIndent(outfile, level)
            outfile.write('wavelength=XSDataWavelength(\n')
            self.wavelength.exportLiteral(outfile, level, name_='wavelength')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.transmission:
            showIndent(outfile, level)
            outfile.write('transmission=XSDataDouble(\n')
            self.transmission.exportLiteral(outfile, level, name_='transmission')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.dataCollectionId:
            showIndent(outfile, level)
            outfile.write('dataCollectionId=XSDataInteger(\n')
            self.dataCollectionId.exportLiteral(outfile, level, name_='dataCollectionId')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.shortComments:
            showIndent(outfile, level)
            outfile.write('shortComments=XSDataString(\n')
            self.shortComments.exportLiteral(outfile, level, name_='shortComments')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.comments:
            showIndent(outfile, level)
            outfile.write('comments=XSDataString(\n')
            self.comments.exportLiteral(outfile, level, name_='comments')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.inputCharacterisation:
            showIndent(outfile, level)
            outfile.write('inputCharacterisation=XSDataInputCharacterisation(\n')
            self.inputCharacterisation.exportLiteral(outfile, level, name_='inputCharacterisation')
            showIndent(outfile, level)
            outfile.write('),\n')
    def build(self, node_):
        attrs = node_.attributes
        self.buildAttributes(attrs)
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildAttributes(self, attrs):
        pass
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'experimentalCondition':
            obj_ = XSDataExperimentalCondition.factory()
            obj_.build(child_)
            self.setExperimentalCondition(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'diffractionPlan':
            obj_ = XSDataDiffractionPlan.factory()
            obj_.build(child_)
            self.setDiffractionPlan(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'sample':
            obj_ = XSDataSample.factory()
            obj_.build(child_)
            self.setSample(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'imagePath':
            obj_ = XSDataFile.factory()
            obj_.build(child_)
            self.imagePath.append(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'flux':
            obj_ = XSDataFloat.factory()
            obj_.build(child_)
            self.setFlux(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'minExposureTimePerImage':
            obj_ = XSDataTime.factory()
            obj_.build(child_)
            self.setMinExposureTimePerImage(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'beamSize':
            obj_ = XSDataLength.factory()
            obj_.build(child_)
            self.setBeamSize(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'beamSizeX':
            obj_ = XSDataLength.factory()
            obj_.build(child_)
            self.setBeamSizeX(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'beamSizeY':
            obj_ = XSDataLength.factory()
            obj_.build(child_)
            self.setBeamSizeY(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'templateMode':
            obj_ = XSDataBoolean.factory()
            obj_.build(child_)
            self.setTemplateMode(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'generatedTemplateFile':
            obj_ = XSDataFile.factory()
            obj_.build(child_)
            self.setGeneratedTemplateFile(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'resultsFilePath':
            obj_ = XSDataFile.factory()
            obj_.build(child_)
            self.setResultsFilePath(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'beamPosX':
            obj_ = XSDataFloat.factory()
            obj_.build(child_)
            self.setBeamPosX(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'beamPosY':
            obj_ = XSDataFloat.factory()
            obj_.build(child_)
            self.setBeamPosY(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'wavelength':
            obj_ = XSDataWavelength.factory()
            obj_.build(child_)
            self.setWavelength(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'transmission':
            obj_ = XSDataDouble.factory()
            obj_.build(child_)
            self.setTransmission(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'dataCollectionId':
            obj_ = XSDataInteger.factory()
            obj_.build(child_)
            self.setDataCollectionId(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'shortComments':
            obj_ = XSDataString.factory()
            obj_.build(child_)
            self.setShortComments(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'comments':
            obj_ = XSDataString.factory()
            obj_.build(child_)
            self.setComments(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'inputCharacterisation':
            obj_ = XSDataInputCharacterisation.factory()
            obj_.build(child_)
            self.setInputCharacterisation(obj_)
# end class XSDataInputInterface


class XSDataResultInterface:
    subclass = None
    def __init__(self, resultCharacterisation=None, resultControlISPyB=None):
        self.resultCharacterisation = resultCharacterisation
        self.resultControlISPyB = resultControlISPyB
    def factory(*args_, **kwargs_):
        if XSDataResultInterface.subclass:
            return XSDataResultInterface.subclass(*args_, **kwargs_)
        else:
            return XSDataResultInterface(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getResultCharacterisation(self): return self.resultCharacterisation
    def setResultCharacterisation(self, resultCharacterisation): self.resultCharacterisation = resultCharacterisation
    def getResultControlISPyB(self): return self.resultControlISPyB
    def setResultControlISPyB(self, resultControlISPyB): self.resultControlISPyB = resultControlISPyB
    def export(self, outfile, level, name_='XSDataResultInterface'):
        showIndent(outfile, level)
        outfile.write('<%s>\n' % name_)
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='XSDataResultInterface'):
        pass
    def exportChildren(self, outfile, level, name_='XSDataResultInterface'):
        if self.getResultCharacterisation() != None :
            if self.resultCharacterisation:
                self.resultCharacterisation.export(outfile, level, name_='resultCharacterisation')
        if self.resultControlISPyB:
            self.resultControlISPyB.export(outfile, level, name_='resultControlISPyB')

    #Only to export the entire XML tree to a file stream on disk
    def outputFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write("<?xml version=\"1.0\" ?>\n")
        self.export( outfile, 0, name_='XSDataResultInterface' )
        outfile.close()


    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataResultInterface.factory()
        rootObj.build(rootNode)
        return rootObj
    parseString = staticmethod( parseString ) 


    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataResultInterface.factory()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile ) 


    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO.StringIO()
        oStreamString.write('<?xml version="1.0" ?>\n')
        self.export( oStreamString, 0, name_="XSDataResultInterface" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    def exportLiteral(self, outfile, level, name_='XSDataResultInterface'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        pass
    def exportLiteralChildren(self, outfile, level, name_):
        if self.resultCharacterisation:
            showIndent(outfile, level)
            outfile.write('resultCharacterisation=XSDataResultCharacterisation(\n')
            self.resultCharacterisation.exportLiteral(outfile, level, name_='resultCharacterisation')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.resultControlISPyB:
            showIndent(outfile, level)
            outfile.write('resultControlISPyB=XSDataResultControlISPyB(\n')
            self.resultControlISPyB.exportLiteral(outfile, level, name_='resultControlISPyB')
            showIndent(outfile, level)
            outfile.write('),\n')
    def build(self, node_):
        attrs = node_.attributes
        self.buildAttributes(attrs)
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildAttributes(self, attrs):
        pass
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'resultCharacterisation':
            obj_ = XSDataResultCharacterisation.factory()
            obj_.build(child_)
            self.setResultCharacterisation(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'resultControlISPyB':
            obj_ = XSDataResultControlISPyB.factory()
            obj_.build(child_)
            self.setResultControlISPyB(obj_)
# end class XSDataResultInterface


from xml.sax import handler, make_parser

class SaxStackElement:
    def __init__(self, name='', obj=None):
        self.name = name
        self.obj = obj
        self.content = ''

#
# SAX handler
#
class SaxXSConfigurationHandler(handler.ContentHandler):
    def __init__(self):
        self.stack = []
        self.root = None

    def getRoot(self):
        return self.root

    def setDocumentLocator(self, locator):
        self.locator = locator
    
    def showError(self, msg):
        print '*** (showError):', msg
        sys.exit(-1)

    def startElement(self, name, attrs):
        done = 0
        if name == 'XSConfiguration':
            obj = XSConfiguration.factory()
            stackObj = SaxStackElement('XSConfiguration', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'XSPluginList':
            obj = XSPluginList.factory()
            stackObj = SaxStackElement('XSPluginList', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'shape':
            stackObj = SaxStackElement('shape', None)
            self.stack.append(stackObj)
            done = 1
        elif name == 'size':
            stackObj = SaxStackElement('size', None)
            self.stack.append(stackObj)
            done = 1
        elif name == 'dtype':
            stackObj = SaxStackElement('dtype', None)
            self.stack.append(stackObj)
            done = 1
        elif name == 'data':
            stackObj = SaxStackElement('data', None)
            self.stack.append(stackObj)
            done = 1
        elif name == 'coding':
            obj = XSDataString.factory()
            stackObj = SaxStackElement('coding', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'md5sum':
            obj = XSDataString.factory()
            stackObj = SaxStackElement('md5sum', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'value':
            stackObj = SaxStackElement('value', None)
            self.stack.append(stackObj)
            done = 1
        elif name == 'keyValuePair':
            obj = XSDataKeyValuePair.factory()
            stackObj = SaxStackElement('keyValuePair', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'unit':
            obj = XSDataString.factory()
            stackObj = SaxStackElement('unit', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'error':
            obj = XSDataDouble.factory()
            stackObj = SaxStackElement('error', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'baseDirectory':
            obj = XSDataFile.factory()
            stackObj = SaxStackElement('baseDirectory', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'executionTime':
            obj = XSDataTime.factory()
            stackObj = SaxStackElement('executionTime', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'pluginName':
            obj = XSDataString.factory()
            stackObj = SaxStackElement('pluginName', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'startOfExecution':
            obj = XSDataDate.factory()
            stackObj = SaxStackElement('startOfExecution', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'systeminfo':
            obj = XSDataSysteminfo.factory()
            stackObj = SaxStackElement('systeminfo', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'workingDirectory':
            obj = XSDataFile.factory()
            stackObj = SaxStackElement('workingDirectory', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'configuration':
            obj = XSConfiguration.factory()
            stackObj = SaxStackElement('configuration', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'path':
            obj = XSDataString.factory()
            stackObj = SaxStackElement('path', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'date':
            obj = XSDataString.factory()
            stackObj = SaxStackElement('date', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'number':
            obj = XSDataInteger.factory()
            stackObj = SaxStackElement('number', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'key':
            obj = XSDataString.factory()
            stackObj = SaxStackElement('key', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'm11':
            stackObj = SaxStackElement('m11', None)
            self.stack.append(stackObj)
            done = 1
        elif name == 'm12':
            stackObj = SaxStackElement('m12', None)
            self.stack.append(stackObj)
            done = 1
        elif name == 'm13':
            stackObj = SaxStackElement('m13', None)
            self.stack.append(stackObj)
            done = 1
        elif name == 'm21':
            stackObj = SaxStackElement('m21', None)
            self.stack.append(stackObj)
            done = 1
        elif name == 'm22':
            stackObj = SaxStackElement('m22', None)
            self.stack.append(stackObj)
            done = 1
        elif name == 'm23':
            stackObj = SaxStackElement('m23', None)
            self.stack.append(stackObj)
            done = 1
        elif name == 'm31':
            stackObj = SaxStackElement('m31', None)
            self.stack.append(stackObj)
            done = 1
        elif name == 'm32':
            stackObj = SaxStackElement('m32', None)
            self.stack.append(stackObj)
            done = 1
        elif name == 'm33':
            stackObj = SaxStackElement('m33', None)
            self.stack.append(stackObj)
            done = 1
        elif name == 'debuginfo':
            obj = XSDataString.factory()
            stackObj = SaxStackElement('debuginfo', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'level':
            obj = XSDataString.factory()
            stackObj = SaxStackElement('level', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'text':
            obj = XSDataString.factory()
            stackObj = SaxStackElement('text', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'type':
            obj = XSDataString.factory()
            stackObj = SaxStackElement('typexx', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'q0':
            stackObj = SaxStackElement('q0', None)
            self.stack.append(stackObj)
            done = 1
        elif name == 'q1':
            stackObj = SaxStackElement('q1', None)
            self.stack.append(stackObj)
            done = 1
        elif name == 'q2':
            stackObj = SaxStackElement('q2', None)
            self.stack.append(stackObj)
            done = 1
        elif name == 'q3':
            stackObj = SaxStackElement('q3', None)
            self.stack.append(stackObj)
            done = 1
        elif name == 'x':
            obj = XSDataLength.factory()
            stackObj = SaxStackElement('x', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'y':
            obj = XSDataLength.factory()
            stackObj = SaxStackElement('y', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'z':
            obj = XSDataLength.factory()
            stackObj = SaxStackElement('z', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'executiveSummary':
            obj = XSDataString.factory()
            stackObj = SaxStackElement('executiveSummary', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'isSuccess':
            obj = XSDataBoolean.factory()
            stackObj = SaxStackElement('isSuccess', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'executionInfo':
            obj = XSDataExecutionInfo.factory()
            stackObj = SaxStackElement('executionInfo', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'compiler':
            obj = XSDataString.factory()
            stackObj = SaxStackElement('compiler', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'hostIP':
            obj = XSDataString.factory()
            stackObj = SaxStackElement('hostIP', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'hostName':
            obj = XSDataString.factory()
            stackObj = SaxStackElement('hostName', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'operatingSystem':
            obj = XSDataString.factory()
            stackObj = SaxStackElement('operatingSystem', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'operatingSystemType':
            obj = XSDataString.factory()
            stackObj = SaxStackElement('operatingSystemType', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'userName':
            obj = XSDataString.factory()
            stackObj = SaxStackElement('userName', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'virtualMachine':
            obj = XSDataString.factory()
            stackObj = SaxStackElement('virtualMachine', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'v1':
            stackObj = SaxStackElement('v1', None)
            self.stack.append(stackObj)
            done = 1
        elif name == 'v2':
            stackObj = SaxStackElement('v2', None)
            self.stack.append(stackObj)
            done = 1
        elif name == 'v3':
            stackObj = SaxStackElement('v3', None)
            self.stack.append(stackObj)
            done = 1
        elif name == 'enabled':
            stackObj = SaxStackElement('enabled', None)
            self.stack.append(stackObj)
            done = 1
        elif name == 'name':
            stackObj = SaxStackElement('name', None)
            self.stack.append(stackObj)
            done = 1
        elif name == 'XSOptionItem':
            obj = XSOptionItem.factory()
            stackObj = SaxStackElement('XSOptionItem', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'XSParamItem':
            obj = XSParamItem.factory()
            stackObj = SaxStackElement('XSParamItem', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'XSParamList':
            obj = XSParamList.factory()
            stackObj = SaxStackElement('XSParamList', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'XSOptionList':
            obj = XSOptionList.factory()
            stackObj = SaxStackElement('XSOptionList', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'XSPluginItem':
            obj = XSPluginItem.factory()
            stackObj = SaxStackElement('XSPluginItem', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'concentration':
            obj = XSDataFloat.factory()
            stackObj = SaxStackElement('concentration', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'numberOf':
            obj = XSDataFloat.factory()
            stackObj = SaxStackElement('numberOf', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'symbol':
            obj = XSDataString.factory()
            stackObj = SaxStackElement('symbol', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'atom':
            obj = XSDataAtom.factory()
            stackObj = SaxStackElement('atom', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'exposureTime':
            obj = XSDataTime.factory()
            stackObj = SaxStackElement('exposureTime', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'flux':
            obj = XSDataFlux.factory()
            stackObj = SaxStackElement('flux', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'minExposureTimePerImage':
            obj = XSDataTime.factory()
            stackObj = SaxStackElement('minExposureTimePerImage', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'transmission':
            obj = XSDataDouble.factory()
            stackObj = SaxStackElement('transmission', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'wavelength':
            obj = XSDataWavelength.factory()
            stackObj = SaxStackElement('wavelength', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'angle_alpha':
            obj = XSDataAngle.factory()
            stackObj = SaxStackElement('angle_alpha', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'angle_beta':
            obj = XSDataAngle.factory()
            stackObj = SaxStackElement('angle_beta', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'angle_gamma':
            obj = XSDataAngle.factory()
            stackObj = SaxStackElement('angle_gamma', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'length_a':
            obj = XSDataLength.factory()
            stackObj = SaxStackElement('length_a', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'length_b':
            obj = XSDataLength.factory()
            stackObj = SaxStackElement('length_b', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'length_c':
            obj = XSDataLength.factory()
            stackObj = SaxStackElement('length_c', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'numberOfCopies':
            obj = XSDataFloat.factory()
            stackObj = SaxStackElement('numberOfCopies', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'numberOfMonomers':
            obj = XSDataFloat.factory()
            stackObj = SaxStackElement('numberOfMonomers', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'heavyAtoms':
            obj = XSDataAtomicComposition.factory()
            stackObj = SaxStackElement('heavyAtoms', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'dataCollection':
            obj = XSDataCollection.factory()
            stackObj = SaxStackElement('dataCollection', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'indexingResult':
            obj = XSDataIndexingResult.factory()
            stackObj = SaxStackElement('indexingResult', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'integrationResult':
            obj = XSDataIntegrationResult.factory()
            stackObj = SaxStackElement('integrationResult', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'strategyResult':
            obj = XSDataStrategyResult.factory()
            stackObj = SaxStackElement('strategyResult', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'solvent':
            obj = XSDataSolvent.factory()
            stackObj = SaxStackElement('solvent', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'structure':
            obj = XSDataStructure.factory()
            stackObj = SaxStackElement('structure', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'diffractionPlan':
            obj = XSDataDiffractionPlan.factory()
            stackObj = SaxStackElement('diffractionPlan', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'sample':
            obj = XSDataSampleCrystalMM.factory()
            stackObj = SaxStackElement('sample', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'subWedge':
            obj = XSDataSubWedge.factory()
            stackObj = SaxStackElement('subWedge', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'collectionPlanNumber':
            obj = XSDataInteger.factory()
            stackObj = SaxStackElement('collectionPlanNumber', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'collectionStrategy':
            obj = XSDataCollection.factory()
            stackObj = SaxStackElement('collectionStrategy', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'comment':
            obj = XSDataString.factory()
            stackObj = SaxStackElement('comment', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'strategySummary':
            obj = XSDataStrategySummary.factory()
            stackObj = SaxStackElement('strategySummary', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'statistics':
            obj = XSDataStatisticsStrategy.factory()
            stackObj = SaxStackElement('statistics', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'mosaicity':
            obj = XSDataFloat.factory()
            stackObj = SaxStackElement('mosaicity', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'spaceGroup':
            obj = XSDataSpaceGroup.factory()
            stackObj = SaxStackElement('spaceGroup', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'cell':
            obj = XSDataCell.factory()
            stackObj = SaxStackElement('cell', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'beamPositionX':
            obj = XSDataLength.factory()
            stackObj = SaxStackElement('beamPositionX', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'beamPositionY':
            obj = XSDataLength.factory()
            stackObj = SaxStackElement('beamPositionY', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'bin':
            obj = XSDataString.factory()
            stackObj = SaxStackElement('bin', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'byteOrder':
            obj = XSDataString.factory()
            stackObj = SaxStackElement('byteOrder', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'dataType':
            obj = XSDataString.factory()
            stackObj = SaxStackElement('dataType', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'distance':
            obj = XSDataLength.factory()
            stackObj = SaxStackElement('distance', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'gain':
            obj = XSDataFloat.factory()
            stackObj = SaxStackElement('gain', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'imageSaturation':
            obj = XSDataInteger.factory()
            stackObj = SaxStackElement('imageSaturation', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'numberBytesInHeader':
            obj = XSDataInteger.factory()
            stackObj = SaxStackElement('numberBytesInHeader', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'numberPixelX':
            obj = XSDataInteger.factory()
            stackObj = SaxStackElement('numberPixelX', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'numberPixelY':
            obj = XSDataInteger.factory()
            stackObj = SaxStackElement('numberPixelY', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'pixelSizeX':
            obj = XSDataFloat.factory()
            stackObj = SaxStackElement('pixelSizeX', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'pixelSizeY':
            obj = XSDataFloat.factory()
            stackObj = SaxStackElement('pixelSizeY', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'serialNumber':
            obj = XSDataString.factory()
            stackObj = SaxStackElement('serialNumber', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'twoTheta':
            obj = XSDataAngle.factory()
            stackObj = SaxStackElement('twoTheta', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'aimedCompleteness':
            obj = XSDataDouble.factory()
            stackObj = SaxStackElement('aimedCompleteness', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'aimedIOverSigmaAtHighestResolution':
            obj = XSDataDouble.factory()
            stackObj = SaxStackElement('aimedIOverSigmaAtHighestResolution', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'aimedMultiplicity':
            obj = XSDataDouble.factory()
            stackObj = SaxStackElement('aimedMultiplicity', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'aimedResolution':
            obj = XSDataDouble.factory()
            stackObj = SaxStackElement('aimedResolution', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'anomalousData':
            obj = XSDataBoolean.factory()
            stackObj = SaxStackElement('anomalousData', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'complexity':
            obj = XSDataString.factory()
            stackObj = SaxStackElement('complexity', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'detectorMaxResolution':
            obj = XSDataDouble.factory()
            stackObj = SaxStackElement('detectorMaxResolution', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'detectorMinResolution':
            obj = XSDataDouble.factory()
            stackObj = SaxStackElement('detectorMinResolution', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'estimateRadiationDamage':
            obj = XSDataBoolean.factory()
            stackObj = SaxStackElement('estimateRadiationDamage', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'forcedSpaceGroup':
            obj = XSDataString.factory()
            stackObj = SaxStackElement('forcedSpaceGroup', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'maxExposureTimePerDataCollection':
            obj = XSDataTime.factory()
            stackObj = SaxStackElement('maxExposureTimePerDataCollection', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'requiredCompleteness':
            obj = XSDataDouble.factory()
            stackObj = SaxStackElement('requiredCompleteness', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'requiredMultiplicity':
            obj = XSDataDouble.factory()
            stackObj = SaxStackElement('requiredMultiplicity', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'requiredResolution':
            obj = XSDataDouble.factory()
            stackObj = SaxStackElement('requiredResolution', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'strategyOption':
            obj = XSDataString.factory()
            stackObj = SaxStackElement('strategyOption', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'goniostatMaxOscillationSpeed':
            obj = XSDataAngularSpeed.factory()
            stackObj = SaxStackElement('goniostatMaxOscillationSpeed', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'goniostatMinOscillationWidth':
            obj = XSDataAngle.factory()
            stackObj = SaxStackElement('goniostatMinOscillationWidth', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'minTransmission':
            obj = XSDataDouble.factory()
            stackObj = SaxStackElement('minTransmission', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'beam':
            obj = XSDataBeam.factory()
            stackObj = SaxStackElement('beam', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'detector':
            obj = XSDataDetector.factory()
            stackObj = SaxStackElement('detector', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'goniostat':
            obj = XSDataGoniostat.factory()
            stackObj = SaxStackElement('goniostat', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'selectedIndexingSolution':
            obj = XSDataIndexingSolutionSelected.factory()
            stackObj = SaxStackElement('selectedIndexingSolution', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'predictionImage':
            obj = XSDataImage.factory()
            stackObj = SaxStackElement('predictionImage', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'maxOscillationSpeed':
            obj = XSDataAngularSpeed.factory()
            stackObj = SaxStackElement('maxOscillationSpeed', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'minOscillationWidth':
            obj = XSDataAngle.factory()
            stackObj = SaxStackElement('minOscillationWidth', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'oscillationWidth':
            obj = XSDataAngle.factory()
            stackObj = SaxStackElement('oscillationWidth', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'rotationAxis':
            obj = XSDataString.factory()
            stackObj = SaxStackElement('rotationAxis', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'rotationAxisEnd':
            obj = XSDataAngle.factory()
            stackObj = SaxStackElement('rotationAxisEnd', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'rotationAxisStart':
            obj = XSDataAngle.factory()
            stackObj = SaxStackElement('rotationAxisStart', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'binPopCutOffMethod2Res':
            obj = XSDataDouble.factory()
            stackObj = SaxStackElement('binPopCutOffMethod2Res', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'goodBraggCandidates':
            obj = XSDataInteger.factory()
            stackObj = SaxStackElement('goodBraggCandidates', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'iceRings':
            obj = XSDataInteger.factory()
            stackObj = SaxStackElement('iceRings', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'image':
            obj = XSDataImage.factory()
            stackObj = SaxStackElement('image', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'inResolutionOvrlSpots':
            obj = XSDataInteger.factory()
            stackObj = SaxStackElement('inResolutionOvrlSpots', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'inResTotal':
            obj = XSDataInteger.factory()
            stackObj = SaxStackElement('inResTotal', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'maxUnitCell':
            obj = XSDataDouble.factory()
            stackObj = SaxStackElement('maxUnitCell', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'method1Res':
            obj = XSDataDouble.factory()
            stackObj = SaxStackElement('method1Res', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'method2Res':
            obj = XSDataDouble.factory()
            stackObj = SaxStackElement('method2Res', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'pctSaturationTop50Peaks':
            obj = XSDataDouble.factory()
            stackObj = SaxStackElement('pctSaturationTop50Peaks', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'spotTotal':
            obj = XSDataInteger.factory()
            stackObj = SaxStackElement('spotTotal', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'crystal':
            obj = XSDataCrystal.factory()
            stackObj = SaxStackElement('crystal', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'experimentalCondition':
            obj = XSDataExperimentalCondition.factory()
            stackObj = SaxStackElement('experimentalCondition', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'indexingLogFile':
            obj = XSDataFile.factory()
            stackObj = SaxStackElement('indexingLogFile', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'predictionResult':
            obj = XSDataGeneratePredictionResult.factory()
            stackObj = SaxStackElement('predictionResult', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'solution':
            obj = XSDataIndexingSolution.factory()
            stackObj = SaxStackElement('solution', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'selectedSolution':
            obj = XSDataIndexingSolutionSelected.factory()
            stackObj = SaxStackElement('selectedSolution', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'penalty':
            obj = XSDataFloat.factory()
            stackObj = SaxStackElement('penalty', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'experimentalConditionRefined':
            obj = XSDataExperimentalCondition.factory()
            stackObj = SaxStackElement('experimentalConditionRefined', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'mosaicityEstimation':
            obj = XSDataFloat.factory()
            stackObj = SaxStackElement('mosaicityEstimation', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'orientation':
            obj = XSDataOrientation.factory()
            stackObj = SaxStackElement('orientation', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'characterisationResult':
            obj = XSDataResultCharacterisation.factory()
            stackObj = SaxStackElement('characterisationResult', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'dataCollectionId':
            obj = XSDataInteger.factory()
            stackObj = SaxStackElement('dataCollectionId', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'bestFileContentDat':
            obj = XSDataString.factory()
            stackObj = SaxStackElement('bestFileContentDat', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'bestFileContentHKL':
            obj = XSDataString.factory()
            stackObj = SaxStackElement('bestFileContentHKL', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'bestFileContentPar':
            obj = XSDataString.factory()
            stackObj = SaxStackElement('bestFileContentPar', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'crystalRefined':
            obj = XSDataCrystal.factory()
            stackObj = SaxStackElement('crystalRefined', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'file':
            obj = XSDataFile.factory()
            stackObj = SaxStackElement('file', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'integrationSubWedgeResult':
            obj = XSDataIntegrationSubWedgeResult.factory()
            stackObj = SaxStackElement('integrationSubWedgeResult', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'bestfileDat':
            obj = XSDataString.factory()
            stackObj = SaxStackElement('bestfileDat', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'bestfileHKL':
            obj = XSDataString.factory()
            stackObj = SaxStackElement('bestfileHKL', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'bestfilePar':
            obj = XSDataString.factory()
            stackObj = SaxStackElement('bestfilePar', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'generatedMTZFile':
            obj = XSDataFile.factory()
            stackObj = SaxStackElement('generatedMTZFile', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'integrationLogFile':
            obj = XSDataFile.factory()
            stackObj = SaxStackElement('integrationLogFile', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'subWedgeNumber':
            obj = XSDataInteger.factory()
            stackObj = SaxStackElement('subWedgeNumber', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'statisticsPerResolutionBin':
            obj = XSDataStatisticsIntegrationPerResolutionBin.factory()
            stackObj = SaxStackElement('statisticsPerResolutionBin', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'numberOfLightAtoms':
            obj = XSDataFloat.factory()
            stackObj = SaxStackElement('numberOfLightAtoms', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'matrixA':
            obj = XSDataMatrixDouble.factory()
            stackObj = SaxStackElement('matrixA', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'matrixU':
            obj = XSDataMatrixDouble.factory()
            stackObj = SaxStackElement('matrixU', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'averageIntensity':
            obj = XSDataFloat.factory()
            stackObj = SaxStackElement('averageIntensity', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'averageIntensityOverAverageSigma':
            obj = XSDataFloat.factory()
            stackObj = SaxStackElement('averageIntensityOverAverageSigma', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'averageSigma':
            obj = XSDataFloat.factory()
            stackObj = SaxStackElement('averageSigma', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'chi2':
            obj = XSDataFloat.factory()
            stackObj = SaxStackElement('chi2', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'completeness':
            obj = XSDataFloat.factory()
            stackObj = SaxStackElement('completeness', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'IOverSigma':
            obj = XSDataFloat.factory()
            stackObj = SaxStackElement('IOverSigma', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'IOverSigmaChi':
            obj = XSDataFloat.factory()
            stackObj = SaxStackElement('IOverSigmaChi', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'maxResolution':
            obj = XSDataFloat.factory()
            stackObj = SaxStackElement('maxResolution', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'minResolution':
            obj = XSDataFloat.factory()
            stackObj = SaxStackElement('minResolution', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'percentageOverload':
            obj = XSDataFloat.factory()
            stackObj = SaxStackElement('percentageOverload', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'redundancy':
            obj = XSDataFloat.factory()
            stackObj = SaxStackElement('redundancy', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'rFactor':
            obj = XSDataFloat.factory()
            stackObj = SaxStackElement('rFactor', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'rFriedel':
            obj = XSDataFloat.factory()
            stackObj = SaxStackElement('rFriedel', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'imageQualityIndicators':
            obj = XSDataImageQualityIndicators.factory()
            stackObj = SaxStackElement('imageQualityIndicators', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'shortSummary':
            obj = XSDataString.factory()
            stackObj = SaxStackElement('shortSummary', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'statusMessage':
            obj = XSDataString.factory()
            stackObj = SaxStackElement('statusMessage', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'bFactor':
            obj = XSDataDouble.factory()
            stackObj = SaxStackElement('bFactor', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'scale':
            obj = XSDataDouble.factory()
            stackObj = SaxStackElement('scale', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'bestLogFile':
            obj = XSDataFile.factory()
            stackObj = SaxStackElement('bestLogFile', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'raddoseLogFile':
            obj = XSDataFile.factory()
            stackObj = SaxStackElement('raddoseLogFile', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'collectionPlan':
            obj = XSDataCollectionPlan.factory()
            stackObj = SaxStackElement('collectionPlan', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'absorbedDoseRate':
            obj = XSDataAbsorbedDoseRate.factory()
            stackObj = SaxStackElement('absorbedDoseRate', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'susceptibility':
            obj = XSDataFloat.factory()
            stackObj = SaxStackElement('susceptibility', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'chemicalComposition':
            obj = XSDataChemicalCompositionMM.factory()
            stackObj = SaxStackElement('chemicalComposition', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'atoms':
            obj = XSDataAtomicComposition.factory()
            stackObj = SaxStackElement('atoms', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'ITNumber':
            obj = XSDataInteger.factory()
            stackObj = SaxStackElement('ITNumber', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'beamPositionShiftX':
            obj = XSDataLength.factory()
            stackObj = SaxStackElement('beamPositionShiftX', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'beamPositionShiftY':
            obj = XSDataLength.factory()
            stackObj = SaxStackElement('beamPositionShiftY', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'spotDeviationAngular':
            obj = XSDataAngle.factory()
            stackObj = SaxStackElement('spotDeviationAngular', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'spotDeviationPositional':
            obj = XSDataLength.factory()
            stackObj = SaxStackElement('spotDeviationPositional', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'spotsTotal':
            obj = XSDataInteger.factory()
            stackObj = SaxStackElement('spotsTotal', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'spotsUsed':
            obj = XSDataInteger.factory()
            stackObj = SaxStackElement('spotsUsed', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'iOverSigmaAtHighestResolution':
            obj = XSDataDouble.factory()
            stackObj = SaxStackElement('iOverSigmaAtHighestResolution', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'iOverSigmaOverall':
            obj = XSDataDouble.factory()
            stackObj = SaxStackElement('iOverSigmaOverall', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'numberOfBadReflections':
            obj = XSDataInteger.factory()
            stackObj = SaxStackElement('numberOfBadReflections', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'numberOfFullyRecordedReflections':
            obj = XSDataInteger.factory()
            stackObj = SaxStackElement('numberOfFullyRecordedReflections', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'numberOfNegativeReflections':
            obj = XSDataInteger.factory()
            stackObj = SaxStackElement('numberOfNegativeReflections', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'numberOfOverlappedReflections':
            obj = XSDataInteger.factory()
            stackObj = SaxStackElement('numberOfOverlappedReflections', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'numberOfPartialReflections':
            obj = XSDataInteger.factory()
            stackObj = SaxStackElement('numberOfPartialReflections', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'numberOfReflectionsGenerated':
            obj = XSDataInteger.factory()
            stackObj = SaxStackElement('numberOfReflectionsGenerated', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'RMSSpotDeviation':
            obj = XSDataLength.factory()
            stackObj = SaxStackElement('RMSSpotDeviation', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'averageIOverSigma':
            obj = XSDataDouble.factory()
            stackObj = SaxStackElement('averageIOverSigma', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'numberOfReflections':
            obj = XSDataInteger.factory()
            stackObj = SaxStackElement('numberOfReflections', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'fullyRecorded':
            obj = XSDataStatisticsIntegrationAverageAndNumberOfReflections.factory()
            stackObj = SaxStackElement('fullyRecorded', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'partials':
            obj = XSDataStatisticsIntegrationAverageAndNumberOfReflections.factory()
            stackObj = SaxStackElement('partials', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'profileFitted':
            obj = XSDataStatisticsIntegrationPerReflectionType.factory()
            stackObj = SaxStackElement('profileFitted', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'summation':
            obj = XSDataStatisticsIntegrationPerReflectionType.factory()
            stackObj = SaxStackElement('summation', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'resolutionBin':
            obj = XSDataResolutionBin.factory()
            stackObj = SaxStackElement('resolutionBin', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'attenuation':
            obj = XSDataFloat.factory()
            stackObj = SaxStackElement('attenuation', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'iSigma':
            obj = XSDataFloat.factory()
            stackObj = SaxStackElement('iSigma', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'rankingResolution':
            obj = XSDataFloat.factory()
            stackObj = SaxStackElement('rankingResolution', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'resolution':
            obj = XSDataFloat.factory()
            stackObj = SaxStackElement('resolution', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'resolutionReasoning':
            obj = XSDataString.factory()
            stackObj = SaxStackElement('resolutionReasoning', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'totalDataCollectionTime':
            obj = XSDataTime.factory()
            stackObj = SaxStackElement('totalDataCollectionTime', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'totalExposureTime':
            obj = XSDataTime.factory()
            stackObj = SaxStackElement('totalExposureTime', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'numberOfCopiesInAsymmetricUnit':
            obj = XSDataFloat.factory()
            stackObj = SaxStackElement('numberOfCopiesInAsymmetricUnit', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'chain':
            obj = XSDataChain.factory()
            stackObj = SaxStackElement('chain', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'ligand':
            obj = XSDataLigand.factory()
            stackObj = SaxStackElement('ligand', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'action':
            obj = XSDataString.factory()
            stackObj = SaxStackElement('action', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'imagePath':
            obj = XSDataFile.factory()
            stackObj = SaxStackElement('imagePath', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'beamSize':
            obj = XSDataLength.factory()
            stackObj = SaxStackElement('beamSize', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'beamSizeX':
            obj = XSDataLength.factory()
            stackObj = SaxStackElement('beamSizeX', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'beamSizeY':
            obj = XSDataLength.factory()
            stackObj = SaxStackElement('beamSizeY', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'templateMode':
            obj = XSDataBoolean.factory()
            stackObj = SaxStackElement('templateMode', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'generatedTemplateFile':
            obj = XSDataFile.factory()
            stackObj = SaxStackElement('generatedTemplateFile', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'resultsFilePath':
            obj = XSDataFile.factory()
            stackObj = SaxStackElement('resultsFilePath', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'beamPosX':
            obj = XSDataFloat.factory()
            stackObj = SaxStackElement('beamPosX', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'beamPosY':
            obj = XSDataFloat.factory()
            stackObj = SaxStackElement('beamPosY', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'shortComments':
            obj = XSDataString.factory()
            stackObj = SaxStackElement('shortComments', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'comments':
            obj = XSDataString.factory()
            stackObj = SaxStackElement('comments', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'inputCharacterisation':
            obj = XSDataInputCharacterisation.factory()
            stackObj = SaxStackElement('inputCharacterisation', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'resultCharacterisation':
            obj = XSDataResultCharacterisation.factory()
            stackObj = SaxStackElement('resultCharacterisation', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'resultControlISPyB':
            obj = XSDataResultControlISPyB.factory()
            stackObj = SaxStackElement('resultControlISPyB', obj)
            self.stack.append(stackObj)
            done = 1
        if not done:
            self.reportError('"%s" element not allowed here.' % name)

    def endElement(self, name):
        done = 0
        if name == 'XSConfiguration':
            if len(self.stack) == 1:
                self.root = self.stack[-1].obj
                self.stack.pop()
                done = 1
        elif name == 'XSPluginList':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setXSPluginList(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'shape':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                if content:
                    try:
                        content = int(content)
                    except:
                        self.reportError('"shape" must be integer -- content: %s' % content)
                else:
                    content = -1
                self.stack[-2].obj.addShape(content)
                self.stack.pop()
                done = 1
        elif name == 'size':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                if content:
                    try:
                        content = int(content)
                    except:
                        self.reportError('"size" must be integer -- content: %s' % content)
                else:
                    content = -1
                self.stack[-2].obj.setSize(content)
                self.stack.pop()
                done = 1
        elif name == 'dtype':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                self.stack[-2].obj.setDtype(content)
                self.stack.pop()
                done = 1
        elif name == 'data':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                self.stack[-2].obj.setData(content)
                self.stack.pop()
                done = 1
        elif name == 'coding':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setCoding(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'md5sum':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setMd5sum(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'value':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                if content and content in ('true', '1'):
                    content = 1
                else:
                    content = 0
                self.stack[-2].obj.setValue(content)
                self.stack.pop()
                done = 1
        elif name == 'keyValuePair':
            if len(self.stack) >= 2:
                self.stack[-2].obj.addKeyValuePair(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'unit':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setUnit(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'error':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setError(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'baseDirectory':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setBaseDirectory(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'executionTime':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setExecutionTime(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'pluginName':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setPluginName(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'startOfExecution':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setStartOfExecution(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'systeminfo':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setSysteminfo(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'workingDirectory':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setWorkingDirectory(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'configuration':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setConfiguration(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'path':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setPath(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'date':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setDate(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'number':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setNumber(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'key':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setKey(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'm11':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                if content:
                    try:
                        content = float(content)
                    except:
                        self.reportError('"m11" must be float -- content: %s' % content)
                else:
                    content = -1
                self.stack[-2].obj.setM11(content)
                self.stack.pop()
                done = 1
        elif name == 'm12':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                if content:
                    try:
                        content = float(content)
                    except:
                        self.reportError('"m12" must be float -- content: %s' % content)
                else:
                    content = -1
                self.stack[-2].obj.setM12(content)
                self.stack.pop()
                done = 1
        elif name == 'm13':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                if content:
                    try:
                        content = float(content)
                    except:
                        self.reportError('"m13" must be float -- content: %s' % content)
                else:
                    content = -1
                self.stack[-2].obj.setM13(content)
                self.stack.pop()
                done = 1
        elif name == 'm21':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                if content:
                    try:
                        content = float(content)
                    except:
                        self.reportError('"m21" must be float -- content: %s' % content)
                else:
                    content = -1
                self.stack[-2].obj.setM21(content)
                self.stack.pop()
                done = 1
        elif name == 'm22':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                if content:
                    try:
                        content = float(content)
                    except:
                        self.reportError('"m22" must be float -- content: %s' % content)
                else:
                    content = -1
                self.stack[-2].obj.setM22(content)
                self.stack.pop()
                done = 1
        elif name == 'm23':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                if content:
                    try:
                        content = float(content)
                    except:
                        self.reportError('"m23" must be float -- content: %s' % content)
                else:
                    content = -1
                self.stack[-2].obj.setM23(content)
                self.stack.pop()
                done = 1
        elif name == 'm31':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                if content:
                    try:
                        content = float(content)
                    except:
                        self.reportError('"m31" must be float -- content: %s' % content)
                else:
                    content = -1
                self.stack[-2].obj.setM31(content)
                self.stack.pop()
                done = 1
        elif name == 'm32':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                if content:
                    try:
                        content = float(content)
                    except:
                        self.reportError('"m32" must be float -- content: %s' % content)
                else:
                    content = -1
                self.stack[-2].obj.setM32(content)
                self.stack.pop()
                done = 1
        elif name == 'm33':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                if content:
                    try:
                        content = float(content)
                    except:
                        self.reportError('"m33" must be float -- content: %s' % content)
                else:
                    content = -1
                self.stack[-2].obj.setM33(content)
                self.stack.pop()
                done = 1
        elif name == 'debuginfo':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setDebuginfo(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'level':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setLevel(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'text':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setText(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'type':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setType(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'q0':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                if content:
                    try:
                        content = float(content)
                    except:
                        self.reportError('"q0" must be float -- content: %s' % content)
                else:
                    content = -1
                self.stack[-2].obj.setQ0(content)
                self.stack.pop()
                done = 1
        elif name == 'q1':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                if content:
                    try:
                        content = float(content)
                    except:
                        self.reportError('"q1" must be float -- content: %s' % content)
                else:
                    content = -1
                self.stack[-2].obj.setQ1(content)
                self.stack.pop()
                done = 1
        elif name == 'q2':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                if content:
                    try:
                        content = float(content)
                    except:
                        self.reportError('"q2" must be float -- content: %s' % content)
                else:
                    content = -1
                self.stack[-2].obj.setQ2(content)
                self.stack.pop()
                done = 1
        elif name == 'q3':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                if content:
                    try:
                        content = float(content)
                    except:
                        self.reportError('"q3" must be float -- content: %s' % content)
                else:
                    content = -1
                self.stack[-2].obj.setQ3(content)
                self.stack.pop()
                done = 1
        elif name == 'x':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setX(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'y':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setY(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'z':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setZ(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'executiveSummary':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setExecutiveSummary(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'isSuccess':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setIsSuccess(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'executionInfo':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setExecutionInfo(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'compiler':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setCompiler(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'hostIP':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setHostIP(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'hostName':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setHostName(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'operatingSystem':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setOperatingSystem(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'operatingSystemType':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setOperatingSystemType(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'userName':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setUserName(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'virtualMachine':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setVirtualMachine(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'v1':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                if content:
                    try:
                        content = float(content)
                    except:
                        self.reportError('"v1" must be float -- content: %s' % content)
                else:
                    content = -1
                self.stack[-2].obj.setV1(content)
                self.stack.pop()
                done = 1
        elif name == 'v2':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                if content:
                    try:
                        content = float(content)
                    except:
                        self.reportError('"v2" must be float -- content: %s' % content)
                else:
                    content = -1
                self.stack[-2].obj.setV2(content)
                self.stack.pop()
                done = 1
        elif name == 'v3':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                if content:
                    try:
                        content = float(content)
                    except:
                        self.reportError('"v3" must be float -- content: %s' % content)
                else:
                    content = -1
                self.stack[-2].obj.setV3(content)
                self.stack.pop()
                done = 1
        elif name == 'enabled':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                if content and content in ('true', '1'):
                    content = 1
                else:
                    content = 0
                self.stack[-2].obj.setEnabled(content)
                self.stack.pop()
                done = 1
        elif name == 'name':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                self.stack[-2].obj.setName(content)
                self.stack.pop()
                done = 1
        elif name == 'XSOptionItem':
            if len(self.stack) >= 2:
                self.stack[-2].obj.addXSOptionItem(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'XSParamItem':
            if len(self.stack) >= 2:
                self.stack[-2].obj.addXSParamItem(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'XSParamList':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setXSParamList(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'XSOptionList':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setXSOptionList(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'XSPluginItem':
            if len(self.stack) >= 2:
                self.stack[-2].obj.addXSPluginItem(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'concentration':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setConcentration(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'numberOf':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setNumberOf(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'symbol':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setSymbol(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'atom':
            if len(self.stack) >= 2:
                self.stack[-2].obj.addAtom(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'exposureTime':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setExposureTime(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'flux':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setFlux(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'minExposureTimePerImage':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setMinExposureTimePerImage(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'transmission':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setTransmission(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'wavelength':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setWavelength(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'angle_alpha':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setAngle_alpha(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'angle_beta':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setAngle_beta(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'angle_gamma':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setAngle_gamma(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'length_a':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setLength_a(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'length_b':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setLength_b(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'length_c':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setLength_c(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'numberOfCopies':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setNumberOfCopies(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'numberOfMonomers':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setNumberOfMonomers(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'heavyAtoms':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setHeavyAtoms(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'dataCollection':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setDataCollection(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'indexingResult':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setIndexingResult(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'integrationResult':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setIntegrationResult(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'strategyResult':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setStrategyResult(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'solvent':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setSolvent(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'structure':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setStructure(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'diffractionPlan':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setDiffractionPlan(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'sample':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setSample(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'subWedge':
            if len(self.stack) >= 2:
                self.stack[-2].obj.addSubWedge(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'collectionPlanNumber':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setCollectionPlanNumber(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'collectionStrategy':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setCollectionStrategy(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'comment':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setComment(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'strategySummary':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setStrategySummary(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'statistics':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setStatistics(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'mosaicity':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setMosaicity(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'spaceGroup':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setSpaceGroup(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'cell':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setCell(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'beamPositionX':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setBeamPositionX(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'beamPositionY':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setBeamPositionY(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'bin':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setBin(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'byteOrder':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setByteOrder(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'dataType':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setDataType(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'distance':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setDistance(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'gain':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setGain(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'imageSaturation':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setImageSaturation(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'numberBytesInHeader':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setNumberBytesInHeader(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'numberPixelX':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setNumberPixelX(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'numberPixelY':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setNumberPixelY(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'pixelSizeX':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setPixelSizeX(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'pixelSizeY':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setPixelSizeY(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'serialNumber':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setSerialNumber(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'twoTheta':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setTwoTheta(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'aimedCompleteness':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setAimedCompleteness(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'aimedIOverSigmaAtHighestResolution':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setAimedIOverSigmaAtHighestResolution(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'aimedMultiplicity':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setAimedMultiplicity(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'aimedResolution':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setAimedResolution(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'anomalousData':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setAnomalousData(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'complexity':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setComplexity(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'detectorMaxResolution':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setDetectorMaxResolution(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'detectorMinResolution':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setDetectorMinResolution(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'estimateRadiationDamage':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setEstimateRadiationDamage(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'forcedSpaceGroup':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setForcedSpaceGroup(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'maxExposureTimePerDataCollection':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setMaxExposureTimePerDataCollection(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'requiredCompleteness':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setRequiredCompleteness(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'requiredMultiplicity':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setRequiredMultiplicity(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'requiredResolution':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setRequiredResolution(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'strategyOption':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setStrategyOption(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'goniostatMaxOscillationSpeed':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setGoniostatMaxOscillationSpeed(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'goniostatMinOscillationWidth':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setGoniostatMinOscillationWidth(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'minTransmission':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setMinTransmission(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'beam':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setBeam(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'detector':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setDetector(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'goniostat':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setGoniostat(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'selectedIndexingSolution':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setSelectedIndexingSolution(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'predictionImage':
            if len(self.stack) >= 2:
                self.stack[-2].obj.addPredictionImage(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'maxOscillationSpeed':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setMaxOscillationSpeed(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'minOscillationWidth':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setMinOscillationWidth(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'oscillationWidth':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setOscillationWidth(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'rotationAxis':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setRotationAxis(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'rotationAxisEnd':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setRotationAxisEnd(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'rotationAxisStart':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setRotationAxisStart(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'binPopCutOffMethod2Res':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setBinPopCutOffMethod2Res(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'goodBraggCandidates':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setGoodBraggCandidates(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'iceRings':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setIceRings(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'image':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setImage(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'inResolutionOvrlSpots':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setInResolutionOvrlSpots(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'inResTotal':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setInResTotal(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'maxUnitCell':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setMaxUnitCell(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'method1Res':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setMethod1Res(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'method2Res':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setMethod2Res(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'pctSaturationTop50Peaks':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setPctSaturationTop50Peaks(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'spotTotal':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setSpotTotal(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'crystal':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setCrystal(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'experimentalCondition':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setExperimentalCondition(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'indexingLogFile':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setIndexingLogFile(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'predictionResult':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setPredictionResult(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'solution':
            if len(self.stack) >= 2:
                self.stack[-2].obj.addSolution(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'selectedSolution':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setSelectedSolution(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'penalty':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setPenalty(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'experimentalConditionRefined':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setExperimentalConditionRefined(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'mosaicityEstimation':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setMosaicityEstimation(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'orientation':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setOrientation(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'characterisationResult':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setCharacterisationResult(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'dataCollectionId':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setDataCollectionId(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'bestFileContentDat':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setBestFileContentDat(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'bestFileContentHKL':
            if len(self.stack) >= 2:
                self.stack[-2].obj.addBestFileContentHKL(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'bestFileContentPar':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setBestFileContentPar(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'crystalRefined':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setCrystalRefined(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'file':
            if len(self.stack) >= 2:
                self.stack[-2].obj.addFile(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'integrationSubWedgeResult':
            if len(self.stack) >= 2:
                self.stack[-2].obj.addIntegrationSubWedgeResult(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'bestfileDat':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setBestfileDat(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'bestfileHKL':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setBestfileHKL(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'bestfilePar':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setBestfilePar(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'generatedMTZFile':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setGeneratedMTZFile(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'integrationLogFile':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setIntegrationLogFile(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'subWedgeNumber':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setSubWedgeNumber(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'statisticsPerResolutionBin':
            if len(self.stack) >= 2:
                self.stack[-2].obj.addStatisticsPerResolutionBin(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'numberOfLightAtoms':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setNumberOfLightAtoms(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'matrixA':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setMatrixA(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'matrixU':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setMatrixU(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'averageIntensity':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setAverageIntensity(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'averageIntensityOverAverageSigma':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setAverageIntensityOverAverageSigma(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'averageSigma':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setAverageSigma(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'chi2':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setChi2(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'completeness':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setCompleteness(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'IOverSigma':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setIOverSigma(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'IOverSigmaChi':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setIOverSigmaChi(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'maxResolution':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setMaxResolution(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'minResolution':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setMinResolution(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'percentageOverload':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setPercentageOverload(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'redundancy':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setRedundancy(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'rFactor':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setRFactor(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'rFriedel':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setRFriedel(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'imageQualityIndicators':
            if len(self.stack) >= 2:
                self.stack[-2].obj.addImageQualityIndicators(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'shortSummary':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setShortSummary(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'statusMessage':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setStatusMessage(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'bFactor':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setBFactor(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'scale':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setScale(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'bestLogFile':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setBestLogFile(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'raddoseLogFile':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setRaddoseLogFile(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'collectionPlan':
            if len(self.stack) >= 2:
                self.stack[-2].obj.addCollectionPlan(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'absorbedDoseRate':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setAbsorbedDoseRate(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'susceptibility':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setSusceptibility(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'chemicalComposition':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setChemicalComposition(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'atoms':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setAtoms(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'ITNumber':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setITNumber(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'beamPositionShiftX':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setBeamPositionShiftX(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'beamPositionShiftY':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setBeamPositionShiftY(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'spotDeviationAngular':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setSpotDeviationAngular(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'spotDeviationPositional':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setSpotDeviationPositional(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'spotsTotal':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setSpotsTotal(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'spotsUsed':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setSpotsUsed(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'iOverSigmaAtHighestResolution':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setIOverSigmaAtHighestResolution(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'iOverSigmaOverall':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setIOverSigmaOverall(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'numberOfBadReflections':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setNumberOfBadReflections(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'numberOfFullyRecordedReflections':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setNumberOfFullyRecordedReflections(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'numberOfNegativeReflections':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setNumberOfNegativeReflections(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'numberOfOverlappedReflections':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setNumberOfOverlappedReflections(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'numberOfPartialReflections':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setNumberOfPartialReflections(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'numberOfReflectionsGenerated':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setNumberOfReflectionsGenerated(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'RMSSpotDeviation':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setRMSSpotDeviation(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'averageIOverSigma':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setAverageIOverSigma(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'numberOfReflections':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setNumberOfReflections(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'fullyRecorded':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setFullyRecorded(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'partials':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setPartials(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'profileFitted':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setProfileFitted(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'summation':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setSummation(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'resolutionBin':
            if len(self.stack) >= 2:
                self.stack[-2].obj.addResolutionBin(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'attenuation':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setAttenuation(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'iSigma':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setISigma(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'rankingResolution':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setRankingResolution(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'resolution':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setResolution(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'resolutionReasoning':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setResolutionReasoning(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'totalDataCollectionTime':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setTotalDataCollectionTime(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'totalExposureTime':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setTotalExposureTime(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'numberOfCopiesInAsymmetricUnit':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setNumberOfCopiesInAsymmetricUnit(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'chain':
            if len(self.stack) >= 2:
                self.stack[-2].obj.addChain(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'ligand':
            if len(self.stack) >= 2:
                self.stack[-2].obj.addLigand(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'action':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setAction(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'imagePath':
            if len(self.stack) >= 2:
                self.stack[-2].obj.addImagePath(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'beamSize':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setBeamSize(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'beamSizeX':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setBeamSizeX(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'beamSizeY':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setBeamSizeY(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'templateMode':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setTemplateMode(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'generatedTemplateFile':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setGeneratedTemplateFile(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'resultsFilePath':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setResultsFilePath(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'beamPosX':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setBeamPosX(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'beamPosY':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setBeamPosY(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'shortComments':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setShortComments(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'comments':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setComments(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'inputCharacterisation':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setInputCharacterisation(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'resultCharacterisation':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setResultCharacterisation(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'resultControlISPyB':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setResultControlISPyB(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        if not done:
            self.reportError('"%s" element not allowed here.' % name)

    def characters(self, chrs, start, end):
        if len(self.stack) > 0:
            self.stack[-1].content += chrs[start:end]

    def reportError(self, mesg):
        locator = self.locator
        sys.stderr.write('Doc: %s  Line: %d  Column: %d\n' % \
            (locator.getSystemId(), locator.getLineNumber(), 
            locator.getColumnNumber() + 1))
        sys.stderr.write(mesg)
        sys.stderr.write('\n')
        sys.exit(-1)
        #raise RuntimeError

USAGE_TEXT = """
Usage: python <Parser>.py [ -s ] <in_xml_file>
Options:
    -s        Use the SAX parser, not the minidom parser.
"""

def usage():
    print USAGE_TEXT
    sys.exit(-1)


#
# SAX handler used to determine the top level element.
#
class SaxSelectorHandler(handler.ContentHandler):
    def __init__(self):
        self.topElementName = None
    def getTopElementName(self):
        return self.topElementName
    def startElement(self, name, attrs):
        self.topElementName = name
        raise StopIteration


def parseSelect(inFileName):
    infile = file(inFileName, 'r')
    topElementName = None
    parser = make_parser()
    documentHandler = SaxSelectorHandler()
    parser.setContentHandler(documentHandler)
    try:
        try:
            parser.parse(infile)
        except StopIteration:
            topElementName = documentHandler.getTopElementName()
        if topElementName is None:
            raise RuntimeError, 'no top level element'
        topElementName = topElementName.replace('-', '_').replace(':', '_')
        if topElementName not in globals():
            raise RuntimeError, 'no class for top element: %s' % topElementName
        topElement = globals()[topElementName]
        infile.seek(0)
        doc = minidom.parse(infile)
    finally:
        infile.close()
    rootNode = doc.childNodes[0]
    rootObj = topElement.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
    sys.stdout.write('<?xml version="1.0" ?>\n')
    rootObj.export(sys.stdout, 0)
    return rootObj


def saxParse(inFileName):
    parser = make_parser()
    documentHandler = SaxXSConfigurationHandler()
    parser.setDocumentHandler(documentHandler)
    parser.parse('file:%s' % inFileName)
    root = documentHandler.getRoot()
    sys.stdout.write('<?xml version="1.0" ?>\n')
    root.export(sys.stdout, 0)
    return root


def saxParseString(inString):
    parser = make_parser()
    documentHandler = SaxXSConfigurationHandler()
    parser.setDocumentHandler(documentHandler)
    parser.feed(inString)
    parser.close()
    rootObj = documentHandler.getRoot()
    #sys.stdout.write('<?xml version="1.0" ?>\n')
    #rootObj.export(sys.stdout, 0)
    return rootObj


def parse(inFileName):
    doc = minidom.parse(inFileName)
    rootNode = doc.documentElement
    rootObj = XSConfiguration.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
    sys.stdout.write('<?xml version="1.0" ?>\n')
    rootObj.export(sys.stdout, 0, name_="XSConfiguration")
    return rootObj


def parseString(inString):
    doc = minidom.parseString(inString)
    rootNode = doc.documentElement
    rootObj = XSConfiguration.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
    sys.stdout.write('<?xml version="1.0" ?>\n')
    rootObj.export(sys.stdout, 0, name_="XSConfiguration")
    return rootObj


def parseLiteral(inFileName):
    doc = minidom.parse(inFileName)
    rootNode = doc.documentElement
    rootObj = XSConfiguration.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
    sys.stdout.write('from XSDataInterfacev1_2 import *\n\n')
    sys.stdout.write('rootObj = XSConfiguration(\n')
    rootObj.exportLiteral(sys.stdout, 0, name_="XSConfiguration")
    sys.stdout.write(')\n')
    return rootObj

class XSDataInterfacev1_2:
    pass


def main():
    args = sys.argv[1:]
    if len(args) == 2 and args[0] == '-s':
        saxParse(args[1])
    elif len(args) == 1:
        parse(args[0])
    else:
        usage()


if __name__ == '__main__':
    main()
    #import pdb
    #pdb.run('main()')

