class RecentCounter:
    def __init__(self):
        self.pings = []
        self.cnt = 0

    def ping(self, t: int) -> int:
        while self.pings and self.pings[-1] < t - 3000:
            self.pings.pop()
            self.cnt -= 1

        self.pings.insert(0, t)
        self.cnt += 1
        return self.cnt


# быстрее с очередью, но одному челу собеседующий сказал, надо через array (sic)
