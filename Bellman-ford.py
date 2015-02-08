'''
Created on 2015. 2. 7.

@author: Ingoo
'''
'''
The Bellman-Ford algorithm for single-source shortest paths in general graphs

procedure shortest-paths(G,l,s)
Input : Directed graph G = (V,E);
        edge lengths {l : e in E} with no negative cycles;
        vertex s in V
Output : For all vertices u reachable from s, dist(u is set to the distance from s to u

for all u in V :
    dist(u) = infinite
    prev(u) = nil
    
dist(s) = 0
repeat |v|-1 times :
    for all e in E :
        update(e)

        
procedure update((u,v) in E)
dist(v) = min{ dist(v), dist(u) + l(u,v)}

'''
import networkx as nx
import matplotlib.pyplot as plt

bf = nx.DiGraph()

def bellman_ford(G,s):
    for x in G.nodes() :
        G.node[x]['distance'] = float("inf")
        G.node[x]['prev'] = None
    G.node[s]['distance'] = 0
    for x in range(G.number_of_nodes()-1) :
        for e in G.edges(data=True) :
            G.node[e[1]]['distance'] = min(G.node[e[1]]['distance'],G.node[e[0]]['distance']+e[2].get('weight'))
    for x in G.nodes(data=True) :
        print(x)
            

G = nx.DiGraph()
nodelist = ['s','a','b','c','d','e','f','g']
edgelist = [('s','a',10),('s','g',8),('a','e',2),('b','c',1),
                   ('c','d',3),('d','e',-1),('e','b',-2),('f','a',-4),
                   ('f','e',-1),('g','f',1)]
G.add_nodes_from(nodelist)
G.add_weighted_edges_from(edgelist)

bellman_ford(G,'s')
        