import eteTree as et
import functions as fu
from abberations import abberations as abbrs
"""
import likelyhood as lh
import likelyhood2 as lh2
import likelyhood3 as lh3
"""
import likelyhood4 as lh4
import math as math
import emAlgorithm as em
import numpy as np
import functions as fu
import copy as copy

def testDataPoint(tree,X):		
	#print X, lh.likelyhoodOfX(tree1,X), lh.likelyhoodOfX2(tree1,X), lh.likelyhoodOfX3(tree1,X)
	for node in tree.iter_descendants():
		tmp = lh.likelyhoodOfXandZ(tree,X,node.name,1)/lh.likelyhoodOfX2(tree,X) + lh.likelyhoodOfXandZ(tree,X,node.name,0)/lh.likelyhoodOfX2(tree,X)
		if (tmp != 1):
			print lh.likelyhoodOfXandZ(tree,X,node.name,1)/lh.likelyhoodOfX(tree,X) + lh.likelyhoodOfXandZ(tree,X,node.name,0)/lh.likelyhoodOfX(tree,X)
			print lh.likelyhoodOfXandZ(tree,X,node.name,1)/lh.likelyhoodOfX2(tree,X) + lh.likelyhoodOfXandZ(tree,X,node.name,0)/lh.likelyhoodOfX2(tree,X)
			print node.name,"= 1,",lh.likelyhoodOfXandZ(tree,X,node.name,1)
			print node.name, "= 0,", lh.likelyhoodOfXandZ(tree,X,node.name,0)
			print node
			raw_input("continue")
		else:
			continue



def testTrees2():
	print "="*20, " TEST 2 ","="*20
	mutations1 = list(abbrs)
	tree1 = et.generate(3,mutations1,False, False) # small one-lvl tree 
	tree1 = et.setRandomTreeNodes(tree1,Px = 0.8, test = True)
	data1 = et.createDataHash(tree1, 1000)
	data1 = fu.uniqueData(data1)
	
	fu.printTreeInfo(tree1)
	print len(data1)
	raw_input("continue\n")
	
	fu.sortData(data1)
	for X in data1:
		testDataPoint(tree1,X)

def test3():
	print "="*20, " TEST 3 ","="*20
	mutations = list(abbrs)
	tree = et.generate(2,mutations,False, False) # small one-lvl tree 
	tree = et.setRandomTreeNodes(tree,Px = 0.8, test = True)
	data = et.createDataHash(tree, 1000)
	data = fu.uniqueData(data)
	data = fu.sortData(data)
	fu.printTreeInfo(tree)
	for X in data: 
		print X, lh.likelyhoodOfX(tree,X)
		print X, lh.likelyhoodOfX2(tree,X)
	


