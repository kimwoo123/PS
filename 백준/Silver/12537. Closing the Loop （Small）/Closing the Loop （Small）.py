import sys
input = sys.stdin.readline

def main():
    N = int(input())
    for i in range(N):
        T = int(input())
        rope_list = input().split()
        red_list, blue_list = [], []
        for rope in rope_list:
            rope_len = int(rope[:-1])
            if rope[-1] == 'R':
                red_list.append(rope_len)
            else:
                blue_list.append(rope_len)
                
        red_list.sort(reverse=True)
        blue_list.sort(reverse=True)
        
        total = 0
        for j in range(min(len(red_list), len(blue_list))):
            total += red_list[j] + blue_list[j]
            total -= 2
            
        if total < 0:
            total = 0
            
        print(f"Case #{i+1}: {total}")
    
    
if __name__ == "__main__":
    main()