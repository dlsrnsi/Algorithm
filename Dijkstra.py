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


class Graph :
    nodelist = []
    edgelist = []
    distance = []
    prev = []
    


def dijkstra(G):
    infinite = float("inf")
    for x in G.nodelist :
        G.distance.append(infinite)
        G.prev.append(None)
    G.distance[0] = 0
    
    H = list()
    for x in range(len(G.nodelist)) :
        dic = []
        dic.append(G.distance[x])
        dic.append(G.nodelist[x])
        H.append(dic)
        
    while(len(H)!=0) :
        min = H[0]
        for x in H :
            if(x[0]<min[0]) :
                min = x
        u = H.pop(H.index(min))
        for x in G.edgelist :
            if(x[0].__eq__(u[1])) :
                for y in H :
                    if(y[1] == x[1] and y[0]> u[0] + x[2]) :
                        y[0] = u[0] + x[2]
                        print(u[1], " to ", y[1], y[0], " through", x[2])
                        G.prev[G.nodelist.index(y[1])] = u[1]
                        G.distance[G.nodelist.index(y[1])] = y[0]
    
    print(list(zip(G.nodelist,G.prev,G.distance)))


graph1 = Graph()
graph1.nodelist = ['a','b','c','d','e']
graph1.edgelist = [['a','b',4],['a','c',2],['b','c',3],['b','d',2],['b','e',3],
                  ['c','b',1],['c','d',4],['c','e',5],['e','d',1]]

dijkstra(graph1)




