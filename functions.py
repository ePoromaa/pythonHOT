#
#import emAlgorithm as em
import emAlgorithm2 as em2

def uniqueData(data): # returns a list of only unique datapoints
	ret = []
	for i in data:
		if i not in ret:
			ret.append(i)
	return ret


def printTreeInfo(tree):
	print "="*20,"Tree Info:","="*20,
	print tree
	for node in tree.traverse():
		print node.name, node.Pz, node.Px, node.Ez, node.Ex

def printTreeInfo2(tree,data):
	print "="*20,"Tree Info:","="*20,
	print tree
	probsA = em2.probListA(tree,data)
	probsB = em2.probListB(tree,data)
	tot = 0
	for node in tree.iter_descendants():
		tmp = em2.arcWeigth(probsA,probsB,node.name,node.up.name,data,tree)
		print node.name, node.Pz, node.Px, tmp
		tot += tmp
	print "Qvalue: ", tot


def sortData(data):
	data.sort(reverse = True)
	return data

def getOpposite(X):
	tmp = list(X)
	tmpD = {}
	for mutation in tmp:
		if mutation == "root":
			tmpD[mutation] = X[mutation]
		else:
			tmpD[mutation] = not X[mutation]
	#print X, tmp,tmpD
	return tmpD

def binary(length,number):
	string = bin(number)[2:].zfill(length)
	temp = []
	for i in string:
		temp.append(int(i))

	return temp


def getAllDataPoints(tree):
	data = []
	mutList = []
	for node in tree.iter_descendants():
		mutList.append(node.name)
	all_combos = []
	for i in range(0,2**len(mutList)):
		tmp = {}
		tmp2 = binary(len(mutList),i)
		tmp["root"] = True
		for k in range(len(tmp2)):
			tmp[mutList[k]] = bool(tmp2[k])
		data.append( tmp)
	return data
	