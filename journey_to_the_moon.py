# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import defaultdict


def get_combinations(N, l, list_of_pairs):
    # N, l are ints, list_of_pairs is an iterable of lists of pairs
    astronauts = defaultdict(set)
    all_astronauts = list(xrange(N))
    for i in list_of_pairs:
        a, b = i[0], i[1]
        # Store a and b in an appropriate data structure
        # {
        #    0: {2},
        #    1: {8, 4},
        # }
        astronauts[a].add(b)
        astronauts[b].add(a)

    sizes = []
    visited_nodes = set()
    for astronaut in astronauts:
        if astronaut in visited_nodes:
            continue
        size = 0
        # What does this mean?
        nodes_to_explore = {astronaut}
        while nodes_to_explore:
            current_astronaut = nodes_to_explore.pop()
            visited_nodes.add(current_astronaut)
            size += 1
            nodes_to_explore.update(astronauts[current_astronaut] - visited_nodes)
        sizes.append(size)
    astronauts_missing = set(all_astronauts) - visited_nodes
    number_of_missing_astronauts = len(astronauts_missing)
    result = 0
    for index, size in enumerate(sizes):
        result += size * (sum(other_size for other_size in sizes[index+1:]))
    result += sum(sizes) * number_of_missing_astronauts + (number_of_missing_astronauts-1)*(number_of_missing_astronauts)/2

    return result
