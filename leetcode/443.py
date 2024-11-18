class Solution:
    def compress(self, chars: list[str]) -> int:
        write, read, n = 0, 0, len(chars)

        while read < n:
            chars[write] = chars[read]
            write += 1

            read_new = read + 1
            while read_new < n and chars[read] == chars[read_new]:
                read_new += 1

            if read_new - read > 1:
                st = str(read_new - read)
                for c in st:
                    chars[write] = c
                    write += 1

            read = read_new

        return write
