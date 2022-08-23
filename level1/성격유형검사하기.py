import numpy as np
def solution(survey, choices):
    answer = []
    metrics = {'R':0,'T':0,'C':0,'F':0,'J':0,'M':0,'A':0,'N':0}
    choices = np.array(choices) - 4
    for s,choice in zip(survey,choices):
        if choice<0:
            metrics[s[0]]+=abs(choice)
        elif choice>0:
            metrics[s[1]]+=choice
    if metrics['R']>=metrics['T']:
        answer.append('R')
    else:
        answer.append('T')
    if metrics['C']>=metrics['F']:
        answer.append('C')
    else:
        answer.append('F')
    if metrics['J']>=metrics['M']:
        answer.append('J')
    else:
        answer.append('M')
    if metrics['A']>=metrics['N']:
        answer.append('A')
    else:
        answer.append('N')
    
    answer = ''.join(map(str,answer))
    return answer