from collections import Counter

def solution(k, tangerine):
    # 1. 리스트의 요소 빈도 계산
    counter = Counter(tangerine)
    
    # 2. 빈도수를 기준으로 내림차순 정렬
    sorted_elements = sorted(counter.items(), key=lambda x: x[1], reverse=True)
    
    # 3. k 개 이상의 요소를 만들 수 있는 최소 요소를 찾기
    total_count = 0
    unique_count = 0
    
    for element, count in sorted_elements:
        total_count += count
        unique_count += 1
        
        if total_count >= k:
            return unique_count
    
    return None