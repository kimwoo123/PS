from itertools import combinations, product
from bisect import bisect_left

def find_value(cache, value, l):
    if value in cache:
        return cache[value]
    result = bisect_left(l, value)
    cache[value] = result
    return result

def solution(dice):
    answer = [0, 0]
    l = len(dice)
    dice_combo = tuple(combinations(range(l), l//2))
    dice_set = set(range(l))

    win_max = 0
    for d in dice_combo:
        a_dice = d
        b_dice = dice_set - set(d)
        a_temp = (dice[i] for i in a_dice)
        a_combo = [sum(p) for p in product(*a_temp)]
        b_temp = (dice[i] for i in b_dice)
        b_combo = [sum(p) for p in product(*b_temp)]
        b_combo.sort()
        cache = dict()
        win_count = sum(find_value(cache, a_value, b_combo) for a_value in a_combo)
        if win_max < win_count:
            win_max = win_count
            answer = list(map(lambda x: x+1, a_dice))
    
    return answer