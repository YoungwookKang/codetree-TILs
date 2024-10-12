from collections import deque
n, m = map(int, input().split())
board = [list(map(int,input().split())) for _ in range(n)]
stores = []
for _ in range(m):
    ix,iy = map(int,input().split())
    stores.append((ix-1,iy-1))


people = []

dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]
find_stores = [[False] * n for _ in range(n)]
base_camps = [[False] * n for _ in range(n)]

def bfs(i,j,board,visited):
    q = deque()
    q.append((i,j))
    visited[i][j] = True
    need_search = True
    while q and need_search:
        x,y = q.popleft()
        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and not find_stores[nx][ny] and not base_camps[nx][ny]:
                q.append((nx,ny))
                visited[nx][ny] = True
                if board[nx][ny] == 1:
                    base_camps[nx][ny] = True
                    need_search = False
                    return nx, ny

def move_bfs(i,j,board,visited, idx):
    q = deque()
    q.append((i,j, []))
    visited[i][j] = True
    need_search = True
    # print(f'store {idx} = {stores[idx]}')
    while q and need_search:
        x,y,path = q.popleft()
        # print(f'{idx}사람 x,y,path = {x,y,path}')
        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and not find_stores[nx][ny] and not base_camps[nx][ny]:
                q.append((nx,ny, path+[(nx,ny)]))
                visited[nx][ny] = True
                if nx == stores[idx][0] and ny == stores[idx][1]:
                    return path+[(nx,ny)]
t = 0
count_stores = 0
while True or t < 1000:
    t+=1
    # print(f'{t}분')
    flag_idx = -1
    if t-1 < m:
        px,py = stores[t-1]
        visited = [[False] * n for _ in range(n)]
        bx, by = bfs(px,py, board, visited)
        base_camps[bx][by] == True
        people.append([bx,by])
        flag = False
        flag_idx = len(people) - 1
    
    for i in range(len(people)):
        if i == flag_idx or find_stores[stores[i][0]][stores[i][1]]:
            continue
        pi, pj = people[i][0], people[i][1]
        visited = [[False] * n for _ in range(n)]
        _path = move_bfs(pi,pj,board,visited,i)
        
        npi,npj = _path[0]
        # print(f"{i}번째 사람 {npi,npj}로 움직임")
        people[i][0], people[i][1] = npi,npj
        if npi == stores[i][0] and npj == stores[i][1]:
            find_stores[npi][npj] = True
            # print(f"{i}번째 편의점 찾음")
            count_stores += 1

    if count_stores == m:
        break

    
    


print(t)