def solution(s):
    lst = []
    list = s.split(" ")
    for i in list:
   
        lst.append(i.capitalize())
    return " ".join(lst)