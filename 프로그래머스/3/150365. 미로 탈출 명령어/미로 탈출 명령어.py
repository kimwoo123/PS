def get_distance(pos, dest):
    return abs(pos[0] - dest[0]) + abs(pos[1] - dest[1])

def solution(n, m, x, y, r, c, k):
    start = (x-1, y-1)
    dest = (r-1, c-1)
    
    remain = k - get_distance(start, dest)
    if remain < 0 or remain % 2:
        return "impossible"
    
    # d l r u
    answer = ''
    if start[0] < dest[0]:
        answer += 'd' * (dest[0] - start[0])
    cur_x = max(start[0], dest[0])
    after_u = 0
    while remain and cur_x < n-1:
        cur_x += 1
        after_u += 1
        answer += 'd'
        remain -= 2
    
    if start[1] > dest[1]:
        answer += 'l' * (start[1] - dest[1])
    cur_y = min(dest[1], start[1])
    after_r = 0
    while remain and cur_y > 1:
        cur_y -= 1
        after_r += 1
        answer += 'l'
        remain -= 2
        
    if cur_y != 0:
        answer += 'lr' * (remain // 2)
    else:
        answer += 'rl' * (remain // 2)
    
    if start[1] < dest[1]:
        answer += 'r' * (dest[1] - start[1])
    answer += 'r' * after_r
        
    if start[0] > dest[0]:
        answer += 'u' * (start[0] - dest[0])
    answer += 'u' * after_u
        
    return answer