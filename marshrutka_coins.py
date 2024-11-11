def select_coins(pocket, price):
    """
    You need to obtain required sum using the smallest possible coins.
    If you cannot make the required sum up from what you have got, make the closest bigger possible
    from the smallest coins possible.
    In both cases, return what will you give to the driver of the Berdsk marshrutka.
    """

    if sum(pocket) < price:
        return "Not enough money"

    pocket.sort()

    for i in range(1, len(pocket) + 1):
        if sum(pocket[:i]) == price:
            return pocket[:i]
        if sum(pocket[:i]) > price:
            handful = pocket[:i]
            break

    diff = sum(handful) - price
    handful.reverse()

    away = []
    for coin in handful:
        if coin <= diff:
            away.append(coin)
            diff -= coin
            if diff == 0:
                [handful.remove(item) for item in away]
                handful.reverse()
                return handful

    handful.reverse()
    return "The sum is bigger than the price", handful


example_pocket = [1, 1, 1, 1, 2, 2, 5, 5, 5, 10, 10]
example_price = 35
# kopecks = [0.01, 0.05, 0.1, 0.5]

print(select_coins(example_pocket, example_price))
