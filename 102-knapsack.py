# Uses python3
import sys

def get_optimal_value(capacity, weights, values):
    value = 0.
    dic={}
    r=[]
    for i in range(len(weights)):
        dic[(values[i])/weights[i]]=weights[i]
        r.append((values[i])/weights[i])
    r=list(reversed(sorted(r)))
  
    
    for i in range(len(r)):
        if(capacity==0):
            return value
        f=min(dic[r[i]],capacity)
      
        capacity-=f
        value+=(f)*(r[i])
    return value
        
    # write your code here

    return value


if __name__ == "__main__":
    
    n, capacity = map(int,input().split())
    values=[]
    weights=[]
    for _ in range(n):
        a,b=map(int,input().split())
        values.append(a)
        weights.append(b)
        

    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
