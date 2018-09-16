"""
对应题面 https://leetcode.com/problems/number-of-islands/
"""

from pprint import pprint

OUT_FILE = '201809100141-陈路.txt'

def solve(G):
    visited = set()
    def dfs(G, x, y):
        '''深度遍历查找'''
        #上下左右
        visited.add((y, x))
        print('visit', (y,x))
        for dx, dy in ((-1, 0), (1, 0), (0, 1), (0, -1)):
            newx, newy = x+dx, y+dy
            if 0 <= newx < len(G[0]) and 0 <= newy < len(G):
                # 陆地且未访问过
                if G[newy][newx] == '1' and (newy, newx) not in visited:
                    dfs(G, newx, newy) # 访问邻居
    
    def find_start():
        # 每次找到没有访问过的第一个节点作为探索的起始节点
        for i in range(len(G)):
            for j in range(len(G[0])):
                # print(i, j, G[i][j])
                if (i, j) not in visited and G[i][j] == '1':
                    return i, j
        return None
    
    count = 0
    while 1:
        res = find_start()
        print('select', res)
        if res is None:
            return count
        y, x = res
        dfs(G, x, y)
        count += 1

def read_data(filename):
    sections = open(filename).read().split('---')
    data = []
    for section in sections:
        section = section.strip()
        if section:
            data.append(section.splitlines())
    return data

if __name__ == '__main__':
    data = read_data('islands.txt')
    with open(OUT_FILE, 'w') as f:
        for G in data:
            pprint(G)
            res = solve(G)
            f.write(str(res) + '\n')
    print(f'Write to {OUT_FILE} completed')
