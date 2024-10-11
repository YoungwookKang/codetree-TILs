import heapq

q = int(input())
commands = [list(map(int, input().split())) for _ in range(q)]
n, m, p = commands[0][1], commands[0][2], commands[0][3]
scores = {}

heap = []
# 상 하 좌 우
dx = [0, 1, 2, 3]


def move(direction, n, m, i, j, distance, temp_heap):
    if direction == 0:
        i -= distance
        while 1 > i or i > n:
            if i < 1:
                i = 2 - i
            if i > n:
                i = 2 * n - i
        heapq.heappush(temp_heap, (-(i + j), -i, -j))
    elif direction == 1:
        i += distance
        while 1 > i or i > n:
            if i < 1:
                i = 2 - i
            if i > n:
                i = 2 * n - i
        heapq.heappush(temp_heap, (-(i + j), -i, -j))
    elif direction == 2:
        j -= distance
        while 1 > j or j > m:
            if j < 1:
                j = 2 - j
            if j > m:
                j = 2 * m - j
        heapq.heappush(temp_heap, (-(i + j), -i, -j))
    elif direction == 3:
        j += distance
        while 1 > j or j > m:
            if j < 1:
                j = 2 - j
            if j > m:
                j = 2 * m - j
        heapq.heappush(temp_heap, (-(i + j), -i, -j))
    # print(f'{direction}일때 {i, j} 로 감')


for command in commands:
    if command[0] == 100:
        for i in range(4, len(command), 2):
            heapq.heappush(heap, (0, 2, 1, 1, command[i], command[i + 1]))
            scores[command[i]] = 0
    elif command[0] == 200:
        _, k, s = command
        temp_s_heap = []
        for _ in range(k):
            cnt, low_i_j, low_i, low_j, pid_t, d_t = heapq.heappop(heap)
            temp_heap = []
            for d in dx:
                # print(f"i,j = {low_i, low_j}")
                move(d, n, m, low_i, low_j, d_t, temp_heap)
            add_score, new_i, new_j = heapq.heappop(temp_heap)

            heapq.heappush(temp_s_heap, (add_score, new_i, new_j, -pid_t))
            add_score, new_i, new_j = -add_score, -new_i, -new_j
            # print(f'선택된 위치는 {new_i}, {new_j}')

            for score in scores:
                if score != pid_t:
                    scores[score] += add_score
            # print(scores)
            heapq.heappush(heap, (cnt + 1, add_score, new_i, new_j, pid_t, d_t))

        __i_j, __i, __j, s_pid_t = heapq.heappop(temp_s_heap)
        # print(f'_i, _j, s_pid_t = {__i,__j,s_pid_t}')
        scores[-s_pid_t] += s
        # print(scores)




    elif command[0] == 300:
        _, pid_t, l = command
        new_heap = []
        for i in range(p):
            _cnt, _i_j, _i, _j, _pid_t, _d_t = heapq.heappop(heap)
            if _pid_t == pid_t:
                _d_t *= l
            heapq.heappush(new_heap, (_cnt, _i_j, _i, _j, _pid_t, _d_t))
        heap = new_heap


    elif command[0] == 400:
        max_score = 0
        for score in scores:
            max_score = max(max_score, scores[score])
        print(max_score)