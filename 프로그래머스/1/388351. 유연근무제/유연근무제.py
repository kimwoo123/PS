def time_to_int(time):
    return (time // 100) * 60 + (time % 100)


def solution(schedules, timelogs, startday):
    n = len(schedules)
    answer = n
    
    for i in range(n):
        set_time = time_to_int(schedules[i])
        for j in range(7):
            today = startday + j
            if today == 6 or today == 7 or today == 13 or today == 14:
                continue
            log_time = time_to_int(timelogs[i][j])
            if log_time > set_time + 10:
                answer -= 1
                break
                
    
    return answer

