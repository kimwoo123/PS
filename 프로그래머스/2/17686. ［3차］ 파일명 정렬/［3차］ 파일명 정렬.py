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
    return (head.lower(), number)

def solution(files):
    answer = sorted(files, key=lambda x:prepro(x))
    return answer