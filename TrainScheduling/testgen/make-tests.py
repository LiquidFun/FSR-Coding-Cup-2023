from pathlib import Path
import random
import subprocess
import string

import numpy as np
import networkx as nx
from matplotlib import pyplot as plt

randint = np.random.randint

start_city_name = "rostock"

seed = 337859235
random.seed(seed)
np.random.seed(seed)

def name_generator():
    used = set()
    vowels = sorted("aoiue")
    consonants = sorted(''.join(set(string.ascii_lowercase) - set(vowels)))
    while True:
        name = ''.join(map(random.choice, [consonants, vowels, consonants, vowels, consonants]))
        if name not in used:
            used.add(name)
            yield name

genname = name_generator()


parent_dir = Path(__file__).absolute().parent.parent
solution_path = parent_dir / "solutions" / "with-path.py"

def write_test(name, graph, finish_name) -> bool:
    """Returns False if test-case is impossible"""
    test_path = parent_dir / "tests" / f"{name}.in"
    with open(test_path, 'w') as file:
        print(f"Creating test case {name}:", end="", flush=True)
        file.write(f"{len(graph.nodes)} {len(graph.edges)} {finish_name}\n")
        for fr, to, data in graph.edges.data():
            arrival_times = ' '.join(map(lambda s: f"{s//60:02}:{s%60:02}", data['schedule']))
            file.write(f"{graph.nodes[fr]['name']} {graph.nodes[to]['name']} {data['travel']} {len(arrival_times)} {arrival_times}\n")
        print(f" | ✅ {name}.in (n={len(graph.nodes)})", end="", flush=True)
    ans_path = test_path.parent / f"{name}.ans"
    command = ' '.join(["python", str(solution_path), "<", str(test_path), ">", str(ans_path)])
    subprocess.run(command, shell=True)
    ans = ans_path.open().read().strip()
    if_redoing = "!!! RECREATING TEST-CASE !!!" if ans == "impossible" else ""
    print(f" | ✅ {name}.ans (ans={ans}) {if_redoing}")
    return ans != "impossible"


def make_random(large=False):
    while True:
        if large:
            n = randint(100, 200)
            p = randint(5, 10) / 100
        else:
            n = randint(10, 30)
            p = randint(20, 50) / 100
        graph = nx.generators.fast_gnp_random_graph(n, p, seed=seed, directed=True)
        if all(len(graph.edges(n)) != 0 for n in graph.nodes):
            break

    for node in graph.nodes:
        graph.nodes[node]["name"] = next(genname)
    for edge in graph.edges:
        trains = randint(1, 20)
        graph.edges[edge]["schedule"] = []
        geometric_distribution = np.random.rand() / 1000 + 0.00005 
        while True:
            travel = np.random.geometric(geometric_distribution)
            if travel < 23*60:
                break
        graph.edges[edge]["travel"] = travel
        for _ in range(trains):
            while True:
                depart = randint(0, 24*60-1 - travel)
                if depart + travel <= 24*60-1:
                    break
            graph.edges[edge]["schedule"].append(depart)
        assert len(graph.edges[edge]['schedule']) != 0
        graph.edges[edge]["schedule"].sort()

    early_sort = []
    late_sort = []
    for n in graph.nodes:
        node = graph.nodes[n]
        early_weight = 0
        late_weight = 0
        for e in graph.edges(n):
            edge = graph.edges[e]
            early_weight += 1 - edge["schedule"][0] / (24*60)
            late_weight += edge["schedule"][-1] / (24*60)

        node["early_score"] = early_weight / np.sqrt(len(graph.edges(n)))
        node["late_score"] = late_weight / np.sqrt(len(graph.edges(n)))

        early_sort.append((node["early_score"], n, sorted([graph.edges[e2]["schedule"][0] for e2 in graph.edges(n)])))
        late_sort.append((node["late_score"], n, sorted([graph.edges[e2]["schedule"][-1] for e2 in graph.edges(n)])))
    start_n = sorted(early_sort)[-1][1]
    finish_n = sorted([t for t in late_sort if t[1] != start_n])[-1][1]
    # for a in sorted(early_sort):
    #     print(a)
    # print()
    # for a in sorted(late_sort):
    #     print(a)
    # print(start_n, finish_n)
    graph.nodes[start_n]["name"] = start_city_name
    #nx.draw(graph)
    #plt.show()
    return graph, graph.nodes[finish_n]["name"]


def make_random_large():
    return make_random(large=True)

def main():
    tests_to_be_created = {
        make_random: 30,
        make_random_large: 30,
    }
    
    for func, how_many in tests_to_be_created.items():
        for i in range(1, how_many+1):
            name = func.__name__.replace("make_", "")
            while not write_test(f"{i:02}-{name}", *func()):
                pass

    # sample_test_cases = [
    # ]

    # for i, inputs in enumerate(sample_test_cases):
    #     write_test(f"{i+1:02}-sample", *inputs)


if __name__ == "__main__":
    main()
