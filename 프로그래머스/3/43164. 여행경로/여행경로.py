def solution(tickets):
    
    ticket_dict = dict()
    route_dict = dict()
    for start, end in sorted(tickets, key=lambda x:(x[0], x[1])):
        ticket = (start, end)
        if ticket in ticket_dict:
            ticket_dict[ticket] += 1
        else:
            ticket_dict[ticket] = 1
            
        if start in route_dict:
            route_dict[start].append(end)
        else:
            route_dict[start] = [end]
            
    l = len(tickets)
    def dfs(current, count, route):
        if count == l:
            nonlocal answer
            if not answer:
                answer = route[:]
            return
        if current in route_dict:
            for next_city in route_dict[current]:
                ticket = (current, next_city)
                if ticket in ticket_dict and ticket_dict[ticket] != 0:
                    route.append(next_city)
                    ticket_dict[ticket] -= 1
                    dfs(next_city, count + 1, route)
                    ticket_dict[ticket] += 1
                    route.pop()
    answer = None
    dfs("ICN", 0, ["ICN"])
    return answer