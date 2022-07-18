def solution(strs, t):
    n = len(t)
    dp = [0] * (n + 1)
    strs = set(strs)
    for i in range(1, n + 1):
        dp[i] = float('inf')
        for k in range(1, 6):
            if i - k < 0:
                s = 0
            else:
                s = i - k

            if t[s:i] in strs:
                dp[i] = min(dp[i], dp[i - k] + 1)

    if dp[-1] == float('inf'):
        answer = -1
    else:
        answer = dp[-1]

    return answer