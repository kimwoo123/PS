def solution(picks, minerals):
    pick_count = sum(picks)
    target_mineral = pick_count * 5
    if len(minerals) > target_mineral:
        minerls = minerals[target_mineral]
        
    mapping = {
        "diamond": 0,
        "iron": 1,
        "stone": 2,
    }
    mineral_count = [[0, 0, 0] for _ in range(pick_count)]
    for i in range(min(len(minerals), target_mineral)):
        index = mapping[minerals[i]]
        mineral_count[i // 5][index] += 1
        
    mineral_count.sort(key=lambda x: (-x[0], -x[1], -x[2]))
    
    total = 0
    for dia, iron, stone in mineral_count:
        for i in range(3):
            if picks[i] > 0:
                picks[i] -= 1
                if i == 0:
                    total += dia + iron + stone
                elif i == 1:
                    total += (dia * 5) + iron + stone
                else:
                    total += (dia * 25) + (iron * 5) + stone
                break
    
    return total