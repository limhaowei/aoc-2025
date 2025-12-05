import os

def solve1(map):
    rows = len(map)
    cols = len(map[0])

    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    ret = 0

    for i in range(rows):
        for j in range(cols):
            if map[i][j] != '@':
                continue
            neigbors = 0
            for dr, dc in directions:
                nr, nc = i + dr, j + dc
                if 0 <= nr < rows and 0 <= nc < cols and map[nr][nc] == '@':
                    neigbors += 1
            if neigbors < 4:
                ret += 1
    return ret

def solve2(map):
    rows = len(map)
    cols = len(map[0])

    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    ret = 0
    map = [list(row) for row in map]

    while True:
        to_remove = []
        for i in range(rows):
            for j in range(cols):
                if map[i][j] != '@':
                    continue
                neigbors = 0
                for dr, dc in directions:
                    nr, nc = i + dr, j + dc
                    if 0 <= nr < rows and 0 <= nc < cols and map[nr][nc] == '@':
                        neigbors += 1
                if neigbors < 4:
                    to_remove.append((i, j))
        if not to_remove:
            break
        for i, j in to_remove:
            map[i][j] = '.'
        ret += len(to_remove)
    return ret
 


if __name__ == "__main__":
    with open(os.path.join(os.path.dirname(__file__), 'input.txt'), 'r') as f:
        input_data = [line.strip() for line in f]
    print(solve1(input_data))
    print(solve2(input_data))