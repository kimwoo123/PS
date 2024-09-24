def solution(maze):
    answer = 9999
    
    row_len = len(maze)
    col_len = len(maze[0])
    for i in range(row_len):
        for j in range(col_len):
            if maze[i][j] == 1:
                red_wagon = (i, j)
            elif maze[i][j] == 2:
                blue_wagon = (i ,j)
            elif maze[i][j] == 3:
                red_dest = (i ,j)
            elif maze[i][j] == 4:
                blue_dest = (i ,j)
    
    r_visited = [[0] * col_len for _ in range(row_len)]
    b_visited = [[0] * col_len for _ in range(row_len)]
    r_visited[red_wagon[0]][red_wagon[1]] = 1
    b_visited[blue_wagon[0]][blue_wagon[1]] = 1
    delta = [(0, -1), (0, 1), (1, 0), (-1, 0)]
    def dfs(red_pos, blue_pos, count):
        nonlocal answer
        if answer < count:
            return
        if red_pos == red_dest and blue_pos == blue_dest:       
            if answer > count:
                answer = count
            return
        red_row, red_col = red_pos
        blue_row, blue_col = blue_pos
        
        for red_drow, red_dcol in delta:
            if red_pos == red_dest:
                red_nrow, red_ncol = red_pos
            else:
                red_nrow = red_row + red_drow
                red_ncol = red_col + red_dcol
                
            if 0 <= red_nrow < row_len and 0 <= red_ncol < col_len and maze[red_nrow][red_ncol] != 5:
                if (red_nrow, red_ncol) == red_dest or (r_visited[red_nrow][red_ncol] == 0):
                    r_visited[red_nrow][red_ncol] = 1
                    for blue_drow, blue_dcol in delta:
                        if blue_pos == blue_dest:
                            blue_nrow, blue_ncol = blue_pos
                        else:
                            blue_nrow = blue_row + blue_drow
                            blue_ncol = blue_col + blue_dcol

                        if 0 <= blue_nrow < row_len and 0 <= blue_ncol < col_len and maze[blue_nrow][blue_ncol] != 5:
                            # 겹치는 경우     
                            if red_nrow == blue_nrow and red_ncol == blue_ncol:
                                continue
                            # 교차하는 경우
                            if (blue_nrow, blue_ncol) == red_pos and (red_nrow, red_ncol) == blue_pos:
                                continue
                            if (blue_nrow, blue_ncol) == blue_dest or (b_visited[blue_nrow][blue_ncol] == 0):
                                b_visited[blue_nrow][blue_ncol] = 1
                                dfs((red_nrow, red_ncol), (blue_nrow, blue_ncol), count + 1)
                                b_visited[blue_nrow][blue_ncol] = 0
                    r_visited[red_nrow][red_ncol] = 0
    
    dfs(red_wagon, blue_wagon, 0)
    if answer == 9999:
        return 0
    return answer