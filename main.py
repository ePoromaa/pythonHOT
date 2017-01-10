import eteTree as et
from ete3 import  Tree, NodeStyle, TreeStyle, faces, AttrFace
import likelyhood as lh
import math as math
import emAlgorithm as em
import numpy as np
import functions as fu
import test as test
import treeTest as treeTest
import copy as copy
from abberations import abberations as abbrs
np.random.seed(seed=0) # DONT CHANGE TGIST

print "="*20, " MAIN START ", "="*20
# =============================================================================
#									CONSTANTS
# =============================================================================
constNrVertices = 3 # Report: 10, 25, 40
constNrOfDatapoints = 100 # 



def testingGround(tree,data):
	print "Starting tree log likelyhood: ", lh.logLikelyhood(tree,data)

	for X in data:
		print X
		for node in tree.iter_descendants():
			for a in range(0,2):
				print "P[Z(", node.name,") = ",a,",X|T] = ", lh.calcProbForDataPointAndZ(tree,X,node.name,a)
			print "P[X|T] = ",lh.calcProbForDataPoint(tree,X)
		print "\n"


def newTreeTestingGround(tree,newTree,data):
	
	print "="*20,"TestingGround","="*20,"\nTestedTree:",newTree
	uniqueData = fu.uniqueData(data)
	print "Num datapoints: ", len(data), " Num unique: ", len(uniqueData)
	print "Starting tree log likelyhood: ", lh.logLikelyhood(tree,data)
	print "New tree log likelyhood: ", lh.logLikelyhood(newTree,data)
	print "Starting tree log unique likelyhood: ", lh.logLikelyhood(tree,uniqueData)
	print "New tree log unique likelyhood: ", lh.logLikelyhood(newTree,uniqueData)
	for X in range(len(uniqueData)):
		tmp1 = lh.likelyhoodOfX(tree,uniqueData[X])
		tmp2 = lh.likelyhoodOfX(newTree,uniqueData[X])
		print uniqueData[X], "P[X|T] = ", tmp1, "P[X|nT] = ", tmp2 , tmp1-tmp2
	
	tmp = em.Qfunc(newTree,data)
	tmp2 = em.Qfunc(newTree,uniqueData)
	print "New tree Q func: ", tmp, " Unique data: ", tmp2
	
	for X in uniqueData:
		print X
		for node in newTree.iter_descendants():
			for a in range(0,2):
				print "P[Z(", node.name,") = ",a,",X|T] = ", lh.calcProbForDataPointAndZ(newTree,X,node.name,a)
			#print "P[X|T] = ",lh.calcProbForDataPoint(newTree,X)
		print "\n"
	

