from math import inf

arrival_time, buses = open("input-13.txt").read().split('\n')
arrival_time = int(arrival_time)

buses = [b for b in buses.split(',')]
in_service = [int(b) for b in buses if b != 'x']


lowest_waiting_time = inf
bus_to_catch = 0

for bus in in_service:
    waiting_time = ((arrival_time // bus) + 1) * bus - arrival_time

    if waiting_time < lowest_waiting_time:
        lowest_waiting_time = waiting_time
        bus_to_catch = bus


print("Part 1:", bus_to_catch * lowest_waiting_time)


buses2 = {bus: idx for idx, bus in enumerate(buses) if bus != 'x'}

# found = False
# i = int(buses[0])
# while not found:
#     found = True
#     for bus, idx in buses2.items():
#         offset = (int(idx) + i) % int(bus)
#         if offset != 0:
#             found = False
#             i += int(buses[0])
#             break 
# print(i)

