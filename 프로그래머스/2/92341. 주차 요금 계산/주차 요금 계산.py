def str_to_time(s):
    hh, mm = s.split(":")
    return (int(hh) * 60) + int(mm)


def solution(fees, records):
    default_time, default_charge, unit_time, unit_charge = fees
    park_log = dict()
    time_log = dict()
    for record in records:
        time, number, state = record.split()
        time = str_to_time(time)
        if state == "IN":
            park_log[number] = time
        else:
            in_time = park_log[number]
            if number in time_log:
                time_log[number] += time - in_time
            else:
                time_log[number] = time - in_time
            park_log[number] = None
        
    max_time = str_to_time("23:59")
    for k, v in park_log.items():
        if v != None:
            diff = max_time - v
            if k in time_log:
                time_log[k] += diff
            else:
                time_log[k] = diff

    answer = []
    for k in sorted(time_log.keys()):
        total_time = time_log[k]
        charge = default_charge
        if total_time > default_time:
            charge += -(-(total_time - default_time) // unit_time) * unit_charge
        answer.append(charge)
    
    return answer
    