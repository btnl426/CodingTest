def solution(n):
    ans = 0
    cnt = 1
    if n == 1:
        return 1
    while True:
        if n >= 1:
            ans += 1
        if n > 1:
            n = n - maxDoubleNum(n)
        if n == 1:
            ans += 1

        if n < 2 :
            break
        cnt += 1 

    return ans

def maxDoubleNum(n):
    maxDoubleNum = 1
    for i in range(1, n):
        if n >= maxDoubleNum * 2:
            maxDoubleNum *= 2
        else:
            break
    return maxDoubleNum