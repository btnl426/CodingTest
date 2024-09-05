def solution(elements):
    # 중복을 피하기 위한 집합
    unique_sums = set()
    
    # 원형 수열을 처리하기 위해 수열을 두 번 이어붙임
    n = len(elements)
    extended_elements = elements * 2

    # 모든 길이에 대해 부분 수열의 합 계산
    for length in range(1, n + 1):
        # 슬라이딩 윈도우 기법으로 부분합을 계산
        for start in range(n):
            subarray_sum = sum(extended_elements[start:start + length])
            unique_sums.add(subarray_sum)

    # 중복을 제거한 합의 개수 반환
    return len(unique_sums)