def solution(n, words):
    startIndex = 0
    count = 0
    
    for i in range(len(words)):
        secIndex = 0
        for num, word in enumerate(words[startIndex:startIndex+n]):
            if count >= 1:
                if words[count-1][-1] != words[count][0]:
                    return num+1, i+1
            if word in words[0:startIndex + secIndex]:
                return num+1, i+1
            secIndex += 1
            count += 1 
        startIndex += n
        
    return 0, 0