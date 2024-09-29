def prepro(file):
    l = len(file)
    for i in range(l):
        if file[i].isdigit():
            head = file[:i]
            for j in range(i+1, l):
                if file[j].isdigit() == False:
                    break
            else:
                j = l
            number = file[i:j]
            tail = file[j:]
            break
    number = int(number)
    return (head, number, tail, file)

def solution(files):
    answer = []
    for c in sorted(map(prepro, files), key=lambda x: (x[0].lower(), x[1])):
        answer.append(c[-1])
    return answer