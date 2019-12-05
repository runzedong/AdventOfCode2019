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

def main():
    count = 0
    for i in range(146810, 612564):
        if check_secure_number(i):
            print(i)
            count += 1
    print("Total secure number: ")
    print(count)

main()