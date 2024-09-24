def solution(record):
    answer = []
    
    name_map = dict()
    for log in record:
        log = log.split()
        if log[0] == "Enter":
            name_map[log[1]] = log[2]
        elif log[0] == "Change":
            name_map[log[1]] = log[2]
            
    for log in record:
        log = log.split()
        if log[0] == "Enter":
            answer.append(f"{name_map[log[1]]}님이 들어왔습니다.")
        elif log[0] == "Leave":
            answer.append(f"{name_map[log[1]]}님이 나갔습니다.")
    
    return answer