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

def main():
    f = open("input.txt", 'r')
    codes = list(map(lambda x: int(x), f.read().split(',')))
    f.close()
    # restore to init alarm state
    codes[1] = 12
    codes[2] = 2
    # start to process
    print("Input code")
    print(codes)
    int_code_program(codes)
    print("After code")
    print(codes)

main()
