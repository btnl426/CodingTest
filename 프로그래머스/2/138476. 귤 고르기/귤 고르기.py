def solution(k, tangerine):
    # 1. 빈도 계산을 위한 딕셔너리 생성
    count_dic = {}
    
    # 2. 리스트를 순회하면서 빈도 계산
    for t in tangerine:
        if t in count_dic:
            count_dic[t] += 1
        else:
            count_dic[t] = 1
    
    # 3. 빈도수를 기준으로 내림차순 정렬
    # count_dic.items() -> (숫자, 빈도수) 튜플의 리스트
    sorted_elements = sorted(count_dic.items(), key=lambda x: x[1], reverse=True)
    
    # 4. k 개 이상의 요소를 만들 수 있는 최소 요소 수 찾기
    total_count = 0
    unique_count = 0
    
    for element, count in sorted_elements:
        total_count += count
        unique_count += 1
        
        if total_count >= k:
            return unique_count
    
    return None
