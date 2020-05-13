# Uses python3
import sys

def get_change(m):
    ar=[1,3,4]
    M=[0 for _ in range(m+1)]
    for i in range(1,m+1):
        M[i]=sys.maxsize
        for j in range(0,3):
            if(ar[j]<=i):
                mn=M[i-ar[j]]+1
                if(mn<M[i]):
                    M[i]=mn;
    return M[m]
    
            
    #write your code here
    return m // 4


m = int(input())
print(get_change(m))
