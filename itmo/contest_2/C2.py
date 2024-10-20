def main():
    symbols = input().split()
    operations = {"+", "-", "*"}
    stack = []
    for s in symbols:
        if s not in operations:
            stack.append(int(s))
        else:
            a = stack.pop()
            b = stack.pop()
            if s == "+":
                stack.append(b + a)
            elif s == "-":
                stack.append(b - a)
            elif s == "*":
                stack.append(b * a)
    print(stack[0])


if __name__ == "__main__":
    main()
