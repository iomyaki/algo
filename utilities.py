import sys


sys.stdin.readline()  # instead of input()
sys.stdout.write('sample text')  # instead of print('sample text')  # it is actually slower than print()
sys.setrecursionlimit(10 ** 9)

x = 3.1415
x = int(x + 0.5)  # mathematically correct rounding

print(f"{x:.12f}")  # print with 12 decimal places
