#include<stdio.h>
#include<stdlib.h>

struct node{
int data;
struct node *left;
struct node *right;
};

struct node* newNode(int data)
{
struct node* node = (struct node*)
					malloc(sizeof(struct node));
node->data = data;
node->left = NULL;
node->right = NULL;

return(node);
}

int isbst(struct node *root)
{
    if(!root)
        return 1;
    if(root->left!=NULL&&(root->left->data>root->data))
        return 0;
    if(root->right!=NULL && (root->right->data<root->data))
        return 0;
    if((!isbst(root->left))||(!isbst(root->right)))
        return 0;
    return 1;
}


  main()
 {


     int e,ch,x;
     struct node *root = newNode(4);
root->left	 = newNode(9);
root->right	 = newNode(5);
root->left->left = newNode(1);
root->left->right = newNode(3);

x=isbst(root);
if(x==1)
    printf("Itis bst");
else
    printf("Not bst");
 }
