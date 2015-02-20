'''
Created on 2015. 2. 9.

@author: Ingoo
'''
'''
procedure prim(G,w)

Input : A connectd undirected graph G = (V,E) with edge weights we
output : A minimum spanning tree defined by the array prev

for all u in V
    cost(u) = inf
    prev(u) = nil
pick any initial node u0
cost(u0) = 0
H = makequeue (v) (priority queue, using cost-values as key)

while H is not empty :
    v = deletemin(H)
    for each {v,z} in E :
        if cost(z) > w(v,z) :
            cost(z) = w(v,z)
            prev(z) = v
'''

import networkx as nx
import matplotlib.pyplot as plt
import copy
pri = nx.Graph()

def prim(G):
    infinite = float("inf")
    for x in G.nodes() :
        G.node[x]['cost'] = infinite
        G.node[x]['prev'] = None
    z = G.nodes()[0]
    G.node[z]['cost'] = 0
    H = copy.copy(G.nodes())
    S = []
    H.pop(H.index(z))
    pri.add_node(z, cost=0)
    S.append(z)
    print(H)
    print(z)
    while H :
        minPre = None
        min = None
        minCost = infinite
        print("S : ", S)
        print("S edges :", G.edges(S))
        for x in S :
            for y in S :
                try : G.remove_edge(x,y)
                except nx.exception.NetworkXError : pass
        for x in G.edges(S,data=True) :
            if x[2].get('weight') < minCost :
                minCost = x[2].get('weight')
                min = x[1]
                minPre = x[0]
        print(min," to ",minPre,' cost with ',minCost)
        pri.add_edge(minPre,min, cost=minCost)
        if min in H :
            H.pop(H.index(min))
            S.append(min)
        else :
            H.pop(H.index(minPre))
            S.append(minPre)

    pos = nx.spring_layout(pri)
    nx.draw_networkx(pri,pos)
    nx.draw_networkx_edge_labels(pri,pos,edge_labels=dict([((u,v),d['cost']) for u,v,d in pri.edges(data=True)]))
    plt.show()


graph = nx.Graph()
nodelist = ['a','b','c','d','e','f']
edgelist = [('a','b',5),('a','c',6),('a','d',4),('b','c',1),('b','d',2),
            ('c','d',2),('c','e',5),('c','f',3),('d','f',4),('e','f',4)]
graph.add_nodes_from(nodelist)
graph.add_weighted_edges_from(edgelist)


prim(graph)