# -*- coding: utf-8 -*-

###########################################################################################
#
# Author: astips (animator.well)
#
# Date: 2012.06
#
# Url: https://github.com/astips
#
# Description: Magic Asset Node - Control Asset Informations
#     
###########################################################################################
import sys
import maya.OpenMaya as OpenMaya
import maya.OpenMayaMPx as OpenMayaMPx
import AEmagicAssetTemplate


nodeName = 'magicAsset'
nodeId = OpenMaya.MTypeId(0x101113)
TransformMatrixID = OpenMaya.MTypeId(0x101114)


class magicAssetNode(OpenMayaMPx.MPxTransform) :
    
    project = OpenMaya.MObject()
    branch = OpenMaya.MObject()    
        
    assetType = OpenMaya.MObject()
    assetName = OpenMaya.MObject()
    assetState = OpenMaya.MObject()
    assetVersion = OpenMaya.MObject()
    assetBranch = OpenMaya.MObject()
    
    createdBy = OpenMaya.MObject()
    creationDate = OpenMaya.MObject()
    creationTime = OpenMaya.MObject()
    lastEditBy = OpenMaya.MObject()
    lastEditDate = OpenMaya.MObject()
    lastEditTime = OpenMaya.MObject()
        
    alembicGeo = OpenMaya.MObject()
    
    customTag = OpenMaya.MObject()
    meta = OpenMaya.MObject()
    description = OpenMaya.MObject()
    
    referenceId = OpenMaya.MObject()

    # deformShape = OpenMaya.MObject()

    def __init__(self) :
        OpenMayaMPx.MPxTransform.__init__(self)
        
    def postConstructor(self) :
        this_object = self.thisMObject()
        depNodeFn = OpenMaya.MFnDependencyNode(this_object)
        channelAttributes = ["translateX", 
                             "translateY", 
                             "translateZ", 
                             "rotateX", 
                             "rotateY", 
                             "rotateZ", 
                             "scaleX", 
                             "scaleY", 
                             "scaleZ", 
                             "visibility"
                             ]
        
        for attribute in channelAttributes :
            attrObject = depNodeFn.attribute(attribute)
            plug = OpenMaya.MPlug(this_object, attrObject)
            plug.setLocked(False)
            plug.setChannelBox(True)
            plug.setKeyable(True)

        hiddenAttributes = ["shearXY", 
                            "shearXZ", 
                            "shearYZ", 
                            "rotateOrder", 
                            "rotateAxisX", 
                            "rotateAxisY", 
                            "rotateAxisZ"
                            ]    
        for attribute in hiddenAttributes :
            attrObject = depNodeFn.attribute(attribute)
            plug = OpenMaya.MPlug(this_object, attrObject)
            plug.setLocked(False)
            plug.setChannelBox(False)
            plug.setKeyable(False)
                
def nodeCreator() :
    return OpenMayaMPx.asMPxPtr( magicAssetNode() )

