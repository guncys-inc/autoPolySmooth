# -*- coding:utf-8
import maya.mel as mel
import pymel.core as pm

melCmd ="""
global proc autoSmooth(int $v){
	if($v == 0){
		string $psFaces[] = `ls -et polySmoothFace`;
		for($poly in $psFaces)
		{
			if (attributeExists("div", $poly)){
				setAttr ($poly + ".divisions") 0;
			}
			if (attributeExists("level", $poly)){
				setAttr ($poly + ".subdivisionLevels") 0;
			}
		}
	}else{
		string $psFaces[] = `ls -et polySmoothFace`;
		
		for($poly in $psFaces)
		{
			if (attributeExists("div", $poly)){
				int $div = `getAttr ($poly+".div")`;
				setAttr ($poly + ".divisions") $div;
			}
			if (attributeExists("level", $poly)){
				int $level = `getAttr ($poly+".level")`;			
				setAttr ($poly + ".subdivisionLevels") $level;				
			}
		}	
	}
}
"""
#======================================================================#
def addCustomAttrs():
	selected = pm.ls(sl=True)
	
	for sel in selected:
		if sel.getShape().type() == 'mesh':
			pm.select(sel, r=True)
			smooth = pm.polySmooth(dv=0)
			pm.rename(smooth, 'autoPS#')
			pm.addAttr(smooth, ln='div', at='long', min=0, max=3, k=True, dv=1)
			pm.addAttr(smooth, ln='level', at='long', min=0, max=3, k=True, dv=1)
			
	pm.select(selected)

#======================================================================#
def setMel():
	drg = pm.PyNode('defaultRenderGlobals')
	preMel = drg.preMel
	postMel = drg.postMel

	if preMel.get() == None:
		preMel.set('autoSmooth 1;')
	elif not 'autoSmooth' in preMel.get():
		if not preMel.get().endswith(';'):
			preMel.set(preMel.get()+';')
		preMel.set(preMel.get()+'autoSmooth 1;')
		
	if postMel.get() == None:
		postMel.set('autoSmooth 0;')
	elif not 'autoSmooth' in postMel.get():
		if not postMel.get().endswith(';'):
			postMel.set(postMel.get()+';')	
		postMel.set(postMel.get()+'autoSmooth 0;')
	
	mel.eval(melCmd)