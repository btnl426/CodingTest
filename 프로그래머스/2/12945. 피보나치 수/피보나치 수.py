def solution(n):
    list = func_make_fibo_list(n)
    answer = list[n-1]+list[n-2]
    # print(n)
    # print(list)
    # print(answer)
    answer %= 1234567
    return answer


def func_make_fibo_list(n):
    list_fibo = [0, 1]
    for i in range(2, n):
        list_fibo.append(list_fibo[i-2]+list_fibo[i-1])
    
    return list_fibo