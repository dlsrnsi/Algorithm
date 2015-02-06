'''
Created on 2015. 2. 6.

@author: Ingoo
'''

'''
procedure mergesort
Input : An array of numbers a[1...n]
Output : A sorted version of this array

if n> 1 :
    return merge(mergesort(a[1...n/2]),mergesort(a[n/2...n])
else
    return a

procedure merge(x[1...k], y[1...y])
if k = 0 :
    return y[1...y]
if l = 0 :
    return x[1...k]
if x[1] <= y[1] :
    return x[1] + merge(x[2...k], y[1...l])
if x[1] >  y[1] :
    return y[1] + merge(x[1...k], y[2...l])
'''
import random

def mergesort(a):
    if len(a)>1 :
        print("x : ", a[:int(len(a)/2)])
        print("y : ", a[int(len(a)/2):])
        return merge(mergesort(a[:int(len(a)/2)]), mergesort(a[int(len(a)/2):]))
    else :
        return a
    

def merge(x,y):
    if x.__eq__([]) :
        return y
    if y.__eq__([]) :
        return x
    if (x[0] <= y[0]) :
        return [x[0]]+merge(x[1:],y)
    if (x[0] > y[0]) :
        return [y[0]]+merge(x,y[1:])
    
def selection(list , selNum): # This function is based on randomized divide-and-conquer algorithm
    v = random.choice(list)
    sl = []
    sv = []
    sr = []
    for x in list :
        if (x == v) :
            sv.append(x)
        if (x < v) :
            sl.append(x)
        if (x > v) :
            sr.append(x)
    print("sv :", sv)
    if(len(sl)>=selNum) :
        return selection(sl, selNum)
    elif(selNum > len(sl) + len(sv)) :
        return selection(sr, selNum - len(sl) - len(sv))
    else :
        return sv[0]

list = [5, 7, 6, 20, 16 ,1, 55, 34, 60]

print(mergesort(list))
print(selection(list, 5))