import re

lines = [x.rstrip() for x in open("input-07.txt").readlines()]

contains = {}
contained_in = {}

for line in lines:
    sub_bags = re.findall(r"(\d) (\w+ \w+)", line)
    bag = re.findall(r"^\w+ \w+", line)[0]


    for amount, colour in sub_bags:
        if bag not in contains:
            contains[bag] = []
        contains[bag].append([colour, int(amount)])

        if bag not in contained_in:
            contained_in[bag] = []

        if colour not in contained_in:
            contained_in[colour] = []
        contained_in[colour].append(bag)


def bfs(colour):
    visited = set()
    queue = [colour]
    while queue:
        current = queue.pop()
        for neighbour in contained_in[current]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.insert(0, neighbour)
    return visited

print(len(bfs("shiny gold")))