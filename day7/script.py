import os

def solve1(input_data):
    rows = len(input_data)
    cols = len(input_data[0])

    start_col = input_data[0].index('S')

    beams = [start_col]
    split_count = 0
    visited = set()

    for row in range(1, rows):
        new_beams = []

        for col in beams:
            if not (0 <= col < cols):
                continue

            if (row, col) in visited:
                continue
            visited.add((row, col))

            cell = input_data[row][col]

            if cell == '^':
                split_count += 1
                if col - 1 >= 0:
                    new_beams.append(col - 1)
                if col + 1 < cols:
                    new_beams.append(col + 1)
            else:
                new_beams.append(col)

        beams = new_beams
        if not beams:
            break

    return split_count

def solve2(input_data):
    rows = len(input_data)
    cols = len(input_data[0])

    start_col = input_data[0].index('S')
    memo = {}

    def dfs(row, col):
        if row >= rows:
            return 1

        if col < 0 or col >= cols:
            return 0

        if (row, col) in memo:
            return memo[(row, col)]

        cell = input_data[row][col]

        if cell == '^':
            result = dfs(row + 1, col - 1) + dfs(row + 1, col + 1)
        else:
            result = dfs(row + 1, col)

        memo[(row, col)] = result
        return result

    return dfs(1, start_col)

if __name__ == "__main__":
    p = os.path.join(os.path.dirname(__file__), 'input.txt')
    with open(p, 'r') as f:
        input_data = [line.strip() for line in f if line.strip()]

    print(solve1(input_data))
    print(solve2(input_data))
