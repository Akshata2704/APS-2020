#include<stdio.h>
#include<stdlib.h>

struct node{
int data;
struct node *left;
struct node *right;
};

struct node *getnode(int e)
{
struct node *p;
p=(struct node*)malloc(sizeof(struct node));
if(p!=NULL)
{
p->data=e;
p->left=p->right=NULL;


}
return p;
 }

 void insertBST(struct node **root,int e)
 {
 struct node *p=getnode(e);
 if(p==NULL)
 {
 return;
 }
 if(*root==NULL)
 *root=p;
 else
 {
 struct node *q=*root;
 struct node *parent;
 while(q!=NULL)
 {
 parent=q;
 if(p->data>q->data)
 q=q->right;
 else if(p->data<q->data)
 q=q->left;
 else
 {
 free(p);
 return ;
 }
 }
 if(p->data>parent->data)
 parent->right=p;
 else
 parent->left=p;
 }
 return ;
 }

 int heightoftree(struct node *root)
 {

     int height_left,height_right;
     if(root==NULL)
        return 0;
        else
        {
            height_left=heightoftree(root->left);
            height_right=heightoftree(root->right);
            if(height_left>height_right)
                return(height_left+1);
            else
                return(height_right+1);
        }

 }

 main()
 {

     struct node *root=NULL;
     int e,ch,x;
     ch=5;
     while(ch)
     {
         printf("Enter data:");
         scanf("%d",&e);
         insertBST(&root,e);
         ch--;
     }

     x=heightoftree(root);
     printf("h=%d",x);
 }
