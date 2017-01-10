def calcProbForNode(tree,X,ret1 = 1, ret0 = 1):
	if (X[tree.name]):	
		ret1 *= (tree.Pz*tree.Px) + ((1-tree.Pz)*tree.Ex)
		ret0 *= (tree.Ez*tree.Px) + ((1-tree.Ez)*tree.Ex)
	else: 
		ret1 *= tree.Pz*(1-tree.Px) + ((1-tree.Pz)*(1-tree.Ex))
		ret0 *= tree.Ez*(1-tree.Px) + ((1-tree.Ez)*(1-tree.Ex))
	return ret1, ret0

def calcProbForDataPoint(tree,X): # X is a datapoint
	ret1 = 1
	ret0 = 1
	if(tree.is_leaf()):
		return calcProbForNode(tree,X)

	for node in tree.children:
		tmpRet1, tmpRet0 = calcProbForDataPoint(node,X)
		ret1 *= tmpRet1
		ret0 *= tmpRet0

	return calcProbForNode(tree,X,ret1,ret0)

def calcProbForX(tree,X):
	#print "="*20," SLASK ","="*20
	ret1,ret0 = calcProbForDataPoint(tree,X)
	return ret1+ret0

def	calcProbForNodeAndZ(tree,X,ZuName,ZuValue,ret1=1,ret0=1):
	if (tree.name == ZuName):
		if ZuValue:
			if (X[tree.name]):	
				ret1 *= tree.Pz*tree.Px
				ret0 *= tree.Ez*tree.Px
			else:
				ret1 *= tree.Pz*(1-tree.Px)
				ret0 *= tree.Ez*(1-tree.Px)
		else:
			if (X[tree.name]):	
				ret1 *= (1-tree.Pz)*tree.Ex
				ret0 *= (1-tree.Ez)*tree.Ex
			else:
				ret1 *= (1-tree.Pz)*(1-tree.Ex)
				ret0 *= (1-tree.Ez)*(1-tree.Ex)
	else:
		return calcProbForNode(tree,X,ret1,ret0)
	return ret1, ret0

def	calcProbForXandZHelp(tree,X,ZuName,ZuValue):
	ret1 = 1
	ret0 = 1
	if(tree.is_leaf()):
		return calcProbForNodeAndZ(tree, X, ZuName, ZuValue)

	for node in tree.children:
		tmpRet1, tmpRet0 = calcProbForXandZHelp(node, X, ZuName, ZuValue)
		ret1 *= tmpRet1
		ret0 *= tmpRet0

	return calcProbForNodeAndZ(tree, X, ZuName, ZuValue, ret1, ret0)	

def calcProbForXandZ(tree,X,ZuName,ZuValue):
	ret1,ret0 = calcProbForXandZHelp(tree,X,ZuName,ZuValue)
	return ret1+ret0

def	calcProbNode_X_Z_Zp(tree,X,ZuName,ZuValue,ZuPName,ZuPValue,ret1=1,ret0=1):
	if (tree.name == ZuPName):
		if ZuPValue:
			if (X[tree.name]):	
				ret1 *= tree.Pz*tree.Px
				ret0 *= tree.Ez*tree.Px
			else:
				ret1 *= tree.Pz*(1-tree.Px)
				ret0 *= tree.Ez*(1-tree.Px)
		else:
			if (X[tree.name]):	
				ret1 *= (1-tree.Pz)*tree.Ex
				ret0 *= (1-tree.Ez)*tree.Ex
			else:
				ret1 *= (1-tree.Pz)*(1-tree.Ex)
				ret0 *= (1-tree.Ez)*(1-tree.Ex)
	elif (tree.name == ZuName):
		if ZuValue:
			if (X[tree.name]):	
				ret1 *= tree.Pz*tree.Px
				ret0 *= tree.Ez*tree.Px
			else:
				ret1 *= tree.Pz*(1-tree.Px)
				ret0 *= tree.Ez*(1-tree.Px)
		else:
			if (X[tree.name]):	
				ret1 *= (1-tree.Pz)*tree.Ex
				ret0 *= (1-tree.Ez)*tree.Ex
			else:
				ret1 *= (1-tree.Pz)*(1-tree.Ex)
				ret0 *= (1-tree.Ez)*(1-tree.Ex)
	else:
		return calcProbForNode(tree,X,ret1,ret0)
	return ret1, ret0
"""
def	calcProbNode_X_Z_Zp(tree,X,ZuName,ZuValue,ZuPName,ZuPValue,ret1=1,ret0=1):
	#print tree.name, tree.up.name
	eB = True
	print not tree.is_root()

	if not tree.is_root():
		print "Hej"
		print tree.up.name, ZuPName
		if (tree.up.name == ZuPName):
			print "Here"
			if (tree.name == ZuName):
				print "There"
				if ZuPValue:
					if ZuValue:
						if (X[tree.name]):	
							if(eB): print "E1"
							ret1 *= tree.Pz*tree.Px
							ret0 *= 0
							#ret0 *= tree.Ez*tree.Px
						else:
							if(eB): print "E2"
							ret1 *= tree.Pz*(1-tree.Px)
							ret0 *= 0

							#ret0 *= tree.Ez*(1-tree.Px)
					else:
						if (X[tree.name]):	
							if(eB): print "E3"
							ret1 *= (1-tree.Pz)*tree.Ex
							ret0 *= 0
							#ret0 *= (1-tree.Ez)*tree.Ex
						else:
							if(eB): print "E4"
							ret1 *= (1-tree.Pz)*(1-tree.Ex)
							ret0 *= 0
							#ret0 *= (1-tree.Ez)*(1-tree.Ex)
				else:
					if ZuValue:
						if (X[tree.name]):	
							#ret1 *= tree.Pz*tree.Px
							if(eB): print "E5"
							ret1 *= 0
							ret0 *= tree.Ez*tree.Px
						else:
							#ret1 *= tree.Pz*(1-tree.Px)
							if(eB): print "E6"
							ret1 *= 0
							ret0 *= tree.Ez*(1-tree.Px)
					else:
						if (X[tree.name]):	
							#ret1 *= (1-tree.Pz)*tree.Ex
							if(eB): print "E7"
							ret1 *= 0
							ret0 *= (1-tree.Ez)*tree.Ex
						else:
							#ret1 *= (1-tree.Pz)*(1-tree.Ex)			
							if(eB): print "E8"
							ret1 *= 0
							ret0 *= (1-tree.Ez)*(1-tree.Ex)
			else:
				raw_input("ERROR")
	else:
		return calcProbForNode(tree,X,ret1,ret0)
	print ret1,ret0
	return ret1, ret0
"""
def	calcProb_X_Z_Zp_Help(tree,X,ZuName,ZuValue,ZuPName,ZuPValue):
	ret1 = 1
	ret0 = 1
	if(tree.is_leaf()):
		return calcProbNode_X_Z_Zp(tree, X, ZuName, ZuValue,ZuPName,ZuPValue)

	for node in tree.children:
		tmpRet1, tmpRet0 = calcProb_X_Z_Zp_Help(node, X, ZuName, ZuValue,ZuPName,ZuPValue)
		ret1 *= tmpRet1
		ret0 *= tmpRet0

	return calcProbNode_X_Z_Zp(tree, X, ZuName, ZuValue,ZuPName,ZuPValue, ret1, ret0)	

def calcProb_X_Z_Zp(tree,X,ZuName,ZuValue,ZuPName,ZuPValue):
	ret1,ret0 = calcProb_X_Z_Zp_Help(tree,X,ZuName,ZuValue,ZuPName,ZuPValue)
	return ret1+ret0