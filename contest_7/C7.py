from collections import deque


# receive the data
n, k = map(int, input().split())
costs = list(map(int, input().split()))

# prepare lists and deques for work
costs = [0] + costs + [0]
d = [0 for _ in range(n + k)]
queue = deque([0 for _ in range(k)])
q_max = deque([(0, 0) for _ in range(k)])  # contains (value, idx(value) in list d)
gr_is = []

# iterate through every pile
for i in range(k, n + k):
    # calculate the sum for the ith pile and indicate its "parent"
    d[i] = q_max[0][0] + costs[i - k]
    gr_is.append(q_max[0][1] + 1)

    # refresh the main queue
    queue.append(d[i])
    if q_max[0][0] == queue.popleft():
        q_max.popleft()

    # refresh the max queue
    while len(q_max) > 0 and q_max[-1][0] < d[i]:
        q_max.pop()
    q_max.append((d[i], i - k))

# prepare the list of piles in 1-based indexing
piles = [n]
last_pile = gr_is[-1]
while last_pile > 1:
    piles.append(last_pile)
    last_pile = gr_is[last_pile - 1]

# display the answer
print(d[-1])
print(len(piles))
print(*[1] + piles[::-1])
