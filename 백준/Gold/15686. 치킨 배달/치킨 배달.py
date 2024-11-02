def calculate_distance(home_arr: list, choice_arr:list):
    total = 0
    for index_one in range(len(home_arr)):
        min_distance = 9999
        for index_two in range(len(choice_arr)):
            distance = abs(home_arr[index_one][0] - choice_arr[index_two][0]) + abs(home_arr[index_one][1] - choice_arr[index_two][1])
            if min_distance > distance:
                min_distance = distance
        total += min_distance
    total_list.append(total)


def store_choice(index, start):
    if index == M:
        return calculate_distance(home_list, choice_list)

    for i in range(start, len(chicken_store) - M + index + 1):
        choice_list[index] = chicken_store[i]
        store_choice(index + 1, i + 1)


N, M = map(int, input().split())
town = [list(map(int, input().split())) for _ in range(N)]

chicken_store = []
choice_list = [0] * M
home_list = []
total_list = []
for row in range(N):
    for col in range(N):
        if town[row][col] == 2:
            chicken_store.append([row, col])
        elif town[row][col] == 1:
            home_list.append([row, col])

store_choice(0, 0)
print(min(total_list))