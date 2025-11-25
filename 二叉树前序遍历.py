#python笑传之抄抄编
#二叉树之前序遍历
class node:
    def __init__(self,data=-1,left=None,right=None):
        self.data = data
        self.left = left
        self.right = right
class Tree:
    def __init__(self):
        self.root = None
        self.queue = []
    def insert_node(self,data):
        new_node = node(data)
        self.queue.append(new_node)
        if self.root is None:
            self.root = new_node
        elif self.queue[0].left is None:
            self.queue[0].left = new_node
        else:
            self.queue[0].right = new_node
            self.queue.pop(0)
    def preorder(self,current_node:node)    :
        if current_node :
            print(current_node.data,end="")
            self.preorder(current_node.left)
            self.preorder(current_node.right)
if __name__ == '__main__':
    tree=Tree(  )
    for i in range(1,10):
        tree.insert_node(i)
    tree.preorder(tree.root)