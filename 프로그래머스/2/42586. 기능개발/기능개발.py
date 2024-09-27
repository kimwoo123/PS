def remain_day(progres, speed):
    return -(-(100 - progres) // speed)

def solution(progresses, speeds):
    answer = []
    stack = []
    for progres, speed in zip(progresses, speeds):
        remain = remain_day(progres, speed)
        count = 0
        if stack and stack[0] < remain:
            answer.append(len(stack))
            stack = []
        stack.append(remain)
        
    if stack:
        answer.append(len(stack))
    
    return answer