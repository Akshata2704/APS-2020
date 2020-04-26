#include<iostream>
using namespace std;
int main()
{
int a,b,c;
cout<<"Enter a:";
cin>>a;
cout<<"Enter b:";
cin>>b;
a=a+b;
b=a-b;
a=a-b;
cout<<"After swapping a="<<a<<","<<"b="<<b;
return 0;
}
