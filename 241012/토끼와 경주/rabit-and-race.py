import heapq

q = int(input())
commands = [list(map(int, input().split())) for _ in range(q)]
n, m, p = commands[0][1], commands[0][2], commands[0][3]
my_sum = {}
S_additional = {}
rabbits = {}
total_sum = 0

heap = []
# 상 하 좌 우
dx = [0, 1, 2, 3]


def move(direction, n, m, i, j, distance, temp_heap):
    if direction == 0:
        distance %= 2 * (n - 1)
        i -= distance
        while 1 > i or i > n:
            if i < 1:
                i = 2 - i
            if i > n:
                i = 2 * n - i
        temp.append((i+j, i, j))

    elif direction == 1:
        distance %= 2 * (n - 1)
        i += distance
        while 1 > i or i > n:
            if i < 1:
                i = 2 - i
            if i > n:
                i = 2 * n - i
        temp.append((i+j, i, j))
    elif direction == 2:
        distance %= 2 * (m - 1)
        j -= distance
        while 1 > j or j > m:
            if j < 1:
                j = 2 - j
            if j > m:
                j = 2 * m - j
        temp.append((i+j, i, j))
    elif direction == 3:
        distance %= 2 * (m - 1)
        j += distance
        while 1 > j or j > m:
            if j < 1:
                j = 2 - j
            if j > m:
                j = 2 * m - j
        temp.append((i+j, i, j))



for command in commands:
    if command[0] == 100:
        for i in range(4, len(command), 2):
            heapq.heappush(heap, (0, 2, 1, 1, command[i]))
            rabbits[command[i]] = command[i + 1]
            my_sum[command[i]] = 0
            S_additional[command[i]] = 0
    elif command[0] == 200:
        _, k, s = command
        candidates = []
        for _ in range(k):
            cnt, low_i_j, low_i, low_j, pid_t= heapq.heappop(heap)
            d_t = rabbits[pid_t]
            temp = []
            for d in dx:
                # print(f"i,j = {low_i, low_j}")
                move(d, n, m, low_i, low_j, d_t, temp)
            temp.sort(reverse=True)
            add_score, new_i, new_j = temp[0]
            candidates.append((add_score, new_i, new_j, pid_t))
            total_sum += add_score
            my_sum[pid_t] += add_score
            # print(my_sum)
            heapq.heappush(heap, (cnt + 1, add_score, new_i, new_j, pid_t))
        candidates.sort(reverse=True)
        __i_j, __i, __j, s_pid_t = candidates[0]
        # print(f'_i, _j, s_pid_t = {__i,__j,s_pid_t}')
        S_additional[s_pid_t] += s
        # print(my_sum)




    elif command[0] == 300:
        _, pid_t, l = command
        rabbits[pid_t] *= l


    elif command[0] == 400:
        max_score = 0
        for score in my_sum:
            max_score = max(max_score, total_sum - my_sum[score] + S_additional[score])
        print(max_score)