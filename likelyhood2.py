def calcProbForNode(tree,X,ret = 1, observed = False):
	#print tree, X, ret, observed
	if (X[tree.name]):	
		#print tree.dist, tree.Ex
		if (observed):
			#print tree, X, observed
			ret *= (tree.Pz*tree.Px)
		else:
			ret *= ((tree.Pz * tree.Px) + ((1-tree.Pz) * tree.Ex)) #+(tree.Ez*tree.Px)
		observed = True
	else: 
		if (observed):
			ret *= (tree.Pz*(1-tree.Px))+(tree.Ez*(1-tree.Px))
		else: 
			ret *= (tree.Pz*(1-tree.Px))#+(tree.Ez*(1-tree.Px)))
			ret += ((1-tree.Pz)*(1-tree.Ex))
	#print "leaf: ",tree.name, ret, observed
	return ret, observed

""" Old Calc prob for Node
def calcProbForNode(tree,X,ret = 1, observed = False):
	#print tree, X, ret, observed
	if (X[tree.name]):	
		#print tree.dist, tree.Ex
		if (observed):
			ret *= tree.Pz*tree.Px
		else:
			ret *= ((tree.Pz * tree.Px) + ((1-tree.Pz) * tree.Ex))
		observed = True
	else: 
		if (observed):
			ret *= tree.Pz*(1-tree.Px)
			observed = True
		else: 
			ret *= (tree.Pz*(1-tree.Px))
			ret += ((1-tree.Pz)*(1-tree.Ex))
	#print "leaf: ",tree.name, ret, observed
	return ret, observed
"""

def calcProbForDataPoint(tree,X): # X is a datapoint
	""" Should probably use reverse order traversal for this. The use dynamic 
		programming to speed up process. """
	ret = 1
	observed = False
	if(tree.is_leaf()):
		return calcProbForNode(tree,X)
	#print "Tree: ",tree
	for node in tree.children:
		#print "Node: ",node
		tmp, tmpObs = calcProbForDataPoint(node,X)
		ret *= tmp
		observed = observed or tmpObs

	return calcProbForNode(tree,X,ret, observed)

def calcProbForX(tree,X):
	#print "="*20," SLASK ","="*20
	return calcProbForDataPoint(tree,X)[0]
	 


def nodeProb(node, X, Zu, ZValue, ret = 1, observed = False):
	ePrint = False
	if(ePrint): print "StartInside: ",node.name, Zu
	tmpRet = 0
	if (node.name == Zu):
		if (ZValue): # P[z(node) = 1,X|T]
			if X[node.name]:
				if(ePrint): print "Bing 1"
				tmpRet = node.Pz*node.Px
				observed = True
			else:	
				if(ePrint): print "Bing 2"
				tmpRet = node.Pz*(1-node.Px) 
			
		else: # P[z(node) = 0,X|T]
			if X[node.name]:
				if(ePrint): print "Bing 3"
				observed = True
				tmpRet = (1-node.Pz)*node.Ex 
			else:	
				if(ePrint): print "Bing 4"
				tmpRet = (1-node.Pz)*(1-node.Ex)
	elif (not node.is_root() and node.up.name == Zu):
		if(ZValue):
			if X[node.name]:
				if(ePrint): print "Bing 5"
				tmpRet = (node.Pz*node.Px)+((1-node.Pz)*node.Ex)
				observed = True
			else:
				if(ePrint): print "Bing 6"
				tmpRet = ((1-node.Pz)*(1-node.Ex)) + (node.Pz*(1-node.Px))
			
		else: 
			if X[node.name]:
				if(ePrint): print "Bing 7"
				observed = True
				tmpRet = (node.Ez*node.Px)+((1-node.Ez)*node.Ex)
			else:
				if(ePrint): print "Bing 8"
				tmpRet = (1-node.Ez)*(1-node.Ex)+(node.Ez*(1-node.Px))
	else:
		if X[node.name]:
			if (observed):
				if(ePrint): print "Bing 9"
				tmpRet = (node.Pz*node.Px)

			else:
				if(ePrint): print "Bing 10"
				tmpRet = (node.Pz*node.Px)+((1-node.Pz)*node.Ex)
			observed = True
		else:
			if (observed):
				if(ePrint): print "Bing 11"
				tmpRet = node.Pz*(1-node.Px)
			else:
				if(ePrint): print "Bing 12"
				tmpRet = (node.Pz*(1-node.Px)) * ret
				ret = 1
				tmpRet += (1-node.Pz)*(1-node.Ex)
	if(ePrint): print "Inside: ",tmpRet, ret, tmpRet*ret, observed
	return tmpRet * ret, observed

def calcProbwithZ(tree,X,ZuName,Zvalue):
	ret = 1
	observed = False
	if(tree.is_leaf()):
		return nodeProb(tree,X,ZuName,Zvalue)

	for node in tree.children:
		tmpRet, tmpObserved = calcProbwithZ(node,X,ZuName,Zvalue)
		ret *= tmpRet
		observed = observed or tmpObserved
	return nodeProb(tree,X,ZuName,Zvalue,ret,observed)

def calcProbForXandZ(tree,X,ZuName,ZuValue):
	#print "="*20,"START", "="*20
	return calcProbwithZ(tree,X,ZuName,ZuValue)[0]
