



def main():
    ROWS = 3
    COLUMNS = 3
    rect = [[0]*COLUMNS for _ in range(ROWS)]
    i = 0
    j = 0
    
    dir = 0
    di = -1
    dj = 0


    for k in range (1, ROWS*COLUMNS + 1):
        rect[i][j] = k
        
    print(rect)


if __name__ == "__main__":
    main()
