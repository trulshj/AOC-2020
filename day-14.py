import re

data = open("input-14.txt").read().split("mask = ")


def apply_mask(value, mask):
    b_val = str(bin(int(value)))[2:].zfill(36)
    for i in range(len(b_val)):
        if mask[i] != 'X':
            b_val = b_val[:i] + mask[i] + b_val[i+1:]
    return int(b_val, 2)


memory = {}

for program in data[1:]:
    program = program.split("\n")
    mask = program[0]
    if program[-1] == '':
        program.pop()
    instructions = [re.findall(r"mem\[(\d+)\] = (\d+)", x)[0] for x in program[1:]]

    for location, value in instructions:
        memory[location] = apply_mask(value, mask)

print("Part 1:", sum(memory.values()))

