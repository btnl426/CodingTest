def solution(numbers):
    # numbers 배열에서 서로 다른 인덱스의 숫자 두 개의 수를 더해서 만들 수 있는 모든 수
    answer = []
    # for i in numbers가 안되는 이유는
    # 안쪽 for문에서 j로 i+1 인덱스를 사용하기 때문
    # 그런데 for i in numbers로 하면 
    # i가 0부터 순차적으로 커지는 숫자가 되는게 아니라
    # numbers 배열 하나하나의 요소가 되는 것
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            answer.append(numbers[i]+numbers[j])
    return sorted(set(answer))