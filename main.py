from typing_extensions import Self

class Node():
    # this is our Node constructor (note that constructors return null)
    def __init__(self, id: int, name: str) -> None:
        self._id: int = id
        self._name: str = name

        # python is kind of weird in this area...since we want the next property to also be a Node object, python doesn't allow us to 
        # simply reference the datatype "Node" when initializing the private memory variable self._next. In other languages like Java or C#, the following would work:
        # self._next: Node = None # but python doesn't like this...however python still facilitates what we need here with this Self type. 
        # So in our case here, Self is Node class type. 
        self._next: Self = None

    @property
    def id(self) -> int:
        return self._id
    @id.setter
    def id(self, value: int):
        self._id = value

    @property
    def name(self) -> str:
        return self._name
    @name.setter
    def name(self, value: str):
        self._name = value

    @property
    def next(self) -> Self | None:
        return self._next
    @next.setter
    def next(self, value: Self | None):
        self._next = value


class LinkedList():
    # this is our LinkedList constructor (note that constructors return null)
    def __init__(self) -> None:
        # here we're initializing a dictionary to store node objects where the key is the id of the node being stored
        self._nodeList: dict[int, Node] = {}

        # here we're initializing a dictionary to store node ids where the key is the position of the node id being stored
        self._nodePos: dict[int, int] = {}

    # this is our addNode method (note that it returns null)
    def addNode(self, node:Node) -> None:
        # We need to dedupe the node being passed in...gotta be unique
        if node is not None:  # ensure that a good node object was passed in
            # to dedupe, we establish a found boolean variable by checking the id of the node against the _nodeList dictionary using the in operator
            # with python dictionaries, you can use the in operator to check if a key exists in it and it's much faster than a for loop (it's O(n) operation)
            found: bool = node.id in self._nodeList
            if not found: # so we only do anything if the node wasn't found
                pos = len(self._nodeList) + 1  # here we're calculating the new position of the node we're adding (which is the last position + 1) / the last position is the same as the length of the node dictionary
                self._nodePos[pos] = node.id  # here we're adding the node id to the position dictionary using the newly calculated position as the key
                self._nodeList[node.id] = node  # here we're adding the node itself to the node dictionary using the node id as the key
                
                # if the node that we've just added isn't the very first node in our linked list, then we need to get the previous node and point its
                # next property to our newly added node (this is why we're keeping track of the nodes' positions)
                if pos > 1:  # so we can know if we're dealing with NOT the first node if the position that we've calculated is beyond the 1st position
                    prevNodePos = pos - 1  # here we're calculating the previous position
                    prevNodeId = self._nodePos[prevNodePos]  # here we're getting the node id that's in the previous position that we've calculated
                    prevNode = self._nodeList[prevNodeId]  # here we're getting the previous node using the node id that we found from the last line
                    prevNode.next = node  # here we're taking that previous node that we found from the last line and seting its next property to the node that we've been adding in this method
        
# This code marks the beginning of code that is outside of any classes and so now we're just instantiating new nodes and adding them to a new LinkedList object
node1 = Node(1, 'Mike')
node2 = Node(2, 'Mary')
node3 = Node(3, 'Felicity')
node4 = Node(4, 'Daniel')
node11 = Node(1, 'Mikey')


myLL = LinkedList()
myLL.addNode(node1)
myLL.addNode(node2)
myLL.addNode(node3)
myLL.addNode(node4)
myLL.addNode(node11) # this will NOT succeed because node1 has already been added and they both have the same node id of 1 (and so it's not unique)


