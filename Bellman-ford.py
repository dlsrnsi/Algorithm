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
class Graph :
    nodelist = []
    edgelist = []
    distance = []
    prev = []
    

graph = Graph()
graph.nodelist = ['s','a','b','c','d','e','f','g']
graph.edgelist = [['s','a',10],['s','g',8],['a','e',2],['b','c',1],
                   ['c','d',3],['d','e',-1],['e','b',-2],['f','a',-4],
                   ['f','e',-1],['g','f',1]]

def bellman_ford(G):
    infinite = float("inf")
    print("infinite : ", infinite )
    for x in G.nodelist :
        G.distance.append(infinite)
        G.prev.append(None)
    G.distance[0] = 0
    print(G.distance)
    for x in range(1,len(G.nodelist)) :
        for e in G.edgelist :
            G.distance[G.nodelist.index(e[1])] = min(G.distance[G.nodelist.index(e[1])],G.distance[G.nodelist.index(e[0])]+e[2])
        print(G.distance)
    print("result : ", list(zip(G.nodelist,G.distance)))
            
            
bellman_ford(graph)
        