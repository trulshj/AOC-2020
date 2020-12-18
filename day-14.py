import re

data = open("input-14.txt").read()
mask = re.findall(r"^mask = ([X01]+)", data)[0]
instructions = re.findall(r"mem\[(\d+)\] = (\d+)", data)


def apply_mask(value, mask=mask):
    b_val = str(bin(int(value)))[2:]
    print(b_val)

memory = {}

for location, value in instructions:
    memory[location] = apply_mask(value)
