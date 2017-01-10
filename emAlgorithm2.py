#emAlgorithm2.py
from __future__ import division
from eteTree import generate
from operator import itemgetter
import functions as fu
import copy as copy
import math as math
import likelyhood4 as lh4
import numpy as np


def observedMutationSet(data):
	flatData = []#[item for sublist in data for item in sublist.keys()]
	for X in data:
		for mutation in X.keys():
			flatData.append(mutation)
	flatDataSet = list(set(flatData))
	return flatDataSet

def createTreeFromData(data):
	flatDataset = observedMutationSet(data)
	print flatDataset
	return generate(len(flatDataset),flatDataset)

def probListA(tree,data): #Creates a dict with each arcs probabilities.  P[Z(u) = a, Z(p(u)) = b, |X,T]
	probDict = {}
	for node in tree.iter_descendants():
		ab = np.array([[0.000000001,0.000000001],[0.000000001,0.000000001]])
		#ab = np.array([[0.0,0.0],[0.0,0.0]])
		for X in data:	
			tmp = lh4.calcProb_X(tree,X)
			for a in range(0,2):
				for b in range(0,2):
					tmp2 = lh4.calcProb_X_Z_Zp(tree,X,node.name,a,node.up.name,b) 
					ab[a][b] += tmp2 / tmp
		probDict[node.name] = ab
	return probDict

def probListB(tree,data): # P[Z(u) = a|X,T]
	probDict = {}
	for node in tree.iter_descendants():
		#aList = np.array([[0.00000001,0.0000001],[0.00000001,0.00000001]]) # If nothin ever happens... ERROR check, COMMENT
		aList = np.array([[0.0,0.0],[0.0,0.0]])
		
		for X in data:
			tmp = lh4.calcProb_X(tree,X)
			for a in range(0,2):
				if X[node.name]:
					aList[1][a] += lh4.calcProb_X_Z(tree,X,node.name,a) / tmp
				else:
					aList[0][a] += lh4.calcProb_X_Z(tree,X,node.name,a) / tmp

		
			#print "HORUNGE2: ",arc.name,aList , "STOP"
		probDict[node.name] = aList
	return probDict
def Asum(probListA,nodeName,a,b): # P[Z(u) = a | Z(p'(u)) = b,  Sigma_z(u)]
	total = 0 
	tmp = probListA[nodeName][a][b]
	for tmpA in range(0,2):
		total += probListA[nodeName][tmpA][b]
	return tmp / total


def Bsum(probListB,nodeName,sigma,a): # P[X(u) = sigma | Z(u) = a,  Sigma_z(u)]
	# probDict = {}
	# ab = np.matrix([[0,0],[0,0]])
	total = 0 
	tmp = probListB[nodeName][sigma][a]
	for tmpSigma in range(0,2):
		total += probListB[nodeName][tmpSigma][a]
	return tmp / total

def arcWeigth(probListA,probListB,u,uParent,data,tree): # u is a node
	ret = 0
	for X in data:
		p_X = lh4.calcProb_X(tree,X)
		for a in range(0,2):
			for b in range(0,2):
				t1f1 = lh4.calcProb_X_Z_Zp(tree,X,u,a,uParent,b) / p_X # OK
				t1f2 = math.log(Asum(probListA,u,a,b))
				ret += (t1f1 * t1f2)
			
			for sigma in range(0,2):
				t2f1 = lh4.calcProb_X_Z(tree,X,u,a) / p_X # OK
				t2f2 = math.log(Bsum(probListB,u,sigma,a))		
				ret += (t2f1 * t2f2)

		if (math.isnan(ret)):
			print "\n",t2f1, t2f2, t1f1, t1f2
			print Asum(probListA,ZuName,a,b)
			#print probListA,ZuName,a,b
			raw_input("ERROR")
				
		
	return ret



def maximizeTree2(tree,data):
	
	qValue = 0
	pzValues = np.arange(0.1,1,0.1)
	newTree = copy.deepcopy(tree)
	for node in newTree.iter_descendants(): 
		tmpMax = -1000000
		arcW = 0
		for tmpPz in pzValues:
			node.Pz = tmpPz
			#print "NewTree"
			#fu.printTreeInfo(newTree)
			#print "OldTree" 
			#fu.printTreeInfo(tree)
			probsA = probListA(newTree,data)
			probsB = probListB(newTree,data)
			tmp = arcWeigth(probsA,probsB,node.name,node.up.name,data,tree)
			print node.name, node.dist, node.Px, tmpPz, tmp
			#raw_input("ArchWeigth")
			#print node.name, node.dist, node.Px, tmp
			if tmpMax < tmp:
				#print tmp, tmpMax,tmpPz
				tmpMax = tmp   
				arcW = tmpPz
		node.Pz = arcW
		qValue += tmpMax

	return newTree, qValue