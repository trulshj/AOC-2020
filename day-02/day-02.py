import time

start_time = time.time()
print()
print(" Day 2 ".center(48, '-'))

lines = [x.rstrip() for x in open("input-02.txt").readlines()]

valid_passwords_1 = 0
valid_passwords_2 = 0
for line in lines:
    line = line.split(" ")
    min, max = [int(x) for x in line[0].split('-')]
    char = line[1][0]
    password = line[2]

    policy_1 = password.count(char) >= min and password.count(char) <= max
    policy_2 = (password[min-1] == char) ^ (password[max-1] == char)
    if policy_1:
        valid_passwords_1 += 1
    if policy_2:
        valid_passwords_2 += 1


print(f"Part 1: {valid_passwords_1}".center(48))
print(f"Part 2: {valid_passwords_2}".center(48))
print("\n")
print(f"Found in {time.time() - start_time} seconds".center(48))
print(48 * '-')
