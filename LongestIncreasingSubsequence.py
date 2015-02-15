'''
Created on 2015. 2. 15.

@author: dlsrn_000
'''
'''
for j = 1, 2, ... n :
    L(j) = 1 + max{L(i) : (i,j) in E }
return maxjL(j)
'''
import networkx as nx
import matplotlib as plt

lis = nx.DiGraph()

def LIS(list):
    num = 1
    result = [1 for x in range(len(list))]
    for x in list :
        for y in list[num:] :
            if y > x :
                lis.add_edge(x,y)
        num += 1
    print(lis.edges())
    for j in range(1,len(list)) :
        print("node : ", list[j])
        edge = [y for y in lis.in_edges(list[j])]
        print("edge :", edge)
        i = [x[0] for x in edge]
        try : 
            print("L(i) : ", [result[list.index(x)] for x in i])
            result[j] = 1 + max([result[list.index(x)] for x in i])
            print("result : ",result)
        except : result[j] = 1
    return max(result)

list = [5,2,8,10,3,6,9,7]
print(LIS(list))