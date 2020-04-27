# -*- coding: utf-8 -*-
"""
Created on Sun Feb  9 19:11:21 2020

@author: AKSHATA
"""
def dfs(node):
    for i in range(len(visited)):
        if(matrix[i][node]==1 and visited[i]==0):
            stack.append(i);
            visited[i]=1;
            print(i)
            return 1;
    return 0

n=int(input())
matrix=[[0]*n]*n
for i in range(n):
    matrix[i]=list(map(int,input().split()))

stack=[0];
print(0);
top=0;
visited=[0]*n;
visited[0]=1
node=stack[len(stack)-1]
f=dfs(node)
while(len(stack)):
    if(f==1):
        node=stack[len(stack)-1]
        f=dfs(node)
    else:
        stack.pop();
        if(len(stack)):
            f=dfs(stack[len(stack)-1]) 
    


        
        
        
        
    
    

	
	
        
        