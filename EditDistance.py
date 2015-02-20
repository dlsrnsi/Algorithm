'''
Created on 2015. 2. 16.

@author: Ingoo
'''
'''
for i = 0,1,2,...,m :
    E(i,0) = i
for j = 1,2,...,n :
    E(0,j) = j
for i = 1,2,...,m :
    for j = 1,2,...,n :
        E(i,j) = min(E(i-1,j)+1, E(i,j-1)+1, E(i-1,j-1) + dff(i,j))
return E(m,n)
'''

from pprint import pprint

def editDistance(a,b):
    m = len(a)+1
    n = len(b)+1
    E = [[0 for x in range(n)] for y in range(m)]
    for i in range(m) :
        E[i][0] = i
    for j in range(1,n) :
        E[0][j] = j
    for i in range(1,m) :
        for j in range(1,n) :
            E[i][j] = min([E[i-1][j]+1,E[i][j-1]+1,E[i-1][j-1]+diff(a[i-1],b[j-1])])
            
    pprint(E)

def diff(a,b):
    if a==b :
        return 0
    else :
        return 1
editDistance('exponential', 'polynomial')