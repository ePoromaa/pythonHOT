from __future__ import division
import likelyhood3 as lh3
import math as math

#epsilonZ = 0.01
#epsilonX = 0.01
def allChildrenAreLeaves(tree):
	if (tree.is_leaf()):
		return False
	for node in tree.children:
		if not (node.is_leaf()):
			return False
	return True


def calcProbForLeaf(tree,X):
	if (X[tree.name]):	
		return (tree.dist * tree.Px), True # + ((1-tree.dist) * tree.Ex)), True
	else: 
		return ((1-tree.dist) + (tree.dist*(1-tree.Px))), False
	#print "leaf: ",tree.name, ret, observed
	


def calcProbForDataPoint(tree,X): # X is a datapoint
	""" Should probably use reverse order traversal for this. The use dynamic 
		programming to speed up process. """
	ret = 1
	observed = False
	if(tree.is_leaf()):
		return calcProbForLeaf(tree,X)
	
	for node in tree.children:
		tmp, tmpObs = calcProbForDataPoint(node,X)
		ret *= tmp
		observed = observed or tmpObs

	if (X[tree.name]):
		ret *= tree.dist*tree.Px
	else:
		if (observed):
			ret *= tree.dist*(1-tree.Px)
		else: 
			ret *= (tree.dist*(1-tree.Px))
			ret += (1-tree.dist) # Change made here 
			
	#print "inner node: ", tree.name, ret, observed
	return ret, observed


def calcProbForLeaf2(tree,X):
	if (X[tree.name]):	
		#print tree.dist, tree.Ex
		return ((tree.dist * tree.Px) + ((1-tree.dist) * tree.Ex)), True
	else: 
		return ((1-tree.dist) + (tree.dist*(1-tree.Px))), False
	#print "leaf: ",tree.name, ret, observed
	


def calcProbForDataPoint2(tree,X): # X is a datapoint
	""" Should probably use reverse order traversal for this. The use dynamic 
		programming to speed up process. """
	ret = 1
	observed = False
	if(tree.is_leaf()):
		return calcProbForLeaf2(tree,X)
	
	for node in tree.children:
		tmp, tmpObs = calcProbForDataPoint2(node,X)
		ret *= tmp
		observed = observed or tmpObs

	if (X[tree.name]):
		ret *= (tree.dist*tree.Px)+((1-tree.dist) * tree.Ex)
	else:
		if (observed):
			ret *= tree.dist*(1-tree.Px)
		else: 
			ret *= (tree.dist*(1-tree.Px))
			ret += (1-tree.dist) # Change made here 
			
	#print "inner node: ", tree.name, ret, observed
	return ret, observed

def calcProbForLeaf3(tree,X,ret = 1, observed = False):
	if (X[tree.name]):	
		#print tree.dist, tree.Ex
		ret *= ((tree.dist * tree.Px) + ((1-tree.dist) * tree.Ex))
		observed = True
	else: 
		if (observed):
			ret *= tree.dist*(1-tree.Px)
		else: 
			ret *= (tree.dist*(1-tree.Px))
			ret += (1-tree.dist) # Change made here 

	#print "leaf: ",tree.name, ret, observed
	return ret, observed


def calcProbForDataPoint3(tree,X): # X is a datapoint
	""" Should probably use reverse order traversal for this. The use dynamic 
		programming to speed up process. """
	ret = 1
	observed = False
	if(tree.is_leaf()):
		return calcProbForLeaf3(tree,X)
	#print "Tree: ",tree
	for node in tree.children:
		#print "Node: ",node
		tmp, tmpObs = calcProbForDataPoint3(node,X)
		ret *= tmp
		observed = observed or tmpObs

	return calcProbForLeaf3(tree,X,ret, observed)


def likelyhoodOfX(tree,X):
	tmp, observed = calcProbForDataPoint(tree,X)
	return tmp


def likelyhoodOfX2(tree,X):
	tmp, observed = calcProbForDataPoint2(tree,X)
	return tmp

