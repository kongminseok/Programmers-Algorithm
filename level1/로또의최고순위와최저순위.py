def solution(lottos, win_nums):
    answer = [7,7]
    win_nums = sorted(win_nums)
    answer[0] -= lottos.count(0)
    for element in win_nums:
        if element in lottos:
            answer[0] -= 1
            answer[1] -= 1
    if answer[0]==7:
        answer[0]=6
    if answer[1]==7:
        answer[1]=6
    return answer