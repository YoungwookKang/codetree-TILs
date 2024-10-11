from copy import deepcopy
from collections import deque

"""
회전 목표
 (1) 유물 1차 획득 가치를 최대화하고, 
 (2) 회전한 각도가 가장 작은 방법을 선택합니다. 
 (3) 회전 중심 좌표의 열이 가장 작은 구간을, 
 행이 가장 작은 구간을 선택합니다.

 열부터 행으로 찾기 -> 90도 돌리기 -> 180도 돌리기 -> 270도 돌리기
"""

"""
bfs 돌리면서 유물 같은 거 세 개 이상이면 temp에 저장후 삭제
"""
"""
새로운 조각은 열번호가 작은 순으로 생김
행번호가 큰 순으로
다시 사용 불가 pop하면 될듯
"""

"""
한번 더 bfs로 찾기
"""

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def remove_block(board, indices):
    visited = [[False] * len(board) for _ in range(len(board))]
    for index in indices:
        x,y = index
        q = deque()
        q.append((x, y))
        delete_value = board[x][y]
        visited[x][y] = True
        while q:
            x, y = q.popleft()
            board[x][y] = 0
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if 0 <= nx < len(board) and 0 <= ny < len(board[0]) and not visited[nx][ny] and board[nx][ny] == delete_value:
                    q.append((nx, ny))
                    visited[nx][ny] = True
    return board
def bfs(temp, start_x, start_y, visited):
    if temp[start_x][start_y] == 0 and visited[start_x][start_y]:
        return 0, (-1,-1)
    q = deque()
    q.append((start_x, start_y))
    visited[start_x][start_y] = True
    cnt = 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < len(temp) and 0 <= ny < len(temp[0]) and not visited[nx][ny] and temp[nx][ny] == temp[x][y]:
                q.append((nx, ny))
                visited[nx][ny] = True
                cnt += 1
    if cnt >= 3:
        # print(f'여기서 찾음')
        # for ele in temp:
        #     print(ele)
        # print(start_x, start_y, cnt)
        return cnt, (start_x, start_y)
    else:
        return 0, (-1,-1)
def change_board(board, i, j, degree):
    # 90
    temp = deepcopy(board)
    if degree == 0:
        for x in range(3):
            for y in range(3):
                temp[y + i][3 - x - 1 + j] = board[x + i][y + j]
    elif degree == 1:
        for x in range(3):
            for y in range(3):
                temp[3 - 1 - x + i][3 - 1 - y + j] = board[x + i][y + j]
    elif degree == 2:
        for x in range(3):
            for y in range(3):
                temp[3 - 1 - y + i][x + j] = board[x + i][y + j]
    return temp
def rotate(board, i, j, degree):
    global max_count, find_i_j_d, where_i_j
    # 90
    temp = deepcopy(board)
    if degree == 0:
        for x in range(3):
            for y in range(3):
                temp[y + i][3 - x - 1 + j] = board[x + i][y + j]
    elif degree == 1:
        for x in range(3):
            for y in range(3):
                temp[3 - 1 - x + i][3 - 1 - y + j] = board[x + i][y + j]
    elif degree == 2:
        for x in range(3):
            for y in range(3):
                temp[3 - 1 - y + i][x + j] = board[x + i][y + j]
    current_count = 0
    visited = [[False] * len(temp) for _ in range(len(temp))]
    curr_idxes = []
    for x in range(5):
        for y in range(5):
            curr, idx = bfs(temp, x, y, visited)
            current_count += curr
            if curr > 0:
                curr_idxes.append(idx)
    if current_count > max_count:
        max_count = current_count
        find_i_j_d = (i, j, degree)
        where_i_j = curr_idxes

    # for ele in temp:
    #     print(ele)

def refill(board, max_count, remain):
    cnt = 0
    for j in range(5):
        if cnt >= max_count or len(remain) <= 0:
            break
        for i in range(4, -1, -1):
            if cnt >= max_count or len(remain) <= 0:
                break
            if board[i][j] == 0:
                new_block = remain.popleft()
                board[i][j] = new_block
                cnt += 1
    return board

degrees = [0, 1, 2]

k, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(5)]
remains = list(map(int, input().split()))
remain = deque()
for ele in remains:
    remain.append(ele)
total_count = []
for _ in range(k):
    max_count = 0
    find_i_j_d = (0, 0, 0)
    where_i_j = []
    for degree in degrees:
        for j in range(0, 3):
            for i in range(0, 3):
                rotate(board, i, j, degree)
    if max_count == 0:
        break
    # print(f'max_count = {max_count}')
    # print(f"find_i_j = {find_i_j_d}")
    # print(where_i_j)
    board = change_board(board, find_i_j_d[0], find_i_j_d[1], find_i_j_d[2])
    # print("회전")
    # for ele in board:
    #     print(ele)
    # print("지우기")
    board = remove_block(board, where_i_j)
    # for ele in board:
    #     print(ele)

    board = refill(board, max_count, remain)
    # print("채우기")
    # for ele in board:
    #     print(ele)

    need_search = True
    while need_search:
        check_count = 0
        visited = [[False] * len(board) for _ in range(len(board))]
        curr_indices = []
        for x in range(5):
            for y in range(5):
                curr, idx = bfs(board, x, y, visited)
                check_count += curr
                if curr > 0:
                    curr_indices.append(idx)

        if check_count < 3:
            need_search = False
        else:
            board = remove_block(board, curr_indices)
            board = refill(board, max_count, remain)
            max_count += check_count
    total_count.append(max_count)


print(" ".join(map(str, total_count)))