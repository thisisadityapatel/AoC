import collections
import itertools
import math
import time


def input_parser(filename: str) -> list[list[int]]:
    data = []
    with open(filename, "r") as file:
        for line in file:
            data.append(list(map(int, line.strip().split(","))))
    return data


def distance(point1, point2):
    return math.sqrt(
        (point1[0] - point2[0]) ** 2
        + (point1[1] - point2[1]) ** 2
        + (point1[2] - point2[2]) ** 2
    )


def make_tree(coordinates: list[list[int]]):
    combinations = itertools.combinations(coordinates, 2)
    combinations = list(
        map(
            lambda comb: (
                tuple(comb[0]),
                tuple(comb[1]),
                distance(tuple(comb[0]), tuple(comb[1])),
            ),
            combinations,
        )
    )
    combinations.sort(key=lambda x: x[2])
    return combinations


def aggregate_chains(nearest: list):
    tracker = collections.defaultdict(bool)
    chains = []
    for i in range(len(nearest)):
        point1, point2, _ = nearest[i]
        if not tracker[point1]:
            if tracker[point2]:
                for chain in chains:
                    if point2 in chain:
                        chain.add(point1)
                        tracker[point1] = True
                        break
            else:
                chains.append(set([point1, point2]))
                tracker[point1] = True
                tracker[point2] = True
        else:
            if tracker[point2]:
                point1_index, point2_index = -1, -1
                for i, chain in enumerate(chains):
                    if point1_index != -1 and point2_index != -1:
                        break
                    if point1 in chain:
                        point1_index = i
                    if point2 in chain:
                        point2_index = i
                if point1_index != point2_index:
                    chains[point1_index] = chains[point1_index].union(
                        chains[point2_index]
                    )
                    chains.pop(point2_index)
            else:
                for chain in chains:
                    if point1 in chain:
                        chain.add(point2)
                        tracker[point2] = True
                        break
    return chains


def count_chains(chains):
    chain_length = [len(chain) for chain in chains]
    chain_length.sort(reverse=True)
    return math.prod(chain_length[:3])


if __name__ == "__main__":
    start_time = time.time()
    coordinates = input_parser("data.txt")
    tree = make_tree(coordinates)
    chains = aggregate_chains(tree)
    result = count_chains(chains)
    print(result)
    end_time = time.time()
    print(f"Execution time: {end_time - start_time:.6f} seconds")
