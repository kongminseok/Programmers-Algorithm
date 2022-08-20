def solution(arr):
    answer = []
    for idx in range(len(arr)):
        if idx == len(arr)-1:
            answer.append(arr[idx])
            break
        elif arr[idx] == arr[idx+1]:
            continue
        else:
            answer.append(arr[idx])
    return answer