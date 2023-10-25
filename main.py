from typing_extensions import Self

class Node():
    def __init__(self, id: int, name: str) -> None:
        self._id:int = id
        self._name:str = name
        self._next:Self = None

    @property
    def id(self) -> int:
        return self._id
    @id.setter
    def id(self, value:int):
        self._id = value

    @property
    def name(self) -> str:
        return self._name
    @name.setter
    def name(self, value:str):
        self._name = value

    @property
    def next(self) -> Self:
        return self._next
    @next.setter
    def next(self, value:Self):
        self._next = value

class LinkedList():
    def __init__(self) -> None:
        self._nodeList: dict[int, Node] = {}
        self._nodePos: dict[int, int] = {}

    def addNode(self, node:Node) -> None:
        # We need to dedupe the node being passed in...gotta be unique
        found: bool = False
        if node is not None:
            for x in self._nodeList.keys():
                if x == node.id:
                    found = True
            if not found:
                pos = len(self._nodeList) + 1
                self._nodePos[pos] = node.id
                self._nodeList[node.id] = node
                
                if pos > 1:
                    prevNodePos = pos - 1
                    prevNodeId = self._nodePos[prevNodePos]
                    prevNode = self._nodeList[prevNodeId]
                    prevNode.next = node
        
        # Add node to internal list
        # Ensure last node in list has its next property pointed to this node being added
        pass


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
myLL.addNode(node11) # this should NOT succeed because node1 has already been added (and so it's not unique)

myVar: str = 'hello world'

# myList = [node1, node2, node3, node4]
# myList[0].name = 'Mike2'
# print(f'node1.name equals: {node1.name}')

