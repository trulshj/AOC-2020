from math import ceil


def check_boarding_pass(boarding_pass):
    low, high = 0, 127
    for c in boarding_pass[:7]:
        mid = (low + high) // 2
        if c == 'B':
            low = mid
        elif c == 'F':
            high = mid
    row = high

    low, high = 0, 7
    for c in boarding_pass[7:]:
        mid = (low + high) // 2
        if c == 'R':
            low = mid
        elif c == 'L':
            high = mid
    col = high

    id = row * 8 + col

    return [row, col, id]


boarding_passes = [x.rstrip() for x in open("input-05.txt").readlines()]

pass_scores = [check_boarding_pass(boarding_pass)[2] for boarding_pass in boarding_passes]

print(f"Part 1: {max(pass_scores)}")

            