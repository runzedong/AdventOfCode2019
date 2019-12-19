def calculate_node_orbit(graph, orbit_map, node):
    if node in orbit_map:
        return orbit_map[node]
    if node not in graph:
        return 0
    total_orbit = 0
    for next_node in graph[node]:
        total_orbit += 1 + calculate_node_orbit(graph, orbit_map, next_node)
    return total_orbit

def calculate_orbits(graph):
    orbit_total = 0
    orbit_map = {}
    for node, parents in graph.items():
        node_orbit = 0
        for p in parents:
            node_orbit += calculate_node_orbit(graph, orbit_map, p) + 1
        orbit_total += node_orbit
        orbit_map[node] = node_orbit
    return orbit_total

def main():
    print('Build graph...')
    graph = {}
    f = open("input.txt", "r")
    for edge in f.readlines():
        r = edge.rstrip('\n').split(')')
        if r[1] not in graph:
            graph[r[1]] = []
        graph[r[1]].append(r[0])
    f.close()
    print('Process graph to find orbit total...')
    total_orbits = calculate_orbits(graph)
    print('Result: ' + str(total_orbits))
main()