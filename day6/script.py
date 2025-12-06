import os

def product(lst):
    p = 1
    for x in lst:
        p *= x
    return p

def parse_grid(text):
    lines = text.splitlines()
    while lines and lines[-1].strip() == "":
        lines.pop()

    op_idx = None
    for i in range(len(lines) - 1, -1, -1):
        if '+' in lines[i] or '*' in lines[i]:
            op_idx = i
            break

    ops_line = lines[op_idx]
    num_lines = lines[:op_idx]

    width = max(len(l) for l in lines)
    padded_nums = [l.ljust(width) for l in num_lines]
    padded_ops = ops_line.ljust(width)

    spans = []
    in_span = False
    for col in range(width):
        col_has = padded_ops[col] != " " or any(row[col] != " " for row in padded_nums)
        if col_has and not in_span:
            start = col
            in_span = True
        if not col_has and in_span:
            spans.append((start, col))
            in_span = False
    if in_span:
        spans.append((start, width))

    return padded_nums, padded_ops, spans

def solve1(padded_nums, padded_ops, spans):
    part1 = 0
    for start, end in spans:
        op_frag = padded_ops[start:end].strip()
        if not op_frag:
            continue
        op = op_frag[0]
        nums = []
        for row in padded_nums:
            tok = row[start:end].strip()
            if tok:
                nums.append(int(tok))
        if not nums:
            continue
        if op == '+':
            part1 += sum(nums)
        else:
            part1 += product(nums)
    return part1

def solve2(padded_nums, padded_ops, spans):
    part2 = 0
    for start, end in spans:
        op_frag = padded_ops[start:end].strip()
        if not op_frag:
            continue
        op = op_frag[0]
        nums = []
        for col in range(end - 1, start - 1, -1):
            vertical = "".join(padded_nums[r][col] for r in range(len(padded_nums))).strip()
            if vertical:
                vertical = vertical.replace(" ", "")
                nums.append(int(vertical))
        if not nums:
            continue
        if op == '+':
            part2 += sum(nums)
        else:
            part2 += product(nums)
    return part2

def solve(text):
    padded_nums, padded_ops, spans = parse_grid(text)
    p1 = solve1(padded_nums, padded_ops, spans)
    p2 = solve2(padded_nums, padded_ops, spans)
    return p1, p2

if __name__ == "__main__":
    p = os.path.join(os.path.dirname(__file__), "input.txt")
    with open(p, "r") as f:
        text = f.read()
    p1, p2 = solve(text)
