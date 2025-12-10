import os

def solve(input):
    ret = 0 
    for i, (x1,y1) in enumerate(input):
        for j, (x2,y2) in enumerate(input):
            if i < j:
                area = abs((x1 - x2) + 1) * abs((y1 - y2) + 1)
                ret = max(ret, area)
    return ret

            
    

if __name__ == "__main__":
    with open(os.path.join(os.path.dirname(__file__), 'input.txt'), 'r') as f:
        lines = list(map(str.strip, f.readlines()))
        input = []
        for line in lines:
            a, b = map(int, line.split(','))
            input.append((a, b))

    print(solve(input))
  