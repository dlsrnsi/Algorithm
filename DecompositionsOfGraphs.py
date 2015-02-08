'''
Created on 2015. 2. 6.

@author: Ingoo
'''
"""
procedure explore(G,v)
Input : G = (V,E) is a graph; v in V
Output : Visited(u) is set to true for all nodes u reachable from v

visited(v) = true
previsit(v)
for each edge (v, u) in E :
    if visited(u) = False :
        explore(u)
postvisit(v)

procedure dfs(G)
for all v in V :
    visited(v) = False
for all v in V :
    if visited(v) = False :
        explore(v)
"""
import networkx as nx
import matplotlib.pyplot as plt

clock = 1
DFS = nx.DiGraph()

    
def explore(G, v):
    global DFS
    DFS.add_node(v)
    G.node[v]['visited'] = True
    previsit(G,v)
    print(v, end = " ")
    for x in G.edges() :
        if(x[0].__eq__(v) and G.node[x[1]]['visited'] == False) :
            DFS.add_edge(x[0], x[1])
            explore(G, x[1])
    postvisit(G,v)  
          
def previsit(G, v):
    global clock
    G.node[v]['pre'] = clock
    clock += 1
    
def postvisit(G, v):
    global clock
    G.node[v]['post'] = clock
    clock += 1
                
def dfs(G):
    global clock
    clock = 1
    for x in G.nodes() :
        G.node[x]['visited'] = False
    for x in G.nodes() :
        if(G.node[x]['visited'] == False) :
            explore(G, x)
    result = list(zip(G.nodes(data=True)))
    print(result)
    nx.draw_networkx(DFS)
    plt.show()



nodelist = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
edgelist = [('a', 'b'), ('a', 'c'), ('a', 'f'), ('b', 'e'),
            ('c', 'd'), ('d', 'a'), ('e', 'f'), ('e', 'g'),
            ('e', 'h'), ('f', 'g'), ('h', 'g')]  # construct Graph

G = nx.DiGraph()
G.add_nodes_from(nodelist)
G.add_edges_from(edgelist)
print(list(G.nodes_iter()))
dfs(G)