def testTrees():
	print "="*20, " TEST 1 ","="*20
	mutations1 = list(abbrs)
	tree1 = et.generate(3,mutations1,False, True) # small one-lvl tree 
	tree1 = et.setRandomTreeNodes(tree1,Px = 0.8, test = True)
	data1 = et.createDataHash(tree1, 100)
	data1 = fu.uniqueData(data1)
	fu.printTreeInfo(tree1)
	fu.sortData(data1)
	print "P[",data1[0],"|T]", lh.likelyhoodOfX(tree1,data1[0]), 0.9*0.8*0.9*0.8
	print "P[",data1[1],"|T]", lh.likelyhoodOfX(tree1,data1[1]), 0.9*0.8*(0.1+0.9*0.2)
	print "P[",data1[2],"|T]", lh.likelyhoodOfX(tree1,data1[2]), 0.9*0.8*(0.1+0.9*0.2)
	print "P[",data1[3],"|T]", lh.likelyhoodOfX(tree1,data1[3]), (0.1+0.9*0.2)*(0.1+0.9*0.2)
	print "P[",data1[0],"|T]", lh2.calcProbForX(tree1,data1[0]), 0.9*0.8*0.9*0.8
	print "P[",data1[1],"|T]", lh2.calcProbForX(tree1,data1[1]), 0.9*0.8*(0.1+0.9*0.2)
	print "P[",data1[2],"|T]", lh2.calcProbForX(tree1,data1[2]), 0.9*0.8*(0.1+0.9*0.2)
	print "P[",data1[3],"|T]", lh2.calcProbForX(tree1,data1[3]), (0.1+0.9*0.2)*(0.1+0.9*0.2)
	print "="*20," TEST 1.2 ","="*20
	mutations2 = list(abbrs)
	tree2 = et.generate(3,mutations1,  True, False) # small one-lvl tree 
	tree2 = et.setRandomTreeNodes(tree2,Px= 0.8, test = True)
	data2 = et.createDataHash(tree2, 100)
	data2 = fu.uniqueData(data2)
	fu.printTreeInfo(tree2)
	fu.sortData(data2)
	print "P[",data2[0],"|T]", lh.likelyhoodOfX(tree2,data2[0]), 0.9*0.8*0.9*0.8
	print "P[",data2[1],"|T]", lh.likelyhoodOfX(tree2,data2[1]), 0.9*0.8*(0.1+0.9*0.2)
	print "P[",data2[2],"|T]", lh.likelyhoodOfX(tree2,data2[2]), 0.9*0.2*(0.9*0.8)
	print "P[",data2[3],"|T]", lh.likelyhoodOfX(tree2,data2[3]), 0.1+(0.9*0.2*(0.1+0.9*0.2))#(0.1+0.9*0.1)*(0.1+0.9*0.1)
	print "P[",data2[0],"|T]", lh2.calcProbForX(tree2,data2[0]), 0.9*0.8*0.9*0.8
	print "P[",data2[1],"|T]", lh2.calcProbForX(tree2,data2[1]), 0.9*0.8*(0.1+0.9*0.2)
	print "P[",data2[2],"|T]", lh2.calcProbForX(tree2,data2[2]), 0.9*0.2*(0.9*0.8)
	print "P[",data2[3],"|T]", lh2.calcProbForX(tree2,data2[3]), 0.1+(0.9*0.2*(0.1+0.9*0.2))#(0.1+0.9*0.1)*(0.1+0.9*0.1)

	print "="*20," TEST 1.3 ","="*20
	mutations3 = list(abbrs)
	tree3 = et.generate(2,mutations3,  True, False) # small one-lvl tree 
	tree3 = et.setRandomTreeNodes(tree3,Px= 0.8, test = True)
	data3 = et.createDataHash(tree3, 100)
	data3 = fu.uniqueData(data3)
	fu.printTreeInfo(tree3)
	print data3
	print "P[",data3[0],"|T]", lh.likelyhoodOfX(tree3,data3[0]), 0.9*0.8
	print "P[",data3[1],"|T]", lh.likelyhoodOfX(tree3,data3[1]), (0.1+0.9*0.2)
	print "P[ Z(M85) = 0,",data3[0],"|T]", lh.likelyhoodOfXandZ(tree3,data3[0],"[M85]",0), 0.05
	print "P[ Z(M85) = 1,",data3[0],"|T]", lh.likelyhoodOfXandZ(tree3,data3[0],"[M85]",1), 0.9*0.8
	print "P[ Z(M85) = 0,",data3[1],"|T]", lh.likelyhoodOfXandZ(tree3,data3[1],"[M85]",0), 0.1
	print "P[ Z(M85) = 1,",data3[1],"|T]", lh.likelyhoodOfXandZ(tree3,data3[1],"[M85]",1), 0.18
	print 1, "=",  lh.likelyhoodOfXandZ(tree3,data3[0],"[M85]",0)/lh.likelyhoodOfX(tree3,data3[0]),"+", lh.likelyhoodOfXandZ(tree3,data3[0],"[M85]",1)/lh.likelyhoodOfX(tree3,data3[0]), lh.likelyhoodOfXandZ(tree3,data3[0],"[M85]",1)/lh.likelyhoodOfX(tree3,data3[0]) + lh.likelyhoodOfXandZ(tree3,data3[0],"[M85]",0)/lh.likelyhoodOfX(tree3,data3[0])
	print 1, "=",  lh.likelyhoodOfXandZ(tree3,data3[1],"[M85]",0)/lh.likelyhoodOfX(tree3,data3[1]),"+", lh.likelyhoodOfXandZ(tree3,data3[1],"[M85]",1)/lh.likelyhoodOfX(tree3,data3[1]), lh.likelyhoodOfXandZ(tree3,data3[1],"[M85]",1)/lh.likelyhoodOfX(tree3,data3[1]) + lh.likelyhoodOfXandZ(tree3,data3[1],"[M85]",0)/lh.likelyhoodOfX(tree3,data3[1])
	
	print "P[",data3[0],"|T]", lh2.calcProbForX(tree3,data3[0]), 0.9*0.8
	print "P[",data3[1],"|T]", lh2.calcProbForX(tree3,data3[1]), (0.1+0.9*0.2)
	print "P[ Z(M85) = 0,",data3[0],"|T]", lh2.calcProbForXandZ(tree3,data3[0],"[M85]",0), 0.05
	print "P[ Z(M85) = 1,",data3[0],"|T]", lh2.calcProbForXandZ(tree3,data3[0],"[M85]",1), 0.9*0.8
	print "P[ Z(M85) = 0,",data3[1],"|T]", lh2.calcProbForXandZ(tree3,data3[1],"[M85]",0), 0.1
	print "P[ Z(M85) = 1,",data3[1],"|T]", lh2.calcProbForXandZ(tree3,data3[1],"[M85]",1), 0.18
	fu.printTreeInfo(tree3)
	print tree3, data3[0]
	print "SLASK: ", lh2.calcProbForX(tree3,data3[0])
	print 1, "=",  lh2.calcProbForXandZ(tree3,data3[0],"[M85]",0)/lh2.calcProbForX(tree3,data3[0]),"+", lh2.calcProbForXandZ(tree3,data3[0],"[M85]",1)/lh2.calcProbForX(tree3,data3[0]), lh2.calcProbForXandZ(tree3,data3[0],"[M85]",1)/lh2.calcProbForX(tree3,data3[0]) + lh2.calcProbForXandZ(tree3,data3[0],"[M85]",0)/lh2.calcProbForX(tree3,data3[0])
	print 1, "=",  lh2.calcProbForXandZ(tree3,data3[1],"[M85]",0)/lh2.calcProbForX(tree3,data3[1]),"+", lh2.calcProbForXandZ(tree3,data3[1],"[M85]",1)/lh2.calcProbForX(tree3,data3[1]), lh2.calcProbForXandZ(tree3,data3[1],"[M85]",1)/lh2.calcProbForX(tree3,data3[1]) + lh2.calcProbForXandZ(tree3,data3[1],"[M85]",0)/lh2.calcProbForX(tree3,data3[1])
	
	#print data2[1], lh.likelyhoodOfX(tree2,data2[1]), 0.9*0.8*(0.1+0.9*0.2)
	#print data2[2], lh.likelyhoodOfX(tree2,data2[2]), 0.9*0.2*(0.9*0.8)
	#print data2[3], lh.likelyhoodOfX(tree2,data2[3]), 0.1+(0.9*0.2*(0.1+0.9*0.2))#(0.1+0.9*0.1)*(0.1+0.9*0.1)


