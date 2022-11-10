def solution(brown, yellow):
    b_w = []
    b_h = []
    y_w = []
    y_h = []
    
    for h in range(1, brown+yellow+1):
        w = (brown+yellow) / h
        if int(w) == w:
            b_h.append(h)
            b_w.append(int(w))
            
    for h in range(1, yellow+1):
        w = (yellow) / h
        if h > w:
            break
        if int(w) == w:
            y_h.append(h+2)
            y_w.append(int(w)+2)
    
    for w,h in zip(y_w, y_h):
        if w in b_w and h in b_h:
            # if b_w.index(w) == b_h.index(h):
                return [w, h]
        
    return