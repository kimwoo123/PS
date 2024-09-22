answer = [0, 0]
def divide(row, col, l, arr):
    ret = conquer(row, col, l, arr)
    if ret == False:
        ll = l // 2
        divide(row, col, ll, arr)
        divide(row + ll, col, ll, arr)
        divide(row, col + ll, ll, arr)
        divide(row + ll, col + ll, ll, arr)
    else:
        number = arr[row][col]
        answer[number] += 1

def conquer(row, col, l, arr):
    pivot = arr[row][col]
    for i in range(row, row + l):
        for j in range(col, col + l):
            if arr[i][j] != pivot:
                return False
    return True        
    
                
def solution(arr):
    length = len(arr)
    divide(0, 0, length, arr)
        
    return answer