def test4():
	print "="*20, " TEST 4 ","="*20
	mutations = list(abbrs)
	tree = et.generate(30,mutations,False, False) # small one-lvl tree 
	tree = et.setRandomTreeNodes(tree)
	data = et.createDataHash(tree, 2000)
	data = fu.uniqueData(data)
	fu.printTreeInfo(tree)
	fu.sortData(data)
	for X in data: 
		print  lh.likelyhoodOfX2(tree,X) - lh.likelyhoodOfX3(tree,X),
	return None

def test5():
	print "\n","="*20, " TEST 5 , One Child trees","="*20
	tCounter = 0
	fCounter = 0
	for treeSize in range(2,10):	
		mutations = list(abbrs)
		tree = et.generate(treeSize,mutations,True, False) # small one-lvl tree 
		tree = et.setRandomTreeNodes(tree,test=True)
		data = et.createDataHash(tree, 2000)
		data = fu.uniqueData(data)
		fu.printTreeInfo(tree)
		fu.sortData(data)
		for X in data: 
			tmp = lh2.calcProbForX(tree,X)
			for node in tree.iter_descendants():
				
				tCounter+=1
				if (abs(((lh2.calcProbForXandZ(tree,X,node.name,1)/tmp) + (lh2.calcProbForXandZ(tree,X,node.name,0)/tmp)) - 1.0) > 0.001):
					fCounter+=1
					print  treeSize,tree, "\n",X,node.name
					print "P[X|T] = ", tmp
					print 1, " = ",(lh2.calcProbForXandZ(tree,X,node.name,1)/tmp) + (lh2.calcProbForXandZ(tree,X,node.name,0)/tmp)
					print lh2.calcProbForXandZ(tree,X,node.name,1)
					print lh2.calcProbForXandZ(tree,X,node.name,0)
				
					raw_input("continue")
				#if (1 != ((lh2.calcProbwithZ(tree,X,node.name,1)/tmp) + (lh2.calcProbwithZ(tree,X,node.name,0)/tmp))):
		print " TEST 5 TreeSize: ",treeSize, tCounter-fCounter, " out of ", tCounter, "were Successful"
		tCounter = 0
		fCounter = 0
	return None

