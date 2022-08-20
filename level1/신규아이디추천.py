import re
def solution(new_id):
    answer = ''
    #1
    new_id = new_id.lower()
    #2
    p = re.compile('[.\w_-]+')
    new_id = p.findall(new_id)
    new_id = ''.join(map(str, new_id))
    #3
    new_id = re.sub('[.]+','.',new_id)
    #4
    if new_id == '':
        pass
    elif new_id[0]=='.':
        new_id = new_id[1:]
    elif new_id[-1]=='.':
        new_id = new_id[:-1]
    #5
    if new_id=='':
        new_id = 'a'
    #6
    if len(new_id)>=16:
        new_id = new_id[:15]
    if new_id[-1]=='.':
        new_id = new_id[:-1]
    #7 
    if len(new_id)<=2:
        while(1):
            new_id = new_id + new_id[-1]
            if len(new_id)==3:
                break
                
    answer = new_id
    return answer