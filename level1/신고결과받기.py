def solution(id_list, report, k):
    answer = []
    report_dic = {}
    reported_num =  {}
    stop_id = []
    report = list(set(report))
    for id in id_list:
        report_dic[id] = []
        reported_num[id] = 0
    for idx, case in enumerate(report):
        report_id, reported_id = case.split()[0], case.split()[1]
        report_dic[report_id].append(reported_id)
        reported_num[reported_id] += 1 
    for key, value in reported_num.items():
        if reported_num[key]>=k:
            reported_num[key]=1
            stop_id.append(key)
        else:
            reported_num[key]=0
    for idx, (key, value) in enumerate(report_dic.items()):
        cnt = 0
        for element in stop_id:
            if element in value:
                cnt += 1
        answer.append(cnt)
    
    return answer