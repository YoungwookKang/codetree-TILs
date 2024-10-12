from collections import deque
row, col, k = map(int,input().split())
infomations = [list(map(int,input().split())) for _ in range(k)]
row = row + 2
board = [[0] * col for _ in range(row)]
exit_location = [[False] * col for _ in range(row)]
total_count = 0
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
def can_move(r, c):
    global board
    if c-1 <0 or c+1 >= col or r + 1 >= row:
        return False
    if board[r][c] != 0 or board[r+1][c] != 0 or board[r-1][c] != 0 or board[r][c + 1] != 0 or board[r][c-1] != 0: 
        return False
    return True

def bfs(x, y):
    visited = [[False] * col for _ in range(row)]
    q = deque()

    q.append((x,y))
    visited[x][y] = True
    max_row = 0
    while q:
        a, b = q.popleft()
        for i in range(4):
            nx, ny = a + dx[i], b + dy[i]
            if 0 <= nx < row and 0 <= ny < col and not visited[nx][ny] and board[nx][ny] != 0:
                if board[a][b] == board[nx][ny]:
                    # print(f'nx,ny = {nx,ny}')
                    q.append((nx,ny))
                    visited[nx][ny] = True
                    max_row = max(max_row, nx-1)
                elif  exit_location[a][b] and board[nx][ny] != 0:
                    # print(f'nx,ny = {nx,ny}')
                    q.append((nx,ny))
                    visited[nx][ny] = True
                    max_row = max(max_row, nx-1)
    # print(f'max_row = {max_row}')
    return max_row

def move(r,c, d, golem_id):
    global board, exit_location, total_count
    # print(f'r,c = {r,c}')
    if can_move(r + 1, c):
        move(r + 1, c, d, golem_id)
    elif can_move(r + 1, c-1):
        move(r +1, c - 1, (d - 1) % 4, golem_id)
    elif can_move(r+1, c+1):
         move(r +1, c + 1, (d + 1) % 4, golem_id)
    else:
        if 0<= r <= 2:
            board = [[0] * col for _ in range(row)]
            exit_location = [[False] * col for _ in range(row)]
        else:
            board[r][c] = golem_id
            for i in range(4):
                board[r+dx[i]][c+dy[i]] = golem_id
            exit_location[r+dx[d]][c+dy[d]] = True
            total_count += bfs(r, c)
    
for golem_id in range(len(infomations)):
    c_i, d_i = infomations[golem_id]
    r = 0
    # print(f"{golem_id +1}번째 골렘")
    move(r, c_i -1, d_i, golem_id + 1)
    # for ele in board:
    #     print(ele)
print(total_count)