def check_secure_number(num):
    digit = 'NULL'
    has_double = False
    while num:
        if digit == 'NULL':
            digit = num % 10
        else:
            next_digit = num % 10
            if next_digit > digit:
                return False
            elif next_digit == digit:
                has_double = True
            else:
                digit = next_digit
        num //= 10
    return has_double

def check_adjacent_case(num):
    digit = 'NULL'
    count = 0
    while num:
        if digit == 'NULL':
            digit = num % 10
            count = 1
        else:
            next_digit = num % 10
            if next_digit == digit:
                count += 1
            else:
                if count == 2:
                    return True
                digit = next_digit
                count = 1
        num //= 10
    return count == 2

def main():
    numbers_filter_one = []
    for i in range(146810, 612564):
        if check_secure_number(i):
            numbers_filter_one.append(i)
    count = 0
    for n in numbers_filter_one:
        if check_adjacent_case(n):
            print(n)
            count += 1
    print('Total number:')
    print(count)
main()