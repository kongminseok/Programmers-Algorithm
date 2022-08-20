def solution(n, lost, reserve):
    lost1 = sorted([x for x in lost if x not in reserve])
    reserve1 = sorted([x for x in reserve if x not in lost])
    for element in reserve1:
        if element-1 in lost1:
            lost1.remove(element-1)
        elif element+1 in lost1:
            lost1.remove(element+1)       
    answer = n - len(lost1)
    return answer