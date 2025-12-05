import os

def solve1(input):
    
    blank = input.index('')
    id_ranges = input[:blank]
    ids = input[blank + 1:]
    ranges = []
    for i in id_ranges:
        start,end = map(int, i.split("-"))
        ranges.append((start, end))

    id_array = [int(i) for i in ids]
    ret = 0

    for i in id_array:
        for start, end in ranges:
            if start <= i <= end:
                ret += 1
                break
    return ret

def solve2(input):
    blank = input.index('')
    id_ranges = input[:blank]
    ranges = []
    for i in id_ranges:
        start,end = map(int, i.split("-"))
        ranges.append((start, end))

    ranges.sort()
  
    merged = []
    curr_start, curr_end = ranges[0]
    for start, end in ranges[1:]:
        if start <= curr_end + 1:
            curr_end = max(curr_end, end)
        else:
            merged.append((curr_start, curr_end))
            curr_start, curr_end = start, end

    merged.append((curr_start, curr_end))
    ret = 0 
    for start, end in merged:
        ret += end - start + 1
    return ret

if __name__ == "__main__":
    with open(os.path.join(os.path.dirname(__file__), 'input.txt'), 'r') as f:
        input_data = [line.strip() for line in f.readlines()]

    print(solve1(input_data))
    print(solve2(input_data))