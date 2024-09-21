def solution(genres, plays):
    answer = []
    count = dict()
    total = dict()
    l = len(genres)
    for i in range(l):
        genre, play = genres[i], plays[i]
        if genre not in count:
            total[genre] = play
            count[genre] = [(play, i)]
        else:
            total[genre] += play
            count[genre].append((play, i))
            
    picks = sorted(total.items(), key=lambda x: -x[1])
    for pick in picks:
        genre_, total_ = pick
        for k, v in sorted(count[genre_], key=lambda x: (-x[0], x[1]))[:min(len(pick), 2)]:
            answer.append(v)
            
    return answer