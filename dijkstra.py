import math
from typing import Dict

def print_distances_table(table: Dict[str, int]):
    header = 'Current calculated Distances: \n'
    header_bar = (len(header) * '-') + '\n'
    greater_row_size = 0     
    content = ''

    for (key, distance) in table.items():
        row = f'{key}: {distance}\n'
        content += row
        if len(row) > greater_row_size:
            greater_row_size = len(row)

    print(header_bar + header + header_bar + content + header_bar)
        
graph = {
    "Brazil": {
        "Argentina": 5,
        "Uruguai": 3,
        "Chile": 1,
    },
    "Argentina": {
        "England": 20,
        "Sweden": 10,
        "Uruguai": 1
    },
    "Uruguai": {
        "Chile": 1,
        "England": 2,
    },
    "Chile": {
        "Sweden": 3,
        "England": 1,
    },
    "England": {
        "Sweden": 5,
        "Canada": 2,
    },
    "Sweden": {
        "Canada": 1,
        "England": 2
    },
    "Canada": {}
}

source = "Brazil"
destination = "Canada"

not_visited = graph
shortest_distance_table = {}
route = []
path_nodes = {}
infinite = math.inf

## Set firt distances of nodes as infinite
for node in not_visited:
    shortest_distance_table[node] = infinite
## I need to set distance between source and itself as 0
shortest_distance_table[source] = 0

## look in all nodes not visited
while len(not_visited) > 0:
    min_node = None

    print(f'Choosing next to travel:')
    
    for current_node in not_visited:
        if min_node is None:
            min_node = current_node
        elif shortest_distance_table[min_node] > shortest_distance_table[current_node]:
            print(f'Distance to {current_node} is less than {min_node}')
            min_node = current_node

    print(f'Choose {min_node}')
    print_distances_table(shortest_distance_table)
    
    print('--' * 20)
    print(f'Visiting: {min_node} and start checking neighrboorhoods:')
    for (node, distance_to_node) in not_visited[min_node].items():
        total_distance_to_node = shortest_distance_table[min_node] + distance_to_node
        distance_to_current_visited_node = shortest_distance_table[node]

        print(f'The distance from {min_node} to {node}, it is: {total_distance_to_node}')
        if total_distance_to_node < distance_to_current_visited_node:
            shortest_distance_table[node] = total_distance_to_node
            path_nodes[node] = min_node

    print(f'Mark {min_node} as Visited')
    print('--' * 20)
    not_visited.pop(min_node)
    
node = destination

while node != source:
    try:
        route.insert(0, node)
        node = path_nodes[node]
    except Exception:
        print(f'There is no path between {source} and {destination}')
        break
    
route.insert(0, source)

if shortest_distance_table[destination] != infinite:
    print(f'Shortest distance between {source} and {destination} is ' + str(shortest_distance_table[destination]))
    print(f'And the best route should be {str(route)}')
    