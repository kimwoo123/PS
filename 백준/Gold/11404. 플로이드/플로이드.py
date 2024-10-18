import sys
input = sys.stdin.readline

def main():
    N = int(input())
    M = int(input())

    matrix = [[10000001] * (N) for _ in range(N)]
    for _ in range(M):
        a, b, c = map(int, input().split())
        matrix[a-1][b-1] = min(matrix[a-1][b-1], c)

    for i in range(N):
        matrix[i][i] = 0

    for i in range(N):
        for j in range(N):
            for k in range(N):
                matrix[j][k] = min(matrix[j][k], matrix[j][i] + matrix[i][k])
    
    for i in range(N):
        for j in range(N):
            if matrix[i][j] == 10000001:
                matrix[i][j] = 0
    
    for row in matrix: print(*row)

if __name__ == "__main__":
    main()