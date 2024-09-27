def remain_day(progres, speed):
    return -(-(100 - progres) // speed)

def solution(progresses, speeds):
    answer = []
    l = len(progresses)
    stack = []
    for i in range(l):
        remain = remain_day(progresses[i], speeds[i])
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