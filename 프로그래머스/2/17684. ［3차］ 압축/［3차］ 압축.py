def solution(msg):
    count_dict = {chr(ord('A') + i): i+1 for i in range(26)}
    
    index = 27
    l = len(msg)
    answer = []
    i = 0
    while i < l:
        for j in range(2, l-i+1):
            key = msg[i:i+j]
            if key not in count_dict:
                count_dict[key] = index
                answer.append(count_dict[msg[i:i+j-1]])
                index += 1
                i += j-1
                break
        else:
            answer.append(count_dict[msg[i:]])
            return answer
