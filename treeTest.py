import eteTree as et
import functions as fu
from abberations import abberations as abbrs
import math as math
import emAlgorithm as em
import emAlgorithm2 as em2
import numpy as np
import functions as fu
import copy as copy


def treeTest1(numStartingTrees,numGeneratedTrees,numDataPoints,numVertices,mutations):
	print "="*20," Tree Test 111 ", "="*20
	results = []
	baseline = []
	for sTreeNr in range(numStartingTrees):
		print "S"
		cMutations = list(mutations) # Making a COPY of the mutations.
		tree = et.generate(numVertices,cMutations,False,False)
		et.setRandomTreeNodes(tree, False,False)
		data = et.createDataHash(tree,numDataPoints)
		bestQValue = -100000
		bestTree = None
		fu.printTreeInfo2(tree,data)
		#print "logL: ",lh.logLikelyhood(tree,data)
		for gTreeNr in range(numGeneratedTrees):
			print "G"
			print len(data)
			newTree = em2.createTreeFromData(data)
			#print "1",
			newTree = copy.copy(tree) # Forcing same structure as original tree
			newTree = et.setRandomTreeNodes(newTree,False,False, Zonly=True)
			#print "2",
			#fu.printTreeInfo2(newTree,data)
			#print "PrelogL: ",lh.logLikelyhood(newTree,data)
			oldQ = 0
			counter = 0
			while True and counter < 100:
				print "EM it: ",counter
				newTree, qValue = em2.maximizeTree2(newTree,data)
				if (abs(oldQ-qValue) < 0.1):
					break
				oldQ = qValue

				fu.printTreeInfo2(newTree,data)
				print "QValue: ",qValue
				#print "-",
				counter += 1
			print "NewTree: ",
			fu.printTreeInfo2(newTree,data)
			#print "PostlogL: ",lh.logLikelyhood(newTree,data)
				
				
				
			#if bestQValue < qValue:
			#	bestQValue = qValue
			#	bestTree = newTree
			#baseline.append(et.getSimilarity(et.getEdges(tree),et.getEdges(newTree)))
			#print "Q: ",qValue, "PostlogL: ",lh.logLikelyhood(newTree,data)
		#print "\nBestTree:"
		#fu.printTreeInfo(bestTree)
		#results.append(et.getSimilarity(et.getEdges(tree),et.getEdges(bestTree)))

	return results, baseline