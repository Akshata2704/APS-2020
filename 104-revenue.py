#Uses python3


def max_dot_product(a, b):
    #write your code here
    res = 0
    a=sorted(a)
    b=sorted(b)
    for i in range(len(a)):
        res += a[i] * b[i]
    return res



o = int(input())
a = list(map(int,input().split()))
b  =list(map(int,input().split()))
print(max_dot_product(a, b))
    
