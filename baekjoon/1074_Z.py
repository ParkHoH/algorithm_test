N, r, c = map(int, input().split())

def dfs(N, r, c):
	if N == 0:
		return 0

	return 2 * (r % 2) + (c % 2) + 4 * dfs(N-1, int(r/2), int(c/2))

print(dfs(N, r, c))