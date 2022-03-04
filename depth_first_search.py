from custom_types import SimpleGraph

graph: SimpleGraph = {
    'A': ['B', 'C'],
    'B': ['C', 'A', 'D', 'E'],
    'C': ['D', 'A', 'K', 'B'],
    'D': ['K', 'F', 'B', 'C'],
    'F': ['E', 'D'],
    'E': ['F', 'B'],
    'K': ['C', 'D', 'Z'],
    'Z': []
}


class DepthFirstSearchSolver:
    visited = {}
    path = []

    def visit(self, node):
        self.visited[node] = True
        self.path.append(node)
        print(f"Path: {' -> '.join(self.path)}")

    def do_traversal(self, graph: SimpleGraph, current_node):
        self.visit(current_node)
        neighbors = graph[current_node]
        
        for neighborhood in neighbors:
            if not self.visited.get(neighborhood):
                self.do_traversal(graph, neighborhood)
                

DepthFirstSearchSolver().do_traversal(graph, 'A')