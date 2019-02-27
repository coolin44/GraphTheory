import numpy
import collections
import sys
import scipy as sp
import copy
import itertools

row = [line.rstrip('\n') for line in open('amTest.txt')]
num_verticies = len(row)
G = numpy.loadtxt("amTest.txt", int)
v = input("Enter a verticy: ")
V = []
for i in range(0, len(G)):
        V.append(i)

total_verts = []
for i in range(0, len(G)):
        total_verts.append(i)


for x in range(0, num_verticies):
        row[x] = row[x].replace(" ", "")
        print(row[x])

def order():
        return num_verticies

def size():
        size = 0
        for i in range(0, order()):
                data = row[i]
                size += sum([int(x) for x in data])
        return size/2

def max_deg():
        max = sum([int(x) for x in row[0]])
        for i in range(0, (num_verticies -1)):
                test1 = row[i]
                test2 = row[i+1]
                if (sum([int(x) for x in test1]))<(sum([int(x) for x in test2])):
                        max = sum([int(x) for x in test2])
        return max

def min_deg():
        min = sum([int(x) for x in row[0]])
        for i in range(0, (num_verticies -1)):
                test1 = row[i]
                test2 = row[i+1]
                if (sum([int(x) for x in test1])) > (sum([int(x) for x in test2])):
                        min = sum([int(x) for x in test2])
        return min

def deg_seq():
        for i in range(0, (num_verticies)):
                sequence = sum([int(x) for x in row[i]])
                print sequence
        return " "

def neighborsSet(v, G):
        neighbors = []
        for i in range(0, len(G)):
                if G[v][i] == 1:
                        neighbors.append(i)
        return neighbors

def neighborhood(V, G):
	listV = list(V)
	neighborhood = []
	for i in range(0, len(V)):
		S = neighborsSet(listV[i], G)
		neighborhood += S
	return set(neighborhood)


def eccentricity(v, G):
	distance = 0
	observe = {v}
	testing = {v}
	tested = [v]
	S = neighborsSet(v, G)
	while len(observe) != len(G):
		observe = observe.union(S)
		testing = observe.difference(tested)
		testList = list(testing)
		tested += testList
		distance += 1
		for i in range(0, (len(testing))):
			S += neighborsSet(testList[i], G)
	return distance 

def radius(G):
	radius = eccentricity(0, G)
	for i in range(1, len(G)):
		if (eccentricity(i, G)) < radius:
			radius = eccentricity(i, G)
	return radius

def diameter(G):
        diameter = eccentricity(0, G)
        for i in range(1, len(G)):
                if (eccentricity(i, G)) > diameter:
                        diameter = eccentricity(i, G)
        return diameter

def isDominating(S, G):
        dominating = False
        x = neighborhood(S, G)
        x = x.union(S)
        x = set(x)
        if len(x) == len(G):        #if neighbors of S and S are full vertice s$
                dominating = True
        return dominating

def dominationNumber(total_verts):
        number = 0
        dominating_set = []
        while (isDominating(dominating_set, G) == False):
                a = sort(total_verts)
                del total_verts[a-number]
                dominating_set.append(a)
                number+=1
        return number

def totalDominationNumber():
	verts = []
	for i in range(0, len(G)):
        	verts.append(i)
        number = 0
        dominating_set = []
        while (isDominating(dominating_set, G) == False):
                a = sort(verts)
                del verts[a-number]
                dominating_set.append(a)
                number+=1
        for i in range(0, len(dominating_set)):
                if dominating_set not in neighborsSet(dominating_set[i], G):
                        a = list(neighborsSet(dominating_set[i], G))
                        dominating_set.append(a[0])
                        number += 1
                        del verts[i]
        return number



def sort(total_verts):
        highest_deg = total_verts[0]
        most_neighbors = neighborsSet(total_verts[0], G)
         for b in range (1, len(total_verts)):
                a = neighborsSet(total_verts[b], G)
                if len(a) > len(most_neighbors):
                        most_neighbors = a
                        highest_deg = total_verts[b]
        return highest_deg

def isIndependent(S, G):
        independent = False
        if neighborhood(S, G).intersection(S) == set():
                independent = True

        return independent


def independenceNum(G):
        S = set()
        for i in range(len(G), 1, -1):
                for s in set(itertools.combinations(V, i)):
                        if isIndependent(s, G) == True:
                                S = s
                                return len(S)




#def chromaticN(G):
#	test = []
#	num_of_colors = 0
#	for i in range(0, len(G)):
#		test += set(neighborsSet(i, G))
#	for j in range(0, len(G)):
#		a = set(test[j])
#		b = set(test[j+1])
#		c = set(a.intersection(b))
#		if (len(c) > 0):
#			num_of_colors += 1
#	return num_of_colors

def compliment(G):
        C = copy.deepcopy(G)

        for i in range(0, len(C)):
                for j in range(0, len(G)):
                        if C[i][j] == 0:
                                C[i][j] = 1
                        else:
                                C[i][j] = 0
        return C
comp = compliment(G)

def cliqueNum(G):
	return (num_verticies - independenceNum(G))




print "The order is: ", order()
print "The size is: ", size()
print "The max degree is: ", max_deg()
print "The min degree is: ", min_deg()
print "The degree sequence is: "
print deg_seq()
print "The vertex eccentricity is: ", eccentricity(v, G)	
print "The radius is: ", radius(G)
print "The diameter is: ", diameter(G)
print "The domination number is: ", dominationNumber(total_verts)
print "The total domination number is: ", totalDominationNumber()
print "The independence number is : ", independenceNum(G)
print "The clique number of graph G is: ", cliqueNum(G)
