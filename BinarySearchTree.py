class Node(object):

    def __init__(self,data):
        self.data = data;
        self.leftChild = None;
        self.rightChild = None;

class BinarySearchTree(object):

    def __init__(self):
        self.root = None;

    def insert(self, data):
# no Root child then create one
        if not self.root:
            self.root = Node(data)
            # if root child exist we will call new function to check tree rules
        else:
            self.insertNode(data, self.root)


    def insertNode(self, data, node):
# check less than root node
        if data < node.data:
            # check leftchild not none
            if node.leftChild:
                self.insertNode(data, node.leftChild);
            else:
                node.leftChild = Node(data)
        else:
            if node.rightChild:
                self.insertNode(data, node.rightChild);
            else:
                node.rightChild = Node(data)    


    def getMinValue(self):
        if self.root:
            return self.getMin(self.root)            


    def getMaxValue(self):
        if self.root:
            return self.getMax(self.root) 


    def getMin(self, node):

        if node.leftChild:
            return self.getMin(node.leftChild);
        else:

            return node.data    


    def getMax(self, node):

        if node.rightChild:
            return self.getMax(node.rightChild);
        else:

            return node.data         

    def traverse(self):

        if self.root:
            self.traverseInOrder(self.root)

    def traverseInOrder(self, node):

        if node.leftChild:
            self.traverseInOrder(node.leftChild);
        print("%s" %node.data);

        if node.rightChild:
            self.traverseInOrder(node.rightChild);
    
    def removeNode(self, data, node):

        if not node:
            return node;
        if data < node.data:
            node.leftChild = self.removeNode(data, node.leftChild)
        elif data > node.data:
            node.rightChild = self.removeNode(data, node.rightChild)
        else:

            if not node.leftChild and not node.rightChild:
                print("remove leaf node");
                del node;
                return None

            if not node.leftChild:
                print("Removing a node with single chile...");
                tempNode = node.rightChild;
                del node;
                return tempNode;
            elif not node.rightChile:
                print("Removing a node with single left chile...");
                tempNode = node.leftChild;
                del node;
                return tempNode;

            print("Removing node with 2 children...");
            # predessor is the grtst child in left sub tree
            tempNode = self.getPredessor(node.leftChild)
            # swap with root with predessor
            node.data = tempNode.data   
            node.leftChild = self.removeNode(tempNode, node.leftChild);    
        return node

    def getPredessor(self, node):
        if node.rightChild:
            return self.getPredessor(node.rightChild)


    def remove(self,data):
        if self.root:
            self.root = self.removeNode(data, self.root);

        return node;    


bst = BinarySearchTree()

bst.insert(10)
bst.insert(5)
bst.insert(15)
bst.insert(6)

print(bst.getMinValue())

print(bst.getMaxValue())