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
clock = 1

class Graph :
    nodelist = []
    edgelist = []
    visited = []
    pre = []
    post = []
    
def explore(G, v):
    G.visited[G.nodelist.index(v)] = True
    previsit(G,v)
    print(v, end = " ")
    for x in G.edgelist :
        if(x[0].__eq__(v) and G.visited[G.nodelist.index(x[1])] == False) :
            print("to", x[1])
            explore(G, x[1])
    postvisit(G,v)  
          
def previsit(G, v):
    global clock
    G.pre[G.nodelist.index(v)] = clock
    clock += 1
    
def postvisit(G, v):
    global clock
    G.post[G.nodelist.index(v)] = clock
    clock += 1
                
def dfs(G):
    global clock
    clock = 1
    G.visited.clear()
    for x in G.nodelist :
        G.visited.append(False)
        G.pre.append(0)
        G.post.append(0)
    for x in G.nodelist :
        if(G.visited[G.nodelist.index(x)] == False) :
            explore(G, x)
    result = list(zip(G.nodelist, G.pre, G.post))
    print(result)

g = Graph()
g.nodelist = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
g.edgelist = [['a', 'b'], ['a', 'c'], ['a', 'f'], ['b', 'e'],
              ['c', 'd'], ['d', 'a'], ['e', 'f'], ['e', 'g'],
              ['e', 'h'], ['f', 'g'], ['h', 'g']]  # construct Graph

dfs(g)