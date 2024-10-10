n = int(input())
board = [list(map(int,input().split())) for _ in range(n)]

min_diff = float('inf')
def backtracking(curr, depth, board, curr_list, n):
    global min_diff
    # print(f'현재 리스트 {curr_list}')
    
    if len(curr_list) == depth:
        total_set = set()
        other_list = []
        for i in range(n + 1):
            total_set.add(i)
        for ele in curr_list:
            total_set.remove(ele)
        for ele in total_set:
            other_list.append(ele)
        
        # print(f'other_list = {other_list}')

        morning_value = 0
        evening_value = 0
        for i in range(len(curr_list)):
            for j in range(i+1, len(curr_list)):
                morning_value += board[curr_list[i]][curr_list[j]]
                morning_value += board[curr_list[j]][curr_list[i]]
        for i in range(len(other_list)):
            for j in range(i + 1, len(other_list)):
                evening_value += board[other_list[i]][other_list[j]]
                evening_value += board[other_list[j]][other_list[i]]
        curr_diff = abs(morning_value - evening_value)
        # print(f'{curr_list}, {curr_diff}')
        min_diff = min(min_diff, curr_diff)
        return
    if curr > n:
        return
    backtracking(curr + 1, depth, board, curr_list + [curr], n)
    backtracking(curr + 1, depth, board, curr_list, n)
        
        
        
        

backtracking(0, n//2, board, [], n-1)
print(min_diff)