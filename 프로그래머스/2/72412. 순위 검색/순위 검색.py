from bisect import bisect_left

def solution(info, query):
    answer = []
    count = dict()
    for each_info in info:
        i = each_info.split()
        score = int(i[4])
        score = i[4] = int(i[4])
        node = count
        for k in i[:-2]:
            if k not in node:
                node[k] = {}
            node = node[k]
        food = i[3]
        if food not in node:
            node[food] = []
        node = node[food]
        node.append(score)
        
    def dfs(node):
        for k in node:
            if k == "pizza" or k == "chicken":
                node[k].sort()
            else:
                dfs(node[k])
    dfs(count)
    
    for q in query:
        temp = q.split()
        q = (temp[0], temp[2], temp[4], temp[6], temp[7])
        
        current_nodes = [count]
        for k in q[:4]:
            next_nodes = []
            for node in current_nodes:
                if k == '-':
                    for key in node:
                        next_nodes.append(node[key])
                elif k in node:
                    next_nodes.append(node[k])
            current_nodes = next_nodes

        total = 0
        target = int(q[-1])
        for scores in current_nodes:
            l = len(scores)
            i = bisect_left(scores, target)
            diff = l - i
            total += diff
        answer.append(total)
        
    return answer