class Hash:
    def __init__(self, str, simple_base=31):
        self.str = str
        self.simple_base = simple_base
        self.simple_numbers = [1]
        self.prefix_hash = [0] * len(str)
        self.suffix_hash = [0] * len(str)
        self.odd_count = [0] * len(str)
        self.even_count = [0] * len(str)
        self.cnt_palindromes = 0

    def get_hash(self, ind_left, ind_right):
        return self.prefix_hash[ind_right] - (self.prefix_hash[ind_left - 1] if ind_left > 0 else 0)

    def get_rev_hash(self, ind_left, ind_right):
        return self.suffix_hash[ind_left] - (self.suffix_hash[ind_right + 1] if ind_right < len(self.suffix_hash) - 1 else 0)

    def prepare_simple_numbers(self):
        if len(self.str) > len(self.simple_numbers):
            old_size = len(self.simple_numbers)
            self.simple_numbers.extend([self.simple_numbers[-1] * self.simple_base for _ in range(len(self.str) - old_size)])

    def counting_prefix_hash(self):
        self.prefix_hash[0] = ord(self.str[0])
        for i in range(1, len(self.prefix_hash)):
            self.prefix_hash[i] = self.prefix_hash[i - 1] + ord(self.str[i]) * self.simple_numbers[i]

    def counting_suffix_hash(self):
        self.suffix_hash[-1] = ord(self.str[-1])
        for i in range(len(self.str) - 2, -1, -1):
            self.suffix_hash[i] = self.suffix_hash[i + 1] + ord(self.str[i]) * self.simple_numbers[len(self.str) - i - 1]

    def is_palindrome(self, ind_left, ind_right):
        return self.get_hash(ind_left, ind_right) * self.simple_numbers[len(self.str) - ind_right - 1] == self.get_rev_hash(ind_left, ind_right) * self.simple_numbers[ind_left]

    def counting_odd(self):
        for i in range(len(self.odd_count)):
            ind_left = 1
            ind_right = min(i + 1, len(self.odd_count) - i)
            while ind_left <= ind_right:
                middle = (ind_left + ind_right) // 2
                if self.is_palindrome(i - middle + 1, i + middle - 1):
                    #self.odd_count[i] = middle
                    self.cnt_palindromes += 1
                    ind_left = middle + 1
                else:
                    ind_right = middle - 1

    def counting_even(self):
        for i in range(len(self.even_count)):
            ind_left = 1
            ind_right = min(i, len(self.even_count) - i)
            while ind_left <= ind_right:
                middle = (ind_left + ind_right) // 2
                if self.is_palindrome(i - middle, i + middle - 1):
                    #self.even_count[i] = middle
                    self.cnt_palindromes += 1
                    ind_left = middle + 1
                else:
                    ind_right = middle - 1

    def __call__(self):
        self.prepare_simple_numbers()
        self.counting_prefix_hash()
        self.counting_suffix_hash()
        self.counting_odd()
        self.counting_even()
        #for i in range(len(self.str)):
            #self.cnt_palindromes += self.odd_count[i] + self.even_count[i]
        return self.cnt_palindromes


s = 'aaaaa'
h = Hash(s)
print(h())
