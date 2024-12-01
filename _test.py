def count_dots_in_segments(dots, segments):
    """
    Count how many dots fall within each segment.

    :param dots: List of integers representing the positions of the dots.
    :param segments: List of tuples, where each tuple (start, end) represents a segment.
    :return: List of integers where each value corresponds to the number of dots in the respective segment.
    """
    counts = []
    for start, end in segments:
        count = sum(start <= dot <= end for dot in dots)
        counts.append(count)
    return counts


# Example usage
dots = [1, 2, 3, 5]
segments = [(1, 4), (1, 5), (2, 5), (3, 3), (0, 0)]
result = count_dots_in_segments(dots, segments)
print(result)  # Output: [2, 2, 1]
