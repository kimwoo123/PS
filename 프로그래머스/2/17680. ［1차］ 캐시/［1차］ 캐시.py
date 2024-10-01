def find(it, elem):
    for i in range(len(it)):
        if it[i] == elem:
            return i
    return -1

def solution(cacheSize, cities):
    answer = 0
    cache = [''] * cacheSize
    for city in cities:
        city = city.lower()
        index = find(cache, city)
        if index != -1:
            answer += 1
            del cache[index]
            cache.insert(0, city)
        else:
            answer += 5
            cache.insert(0, city)
            del cache[-1]
    return answer