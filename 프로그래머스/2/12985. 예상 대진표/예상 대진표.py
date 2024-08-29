def solution(n,a,b):
    cnt = 1
    while n>1:
        room = 1
        room_lst = []
        for i in range(1,n+1,2):
            if a == i or a == i + 1:
                room_lst.append(room)
            if b == i or b == i + 1:
                room_lst.append(room)
            room += 1
        if room_lst[0] == room_lst[1]:
            return cnt
        else:
            a = room_lst[0]
            b = room_lst[1]
        n /= 2
        n = int(n)
        cnt += 1
    return 1