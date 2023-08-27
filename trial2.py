# -*- coding: utf-8 -*-
"""
Created on Sun Jun 12 14:07:09 2022

@author: preth
"""

import numpy as np
class graph:
    def __init__(self,n):
        self.adjmatrix=np.zeros((n,n))
        self.vertices=n
    def setmat(self,i,j):
        self.adjmatrix[i][j]=1
        self.adjmatrix[j][i]=1
    def getmat(self):
        c=0
        for i in self.adjmatrix:
            c+=1
            print(i)
            if(c%self.vertices==0):
                print("\n")
    def iterate(self):
             return self.adjmatrix       
class Tree:
    pass


N = int(input("Enter the number of vertices : "))
M = int(input("Enter the number of edges : "))
g=graph(N)
print("Enter the edges \n")
for i in range(M):
    i,j=map(int,input().split())
    g.setmat(i, j)
g.getmat()
edge_vertex=[]
for i in range(N):
    temp=[0,i]
    edge_vertex.append(temp)
adj=g.iterate()
for i in range(N):
    for j in range(N):
        if(adj[i][j]==1):
            edge_vertex[i][0]+=1;
                     #to print the nested list
edge_vertex=sorted(edge_vertex)   
print(edge_vertex)           #sorted nested list
changed=0
total_edges=M*2
length=len(edge_vertex)-1;
while(total_edges>2*N-2 and length>=0):
    val1=total_edges-(2*N-2)
    val2=edge_vertex[length][0]-1
    chk_value=min(val1,val2)
    total_edges-=chk_value
    edge_vertex[length][0]-=chk_value
    changed+=1
    length-=1
edge_vertex=sorted(edge_vertex)              #sorted nested list
#print(edge_vertex)
#print(changed)
#print(N,N-1)
arr_odegree=[]
arr_available=[]
for i in edge_vertex:
    arr_odegree.append(i[0])
    arr_available.append(i[1])
noof_vertices=len(arr_available)
final=[]
i=0
while(noof_vertices>0 and i<noof_vertices-1):
    if(arr_odegree[i]<arr_odegree[i+1]):
        #print("\n\n",arr_odegree[i],arr_odegree[i+1])
        temp=[arr_available[i],arr_available[i+1]]
        final.append(temp)
        arr_odegree[i]-=1;
        arr_odegree[i+1]-=1;
        #print(arr_odegree)
        #print(arr_available)
        if(arr_odegree[i+1]==0):
            arr_odegree.pop(i+1)
            arr_available.pop(i+1)
            noof_vertices-=1
            i=0
        if(arr_odegree[i]==0):
            arr_odegree.pop(i)
            arr_available.pop(i)
            noof_vertices-=1
            i=0
        #print("\n\n")
        #print(arr_odegree)
        #print(arr_available)
    else:
        i+=1
    
print(final)
"""arr1 = []
arr2 = []
for i in range (len(edge_vertex)):
    x = edge_vertex[i][0]
    y = edge_vertex[i][1]
    arr1.append(x)
    arr2.append(y)
print(arr1)
print(arr2)

ret = 0
total = M*2
for i in range(len(edge_vertex)-1,total>2*N-2):
    amt = min(total-(2*N-2),arr1[i]-1)
    total = total-amt
    ret = ret+1
print(sorted(edge_vertex))"""