POSITION_MODE = 0
IMMEDIATE_MODE = 1
ADD_CODE = 1
MULTIPLE_CODE = 2
INPUT_CODE = 3
OUTPUT_CODE = 4
JUMP_IF_TRUE = 5
JUMP_IF_FALSE = 6
LESS_THAN = 7
EQUALS = 8
HALT_CODE = 99

def read_para_value(codes, mode, pointer):
    if mode == POSITION_MODE:
        return codes[codes[pointer]]
    elif mode == IMMEDIATE_MODE:
        return codes[pointer]
    else:
        # unknown parameter mode
        print("Unknown parameter mode: " + str(mode))
        return None

def yield_para_mode(modes):
    while True:
        yield modes % 10
        modes //= 10

def exec_output(codes, mode, pointer):
    if mode == POSITION_MODE:
        return str(codes[codes[pointer]])
    elif mode == IMMEDIATE_MODE:
        return str(codes[pointer])
    else:
        # unknown parameter mode
        print("Unknown mode: " + str(mode))
        return None

def exec_input(codes, pointer, input_val):
    # input instruction could only be under POSITION_MODE
    codes[codes[pointer]] = input_val
    return None

def exec_calc(codes, pointer, val1, val2, op_code):
    if op_code == ADD_CODE:
        codes[codes[pointer]] = val1 + val2
    elif op_code == MULTIPLE_CODE:
        codes[codes[pointer]] = val1 * val2
    else:
        # unknown calculation op_code
        print("Unknown mode: " + str(op_code))
        return None

def exec_compare(codes, pointer, val1, val2, op_code):
    if op_code == LESS_THAN:
        codes[codes[pointer]] = 1 if val1 < val2 else 0
    elif op_code == EQUALS:
        codes[codes[pointer]] = 1 if val1 == val2 else 0
    else:
        # unknown calculation op_code
        print("Unknown mode: " + str(op_code))
        return None

def int_code_program(codes, input_val):
    instrct_pointer = 0
    while instrct_pointer < len(codes):
        instrcts = codes[instrct_pointer]
        # figure out opcode
        opcode = instrcts % 100
        para_modes = yield_para_mode(instrcts // 100)
        jump = False
        if opcode == HALT_CODE:
            break
        elif opcode == ADD_CODE:
            # get first para val
            instrct_pointer += 1
            first_para_val = read_para_value(codes, next(para_modes), instrct_pointer)
            # get second para val
            instrct_pointer += 1
            second_para_val = read_para_value(codes, next(para_modes), instrct_pointer)
            # wrtie the result
            instrct_pointer += 1
            exec_calc(codes, instrct_pointer, first_para_val, second_para_val, opcode)
        elif opcode == MULTIPLE_CODE:
            # get first para val
            instrct_pointer += 1
            first_para_val = read_para_value(codes, next(para_modes), instrct_pointer)
            # get second para val
            instrct_pointer += 1
            second_para_val = read_para_value(codes, next(para_modes), instrct_pointer)
            # wrtie the result
            instrct_pointer += 1
            exec_calc(codes, instrct_pointer, first_para_val, second_para_val, opcode)
        elif opcode == INPUT_CODE:
            # input can only be position mode
            instrct_pointer += 1
            exec_input(codes, instrct_pointer, input_val)
        elif opcode == OUTPUT_CODE:
            mode = instrcts // 100
            instrct_pointer += 1
            print("Output: " + exec_output(codes, mode, instrct_pointer))
        elif opcode == JUMP_IF_TRUE:
            # check second para if != 0
            instrct_pointer += 1
            first_para_val = read_para_value(codes, next(para_modes), instrct_pointer)
            if first_para_val != 0:
                jump = True
                instrct_pointer = read_para_value(codes, next(para_modes), instrct_pointer + 1)
            else:
                # only increase pointer by 1
                instrct_pointer += 1
        elif opcode == JUMP_IF_FALSE:
            # check first para if == 0
            instrct_pointer += 1
            first_para_val = read_para_value(codes, next(para_modes), instrct_pointer)
            if first_para_val == 0:
                jump = True
                instrct_pointer = read_para_value(codes, next(para_modes), instrct_pointer + 1)
            else:
                # only increase pointer by 1
                instrct_pointer += 1
        elif opcode == LESS_THAN:
            # get first para val
            instrct_pointer += 1
            first_para_val = read_para_value(codes, next(para_modes), instrct_pointer)
            # get second para val
            instrct_pointer += 1
            second_para_val = read_para_value(codes, next(para_modes), instrct_pointer)
            # write the result
            instrct_pointer += 1
            exec_compare(codes, instrct_pointer, first_para_val, second_para_val, opcode)
        elif opcode == EQUALS:
            # get first para val
            instrct_pointer += 1
            first_para_val = read_para_value(codes, next(para_modes), instrct_pointer)
            # get second para val
            instrct_pointer += 1
            second_para_val = read_para_value(codes, next(para_modes), instrct_pointer)
            # write the result
            instrct_pointer += 1
            exec_compare(codes, instrct_pointer, first_para_val, second_para_val, opcode)
        else:
            # find unknown op code
            print("unknown opcode: " + str(opcode))
            continue
        # keep increase instruction pointer if no jump happened
        if not jump:
            instrct_pointer += 1

def main():
    f = open("input.txt", 'r')
    codes = list(map(lambda x: int(x), f.read().split(',')))
    f.close()
    # based on the problem, init input value = 5
    init_input_val = 5
    # start to process
    print("Start code")
    int_code_program(codes, init_input_val)
    print("Finish code")

main()
