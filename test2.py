test2.py


def testWide():
	print "\n","="*20, " TEST W ","="*20
	for treeSize in range(10):	
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
				
				
				if (abs(((lh2.calcProbForXandZ(tree,X,node.name,1)/tmp) + (lh2.calcProbForXandZ(tree,X,node.name,0)/tmp)) - 1.0) > 0.001):
					print  treeSize,tree, "\n",X,node.name
					print "P[X|T] = ", tmp
					print 1, " = ",(lh2.calcProbForXandZ(tree,X,node.name,1)/tmp) + (lh2.calcProbForXandZ(tree,X,node.name,0)/tmp)
					print lh2.calcProbForXandZ(tree,X,node.name,1)
					print lh2.calcProbForXandZ(tree,X,node.name,0)
				
					raw_input("continue")
				#if (1 != ((lh2.calcProbwithZ(tree,X,node.name,1)/tmp) + (lh2.calcProbwithZ(tree,X,node.name,0)/tmp))):
				
	return None

def testDeep():
	print "\n","="*20, " TEST D ","="*20
