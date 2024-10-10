n = int(input())
days = [list(map(int, input().split())) for _ in range(n)]
max_value = 0

def backtracking(curr, n, days, current_value):
    global max_value
    if curr > n:
        return
    elif curr == n:
        max_value = max(current_value, max_value)
        return
    
    duration, profit = days[curr][0], days[curr][1]
    backtracking(curr+duration, n, days, current_value + profit)
    backtracking(curr+1, n, days, current_value)

backtracking(0,n,days,0)

print(max_value)