def test6():
	print "\n","="*20, " TEST 6, One Level Trees ","="*20
	tCounter = 0
	fCounter = 0
		
	for treeSize in range(2,10):	
		mutations = list(abbrs)
		tree = et.generate(treeSize,mutations,False, True) # small one-lvl tree 
		tree = et.setRandomTreeNodes(tree)
		data = et.createDataHash(tree, 2000)
		data = fu.uniqueData(data)
		#fu.printTreeInfo(tree)
		fu.sortData(data)
		for X in data: 
			tmp = lh2.calcProbForX(tree,X)
			for node in tree.iter_descendants():
				
				tCounter +=1
				if (abs(((lh2.calcProbForXandZ(tree,X,node.name,1)/tmp) + (lh2.calcProbForXandZ(tree,X,node.name,0)/tmp)) - 1.0) > 0.001):
					fCounter +=1
					#print  treeSize,tree, "\n",X,node.name
					#print "P[X|T] = ", tmp
					#print 1, " = ",(lh2.calcProbForXandZ(tree,X,node.name,1)/tmp) + (lh2.calcProbForXandZ(tree,X,node.name,0)/tmp)
					#print lh2.calcProbForXandZ(tree,X,node.name,1)
					#print lh2.calcProbForXandZ(tree,X,node.name,0)
				
					#raw_input("continue")
				#if (1 != ((lh2.calcProbwithZ(tree,X,node.name,1)/tmp) + (lh2.calcProbwithZ(tree,X,node.name,0)/tmp))):
		print " TEST 6 TreeSize: ",treeSize, tCounter-fCounter, " out of ", tCounter, "were Successful"
		tCounter = 0
		fCounter = 0

	return None


def test8():
	print "="*20, "Test 8.1, One level trees", "="*20
	for treeSize in range(2,10):
		mutations = list(abbrs)
		tree = et.generate(treeSize,mutations,False,True)
		tree = et.setRandomTreeNodes(tree, test = False)
		data = fu.getAllDataPoints(tree)
		#fu.printTreeInfo(tree)
		tmp = []
		for X in data:
			tmp.append( lh2.calcProbForX(tree,X))
		#if sum(tmp) != 1:
			#fu.printTreeInfo(tree)
			#print tmp
			#raw_input("continue")
		print " TEST 8.1 TreeSize: ",treeSize, len(data), sum(tmp)
		#print data
	print "="*20, "Test 8.2", "="*20
	for treeSize in range(2,10):
		mutations = list(abbrs)
		tree = et.generate(treeSize,mutations,True,False)
		tree = et.setRandomTreeNodes(tree,test = True, Px = 0.95, Pz = 0.5)
		data = fu.getAllDataPoints(tree)
		#fu.printTreeInfo(tree)
		tmp = []
		for X in data:
			tmp.append( lh2.calcProbForX(tree,X))
		if sum(tmp) != 1:
			fu.printTreeInfo(tree)

			print tmp, sum(tmp), data
			raw_input("continue")
		print " TEST 8.2 TreeSize: ",treeSize, len(data), sum(tmp)
		#print data
	print "="*20, "Test 8.3", "="*20
	for treeSize in range(2,10):
		mutations = list(abbrs)
		tree = et.generate(treeSize,mutations,False,False)
		tree = et.setRandomTreeNodes(tree)
		data = fu.getAllDataPoints(tree)
		#fu.printTreeInfo(tree)
		tmp = 0
		for X in data:
			tmp += lh2.calcProbForX(tree,X)
		print " TEST 8.3 TreeSize: ",treeSize, len(data), tmp
		#print data


