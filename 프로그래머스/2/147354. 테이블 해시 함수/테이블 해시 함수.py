def solution(data, col, row_begin, row_end):
    data.sort(key=lambda x:(x[col-1], -x[0]))
    targets = data[row_begin-1: row_end]
    
    i = row_begin
    answer = 0
    for t in targets:
        total = 0
        for n in t:
            total += (n%i)
        answer ^= total
        i += 1
    
    return answer