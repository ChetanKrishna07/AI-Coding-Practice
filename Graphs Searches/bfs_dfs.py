class Node:
    def __init__(self, value):
        self.value = value
        self.children = []
        
    def add_child(self, child_node):
        self.children.append(child_node)
        
    def __repr__(self):
        return str(self.value)
    
    def remove_child(self, child_node):
        self.children.remove(child_node)
        
    def __str__(self) -> str:
        return f"{self.value}: [{self.children}]"
    
    def __eq__(self, other: object) -> bool:
        return other.value == self.value
    def __hash__(self):
        return hash(self.value)

class Graph:
    def __init__(self, root):
        self.root = root
        
    def dfs(self, element):
        if self.root.value == element:
            print(f"{self.root.value}")
            return "Success" 
        fringe = [self.root]
        prev = dict()
        prev[self.root] = None
        while len(fringe) != 0:
            curr = fringe.pop()
            print(f"Exploring {curr}")
            for child in curr.children:
                if child not in prev:
                    prev[child] = curr
                    if child.value == element:
                        print(f"{child.value}<-", end="")
                        parent = prev[child]
                        while parent != self.root:
                            print(f"{parent.value}<-", end="")
                            parent = prev[parent]
                        print(f"{self.root.value}")
                        return "Success"
                    fringe.append(child)
        return f"Fail {element}"
    
    def bfs(self, element):
        if self.root.value == element:
            print(f"{self.root.value}")
            return "Success" 
        fringe = [self.root]
        prev = dict()
        prev[self.root] = None
        while len(fringe) != 0:
            curr = fringe.pop(0)
            print(f"Exploring {curr}")
            for child in curr.children:
                if child not in prev:
                    prev[child] = curr
                    if child.value == element:
                        print(f"{child.value}<-", end="")
                        parent = prev[child]
                        while parent != self.root:
                            print(f"{parent.value}<-", end="")
                            parent = prev[parent]
                        print(f"{self.root.value}")
                        return "Success"
                    fringe.append(child)
                    
        return f"Fail {element}"
    

# Testing
nodes = dict({})
while True:
    option = int(input())
    if option == 0:
        break
    elif option == 1:
        value = input()
        if value not in nodes.keys():
            nodes[value] = Node(value)
            print(f"Added {value}")
        else:
            print(f"Error: {value} already exists")
                
    elif option == 2:
        parent = input()
        child = input()
        
        if parent in nodes.keys() and child in nodes.keys():
            exists = False
            for child_ in nodes[parent].children:
                if nodes[child] == child_:
                    print(f"Error: {child} is already a child of {parent}")
                    exists = True
                    break
            if not exists:
                nodes[parent].add_child(nodes[child])
                print(f"{child} added to {parent}")
        else:
            print(f"Error: {parent} node doesn't exist")
    else: 
        print("Error: Invalid Case")
    

print("\n\n")
for i in nodes.values():
    print(i)
root = input()
if root in nodes.keys():
    friends = Graph(nodes[root])
    search = input()
    print("\n\nDFS Result: ")
    print(friends.dfs(search))
    print("\n\nBFS Result: ")
    print(friends.bfs(search))
else:
    print(f"{root} not found in nodes")
