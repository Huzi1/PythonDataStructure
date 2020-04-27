# construct node
class Node(object):

    def __init__(self,data):
        self.data = data;
        self.nextNode = None;

 # Linked list 


class LinkedList(object):
    def __init__(self):
        self.head= None;
        self.size = 0 ;

    def insertStart(self, data):

        self.size = self.size +1;
        newNode = Node(data);
        # if no head/root node iniate one
        if not self.head:
            self.head = newNode 
        else:
            newNode.nextNode = self.head
            # assign the head to new node inserted
            self.head = newNode

    def size1(self):
        return self.size

    
    def remove(self,data):

        if self.head is None:
            return;

        self.size = self.size -1

        currentNode = self.head
        previousNode = None;

        while currentNode.data != data :
            previousNode = currentNode
            currentNode = currentNode.nextNode;

        if previousNode is None:
            self.head = currentNode.nextNode

        else:
            previousNode.nextNode = currentNode.nextNode




    def insertEnd(self,data):
        self.size = self.size +1;
        newNode = Node(data)
        actualNode = self.head;


        while actualNode.nextNode is not None:
            actualNode = actualNode.nextNode;

        actualNode.nextNode = newNode;


    def traverseList(self):

        actualNode = self.head;

        while actualNode is not None:
            print("%d" % actualNode.data);
            actualNode = actualNode.nextNode           
    # else add one ore node



LinkedList = LinkedList()

LinkedList.insertStart(12)
LinkedList.insertStart(43)
LinkedList.insertStart(13)
LinkedList.insertStart(65)
LinkedList.insertStart(35)
LinkedList.insertEnd(45)

# LinkedList.traverseList()

LinkedList.remove(12)
LinkedList.remove(43)
LinkedList.remove(13)
LinkedList.remove(65)
LinkedList.remove(35)
LinkedList.remove(45)
LinkedList.traverseList()

print(LinkedList.size1())

# LinkedList.remove(12)
# LinkedList.traverseList()
# LinkedList.remove(45)
# LinkedList.traverseList()