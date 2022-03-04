from typing import Dict


GraphType = Dict[str, list[str]]
graph: GraphType = {
    'A': ['B', 'C'],
    'B': ['C', 'A', 'D', 'E'],
    'C': ['D', 'A', 'K', 'B'],
    'D': ['K', 'F', 'B', 'C'],
    'F': ['E', 'D'],
    'E': ['F', 'B'],
    'K': ['C', 'D'],
}


class DepthFirstSearchSolver:
    visited = {}
    path = []

    def visit(self, node):
        self.path.append(node)
        print(f'Visit: {node}')

    def do_traversal(self, graph: GraphType, current_node):
        self.visit(current_node)
        self.visited[current_node] = True
        neighbors = graph[current_node]
        
        for neighborhood in neighbors:
            if not self.visited.get(neighborhood):
                self.do_traversal(graph, neighborhood)
                
        print(f'Path: {self.path}')


DepthFirstSearchSolver().do_traversal(graph, 'A')
