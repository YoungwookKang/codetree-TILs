from itertools import combinations
from collections import deque
n, m = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(n)]

people = []
hospitals = []

dx = [1,-1, 0,0]
dy = [0,0,1,-1]

"""
bfs쓸 필요 없이 |x_2 - x_1| + |y_2 - y_1| 으로 계산하면됨
"""
# def bfs(start, hospitals, board,n):
#     q = deque()
#     visited = [[False for _ in range(n)] for _ in range(n)]
#     i,j = start
#     q.append((i,j,0))

#     while q:
#         x,y, depth = q.popleft()
#         for i in range(4):
#             nx, ny = x + dx[i], y + dy[i]
#             if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
#                 if (nx,ny) in hospitals:
#                     return True, depth + 1
#                 q.append((nx,ny,depth+1))
#                 visited[nx][ny] = True

#     return False, 0

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

distance_board = []
for person in people:
    px,py = person
    distances = []
    for hospital in hospitals:
        hx,hy = hospital
        distance = abs(px-hx) + abs(py-hy)
        distances.append(distance)
    distance_board.append(distances)

# for ele in distance_board:
#     print(ele)
min_path = float('inf')

hospital_indices = [i for i in range(len(hospitals))]
for selections in combinations(hospital_indices, m):
    # print(selections)
    total = 0
    for person_distances in distance_board:
        # 선택된 병원 중 최소 거리 계산
        min_dist = min(person_distances[i] for i in selections)
        total += min_dist
        # 현재 총합이 이미 최소값을 넘으면 더 이상 계산하지 않음
        if total >= min_path:
            break
    if total < min_path:
        min_path = total
    
print(min_path)