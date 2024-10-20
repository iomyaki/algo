from math import sqrt, ceil


def factorization(n):
    answer = ''
    for i in range(2, ceil(sqrt(n)) + 1):
        counter = 0
        while n % i == 0:
            n //= i
            counter += 1

        if counter != 0:
            if counter != 1:
                answer += f'{i}^{counter}*'
            else:
                answer += f'{i}*'

    if n != 1:
        answer += f'{n}'

    if answer[-1] == '*':
        return answer[:-1]

    return answer


def main():
    print(factorization(int(input())))


if __name__ == '__main__':
    main()