def main():
	global abbrs
	global constNrVertices 
	global constNrOfDatapoints

	totalresults = []
	counter = 0
	constStartingTrees = 1
	constGeneratedTrees = 3
	trees = []
	#testResults = test.testTrees()
	#testResults = test.testTrees2()
	#test.test9()
	#test.test10()
	#test.test11()
	#test.test13()
	#test.test12()

	results, baseline = treeTest.treeTest1(1,3,500,3,abbrs)
	#test.test8()
	#test.test4()
	#test.test6()
	#test.test5()
	#test.test7()

	

	#results, baseline = testingTrees(1,10,100,4,abbrs)
	#print "Results: ", sum(results)/len(results)
	#print "Baseline: ",sum(baseline)/len(baseline)
	"""
	for treeNum in range(constStartingTrees): 
		# =========================================================================
		#		 					Create original tree
		# =========================================================================
		mutations = list(abbrs) # Making a COPY of the mutations.
		tree = et.generate(constNrVertices,mutations,False)
		et.setRandomTreeNodes(tree, False,True)
		print "="*20,"Starting tree", treeNum,"="*20
		fu.printTreeInfo(tree)
		trees.append(tree)
		data = et.createDataHash(tree,constNrOfDatapoints) 
		#attributes = ["name","Px","Z","X"]
		
		# =========================================================================
		#							Create 100(x100) new trees.
		# =========================================================================
		#print "="*35, "   Second tree ", "="*35
		 
		results = []
		results2 = []
		results3 = []
		bestResults = []
		treeProbs = []
		treesWithProbs =[]
		treesWithProbs2 = []
		bestProbs =[]
		
		bestScore = -1000000 # Minus infitive 
		#pxValues = np.arange(0.1,1,0.1)


		
		#testingGround(tree,data)

		
		for newTreeNum in range(constGeneratedTrees): # Create 100 new trees for each starting tree
			print "\n","="*35, " TREE NR: ",newTreeNum, "="*35
			newTree = em.createTreeFromData(data)
			et.setRandomTreeNodes(newTree,False,False)
			fu.printTreeInfo(newTree)
			print "Random tree logL: ",lh.logLikelyhood(newTree,data)
			newTree = em.maximizeTree(newTree,data)
			fu.printTreeInfo(newTree)
			print "Maximized Random tree logL: ",lh.logLikelyhood(newTree,data)
			#newTreeTestingGround(tree,newTree,data)
			trees.append(newTree) # Plots tree
			results.append(et.getSimilarity(et.getEdges(tree),et.getEdges(newTree)))
			newTreeLikelyhood = lh.logLikelyhood(newTree,data)
			#treeProbs.append(newTreeLikelyhood)
			
			
			#print " ------------ EM START --------------"
			#print "Observed mutations: ", em.observedMutationSet(data)
			#print newTree

			#for node in newTree.iter_descendants: 	
			#	print "Node: ", node.name, " parent: ", node.up.name, " Old weigth: ", node.dist, node.Px, " New weigth: ", em.arcWeigth(probsA,probsB,node.name,data,newTree)
			treesWithProbs.append((newTree, newTreeLikelyhood))
			#print "sum(log(P(X|T))) = ",newTreeLikelyhood
			#treesWithProbs2.append((newTree, em.Qfunc(newTree,data)))

			#print " ------------ EM END --------------"
			#string = raw_input("continue")

			# =========================================================================
			#								Testing ground
			# =========================================================================
		
		better = treesWithProbs
		while len(better) > 1:
			tmp = []
			better = em.saveBetterHalf(better)
			for i in range(len(better)):
				tmp.append(et.getSimilarity(et.getEdges(tree),et.getEdges(better[i][0])))


			results2.append(tmp)
		
		better2 = treesWithProbs2
		while len(better2) > 1:
			tmp = []
			better2 = em.saveBetterHalf(better2)
			for i in range(len(better2)):
				tmp.append(et.getSimilarity(et.getEdges(tree),et.getEdges(better2[i][0])))


			results3.append(tmp)
		

		# =========================================================================
		#									MISC
		# =========================================================================
		print "="*30, " Induvidual Results ", "="*30,"\n Number of nodes: ", treeNum
		#print bestResults, bestProbs
		print "Average Results ", sum(results)/len(results) # Induvidual results
		#print "Better halfResults ", sum(results2)/len(results2) # Induvidual results
		#print "BestResults ", sum(bestResults)/len(bestResults) # Induvidual results
		#print "Treeprobs ",treeProbs # Induvidual results
		#print "TreeWithprobs ",treesWithProbs # Induvidual results
		for i in range(len(results2)):
			print i, " set is this good: ", sum(results2[i])/len(results2[i]), len(results2[i])
		#for i in range(len(results3)):
		#	print i, " set is this good: ", sum(results3[i])/len(results3[i]), len(results3[i])
		#constNrVertices += 1
	# =========================================================================
	#								PRINTING RESULTS
	# =========================================================================

	print "\n","="*35, "   OVERALL RESULTS ", "="*35
	#print "Count generated trees: ",len(totalresults)
	#print "Trees created: ", counter
	#print "Similarity between starting tree and gen-tree: ",sum(totalresults)/len(totalresults) 
	#print "Data presents probabilities:", xProbs
		
	# =========================================================================
	#								PLOTTING RESULTS
	# =========================================================================	
	
	def my_layout(node):
		# Add name label to all nodes
		faces.add_face_to_node(AttrFace("name"), node, column=0, position="branch-right")
		faces.add_face_to_node(AttrFace("Px"), node, column=0, position="branch-right")
		#faces.add_face_to_node(AttrFace("Z"), node, column=0, position="branch-right")
		#faces.add_face_to_node(AttrFace("X"), node, column=0, position="branch-right")
	
	ts = TreeStyle()
	ts.show_leaf_name = False
	ts.show_branch_length = True
	ts.layout_fn = my_layout	
	for tmpTree in trees:
		tmpTree.show(tree_style=ts)

	 
	# =========================================================================
	#									MISC
	# =========================================================================
	#print "Get edges: ",tree.get_edges()
	#print len(results["common_edges"])/len(results["source_edges"])
	#print "="*35, "   Edges ", "="*35
	#print "Tree1:",getEdges(tree)
	#print "Tree2:",getEdges(tree2)
	#get_topology_id(attr='name')
	return 0
	"""

main()
print "="*20, "  MAIN END  ", "="*20