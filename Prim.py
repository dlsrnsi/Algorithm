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
from networkx.exception import NetworkXError
pri = nx.Graph()

def prim(G):
    infinite = float("inf")
    for x in G.nodes() :
        G.node[x]['cost'] = infinite
        G.node[x]['prev'] = None
    z = G.nodes()[0]
    G.node[z]['cost'] = 0
    
    H = list()
    for x in G.nodes() :
        dic = []
        dic.append(G.node[x]['cost'])
        dic.append(x)
        H.append(dic)
        
    while(len(H)!=0) :
        min = H[0]
        for x in H :
            if(x[0]<min[0]) :
                min = x
        u = H.pop(H.index(min))
        pri.add_node(u[1], cost = u[0])
        for x in G.edges(data=True) :
            if(x[0].__eq__(u[1])) :
                for y in H :
                    print(y)
                    if(y[1] == x[1] and y[0]> x[2].get('weight')) :
                        y[0] = x[2].get('weight')
                        for z in G.neighbors(y[1]) :
                            try : pri.remove_edge(z, y[1])
                            except NetworkXError : pass
                        pri.add_edge(u[1], y[1],weight=y[0])
                        print(u[1], " to ", y[1], " through", x[2])
                        pri.node[y[1]]['prev'] = u[1]
    
    pos = nx.spring_layout(pri)
    nx.draw_networkx(pri,pos)
    nx.draw_networkx_edge_labels(pri,pos,edge_labels=dict([((u,v),d['weight']) for u,v,d in pri.edges(data=True)]))
    print(pri.nodes(data=True))
    plt.show()


graph = nx.Graph()
nodelist = ['a','b','c','d','e','f']
edgelist = [('a','b',5),('a','c',6),('a','d',4),('b','c',1),('b','d',2),
            ('c','d',2),('c','e',5),('c','f',3),('d','f',4),('e','f',4)]
graph.add_nodes_from(nodelist)
graph.add_weighted_edges_from(edgelist)


prim(graph)