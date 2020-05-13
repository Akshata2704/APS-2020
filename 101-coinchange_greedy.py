
# Uses python3
import sys

def get_change(m):
    c=0
    
    if(m>=10):
        c+=m//10;
        m-=10*(m//10)
  
    if(m>=5):
        c+=m//5
        m-=5*(m//5)
 
    if(m>=1):
        c+=m
    return c
        
    #write your code here
    return m

if __name__ == '__main__':
    m = int(input())
    print(get_change(m))

