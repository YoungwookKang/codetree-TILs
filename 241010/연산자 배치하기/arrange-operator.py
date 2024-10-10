n = int(input())
numbers = list(map(int, input().split()))
operators = list(map(int, input().split()))

max_value = -1000000001
min_value = 1000000001
def backtraking(start, depth, numbers, operators, curr_value):
    global max_value, min_value
    if start == depth:
        max_value = max(curr_value, max_value)
        min_value = min(curr_value,min_value)
        return
    if operators[0] > 0:
        operators[0] -= 1
        backtraking(start+1,depth,numbers,operators, curr_value + numbers[start + 1])
        operators[0] += 1
    if operators[1] > 0:
        operators[1] -= 1
        backtraking(start+1, depth, numbers, operators, curr_value - numbers[start + 1])
        operators[1] += 1
    if operators[2] > 0:
        operators[2] -= 1
        backtraking(start+1, depth, numbers, operators, curr_value * numbers[start+1])
        operators[2] += 1





backtraking(0, len(numbers) - 1, numbers, operators, numbers[0])
print(min_value, max_value)