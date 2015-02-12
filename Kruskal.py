'''
Created on 2015. 2. 8.

@author: Ingoo
'''
'''
procdure Kruskal(G,w)
Input : A connected undirected graph G = (V,E) with edge weight we
Output : A minimum spanning tree defined by the edges X

for all u in V
    makeset(u)

X = {}
sort the edges E by weight
for all edges {u,v} in E in increasing order of weight :
    if find(u) != find(v) :
        add edge {u,v} to X
        union(u,v)

procedure makeset()
pi(x) = x
rank(x) = 0

function find(x)
while x!=pi(x) : x=pi(x)
return x

procedure union(x,y)
rx = find(x)
ry = find(y)
if rx=ry : return
if rank(rx) > rank(ry) :
    pi(ry) = rx
else :
    pi(rx) = ry
    if(rank(rx) = rank(ry)) : rank(ry) = rank(ry) + 1

'''
import networkx as nx
import matplotlib.pyplot as plt

def getweight(x):
    return x[2].get('weight')

kru = nx.Graph()

def kruskal(G):
    
    def makeset(x):
        G.node[x]['pi'] = x
        G.node[x]['rank'] = 0
        
    def union(x,y):
        rx = find(x)
        ry = find(y)
        if rx == ry : pass
        if G.node[rx]['rank'] > G.node[ry]['rank'] :
            G.node[ry]['pi'] = rx
        else :
            G.node[rx]['pi'] = ry
            if(G.node[rx]['rank']==G.node[ry]['rank']) : 
                G.node[ry]['rank'] = G.node[ry]['rank'] + 1
    
    def find(x):
        while(G.node[x]['pi']!=x) :
            x = G.node[x]['pi']
        return x
            
    for x in G.nodes() :
        makeset(x[0])
    
    E = sorted(G.edges(data=True), key=getweight)
    X = []
    for x in E :
        if find(x[0]) != find(x[1]) :
            X.append(tuple([x[0],x[1],x[2].get('weight')]))
            union(x[0],x[1])
    kru.add_nodes_from(G)
    print(X)
    kru.add_weighted_edges_from(X)
    pos = nx.spring_layout(kru)
    nx.draw_networkx(kru,pos)
    nx.draw_networkx_edge_labels(kru,pos,edge_labels=dict([((u,v),d['weight']) for u,v,d in kru.edges(data=True)]))
    plt.show()
            
        
G = nx.DiGraph()
nodelist = ['a','b','c','d','e','f']
edgelist = [('a','b',5),('a','c',6),('a','d',4),('b','c',1),
            ('b','d',2),('c','d',2),('c','e',5),('c','f',3),
            ('d','f',4),('e','f',4)]

G.add_nodes_from(nodelist)
G.add_weighted_edges_from(edgelist)

kruskal(G)