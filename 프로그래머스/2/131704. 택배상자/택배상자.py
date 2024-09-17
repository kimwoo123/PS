

def solution(order):
    answer = 0
    l = len(order)
    box_list = list(range(l, 0, -1))
    stack = []
    for target in order:
        if stack and stack[-1] == target:
            del stack[-1]
            answer += 1
            continue
        flag = True
        while box_list:
            box = box_list.pop()
            if box == target:
                flag = False
                answer += 1
                break
            stack.append(box)
        if flag:
            break
    return answer