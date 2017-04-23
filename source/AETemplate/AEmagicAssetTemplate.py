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
import pymel.core as pm
from pymel.internal.plogging import pymelLogger

class NodeTemplate(pm.ui.AETemplate):

    def __init__(self, nodeName):
        pm.ui.AETemplate.__init__(self, nodeName)
        
    def excludeAttributes(self):
        self.beginNoOptimize()
        self.suppress("translate")
        self.suppress("rotate")
        self.suppress("scale")
        self.suppress("shear")
        self.suppress("minTransLimit")
        self.suppress("maxTransLimit")
        self.suppress("minRotLimit")
        self.suppress("maxRotLimit")
        self.suppress("minScaleLimit")
        self.suppress("maxScaleLimit")
        self.suppress("minTransLimitEnable")
        self.suppress("minTransYLimitEnable")
        self.suppress("minTransZLimitEnable")
        self.suppress("maxTransLimitEnable")
        self.suppress("maxTransXLimitEnable")
        self.suppress("maxTransYLimitEnable")
        self.suppress("maxTransZLimitEnable")
        self.suppress("minRotLimitEnable")
        self.suppress("minRotYLimitEnable")
        self.suppress("minRotZLimitEnable")
        self.suppress("maxRotLimitEnable")
        self.suppress("maxRotXLimitEnable")
        self.suppress("maxRotYLimitEnable")
        self.suppress("maxRotZLimitEnable")
        self.suppress("minScaleLimitEnable")
        self.suppress("minScaleYLimitEnable")
        self.suppress("minScaleZLimitEnable")
        self.suppress("maxScaleLimitEnable")
        self.suppress("maxScaleXLimitEnable")
        self.suppress("maxScaleYLimitEnable")
        self.suppress("maxScaleZLimitEnable")
        self.suppress("scalePivot")
        self.suppress("scalePivotTranslate")
        self.suppress("rotatePivotTranslate")
        self.suppress("newTransMinusRotatePivot")
        self.suppress("orient")
        self.suppress("geometry")
        self.suppress("dynamics")
        self.suppress("xformMatrix")
        
        self.suppress("drawOverride")
        self.suppress("projectionGate")
        self.suppress("panScan")
        self.suppress("time")
        self.suppress("aspectRatios")
        self.suppress("filmbackAperture")
        self.suppress("soundTrackWidth")
        self.suppress("safeAction")
        self.suppress("safeTitle")
        self.suppress("text")
        self.suppress("pad")

        self.suppress("instObjGroups")
        self.suppress("useObjectColor")
        self.suppress("lodVisibility")
        self.suppress("localPosition")
        self.suppress("nodeState")
        self.suppress("castsShadows")
        self.suppress("receiveShadows")
        self.suppress("motionBlur")
        self.suppress("primaryVisibility")
        self.suppress("visibleInReflections")
        self.suppress("visibleInRefractions")
        self.suppress("doubleSided")
        self.suppress("opposite")
        self.suppress("geometryAntialiasingOverride")
        self.suppress("antialiasingLevel")
        self.suppress("shadingSamplesOverride")
        self.suppress("shadingSamples")
        self.suppress("maxShadingSamples")
        self.suppress("volumeSamplesOverride")
        self.suppress("volumeSamples")
        self.suppress("depthJitter")
        self.suppress("maxVisibilitySamplesOverride")
        self.suppress("maxVisibilitySamples")
        self.suppress("boundingBoxScale")
        self.suppress("featureDisplacement")
        self.suppress("initialSampleRate")
        self.suppress("extraSampleRate")
        self.suppress("textureThreshold")
        self.suppress("normalThreshold")
        self.suppress("ghosting")
        self.suppress("ghostingControl")
        self.suppress("ghostPreSteps")
        self.suppress("ghostPostSteps")
        self.suppress("ghostStepSize")
        self.suppress("ghostFrames")
        self.suppress("ghostRangeStart")
        self.suppress("ghostRangeEnd")
        self.suppress("ghostDriver")
        self.suppress("ghostFrames")
        self.suppress("ghostCustomSteps")
        self.suppress("drawOverride")
        self.suppress("useObjectColor")
        self.suppress("objectColor")
        self.suppress("center")
        self.suppress("matrix")
        self.suppress("inverseMatrix")
        self.suppress("worldMatrix")
        self.suppress("worldInverseMatrix")
        self.suppress("parentMatrix")
        self.suppress("parentInverseMatrix")
        self.suppress("instObjGroups")
        self.suppress("renderInfo")
        self.suppress("ignoreSelfShadowing")
        self.suppress("caching")
        self.suppress("intermediateObject")
        self.suppress("compInstObjGroups")
        self.suppress("localScale")
        self.suppress("renderLayerInfo")
        self.suppress("rotatePivot")
        self.suppress("rotateAxis")
        self.suppress("selectHandle")
        self.suppress("inheritsTransform")
        self.suppress("displayHandle")
        self.suppress("displayScalePivot")
        self.suppress("displayRotatePivot")
        self.suppress("displayLocalAxis")
        self.suppress("showManipDefault")
        self.suppress("visibility")
        self.suppress("rotateOrder")
        self.suppress("template")
        
        self.suppress("rotateQuaternion")
        self.suppress("mentalRayControls")
        self.endNoOptimize()


