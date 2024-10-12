from collections import defaultdict, deque
import heapq
q = int(input())
commands = [list(map(int,input().split())) for _ in range(q)]
n, m = commands[0][1], commands[0][2]
graph = [[] for _ in range(n)]
start = 0
distances = [float('inf')] * n
goods = defaultdict(list)
heap = []

def dijkstra(graph, start):
    distances = [float('inf')] * n
    distances[start] = 0
    path = []
    heapq.heappush(path, (0,start))
    while path:
        curr_dist, curr_node = heapq.heappop(path)
        if curr_dist > distances[curr_node]:
            continue
        for neighbor, nw in graph[curr_node]:
            if distances[neighbor] > curr_dist + nw:
                distances[neighbor] = curr_dist + nw
                heapq.heappush(path, (curr_dist + nw, neighbor))

    return distances



for command in commands:
    if command[0] == 100:
        for i in range(1,m+1):
            ui,vi,wi = command[3*i], command[3*i+1], command[3*i+2]
            graph[ui].append((vi,wi))
            graph[vi].append((ui,wi))
        
        distances = dijkstra(graph, start)

    elif command[0] == 200:
        _, _id, rv_id, dest_id = command
        goods[_id] = (rv_id, dest_id)
        if rv_id-distances[dest_id] >= 0:
            heapq.heappush(heap, (-(rv_id-distances[dest_id]), _id))
        

    
    elif command[0] == 300:
        _, _id = command
        if _id in goods:
            del goods[_id]
    
    elif command[0] == 400:
        can_sell = False
        while heap:
            neg_profit, _id = heapq.heappop(heap)
            if _id in goods:
                print(_id)
                del goods[_id]
                break
        else:
            print(-1)

    elif command[0] == 500:
        _, new_start = command
        distances = dijkstra(graph, new_start)
        heap = []
        for goods_id in goods:
            revenue, dest = goods[goods_id][0], goods[goods_id][1]
            if distances[dest] <= revenue:
                profit = revenue - distances[dest]
                heapq.heappush(heap, (-profit, goods_id))