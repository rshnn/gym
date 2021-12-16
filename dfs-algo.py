# Do not edit the class below except
# for the depthFirstSearch method.
# Feel free to add new properties
# and methods to the class.


from collections import deque

class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    def depthFirstSearch(self, array):
        # Write your code here.
        

        stack = deque()
        stack.append(self)    

        while stack: 

            curr = stack.pop() 

            if curr: 
                array.append(curr.name) 

                for idx in range(len(curr.children)-1, -1, -1): 
                    stack.append(curr.children[idx])  

        return array 




if __name__ == "__main__": 


    graph = Node("A")
    graph.addChild("B").addChild("C").addChild("D")
    graph.children[0].addChild("E").addChild("F")
    graph.children[2].addChild("G").addChild("H")
    graph.children[0].children[1].addChild("I").addChild("J")
    graph.children[2].children[0].addChild("K")
    
    print(graph.depthFirstSearch([]))
    print(["A", "B", "E", "F", "I", "J", "C", "D", "G", "K", "H"])
