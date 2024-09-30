def str_to_time(s):
    hh, mm = s.split(':')
    return (int(hh) * 60) + int(mm)

def time_to_str(t):
    return str(t // 60).zfill(2) + ":" + str(t % 60).zfill(2)

def solution(n, t, m, timetable):
    answer = ''
    
    time_table = tuple(sorted(map(str_to_time, timetable)))    
    time_index = 0
    l = len(time_table)
    start = str_to_time("09:00")
    for i in range(n):
        current = start + (t * i)
        count = 0
        while time_index < l and count < m:
            if current >= time_table[time_index]:
                time_index += 1
                count += 1
            else:
                break
        if count == m:
            # if time_index == l:
                # answer = time_table[-1] - 1
            # else:
            answer = time_table[time_index - 1] - 1
        else:
            answer = current
        
    return time_to_str(answer)