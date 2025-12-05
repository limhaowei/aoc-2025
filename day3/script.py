import os 

def solve(input):
    input= input.strip().split('\n')
    ret = 0
    for line in input:
        val = process(line)
        ret += val 
    

    return ret

def process(bank):
    stack = []
    remove = len(bank) - 12 

    for i in bank:
        while stack and remove > 0 and stack[-1] < i:
            stack.pop()
            remove -= 1
        stack.append(i)
    return int(''.join(stack[:12]))

# def process(bank):
#     max_jolt = 0
#     for i in range(len(bank)):
#         for j in range(i + 1, len(bank)):
#             jolt = int(bank[i] + bank[j])
#             if jolt > max_jolt:
#                 max_jolt = jolt
#     return max_jolt

if __name__ == "__main__":
    with open(os.path.join(os.path.dirname(__file__), 'input.txt'), 'r') as f:
        input_data = f.read()

    print(solve(input_data))