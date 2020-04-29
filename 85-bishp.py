
tst=int(input())
r=list(map(int,input().split()))
r0=r[0]
c0=r[1]
# print(r0,c0)
steps=[1,7,2,8,8,2,7,1,4,4,1,1,2,2,1,3,3,1,4,2,5,1,1,5,4,8,8,4,6,6,8,8,7,7,6,8,8,6]
if((r0==c0 and r0!=4) or (r0+c0==8 and r0!=4)):
    print(20)
    print(4,end=" ")
    print(4)
    h=0
    while(h<37):
        print(steps[h],end=" ")
        print(steps[h+1])
        h+=2


elif(r0==4 and c0==4):
    print(19)
    h=0
    while(h<37):
        print(steps[h],end=" ")
        print(steps[h+1])
        h+=2
        
else:
    print(21)
    print(int((r0+c0)/2),end=" ")
    print(int((r0+c0)/2))
    print(4,end=" ")
    print(4)
    h=0
    while(h<37):
        print(steps[h],end=" ")
        print(steps[h+1])
        h+=2