def test9():
	print "="*20, "Test 9.1, One level trees", "="*20
	for treeSize in range(2,10):
		mutations = list(abbrs)
		tree = et.generate(treeSize,mutations,False,True)
		tree = et.setRandomTreeNodes(tree, test = False)
		data = fu.getAllDataPoints(tree)
		#fu.printTreeInfo(tree)
		tmp = []
		for X in data:
			tmp.append( lh4.calcProb_X(tree,X))
		if (abs(sum(tmp) - 1) > 0.0000001):
			fu.printTreeInfo(tree)
			print tmp, sum(tmp), data
			raw_input("continue")
		print " TEST 9.1 TreeSize: ",treeSize, len(data), sum(tmp)
		#print data
	print "="*20, "Test 9.2", "="*20
	for treeSize in range(2,10):
		mutations = list(abbrs)
		tree = et.generate(treeSize,mutations,True,False)
		tree = et.setRandomTreeNodes(tree,test = True, Px = 0.95, Pz = 0.5)
		data = fu.getAllDataPoints(tree)
		#fu.printTreeInfo(tree)
		tmp = []
		for X in data:
			tmp.append( lh4.calcProb_X(tree,X))
		if (abs(sum(tmp) - 1) > 0.0000001):
			fu.printTreeInfo(tree)

			print tmp, sum(tmp), data
			raw_input("continue")
		print " TEST 9.2 TreeSize: ",treeSize, len(data), sum(tmp)
		#print data
	print "="*20, "Test 9.3", "="*20
	for treeSize in range(2,10):
		mutations = list(abbrs)
		tree = et.generate(treeSize,mutations,False,False)
		tree = et.setRandomTreeNodes(tree)
		data = fu.getAllDataPoints(tree)
		#fu.printTreeInfo(tree)
		tmp = 0
		for X in data:
			tmp += lh4.calcProb_X(tree,X)
		print " TEST 9.3 TreeSize: ",treeSize, len(data), tmp
		#print data


def test10():
	print "\n","="*20, " TEST 10, ","="*20
	tCounter = 0
	fCounter = 0
		
	for treeSize in range(2,10):	
		mutations = list(abbrs)
		tree = et.generate(treeSize,mutations,False, False) # small one-lvl tree 
		tree = et.setRandomTreeNodes(tree)
		data = fu.getAllDataPoints(tree)
		#fu.printTreeInfo(tree)
		fu.sortData(data)
		for X in data: 
			tmp = lh4.calcProb_X(tree,X)
			for node in tree.iter_descendants():
				
				tCounter +=1
				if (abs(((lh4.calcProb_X_Z(tree,X,node.name,1)/tmp) + (lh4.calcProb_X_Z(tree,X,node.name,0)/tmp)) - 1.0) > 0.00001):
					fCounter +=1
					#print  treeSize,tree, "\n",X,node.name
					#print "P[X|T] = ", tmp
					#print 1, " = ",(lh2.calcProbForXandZ(tree,X,node.name,1)/tmp) + (lh2.calcProbForXandZ(tree,X,node.name,0)/tmp)
					#print lh2.calcProbForXandZ(tree,X,node.name,1)
					#print lh2.calcProbForXandZ(tree,X,node.name,0)
				
					#raw_input("continue")
				#if (1 != ((lh2.calcProbwithZ(tree,X,node.name,1)/tmp) + (lh2.calcProbwithZ(tree,X,node.name,0)/tmp))):
		print " TEST 10 TreeSize: ",treeSize, tCounter-fCounter, " out of ", tCounter, "were Successful, len(data): ", len(data)
		tCounter = 0
		fCounter = 0

	return None

def test11():
	print "\n","="*20, " TEST 11, ","="*20
	tCounter = 0
	fCounter = 0
		
	for treeSize in range(2,10):	
		mutations = list(abbrs)
		tree = et.generate(treeSize,mutations,False, False) # small one-lvl tree 
		tree = et.setRandomTreeNodes(tree, Pz = 0.6, Px = 0.95, test = True)
		tree = et.setRandomTreeNodes(tree)
		data = fu.getAllDataPoints(tree)
		#fu.printTreeInfo(tree)
		fu.sortData(data)
		allPoints = []
		for X in data: 
			tmp = lh4.calcProb_X(tree,X)
			for node in tree.iter_descendants():
				tCounter +=1
				if not node.is_root():
					for a in range(0,2):
						p_x_Zp = (lh4.calcProb_X_Z(tree,X,node.up.name,a))
						p_X_Z0_Zp = lh4.calcProb_X_Z_Zp(tree,X,node.name,0,node.up.name,a)
						p_X_Z1_Zp = lh4.calcProb_X_Z_Zp(tree,X,node.name,1,node.up.name,a)
						#fu.printTreeInfo(tree)
						#print X,"\n", node.up.name," = ", a, node.name
						#print  p_x_Zp, p_X_Z0_Zp, p_X_Z1_Zp, 
						#raw_input("Continue1")
						if (abs(p_X_Z1_Zp+p_X_Z0_Zp-p_x_Zp) > 0.0000000001):
							fu.printTreeInfo(tree)
							print X,"\n", node.up.name," = ", a, node.name
							print  p_x_Zp, p_X_Z0_Zp, p_X_Z1_Zp, 
							raw_input("Continue2")
		print " TEST 11 TreeSize: ",treeSize, tCounter-fCounter, " out of ", tCounter, "were Successful, len(data): ", len(data)
		tCounter = 0
		fCounter = 0

	return None


