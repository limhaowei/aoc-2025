import os 

def solve(input):
    input= input.strip().split(',')

    ret = 0
    for i in input:
        curr_range = i.strip().split('-')
        for i in range(int(curr_range[0]), int(curr_range[1]) + 1):
            if check(str(i)) == False:
                ret += i
    return ret

def check(id):
    for i in range(1, len(id)//2 + 1):
        if len(id) % i != 0:
            continue
        block = id[:i]
        if block * (len(id)//i) == id:
            return False
    return True

# def check(id):
#     if len(id) % 2 != 0:
#         return True
#     if id[:len(id)//2] != id[len(id)//2:]:
#         return True
#     return False






if __name__ == "__main__":
    with open(os.path.join(os.path.dirname(__file__), 'input.txt'), 'r') as f:
        input_data = f.read()

    print(solve(input_data))