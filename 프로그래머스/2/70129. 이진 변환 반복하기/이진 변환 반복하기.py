def solution(s):
    answer = [0, 0]
    x = s
    l = len(x)
    # x -> c
    # 제거할 0의 개수, 반복 회수, 0 제거 후 길이 -> 2진변환
    while l > 1:
        count = 0
        for b in x:
            if b == "0":
                count += 1
        answer[1] += count
        answer[0] += 1
        x_len = l - count
        x = format(x_len, 'b')
        l = len(x)
    
    return answer