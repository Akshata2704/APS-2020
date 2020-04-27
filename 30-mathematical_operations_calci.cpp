#include<iostream>
using namespace std;
int add(int a,int b){
return(a+b);
}

int subs(int a,int b){
return(a-b);
}

int multp(int a,int b){
return(a*b);
}


float divd(int a,int b){
return(((1.0)*a)/b);
}

int main()
{
    int i,a,b;
    while(1)
    {
    cout<<endl<<"Choose any of the following operations:"<<endl<<"1.ADDITION"<<endl<<"2.SUBTRACTION"<<endl<<"3.MULTIPLICATION"<<endl<<"4.DIVISION"<<endl<<"5.Exit"<<endl;
    cin>>i;

    cout<<"Enter 2 operands:";
    cin>>a>>b;
    switch(i)
    {

        case 1:cout<<"Sum of numbers is "<<add(a,b);
                break;


        case 2:cout<<"Difference of numbers is "<<subs(a,b);
                break;


        case 3:cout<<"Product of numbers is "<<multp(a,b);
                break;


        case 4:cout<<"Quotient of numbers is "<<divd(a,b);
                break;
        case 5:return 0;
        break;
            default:cout<<"Invalid";
            break;

    }
    }

}
