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
        self._nodeList = []

    def addNode(self, node:Node) -> None:
        # We need to dedupe the node being passed in...gotta be unique
        # Add node to internal list
        # Ensure last node in list has its next property pointed to this node being added
        pass


node1 = Node(1, 'Mike')
node2 = Node(2, 'Mary')
node3 = Node(3, 'Felicity')
node4 = Node(4, 'Daniel')

myLL = LinkedList()
myLL.addNode(node1)
myLL.addNode(node2)
myLL.addNode(node3)
myLL.addNode(node4)

# myList = [node1, node2, node3, node4]
# myList[0].name = 'Mike2'
# print(f'node1.name equals: {node1.name}')