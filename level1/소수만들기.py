from itertools import combinations
def is_prime_number(num):
    prime = True
    for i in range(2, num):
        if num % i == 0:
            prime = False
    return prime
def solution(nums):
    answer = 0
    for x in combinations(nums, 3):
        if is_prime_number(sum(x)):
            answer += 1
    return answer