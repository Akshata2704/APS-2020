#include<stdio.h>
#include<stdlib.h>

struct node{
int data;
struct node *left;
struct node *right;
};
int arr[15]={0};
int i=0;

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


 int ansce(struct node *root,struct node *node)
 {

     if(root==NULL) return 0;
     if(root->left==node|| root->right==node || ansce(root->left,node) || ansce(root->right,node))
     {
         arr[i]=root->data;
         i++;
         return 1;

     }
     return 0;
 }

 int max(struct node *root,struct node *node1,struct node *node2)
 {

     ansce(root,node1);
     ansce(root,node2);

     int j=0;

     int max_ele=arr[0];

     for(j=0;j<i;j++)
     {

         if(arr[j]<max_ele)
            max_ele=arr[j];
     }


     return(max_ele);

 }
 int abc(struct node *root,struct node *node1,struct node *node2)
 {
     int s;

     if(node1->data<root->data && node2->data<root->data)
        abc(root->left,node1,node2);
        if(node1->data>root->data && node2->data>root->data)
            abc(root->right,node1,node2);

                 if((node1->data<root->data && node2->data>root->data) || (node2->data<root->data && node1->data>root->data))
     {

     s=max(root,node1,node2);
     printf("min element is %d",s);
     return(s);

     }
     return(s);


 }



      main()
 {

     struct node *root=NULL;
     int e,ch,v;
     ch=8;
     while(ch)
     {
         printf("Enter data:");
         scanf("%d",&e);
         insertBST(&root,e);
         ch--;
     }
     v=abc(root,root->left->left->left,root->left->right->left);
     printf("y am %d",v);

    printf("Max between the nodes\n%d\n%d",root->left->left->left->data,root->left->right->left->data);
     printf("max element is %d",v);



 }




