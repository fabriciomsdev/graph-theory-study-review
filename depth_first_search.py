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
        self.possible_paths = []
    
    def visit(self, node):
        self.path.append(node)
        print(f"Path: {' -> '.join(self.path)}")

    def do_traversal_with_preorder(self, graph: SimpleGraph, root_node):
        neighbors = graph[root_node]
        self.visit(root_node)
        self.marked[root_node] = True
        
        for neighborhood in neighbors:
            if not self.marked.get(neighborhood):
                self.do_traversal_with_preorder(graph, neighborhood)
        
        
    def do_traversal_with_postorder(self, graph: SimpleGraph, current_node):
        neighbors = graph[current_node]
        self.marked[current_node] = True
        
        for neighborhood in neighbors:
            if not self.marked.get(neighborhood):
                self.do_traversal_with_postorder(graph, neighborhood)
                
        self.visit(current_node)
    
    
    
    def do_traversal_between_nodes(self, graph: SimpleGraph, begin_node, end_node):
        neighbors = graph[begin_node]
        self.visit(begin_node)
        self.marked[begin_node] = True

        if end_node == begin_node:
            self.possible_paths.append(self.path)
        
        for neighborhood in neighbors:
            if not self.marked.get(neighborhood):
                print('Last', self.path[-1])
                return self.do_traversal_between_nodes(graph, neighborhood, end_node)
            
        return self.possible_paths
                

print('\n Preorder:')
DepthFirstSearchSolver().do_traversal_with_preorder(graph, 'A')

print('\n Postorder:')
DepthFirstSearchSolver().do_traversal_with_postorder(graph, 'A')

print('\n Possible Paths:')
print(DepthFirstSearchSolver().do_traversal_between_nodes(graph, 'A', 'Z'))
