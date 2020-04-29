
t=int(input())
nn=[]


def maxr(ak):
    global ma
    global ch
    tg=-1
    for j in range(4):
        if( ma[ak][j]>tg and ch[ak][j]==0):
            tg=ma[ak][j]
            n=j
    return [tg,n]
    
    
while(t):
    r=int(input())
    ma=[[0 for i in range(4)]for j in range(4)]
    visited=[0 for _ in range(4)]
    re=['A','B','C','D']
    ti=['12','3','6','9']
    sumt=0;
    M=[-1,-1,-1,-1]
    T=[-1,-1,-1,-1]
    ft=0
    for _ in range(r):
        a=input().split()
        ma[re.index(a[0])][(ti.index(a[1]))]+=1;
  
    
    
    
    ft=0   
    for i in range(4):
        cntcol=0
        cntrow=0
        for j in range(4):
            if(ma[j][i]==0):
                cntcol+=1;
            if(ma[i][j]==0):
                cntrow+=1
        if(cntcol==4):
            sumt-=100;
            T[i]=-10
            ft+=1
        if(cntrow==4):
            M[i]=-10

        
  
    ch=[[0 for i in range(4)]for _ in range(4)]
    i=0
    while(ft<4):
        if(i==4):
            i=0
     
        tg=-1;
        if(M[i]==-1):
            y=maxr(i)
            if(T[y[1]]==-1):
                T[y[1]]=i;
                M[i]=y[1]
                ch[i][y[1]]=1;
                ft+=1
            else:
                pre=T[y[1]];
                if(ma[pre][y[1]]>ma[i][y[1]]):
                    ch[i][y[1]]=1               
                    w=maxr(i)
                    wq=maxr(pre)
                    if(w[0]==0 and wq[0]!=0 ):
                        if(ma[i][y[1]]>ma[pre][wq[1]] and (ma[i][y[1]]*100)+(ma[pre][wq[1]]*75)>ma[pre][y[1]]*100):
                            T[y[1]]=i;
                            T[wq[1]]=pre
                            ch[i][y[1]]=1;
                            ch[pre][wq[1]]=1
                            M[i]=y[1];
                            M[pre]=wq[1]
                            ft+=1
                            
                    elif(wq[0]==0 and w[0]!=0):
                        if(ma[i][w[1]]>ma[pre][y[1]] and (ma[i][w[1]]*100)+(ma[pre][y[1]]*75)>ma[pre][y[1]]*100):
                            T[y[1]]=i;
                            T[w[1]]=pre
                            ch[i][y[1]]=1;
                            ch[pre][w[1]]=1
                            M[i]=y[1];
                            M[pre]=w[1]
                            ft+=1
                            
                        
                        
                elif(ma[pre][y[1]]==ma[i][y[1]]):
                    ch[i][y[1]]=1
                    w=maxr(i)
                    wq=maxr(pre)
                    if(w[0]<wq[0]):
                        T[y[1]]=i;
                        M[pre]=wq[1]
                        T[wq[1]]=pre;
                        ch[pre][wq[1]]=1
                        ch[i][y[1]]=1;
                        M[i]=y[1];
                        ft+=1
                
                        
     
                        
                        
                    
               
     
        i+=1
           
    d=[0 for _ in range(4)]               
    for i in range(4):
        if(M[i]<0):
            d[i]=0;
        else:
            d[i]=ma[i][M[i]]
    d.sort()
  
    sumt+=(d[0]*25)+(d[1]*50)+(d[2]*75)+(d[3]*100)
    print(sumt)
    nn.append(sumt)
    t-=1
print(sum(nn))

    
                
                
         
                
                
                
                
            
        
                




        
        




    
    