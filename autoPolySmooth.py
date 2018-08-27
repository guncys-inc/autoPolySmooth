# -*- coding:utf-8
import maya.mel as mel
import pymel.core as pm

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
	
	