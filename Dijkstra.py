'''
Created on 2015. 2. 7.

@author: Ingoo
'''
'''
procedure dkjkstra(G,l,s)
Input : Graph G = (V, E). directed or undirected
        positive edge lengths {l : e in E}; vertex s in V
Output : For all vertices u reachable from s, dist(u) is set
         to the distance from s to u
for all u in V
    dist(u) = infinite
    prev(u) = nil
dist(s) = 0

H = makequeue(V) (using dist-values as keys)
while H is not empty :
    u = deletemin(H)
    for all edges (u,v) in E:
        if dist(v) > dist(u) + l(u,v) :
            dist(v) = dist(u) + l(u,v)
            prev(v) = u
            decreasekey(H,v)
'''

import networkx as nx
import matplotlib.pyplot as plt
from networkx.exception import NetworkXError
dij = nx.DiGraph()

def dijkstra(G,s):
    infinite = float("inf")
    for x in G.nodes() :
        G.node[x]['distance'] = infinite
        G.node[x]['prev'] = None
    G.node[s]['distance'] = 0
    
    H = list()
    for x in G.nodes() :
        dic = []
        dic.append(G.node[x]['distance'])
        dic.append(x)
        H.append(dic)
        
    while(len(H)!=0) :
        min = H[0]
        for x in H :
            if(x[0]<min[0]) :
                min = x
        u = H.pop(H.index(min))
        dij.add_node(u[1], distance = u[0])
        for x in G.edges(data=True) :
            if(x[0].__eq__(u[1])) :
                for y in H :
                    if(y[1] == x[1] and y[0]> u[0] + x[2].get('weight')) :
                        y[0] = u[0] + x[2].get('weight')
                        for z in G.predecessors(y[1]) :
                            try : dij.remove_edge(z, y[1])
                            except NetworkXError : pass
                        dij.add_edge(u[1], y[1])
                        print(u[1], " to ", y[1], y[0], " through", x[2])
                        dij.node[y[1]]['prev'] = u[1]
                        dij.node[y[1]]['distance'] = y[0]
    
    nx.draw_networkx(dij)
    print(dij.nodes(data=True))
    plt.show()


graph = nx.DiGraph()
nodelist = ['a','b','c','d','e']
edgelist = [('a','b',4),('a','c',2),('b','c',3),('b','d',2),('b','e',3),
                  ('c','b',1),('c','d',4),('c','e',5),('e','d',1)]
graph.add_nodes_from(nodelist)
graph.add_weighted_edges_from(edgelist)


dijkstra(graph,'a')



