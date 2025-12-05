import os 
def solve1(input_data):
    
    instructions = input_data.strip().split('\n')
    curr = 50
    ret = 0
    for i in instructions:
        direction = i[0]
        distance = int(i[1:])

        if direction == 'R':
            curr = (curr + distance) % 100
        else:
            curr = (curr - distance) % 100
        
        if curr == 0:
            ret += 1
    
    return ret

def solve2(input_data):
    instructions = input_data.strip().split('\n')
    curr = 50  
    ret = 0
    for i in instructions:
        direction = i[0]
        distance = int(i[1:])

        # holy bruteforce xddd
        for _ in range(distance):
            if direction == 'R':
                curr = (curr + 1) % 100
            else:
                curr = (curr - 1) % 100
            
            if curr == 0:
                ret += 1
    return ret

     

            
if __name__ == "__main__":
    input_file = os.path.join(os.path.dirname(__file__), 'input.txt')
    with open(input_file, 'r') as file:
        input_data = file.read()
    
    print(solve1(input_data))
    print(solve2(input_data))