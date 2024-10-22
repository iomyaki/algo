import sys


sys.stdin.readline()  # faster version of input()
sys.stdout.write("Sample Text")  # slower version of print("Sample Text")
sys.setrecursionlimit(10 ** 9)  # increase recursion stack size, default: 10 ** 3

x = 3.1415
x = int(x + 0.5)  # mathematically correct rounding

print(f"{x:.12f}")  # print with 12 decimal places