def test12():
	print "Example 1, small 3 level tree"
	for treeSize in range(2,10):	
		mutations = list(abbrs)
		tree = et.generate(treeSize,mutations,False, False) # small one-lvl tree 
		tree = et.setRandomTreeNodes(tree, Pz = 0.6, Px = 0.95, test = True)
		data = fu.getAllDataPoints(tree)
		fu.printTreeInfo(tree)
		for X in data:
			p_X = lh4.calcProb_X(tree,X)
			print "\nP[",X,"|T] = ", p_X
			for node in tree.iter_descendants():
				
				p_X_Zp1 = lh4.calcProb_X_Z(tree,X,node.up.name,1)
				p_X_Zp0 = lh4.calcProb_X_Z(tree,X,node.up.name,0)
				print "p(", node.name,") = ",node.up.name
				print "P[z(",node.up.name,") = 1, X, | T] = ",p_X_Zp1
				print "P[z(",node.up.name,") = 0, X, | T] = ",p_X_Zp0
				if not node.is_root():

					p_X_Z1_Zp0 = lh4.calcProb_X_Z_Zp(tree,X,node.name,1, node.up.name, 0)
					p_X_Z1_Zp1 = lh4.calcProb_X_Z_Zp(tree,X,node.name,1, node.up.name, 1)
					p_X_Z0_Zp0 = lh4.calcProb_X_Z_Zp(tree,X,node.name,0, node.up.name, 0)
					p_X_Z0_Zp1 = lh4.calcProb_X_Z_Zp(tree,X,node.name,0, node.up.name, 1)
					print "P[z(",node.name,") = 1, z(",node.up.name,")= 1, X, | T] = ", p_X_Z1_Zp1
					print "P[z(",node.name,") = 0, z(",node.up.name,")= 1, X, | T] = ", p_X_Z0_Zp1
					print "P[z(",node.name,") = 1, z(",node.up.name,")= 0, X, | T] = ", p_X_Z1_Zp0
					print "P[z(",node.name,") = 0, z(",node.up.name,")= 0, X, | T] = ", p_X_Z0_Zp0
					print "P[z(",node.up.name,")) = 1, X, | T] = ", p_X_Zp1
					print "P[z(",node.up.name,")) = 0, X, | T] = ", p_X_Zp0
					tmp = p_X_Z1_Zp0 + p_X_Z0_Zp0 - p_X_Zp0
					tmp2 = 100000 + tmp
					if not ( tmp2 == 100000):
						raw_input("MAJOR ERROR")
					
					#,(p_X_Z0_Zp1 + p_X_Z1_Zp1) - p_X_Zp1, p_X_Zp1, p_X_Z1_Zp0, p_X_Z1_Zp1
					#print " 0 = ",(p_X_Z0_Zp0 + p_X_Z1_Zp0) - p_X_Zp0, p_X_Zp0, p_X_Z0_Zp0, p_X_Z0_Zp1
					


def test13():
	print "Example 2, small 2 level tree"
	print """
	P[!X|T] = 0.59
	P[X|T] = 0.41
	"""
	mutations = list(abbrs)
	tree = et.generate(2,mutations,True, False) # small one-lvl tree 
	tree = et.setRandomTreeNodes(tree, Pz = 0.6, Px = 0.95, test = True)
	data = fu.getAllDataPoints(tree)
	fu.printTreeInfo(tree)
	for X in data:
		p_X = lh4.calcProb_X(tree,X)
		print X, p_X
		
		for node in tree.iter_descendants():
			print node.name
			print "Z(",node.name,") =", 1,lh4.calcProb_X_Z(tree,X,node.name,1), "= 0.57"
			print "Z(",node.name,") =", 0,lh4.calcProb_X_Z(tree,X,node.name,0), "= 0.02"
			if node.is_leaf():
				print lh4.calcProb_X_Z_Zp(tree,X,node.name,0, node.up.name, 0)
				print lh4.calcProb_X_Z_Zp(tree,X,node.name,0, node.up.name, 1)
				print lh4.calcProb_X_Z_Zp(tree,X,node.name,1, node.up.name, 0)
				print lh4.calcProb_X_Z_Zp(tree,X,node.name,1, node.up.name, 1)
