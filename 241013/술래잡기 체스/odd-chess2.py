dxs = [-1, -1,  0,  1, 1, 1, 0, -1]
dys = [ 0, -1, -1, -1, 0, 1, 1,  1]

from copy import deepcopy

n = 4

board = [
    [(0, 0) for _ in range(n)]
    for _ in range(n)
]

max_score = 0
TAGGER = (-2, -2)
BLANK = (-1, -1)

def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n
# 도둑말이 이동할 수 있는 곳인지를 판단합니다.
# 격자 안이면서, 술래가 없어야 합니다.
def thief_can_go(x, y):
    return in_range(x, y) and board[x][y] != TAGGER


# 술래가 이동할 수 있는 곳인지를 판단합니다.
# 격자 안이면서, 도둑말이 있어야만 합니다.
def tagger_can_go(x, y):
    return in_range(x, y) and board[x][y] != BLANK


def done(x, y, d):
    # 현재 위치에도 한 곳이라도 갈 수 있는지 확인합니다.
    # 존재한다면, 아직 게임은 끝나지 않았습니다.
    for dist in range(1, n + 1):
        nx, ny = x + dxs[d] * dist, y + dys[d] * dist
        if tagger_can_go(nx, ny):
            return False
    
    return True


def get_next(x, y, move_dir):
    # 45'씩 8번 회전해보면서 최초로 이동 가능한 곳으로 움직입니다.
    for rotate_num in range(8):
        adjusted_dir = (move_dir + rotate_num) % 8
        next_x, next_y = x + dxs[adjusted_dir], y + dys[adjusted_dir]
        if thief_can_go(next_x, next_y):
            return (next_x, next_y, adjusted_dir)
    
    # 이동이 불가능하다면 현재 위치, 현재 방향 그대로 유지되어야합니다.
    return (x, y, move_dir)


def swap(x, y, nx, ny):
    board[x][y], board[nx][ny] = board[nx][ny], board[x][y]


def move(target_num):
    for x in range(n):
        for y in range(n):
            piece_num, move_dir = board[x][y];
            if piece_num == target_num:
                # 이동해야할 위치와 바라보게 될 방향을 구합니다.
                next_x, next_y, next_dir = get_next(x, y, move_dir)
                # 현재 말의 방향을 바꿔준 뒤, 두 말의 위치를 교환합니다.
                board[x][y] = (piece_num, next_dir)
                swap(x, y, next_x, next_y)
                return


# 모든 도둑말들을 한번씩 움직입니다.
def move_all():
    for i in range(1, n * n + 1):
        move(i)


# 현재 술래말의 위치가 (x, y), 
# 바라보고 있는 방향이 d이고
# 지금까지 얻은 점수가 score일때
# 탐색을 계속 진행하는 함수입니다.
def search_max_score(x, y, d, score):
    global max_score, board
    
    # 더 이상 움직일 곳이 없다면
    # 답을 갱신하고 퇴각합니다.
    if done(x, y, d):
        max_score = max(max_score, score)
        return
    
    # 현재 턴에 움직일 수 있는 곳을 전부 탐색합니다.
    for dist in range(1, n + 1):
        nx, ny = x + dxs[d] * dist, y + dys[d] * dist
        # 술래가 이동 할 수 없는 위치라면, 패스합니다.
        if not tagger_can_go(nx, ny):
            continue
        
        # 더 탐색을 진행한 이후, 초기 상태로 다시 만들기 위해
        # temp 배열에 현재 board 상태를 저장해놓습니다.
        temp = deepcopy(board)
        
        # 해당 위치의 도둑말을 잡고
        extra_score, next_dir = board[nx][ny];
        board[nx][ny], board[x][y] = TAGGER, BLANK
        
        # 모든 도둑말을 움직입니다.
        move_all()
        
        # 그 다음 탐색을 진행합니다. 
        search_max_score(nx, ny, next_dir, score + extra_score)
        
        # 퇴각시 다시 이전 board의 값을 넣어줍니다.
        board = temp

for i in range(n):
    given_row = list(map(int, input().split()))
    for j in range(n):
        p, d = given_row[j * 2], given_row[j * 2 + 1]
        board[i][j] = (p, d - 1)

init_score, init_dir = board[0][0]
board[0][0] = TAGGER

move_all()

search_max_score(0, 0, init_dir, init_score)
print(max_score)