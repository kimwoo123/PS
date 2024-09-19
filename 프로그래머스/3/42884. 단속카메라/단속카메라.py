def solution(routes):
    answer = 1
    routes.sort()
    his = routes[0][:]
    for s, e in routes:
        if s <= his[1]:
            his[0] = s
            if e <= his[1]:
                his[1] = e
        else:
            his[0], his[1] = s, e
            answer += 1
    return answer