from collections import deque


def earliest_ancestor(ancestors, starting_node):
    graph = dict(set())

    def get_parents(vertex):
        if vertex in graph:
            return graph[vertex]
        else:
            return set()

    for ancestor in ancestors:
        # print(ancestor[1], ancestor[0])
        # graph[ancestor[0]] = ancestor[1]
        # graph[ancestor[1]].add(ancestor[0])

        if ancestor[1] in graph:
            graph[ancestor[1]].add(ancestor[0])
        else:
            graph[ancestor[1]] = {ancestor[0]}

    earliest = None
    distance = 0

    # DFS - Depth Breadth First Search
    q = deque()
    q.append([starting_node])
    visited = set()

    while len(q) > 0:
        path = q.pop()
        v = path[-1]

        if v not in visited:
            # print(v, path)

            # solution 1
            # if earliest is None:
            #     earliest = path

            # if len(path) == len(earliest):
            #     # print(v, earliest[-1])
            #     if v < earliest[-1]:
            #         # earliest = earliest[:-1] + [v]
            #         earliest = path

            # if len(path) > len(earliest):
            #     earliest = path

            # solution 2
            if len(path) > distance:
                distance = len(path)
                earliest = v

                # if earliest is None:
                #     earliest = v

                # if distance > 1:
                #     earliest = v

                # if v < earliest:
                #     earliest = v

            visited.add(v)
            for parent in get_parents(v):
                q.append(path + [parent])

    if earliest is not None:
        # if only visited 1 node means doesnt have parents
        if distance == 1:
            return -1
        else:
            return earliest
    else:
        return -1


test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7),
                  (4, 5), (4, 8), (8, 9), (11, 8), (12, 1), (10, 1)]

# print()
# print(earliest_ancestor(test_ancestors, 1), 10)