def likelyhoodOfX3(tree,X):
	tmp, observed = calcProbForDataPoint3(tree,X)
	return tmp

def logLikelyhood(tree,data):
	ret = 0
	for i in range(len(data)):
		ret += math.log(lh3.calcProbForX(tree,data[i]))
	return ret


def calcProbForLeafAndZ(tree,X,ZuName,Zvalue):
	ret = 0
	observed = False
	if (X[tree.name]): # If observed
		if (tree.name == ZuName): 
			if(Zvalue):
				ret = tree.dist * tree.Px
			else:
				ret = tree.Ex # constant tree.dist?
		else: 
			ret = tree.dist * tree.Px
		observed = True
	else:
		if (tree.name == ZuName): 
			if(Zvalue):
				ret = tree.dist* (1-tree.Px)
				#observed = True  # Check
			else:
				ret = 1-tree.dist
		else:
			ret = ((1-tree.dist) + (tree.dist*(1-tree.Px)))
	#print tree, observed, " is this likley ", ret
	return ret, observed

def calcProbForDataPointAndZ(tree,X,ZuName,Zvalue):
	ret = 1 
	observed = False
	if(tree.is_leaf()):
		return calcProbForLeafAndZ(tree,X,ZuName,Zvalue)

	for node in tree.children:
		tmp, tmpObs = calcProbForDataPointAndZ(node,X,ZuName,Zvalue)
		ret *= tmp
		observed = observed or tmpObs

	if X[tree.name]:
		if (tree.name == ZuName and Zvalue):
			ret *= tree.dist * tree.Px
		elif (tree.name == ZuName and not Zvalue):
			ret *= tree.Ex # Check 
		else:
			ret *= tree.dist * tree.Px
	else:
		if (observed):
			if (tree.name == ZuName and Zvalue):
				ret *= tree.dist*(1-tree.Px)
			elif (tree.name == ZuName and not Zvalue):
				ret *= tree.Ex # Check ASK JENS
			else:
				ret *= tree.dist*(1-tree.Px)
		else: 
			if (tree.name == ZuName and Zvalue):
				ret *= tree.dist*(1-tree.Px)
			elif (tree.name == ZuName and not Zvalue):
				ret = 1-tree.dist # Change made for test 3 ret *= 1-tree.dist
			else:
				ret *= tree.dist*(1-tree.Px)
				ret += 1-tree.dist
	#if tree.name == "[M91]":
	#	print "S5: ",ret
	if (ret == 0):
		raw_input("ERROR")
	return ret, observed

def calcProbForLeafZandZp(tree,X,Zu,Zp,Zvalue,Zpvalue):
	Zswitch = False
	ret = 0
	#global epsilonZ
	#global epsilonX
	observed = False
	if (X[tree.name]): # If observed
		#print tree.name, Zu, Zvalue
		if (tree.name == Zu): 
			if(tree.up.name == Zp):
				if(Zvalue and not Zpvalue):
					ret = tree.Ez
				elif(Zvalue and Zpvalue):
					ret = tree.dist * tree.Px
				elif(not Zvalue and Zpvalue):
					ret = tree.Ex
				elif(not Zvalue and not Zpvalue):
					ret = tree.Ex  
			else:
				raw_input("ERROR")
		else: 
			ret *= tree.dist * tree.Px
		observed = True
	else:
		if (tree.name == Zu): 
			if(tree.up.name == Zp):
				if(Zvalue and not Zpvalue):
					ret = 1-tree.Px
					observed = True
				elif(Zvalue and Zpvalue):
					ret = 1-tree.Px
					observed = True
				elif(not Zvalue and Zpvalue):
					ret = 1-tree.dist
				elif(not Zvalue and not Zpvalue):
					ret = 1-tree.Ez # Check
			else:
				raw_input("ERROR")
		else:
			ret *= ((1-tree.dist) + (tree.dist*(1-tree.Px)))
	#print tree, observed, " is this likley ", ret
	return ret, observed

