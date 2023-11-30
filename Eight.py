content = []

p1, p2 = set(), set()

if __name__ == "__main__":
    with open("inputs/Eight.txt") as f:
        content = f.read().strip()

    map = [[tree for tree in row] for row in content.split("\n")]
    for i in range(1, len(map) - 1):
        for j in range(1, len(map[0]) - 1):
            seen = 1
            for row_move, tree_move in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                row, tree = i, j
                neighbors = []
                while (tree + tree_move >= 0) and (tree + tree_move < len(map[0])) and (row + row_move >= 0) and (row + row_move < len(map)):
                    row += row_move
                    tree += tree_move
                    neighbors.append(map[row][tree])
                if map[i][j] > max(neighbors):
                    p1.add((i, j))
                    seen *= len(neighbors)
                else:
                    seen *= [k+1 for k,
                             n in enumerate(neighbors) if n >= map[i][j]][0]
                p2.add(seen)
    print(f"Part 1: {len(p1) + (4 * (len(map) - 1))}")
    print(f"Part 2: {max(p2)}")
