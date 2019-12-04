from functools import reduce

def main():
    print("In Main")
    f = open("p1-input.txt", "r")
    result = reduce(lambda acc, x: acc + int(x) // 3 - 2, f.readlines(), 0)
    f.close()
    print("Result")
    print(result)
main()