class AEmagicAssetTemplate(NodeTemplate):

    def __init__(self, nodeName):
        NodeTemplate.__init__(self, nodeName)
        
        self.beginScrollLayout()

        self.beginLayout("Project Setting", collapse=0)
        self.addControl("project", label="Project", preventOverride=True)
        self.addControl("branch", label="Branch", preventOverride=True)
        self.endLayout()
        
        self.beginLayout("Asset Info",collapse=0)
        self.addControl("assetType", label="Type", preventOverride=True)
        self.addControl("assetState", label="State", preventOverride=True)
        self.addControl("assetName", label="Name", preventOverride=True)
        self.addControl("assetVersion", label="Version", preventOverride=True)
        self.addControl("assetBranch", label="Asset Branch", preventOverride=True)
        self.endLayout()
                                        
        self.beginLayout("Creation", collapse=0)
        self.addControl("createdBy", label="Created By", preventOverride=True)
        self.addControl("createDate", label="Creation Date", preventOverride=True)
        self.addControl("createTime", label="Creation Time", preventOverride=True)
        self.endLayout()
        
        self.beginLayout("Last Edit", collapse=0)
        self.addControl("lastEditBy", label="Last Edit By", preventOverride=True)
        self.addControl("lastEditDate", label="Last Edit Date", preventOverride=True)
        self.addControl("lastEditTime", label="Last Edit Time", preventOverride=True)
        self.endLayout()
                
        self.beginLayout("Alembic Geometry", collapse=1)
        self.callCustom(self.toBakeLayout, self.bakeRefreshButtonCommand, "alembicGeo")
        self.endLayout()
        
        self.beginLayout("Custom Tag", collapse=0)
        self.addControl("customTag", label="Custom Tag", preventOverride=True)
        self.endLayout()
                
        self.beginLayout("Meta", collapse=0)
        self.addControl("meta", label="Meta", preventOverride=True)
        self.endLayout()
        
        self.beginLayout("Description", collapse=1)
        self.addControl("description", label="Description", preventOverride=True)
        self.endLayout()
        
        self.beginLayout("Reference Id", collapse=0)
        self.addControl("referenceId", label="Reference Id", preventOverride=True)
        self.endLayout()
        
        self.addExtraControls()
        self.excludeAttributes()
        self.endScrollLayout()
                
    def toBakeLayout(self, plug) :
        """
        Layout for the geometryToBake connections.
        """
        self.currentNode = pm.PyNode(plug.split(".")[0]) # store the node linked to the AE
        
        pm.setUITemplate ("attributeEditorTemplate", pst=True)
        vLayout = pm.verticalLayout(ratios=[4, 1])
        
        # geometry textScrollList
        self.geometryToBakeTSL = pm.uitypes.TextScrollList(parent=vLayout)
        self.geometryToBakeTSL.setAllowMultiSelection(True)
        
        # button
        hLayout = pm.horizontalLayout(spacing=2)
        pm.uitypes.Button(parent=hLayout, l="Add", command=pm.Callback(self.bakeAddButtonCommand))
        pm.uitypes.Button(parent=hLayout, l="Remove", command=pm.Callback(self.bakeRemoveButtonCommand))
        pm.uitypes.Button(parent=hLayout, l="Refresh", command=pm.Callback(self.bakeRefreshButtonCommand))
        hLayout.redistribute()
        
        vLayout.redistribute()
        pm.setUITemplate(ppt=True)
        
        self.bakeRefreshButtonCommand()
        
    def bakeAddButtonCommand (self):
        """
        Connect the selected shapes to the geometryToBake attribute of the assetNode
        and update the TSL
        """
        for node in pm.selected() :
            if pm.nodeType(node) == "mesh" or pm.nodeType(node) == "nurbsCurve":
                try :
                    node.message.connect(self.currentNode.alembicGeo, na=True)
                except :
                    pass
        self.bakeRefreshButtonCommand()
            
    def bakeRemoveButtonCommand(self):
        """
        Disconnect node from the geometryToBake attribute of the assetNode
        and update the TSL
        """
        for node in self.geometryToBakeTSL.getSelectItem() :
            node = pm.PyNode(node)
            for connection in node.message.outputs(plugs=True) :
                # break only the connection to the current asset node
                if str(self.currentNode) in str(connection) : 
                    node.message.disconnect(connection)  
        self.bakeRefreshButtonCommand()
        
    def bakeRefreshButtonCommand(self, plug=None):
        """
        Refresh the bake TSL
        """
        if plug :
            self.currentNode = pm.PyNode(plug.split(".")[0])
        try :
            self.geometryToBakeTSL.removeAll()
        except RuntimeError :
            pass
        for shape in self.currentNode.alembicGeo.inputs(shapes=True) :
            self.geometryToBakeTSL.append(shape)
