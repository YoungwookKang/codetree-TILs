from itertools import combinations
from collections import deque
n, m = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(n)]

people = []
hospitals = []

dx = [1,-1, 0,0]
dy = [0,0,1,-1]

def bfs(start, hospitals, board,n):
    q = deque()
    visited = [[False for _ in range(n)] for _ in range(n)]
    i,j = start
    q.append((i,j,0))

    while q:
        x,y, depth = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                if (nx,ny) in hospitals:
                    return True, depth + 1
                q.append((nx,ny,depth+1))
                visited[nx][ny] = True

    return False, 0

def calculate_path(hospitals, people, board,n):
    global min_path
    current_path = 0
    can_do = True
    for person in people:
        check, path = bfs(person, hospitals, board, n)
        if check:
            current_path += path
        else:
            can_do = False
            break
    if can_do:
        min_path = min(min_path, current_path)


for i in range(n):
    for j in range(n):
        if board[i][j] == 1:
            people.append((i,j))
        elif board[i][j] == 2:
            hospitals.append((i,j))


min_path = float('inf')

for selections in combinations(hospitals, m):
    selected_hospitals = {}
    for selection in selections:
        selected_hospitals[selection] = 1
    # print(selected_hospitals)
    calculate_path(selected_hospitals,people,board,n)

print(min_path)