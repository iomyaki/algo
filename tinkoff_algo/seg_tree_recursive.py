def build(a, v, tl, tr):
    """
    :param a: initial array
    :param v: current tree vertex number
    :param tl: half-segment left border
    :param tr: half-segment right border
    :return: None (modifies tree)
    """
    if tl == tr:
        tree[v] = a[tl]
    else:
        tm = (tl + tr) // 2
        build(a, v * 2, tl, tm)
        build(a, v * 2 + 1, tm + 1, tr)
        tree[v] = tree[v * 2] + tree[v * 2 + 1]


def update(v, tl, tr, pos, new_val):
    """
    :param v: current tree vertex number
    :param tl: half-segment left border
    :param tr: half-segment right border
    :param pos: position to change
    :param new_val: new value to change to
    :return: None (modifies tree)
    """
    if tl == tr:
        tree[v] = new_val
    else:
        tm = (tl + tr) // 2
        if pos <= tm:
            update(v * 2, tl, tm, pos, new_val)
        else:
            update(v * 2 + 1, tm + 1, tr, pos, new_val)
        tree[v] = tree[v * 2] + tree[v * 2 + 1]


def query_sum(v, tl, tr, l, r):
    """
    :param v: current tree vertex number
    :param tl: half-segment left border
    :param tr: half-segment right border
    :param l: query left border
    :param r: query right border
    :return: sum on the [l; r] segment
    """
    if l > r:
        return 0
    if l == tl and r == tr:
        return tree[v]
    tm = (tl + tr) // 2
    return query_sum(v * 2, tl, tm, l, min(r, tm)) + query_sum(v * 2 + 1, tm + 1, tr, max(l, tm + 1), r)


n = 10
tree = [0 for _ in range(n * 4)]
