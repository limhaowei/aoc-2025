import os
from collections import defaultdict
from math import prod

class UnionFind:
    """
    STRAIGHT FROM GEEKSFORGEEKS
    """
    def __init__(self, n):
        self.parent = list(range(n))
        self.components = n


    def find(self, x):
        if self.parent[x] == x:
            return x
        return self.find(self.parent[x])

    def unite(self, x, y):
        xrep = self.find(x)
        yrep = self.find(y)
        if xrep != yrep:
            self.parent[xrep] = yrep
            self.components -= 1
            return True
        return False


def solve(input):
    distances = []
    for n, (x1,y1,z1) in enumerate(input):
        for m, (x2,y2,z2) in enumerate(input):
            if n < m:
                dist = pow(x1 - x2, 2) + pow(y1 - y2, 2) + pow(z1 - z2, 2)
                distances.append((dist, n, m))

    distances.sort()

    uf = UnionFind(len(input))

    last_box1, last_box2 = None, None

    for d,n,m in distances:
        if uf.unite(n,m):
            last_box1, last_box2 = n, m
            if uf.components == 1:
                break

    x1 = input[last_box1][0]
    x2 = input[last_box2][0]

    return x1 * x2


# for d,n,m in distances[:1000]:
#     uf.unite(n,m)
# 
# sizes = defaultdict(int)
# for i in range(len(input)):
#     sizes[uf.find(i)] += 1
# 
# arr = sorted(sizes.values(), reverse = True)
# return arr[0] * arr[1] * arr[2]

if __name__ == "__main__":
    with open(os.path.join(os.path.dirname(__file__), 'input.txt'), 'r') as f:
        lines = list(map(str.strip, f.readlines()))
        points = []
        for line in lines:
            x,y,z = map(int, line.split(','))
            points.append((x,y,z))

    print(solve(points))
