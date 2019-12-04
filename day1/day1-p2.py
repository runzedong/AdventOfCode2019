from functools import reduce

def calculate_fuel(mass):
    require_fuel = mass // 3 - 2
    if require_fuel <= 0:
        return 0
    return require_fuel + calculate_fuel(require_fuel)

def main():
    print("In Main")
    f = open("p1-input.txt", "r")
    result = reduce(lambda acc, x: acc + calculate_fuel(int(x)), f.readlines(), 0)
    f.close()
    print("Result")
    print(result)

main()