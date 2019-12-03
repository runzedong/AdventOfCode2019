import copy

def int_code_program(codes):
    offset = 4
    start_position = 0
    halt_code = 99
    add_code = 1
    multiple_code = 2
    while start_position < len(codes):
        curr_process = codes[start_position: start_position + offset]
        opcode = curr_process[0]
        if opcode == halt_code:
            break
        elif opcode == add_code:
            codes[curr_process[3]] = codes[curr_process[1]] + \
                codes[curr_process[2]]
        elif opcode == multiple_code:
            codes[curr_process[3]] = codes[curr_process[1]] * \
                codes[curr_process[2]]
        else:
            # find unknown op code
            print("unknown opcode: " + opcode)
            continue
        start_position += offset

def find_target_pair_input(target, codes):
    for noun in range(100):
        for verb in range(100):
            init_new_codes = copy.copy(codes)
            init_new_codes[1] = noun
            init_new_codes[2] = verb
            int_code_program(init_new_codes)
            if (init_new_codes[0] == target):
                print('noun: ' + str(noun))
                print('verb: ' + str(verb))
                return (noun, verb)
    

def main():
    f = open("input.txt", 'r')
    codes = list(map(lambda x: int(x), f.read().split(',')))
    f.close()
    target = 19690720
    noun, verb = find_target_pair_input(target, codes)
    print("Result...")
    print(noun * 100 + verb)

main()
