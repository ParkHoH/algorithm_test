# 그리디 문제
# 잘 풀리지 않아 정답을 봤음
N = int(input())
weights = list(map(int, input().split()))
weights.sort()
limit = 1
 
for weight in weights:
    if weight <= limit:
        limit += weight
    else: break

print(limit)