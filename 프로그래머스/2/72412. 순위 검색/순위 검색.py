from bisect import bisect_left

def solution(info, query):
    answer = []
    count = dict()
    for each_info in info:
        lan, group, exp, food, score = each_info.split()
        score = int(score)
        if lan not in count:
            count[lan] = {}
        node = count[lan]
        if group not in node:
            node[group] = {}
        node = node[group]
        if exp not in node:
            node[exp] = {}
        node = node[exp]
        if food not in node:
            node[food] = []
        node = node[food]
        node.append(score)
    
    visited = set()
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