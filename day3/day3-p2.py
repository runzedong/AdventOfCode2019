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

def check_joint_point_on_line(origin, next_origin, joint_point):
    if origin[0] - next_origin[0] == 0 and joint_point[0] - origin[0] == 0 and joint_point[1] >= min(origin[1], next_origin[1]) and joint_point[1] <= max(origin[1], next_origin[1]):
        return abs(joint_point[1] - origin[1])
    if origin[1] - next_origin[1] == 0 and joint_point[1] - origin[1] == 0 and joint_point[0] >= min(origin[0], next_origin[0]) and joint_point[0] <= max(origin[0], next_origin[0]):
        return abs(joint_point[0] - origin[0])
    return -1


def find_step_to_reach(line_data, joint_point):
    origin = (0, 0)
    acc_steps = 0
    for p in line_data:
        direction = p[0]
        step = int(p[1:])
        if direction == 'R':
            new_origin = (origin[0] + step, origin[1])
        elif direction == 'L':
            new_origin = (origin[0] - step, origin[1])
        elif direction == 'U':
            new_origin = (origin[0], origin[1] + step)
        elif direction == 'D':
            new_origin = (origin[0], origin[1] - step)
        else:
            new_origin = origin
            print('Unknown direction: ' + direction)
        check_joint = check_joint_point_on_line(origin, new_origin, joint_point)
        if  check_joint > -1:
            acc_steps += check_joint
            break
        else:
            acc_steps += step
        origin = new_origin
    return acc_steps

def main():
    line1, line2 = read_input('input.txt')
    points = set()
    generate_point_set(line1, points)
    intersections = find_intersections(line2, points)
    distance = 'NULL'
    for intersection in intersections:
        new_distance = find_step_to_reach(line1, intersection) + find_step_to_reach(line2, intersection)
        if distance == 'NULL':
            distance = new_distance
        else:
            distance = min(distance, new_distance)
    print('Min combined distance')
    print(distance)

main()