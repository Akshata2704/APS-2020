# -*- coding: utf-8 -*-
"""
Created on Fri Feb 14 16:20:23 2020

@author: AKSHATA
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 19:25:49 2020

@author: AKSHATA
"""

import calendar
t=int(input())

if(1<=t<=100000):
    while(t):
    
    
        m1,y1=(input().split())
        m2,y2=(input().split())
        m1=int(m1)
        m2=int(m2)
        y1=int(y1)
        y2=int(y2)
        if(1<= m1,m2<=12 and 1<=y1,y2<=1000000000 and y2>=y1):
            if(m1<=2):
                s=y1;
            else:
                s=y1+1;
            if(m2>=2):
                e=y2;
            else:
                e=y2-1
            cnt=0
            if(s<=e):

                flag=1  
                while(flag==1 and s<=e):
                    first_fridays = list((week[calendar.FRIDAY] 
                    for week in calendar.monthcalendar(s,2) ))
                
                    if(first_fridays[0]==0):
                        if(calendar.isleap(s)==1 and first_fridays[1]==7):
                            flag=0;
                            #print(s)
                            cnt+=1
                            break;
                        elif(first_fridays[1]!=6):
       
                            #print(s)
                            cnt+=1
                        elif(calendar.isleap(s)==0 and first_fridays[1]==6):
                            cnt+=1;
                            #print(s)
      
        
                    s+=1;

        
                s=s-1
           
                if(e-s>=28):
                    cnt-=1
                    while(e-s>=28):
                      
                     
                 
                        
                
                        if(calendar.isleap(s+29)):
                           
                            first_fridays = list((week[calendar.FRIDAY] 
                                  for week in calendar.monthcalendar(s+29,2) ))
                                
                            
                            if(first_fridays[0]==0  and first_fridays[1]==7 ):
                               
                                cnt+=7;
                                s+=28;
                                
                            elif(calendar.isleap(s+13)):
                              
                                cnt+=3;
                                s+=12
                         
                   
                            
                
                       
                    
                        elif((s+40)<=e and calendar.isleap(s+41)):
                          
                            cnt+=11;
                            s+=40
                        else:
                            break
                      
                        
                    
                
                else:
                    s+=2

               
                if(e>=s):
                    while(s<=(e)):
                        
                        first_fridays = list((week[calendar.FRIDAY] 
                        for week in calendar.monthcalendar(s,2) ))
                            
                        if((first_fridays[0]==0) and (first_fridays[1]!=6 or calendar.isleap(s)==0)):
                            cnt+=1;
                          
                        
                       
            
                        s+=1
         
            print(cnt)

        t-=1

    
    
    