def nodeInit() :
    # attribute provide
    nAttr = OpenMaya.MFnNumericAttribute()
    tAttr = OpenMaya.MFnTypedAttribute()
    bAttr = OpenMaya.MFnNumericAttribute()
    eAttr = OpenMaya.MFnEnumAttribute()
    mAttr = OpenMaya.MFnMessageAttribute()

    # attribute project
    stringData = OpenMaya.MFnStringData().create('project')
    magicAssetNode.project = tAttr.create('project', 'pjt', OpenMaya.MFnData.kString, stringData)    
    tAttr.setStorable(True)
    tAttr.setHidden(False)
    tAttr.setKeyable(False)
    
    # attribute branch
    stringData = OpenMaya.MFnStringData().create('')
    magicAssetNode.branch = tAttr.create('branch', 'brh', OpenMaya.MFnData.kString, stringData)    
    tAttr.setStorable(True)
    tAttr.setHidden(False)
    tAttr.setKeyable(False)
    
    # attribute type
    magicAssetNode.assetType = eAttr.create('assetType', 'type', 0)    
    eAttr.addField("stage", 0)
    eAttr.addField("character", 1)
    eAttr.addField("prop", 2)
    eAttr.addField("camera", 3)
    
    eAttr.setReadable(True)
    eAttr.setStorable(True)
    eAttr.setHidden(False)
    eAttr.setKeyable(False)
    
    # attribute assetName
    stringData = OpenMaya.MFnStringData().create('assetName')
    magicAssetNode.assetName = tAttr.create("assetName", "name", OpenMaya.MFnData.kString, stringData)    
    tAttr.setStorable(True)
    tAttr.setHidden(False)
    tAttr.setKeyable(False)
    
    # attribute assetState
    magicAssetNode.assetState = eAttr.create('assetState', 'state', 0)    
    eAttr.addField('modeling', 0)
    eAttr.addField('shading', 1)
    eAttr.addField('rigging', 2)
    
    eAttr.setReadable(True)
    eAttr.setStorable(True)
    eAttr.setHidden(False)
    eAttr.setKeyable(False)
    
    # attribute assetVersion        
    magicAssetNode.assetVersion = nAttr.create('assetVersion', 'version', OpenMaya.MFnNumericData.kInt, 1)
    nAttr.setStorable(True)
    nAttr.setReadable(True)
    nAttr.setKeyable(False)
    nAttr.setHidden(False)
    
    # attribute assetBranch        
    magicAssetNode.assetBranch = nAttr.create('assetBranch', 'aBch', OpenMaya.MFnNumericData.kInt, 0)
    nAttr.setStorable(True)
    nAttr.setReadable(True)
    nAttr.setKeyable(False)
    nAttr.setHidden(False)
    
    # attribute customTag
    stringData = OpenMaya.MFnStringData().create('')
    magicAssetNode.customTag = tAttr.create("customTag", "ctg", OpenMaya.MFnData.kString, stringData)    
    tAttr.setStorable(True)
    tAttr.setHidden(False)
    tAttr.setKeyable(False)
    
    # attribute customTag
    stringData = OpenMaya.MFnStringData().create('')
    magicAssetNode.meta = tAttr.create("metaData", "meta", OpenMaya.MFnData.kString, stringData)    
    tAttr.setStorable(True)
    tAttr.setHidden(False)
    tAttr.setKeyable(False)
    
    # attribute description
    stringData = OpenMaya.MFnStringData().create('')
    magicAssetNode.description = tAttr.create("description", "descrip", OpenMaya.MFnData.kString, stringData)    
    tAttr.setStorable(True)
    tAttr.setHidden(False)
    tAttr.setKeyable(False)
    
    # attribute alembicGeo    
    magicAssetNode.alembicGeo = mAttr.create('alembicGeo','abcGeo')
    mAttr.setWritable(True)
    mAttr.setStorable(True)
    mAttr.setKeyable(False)
    mAttr.setHidden(False)
    mAttr.setReadable(False)
    mAttr.setArray(True)
    mAttr.setIndexMatters(False)
    
    # attribute referenceId        
    magicAssetNode.referenceId = nAttr.create('referenceId', 'refId', OpenMaya.MFnNumericData.kInt, 1)
    nAttr.setStorable(True)
    nAttr.setReadable(True)
    nAttr.setKeyable(False)
    nAttr.setHidden(False)
    
    """
    # attribute deformShape    
    magicAssetNode.deformShape = nAttr.create('deformShape','defShape',OpenMaya.MFnNumericData.kBoolean,1)
    nAttr.setStorable(1)
    """
    
    # attribute createdBy 
    stringData = OpenMaya.MFnStringData().create('createdBy')
    magicAssetNode.createdBy = tAttr.create("createdBy", "crb", OpenMaya.MFnData.kString, stringData)
    tAttr.setStorable(True)
    tAttr.setHidden(False)
    tAttr.setKeyable(False)
    
    # attribute creationDate 
    magicAssetNode.creationDate = nAttr.create("createDate", "cdt", OpenMaya.MFnNumericData.k3Int, 1)
    nAttr.setStorable(True)
    nAttr.setReadable(True)
    nAttr.setKeyable(False)
    nAttr.setHidden(False)    

    # attribute creationTime 
    magicAssetNode.creationTime = nAttr.create("createTime", "crt", OpenMaya.MFnNumericData.k3Int, 1)
    nAttr.setStorable(True)
    nAttr.setReadable(True)
    nAttr.setKeyable(False)
    nAttr.setHidden(False)
    
    # attribute lastEditBy 
    stringData = OpenMaya.MFnStringData().create('lastEditBy')
    magicAssetNode.lastEditBy = tAttr.create("lastEditBy", "leb", OpenMaya.MFnData.kString, stringData)
    tAttr.setStorable(True)
    tAttr.setHidden(False)
    tAttr.setKeyable(False)    
    
    # attribute lastEditDate 
    magicAssetNode.lastEditDate = nAttr.create("lastEditDate", "led", OpenMaya.MFnNumericData.k3Int, 1)
    nAttr.setStorable(True)
    nAttr.setReadable(True)
    nAttr.setKeyable(False)
    nAttr.setHidden(False)
            
    # attribute lastEditTime 
    magicAssetNode.lastEditTime = nAttr.create("lastEditTime", "let", OpenMaya.MFnNumericData.k3Int, 1)
    nAttr.setStorable(True)
    nAttr.setReadable(True)
    nAttr.setKeyable(False)
    nAttr.setHidden(False)    
          
    # create all attributes
    magicAssetNode.addAttribute(magicAssetNode.project)
    magicAssetNode.addAttribute(magicAssetNode.branch)
    
    magicAssetNode.addAttribute(magicAssetNode.assetType)
    magicAssetNode.addAttribute(magicAssetNode.assetName)
    magicAssetNode.addAttribute(magicAssetNode.assetState)
    magicAssetNode.addAttribute(magicAssetNode.assetVersion)
    magicAssetNode.addAttribute(magicAssetNode.assetBranch)
    
    magicAssetNode.addAttribute(magicAssetNode.createdBy)
    magicAssetNode.addAttribute(magicAssetNode.creationDate)
    magicAssetNode.addAttribute(magicAssetNode.creationTime)
    magicAssetNode.addAttribute(magicAssetNode.lastEditBy)
    magicAssetNode.addAttribute(magicAssetNode.lastEditDate)
    magicAssetNode.addAttribute(magicAssetNode.lastEditTime)
    
    magicAssetNode.addAttribute(magicAssetNode.alembicGeo)
            
    magicAssetNode.addAttribute(magicAssetNode.customTag)
    magicAssetNode.addAttribute(magicAssetNode.meta)
    magicAssetNode.addAttribute(magicAssetNode.description)
    
    magicAssetNode.addAttribute(magicAssetNode.referenceId)   
    # magicAssetNode.addAttribute(magicAssetNode.deformShape)

def initializePlugin(mobject) :
    mplugin = OpenMayaMPx.MFnPlugin(mobject)
    try:
        mplugin.registerTransform(nodeName, nodeId, nodeCreator, nodeInit, OpenMayaMPx.MPxTransformationMatrix, TransformMatrixID)
    except:
        sys.stderr.write("Error loading")
        raise Exception('Failed to registerTransform')

def uninitializePlugin(mobject) :
    mplugin = OpenMayaMPx.MFnPlugin(mobject)
    try:
        mplugin.deregisterNode( nodeId )
    except:
        sys.stderr.write("Error removing")
        raise Exception('Failed to deregisterNode')
