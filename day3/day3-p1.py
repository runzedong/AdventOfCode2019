def read_input(file_name):
    f = open(file_name, 'r')
    data = f.read().split('\n')
    f.close()
    return (data[0].split(','), data[1].split(','))

def generate_point_set(line_data, point_set):
    origin = (0, 0)
    for p in line_data:
        direction = p[0]
        step = int(p[1:])
        for i in range (step):
            if direction == 'R':
                origin = (origin[0] + 1, origin[1])
            elif direction == 'L':
                origin = (origin[0] - 1, origin[1])
            elif direction == 'U':
                origin = (origin[0], origin[1] + 1)
            elif direction == 'D':
                origin = (origin[0], origin[1] - 1)
            else:
                print('Unknown direction: ' + direction)
            point_set.add(origin)

def find_intersections(line_data, point_set):
    intersections = []
    origin = (0, 0)
    for p in line_data:
        direction = p[0]
        step = int(p[1:])
        for i in range (step):
            if direction == 'R':
                origin = (origin[0] + 1, origin[1])
            elif direction == 'L':
                origin = (origin[0] - 1, origin[1])
            elif direction == 'U':
                origin = (origin[0], origin[1] + 1)
            elif direction == 'D':
                origin = (origin[0], origin[1] - 1)
            else:
                print('Unknown direction: ' + direction)
            if origin in point_set:
                intersections.append(origin)
    return intersections
    
def main():
    line1, line2 = read_input('input.txt')
    points = set()
    generate_point_set(line1, points)
    intersections = find_intersections(line2, points)
    distance = 'NULL'
    print("Found intersections: ")
    print(intersections)
    for p in intersections:
        new_dis = abs(p[0]) + abs(p[1])
        if distance == 'NULL':
            distance = new_dis
        else:
            distance = min(distance, new_dis)
    print('Min Distance')
    print(distance)
# There is another way to parse the input and generate the line as the
# format of (x-axis or y-axis; position related to x/y axis; values).
# Because the line is either lined up with X or Y axis, the complexity to
# find the intersection of lines should be decreased log2 if we assume the
# lines are distrubted uniformed on the panel. And also, find intersection 
# between two lines along with X or Y should be simplied problem than generic case.
main()