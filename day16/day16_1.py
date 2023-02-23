from sys import stdin
import functools



graph = {}

@functools.cache
def find_best_path(cur_pos, opened, minutes_left):
    # print(cur_pos, opened, minutes_left, len(opened))
    if len(opened) == len(graph.keys()):
        return 0
    if minutes_left == 0:
        return 0
    if minutes_left == 1 and cur_pos in opened:
        return 0
    if minutes_left == 1 and cur_pos not in opened:
        return graph[cur_pos][0]

    best_flow = 0

    if cur_pos not in opened:
        new_opened = opened + (cur_pos,)
        best_flow = max(best_flow, \
                        find_best_path(cur_pos, new_opened, minutes_left-1) + \
                        graph[cur_pos][0]*(minutes_left-1))

    for pos in graph[cur_pos][1]:
        best_flow = max(best_flow, find_best_path(pos, opened, minutes_left-1))

    return best_flow


if __name__ == '__main__':
    for line in stdin:
        # Valve UU has flow rate=24; tunnels lead to valves MO, FW, LQ
        flow = int(line.strip().split("rate=")[1].split(";")[0])
        valve = line.strip()[6:8]

        if "valves " in line:
            leads = line.strip().split("valves ")[1].split(", ")
        else:
            leads = [line.strip().split("valve ")[1]]

        graph[valve] = (flow, leads)


    cur_pos = 'AA'
    minutes_left = 30
    opened = ('AA',)
    print(find_best_path(cur_pos, opened, minutes_left))
