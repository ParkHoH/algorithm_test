import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = int(input())
graph = [[] for _ in range(n+1)]

for _ in range(n-1):
    a, b, c = map(int, input().split())
    graph[a].append([b, c])
    graph[b].append([a, c])


def dfs(node, dist):
    if distance[node] == -1:
        distance[node] = dist

        for i, new_dist in graph[node]:
            if distance[i] == -1:
                dfs(i, dist + new_dist)


distance = [-1] * (n+1)
dfs(1, 0)

max_dist = 0
max_idx = 0

for i in range(1, n+1):
    if distance[i] > max_dist:
        max_dist = distance[i]
        max_idx = i

distance = [-1] * (n+1)
dfs(max_idx, 0)
print(max(distance))