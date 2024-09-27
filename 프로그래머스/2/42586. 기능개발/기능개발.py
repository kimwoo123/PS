def remain_day(progres, speed):
    return -(-(100 - progres) // speed)

def solution(progresses, speeds):
    answer = []
    stack = []
    for progres, speed in zip(progresses, speeds):
        remain = remain_day(progres, speed)
        count = 0
        while stack and stack[0] < remain:
            del stack[-1]
            count += 1
        if count != 0:
            answer.append(count)
        stack.append(remain)
        
    if stack:
        answer.append(len(stack))
    
    return answer