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


class DepthFirstSearchSolver:

    def __init__(self):
        self.marked = {}
        self.path = []
    
    def visit(self, node):
        self.path.append(node)
        print(f"Path: {' -> '.join(self.path)}")

    def do_traversal_with_preorder(self, graph: SimpleGraph, current_node):
        neighbors = graph[current_node]
        self.visit(current_node)
        self.marked[current_node] = True
        
        for neighborhood in neighbors:
            if not self.marked.get(neighborhood):
                self.do_traversal_with_preorder(graph, neighborhood)
        
        
    def do_traversal_with_postorder(self, graph: SimpleGraph, current_node):
        neighbors = graph[current_node]
        self.marked[current_node] = True
        
        for neighborhood in neighbors:
            if not self.marked.get(neighborhood):
                self.do_traversal_with_preorder(graph, neighborhood)
                
        self.visit(current_node)
                

print('\n Preorder:')
DepthFirstSearchSolver().do_traversal_with_preorder(graph, 'A')

print('\n Postorder:')
DepthFirstSearchSolver().do_traversal_with_postorder(graph, 'A')