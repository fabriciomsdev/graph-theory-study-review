import queue
from custom_types import SimpleGraph

graph: SimpleGraph = {
    'A': ['B', 'C'],
    'B': ['C', 'A', 'D', 'E'],
    'C': ['D', 'A', 'K', 'B'],
    'D': ['K', 'F', 'B', 'C'],
    'F': ['E', 'D'],
    'E': ['F', 'B'],
    'K': ['C', 'Z', 'D',],
    'Z': []
}


class BreadthFirstSearchSolver:

    def __init__(self):
        self.marked = {}
        self.path = []
    
    def visit(self, node):
        self.path.append(node)
        print(f"Path: {' -> '.join(self.path)}")

    def do_traversal(self, graph: SimpleGraph, current_node):
        queue = [current_node]
        
        while len(queue) > 0:
            current_node = queue.pop()

            if not self.marked.get(current_node):
                self.visit(current_node)
                self.marked[current_node] = True
                neigborhoods = graph[current_node]

                for neigborhood in neigborhoods:
                    if not self.marked.get(neigborhood):
                        queue.append(neigborhood)

                

BreadthFirstSearchSolver().do_traversal(graph, 'K')
