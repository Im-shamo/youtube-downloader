def main():
    box = [[0]*3 for _ in range(3)]
    
    
    x = 0
    y = 0
    d = 0
    dx = -1
    dy = 0
    
    for k in range(1, 10):
        box[x][y] = k
        
        if (x + dx == -1) or (x + dx > 2) or (y + dy == -1) or (y + dy > 2) or (k == 8):
            d = d + 1
            d = d%4

            if d == 0:
                dx = -1
                dy = 0 
                
            elif d == 1:
                dx = 0
                dy = 1
                
            elif d == 2:
                dx = 1
                dy = 0
                
            elif d == 3:
                dx = 0
                dy = -1
                
        x = x + dx
        y = y + dy
    [print(i) for i in box]



if __name__ == "__main__":
    main()