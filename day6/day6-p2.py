# If the graph model is non-cycle graph, 
# that will make the question much easier
# by only applying {node: next_node} in {str, str} dictionary
# so the data structure used in part1 can be simplify

def find_orbit_path(graph, node):
    path = []
    while node in graph:
        path.append(node)
        node = graph[node]
    return path

def find_min_transfer_orbits(graph, start, end):
    path1 = find_orbit_path(graph, start)
    path2 = find_orbit_path(graph, end)
    for i1, v1 in enumerate(path1):
        for i2, v2 in enumerate(path2):
            if v1 == v2:
                return i1 + i2
    return None

def main():
    print('Build graph...')
    graph = {}
    f = open("input.txt", "r")
    for edge in f.readlines():
        r = edge.rstrip('\n').split(')')
        if r[1] not in graph:
            graph[r[1]] = r[0]
    f.close()
    print('Process graph to find orbit total...')
    start = 'YOU'
    end = 'SAN'
    min_transfer_orbits = find_min_transfer_orbits(graph, start, end)
    # min_transfer_orbits includes count of 'YOU' & 'SAN' (start point and end point)
    print('Result: ' + str(min_transfer_orbits - 2))
main()