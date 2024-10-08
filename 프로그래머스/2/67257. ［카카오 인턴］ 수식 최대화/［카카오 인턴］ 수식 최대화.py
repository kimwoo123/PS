def my_split(s):
    start_index = -1
    operand = ('*', '+', '-')
    number_list, operand_list = [], []
    for i in range(len(s)):
        if s[i] in operand:
            number_list.append(int(s[start_index+1:i]))
            operand_list.append(s[i])
            start_index = i
    number_list.append(int(s[start_index+1:]))
    return number_list, operand_list

def permutation(operand):
    for i in range(3):
        for j in range(3):
            if i == j:
                continue
            for k in range(3):
                if k == i or k == j:
                    continue
                yield (operand[i], operand[j], operand[k])
                

def solution(expression):
    answer = 0
    
    numbers, operators = my_split(expression)
    for order in permutation(('*', '+', '-')):
        numbers_, operators_ = numbers[:], operators[:]
        for o in order:
            while o in operators_:
                i = operators_.index(o)
                if o == '*':
                    n = numbers_[i] * numbers_[i+1]
                elif o == '+':
                    n = numbers_[i] + numbers_[i+1]
                elif o == '-':
                    n = numbers_[i] - numbers_[i+1]
                numbers_[i] = n
                numbers_.pop(i+1), operators_.pop(i)
                
        if answer < abs(numbers_[0]):
            answer = abs(numbers_[0])
    
    return answer