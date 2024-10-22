import sys


def main():
    sys.stdin.readline()
    employees = list(enumerate(map(int, sys.stdin.readline().split()), start=1))
    prices = list(enumerate(map(int, sys.stdin.readline().split()), start=1))

    employees.sort(key=lambda x: x[1])
    prices.sort(key=lambda y: -y[1])

    comparison = list(zip(employees, prices))
    comparison.sort(key=lambda z: z[0][0])

    for entry in comparison:
        print(entry[1][0], end=" ")


if __name__ == "__main__":
    main()