def calcProbForDataPointZandZp(tree,X,Zu,Zp,Zvalue,Zpvalue):
	ret = 1 
	observed = False
	if(tree.is_leaf()):
		return calcProbForLeafZandZp(tree,X,Zu,Zvalue,Zp,Zpvalue)

	for node in tree.children:
		tmp, tmpObs = calcProbForDataPointAndZ(node,X,Zu,Zvalue)
		ret *= tmp
		observed = observed or tmpObs

	if X[tree.name]:
		if (tree.name == Zu):
			if(tree.up.name == Zp):
				if(Zvalue and not Zpvalue):
					ret = tree.Ez
				elif(Zvalue and Zpvalue):
					ret = tree.dist * tree.Px
				elif(not Zvalue and Zpvalue):
					ret = tree.Ex
				elif(not Zvalue and not Zpvalue):
					ret = tree.Ex  
			else:
				raw_input("ERROR")
		else:
			ret *= tree.dist*tree.Px
		observed = True
	else:
		#if (observed):
		if (tree.name == Zu):
			if(tree.up.name == Zp):
				if(Zvalue and not Zpvalue):
					ret = 1-tree.Px
					observed = True
				elif(Zvalue and Zpvalue):
					ret = 1-tree.Px
					observed = True
				elif(not Zvalue and Zpvalue):
					ret = 1-tree.dist
				elif(not Zvalue and not Zpvalue):
					ret = 1-tree.Ez # Check
		else:
			ret *= tree.dist*(1-tree.Px)	
			ret += 1-tree.dist # Change made here
		"""		
		else: 
			if (tree.name == Zu and Zvalue):
				ret *= tree.dist*(1-tree.Px)
			elif (tree.name == Zu and not Zvalue):
				ret *= 1-tree.dist
			else:
				ret *= ((1-tree.dist) + (tree.dist*(1-tree.Px)))
		"""
	return ret, observed

def likelyhoodOfXandZ(tree,X,Z,Zvalue): # P[Z(u) = a, X|T]
	tmp, observed = calcProbForDataPointAndZ(tree,X,Z,Zvalue)
	#print "Obeservation ", X, " in tree ", tree, " is this likley ", tmp
	return tmp		


def likelyhoodOfXZandZp(tree,X,Zu,Zvalue,Zpvalue): # P[Z(u) = a, Z(p(u)) = b, X|T]
	#print tree, Zu, tree.search_nodes(name = Zu) # FAULT, check for correct search function. 
	Zp = tree.search_nodes(name = Zu)[0].up.name
	tmp, observed = calcProbForDataPointZandZp(tree,X,Zu,Zp,Zvalue,Zpvalue)
	#print "Obeservation ", X, " in tree ", tree, " is this likley ", tmp
	return tmp


def nodeProb(node, X, Zu, ZValue, ret = 1):
	if (node.name == Zu):
		if (Zvalue): # P[z(node) = 1,X|T]
			if X[node.name]:
				ret *= node.Pz*node.Px
			else:	
				ret *= node.Pz*(1-node.Px)
		else: # P[z(node) = 0,X|T]
			if X[node.name]:
				ret *= (1-node.Pz)*node.Ex
			else:	
				ret *= 1-node.Pz
	elif (node.up.name == Zu):
		if(Zvalue):
			return #NOT DONE
		else: 
			return #NOT DONE
	else:
		if X[node.name]:
			ret *= node.Pz*node.Px+((1-node.Pz)*node.Ex)
		else:
			ret *= (1-node.Pz)+node.Pz*(1-node.Px)
	return ret, observed

def calcProbwithZ(tree,X,Zu,Zvalue):
	ret = 1
	observed = False
	if(tree.is_leaf()):
		return nodeProb(tree,X,ZuName,Zvalue)

	for node in tree.children:
		tmpRet, tmpObserved = calcProbForDataPointAndZ(node,X,ZuName,Zvalue)
		ret *= tmpRet
		observed = observed or tmpObserved
	return nodeProb(tree,X,Zu,Zvalue,ret)



# -------------------------------------------------------------------------------------------------
#												SCRAP
# -------------------------------------------------------------------------------------------------
