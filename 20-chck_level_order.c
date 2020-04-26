#include<stdio.h>
#include<stdlib.h>
struct node
{
struct node * lc;
int data;
struct node * rc;
};
struct node * buildtree(int);
void inorder(struct node *);
int a[]={ 3,5,9,6,8,20,10,0,0,9,0,0,0,0,0,0,0,0,0,0,0};

void main( )
{
struct node * root;
root= buildtree(0);
printf(" Inorder Traversal");
inorder(root);
getch( );
}

struct node * buildtree(int n)
{
struct node *temp =NULL;
if( a[n] != NULL)
{
temp = (struct node *) malloc(sizeof(struct node));
temp-> lc=buildtree(2*(n) + 1);
temp-> data= a[n];
temp-> rc=buildtree(2*(n) + 2);
}
return temp;
}

void inorder(struct node * root)
{
if(root != NULL)
{
if(root!= NULL)
{
inorder(root-> lc);
printf("%d \t",root->data);
inorder(root->rc);
}
}
}
