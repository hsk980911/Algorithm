def solution(s):
    split_str = []
    start = 0
    str = ''
    
    x_count = 0
    other_count = 0
    
    for i in range(len(s)):
        if len(str) == 0:
            str += s[i]
            x_count += 1
        else:
            str += s[i]
            if s[i] == str[0]:
                
                x_count += 1
            else:
                other_count += 1
        
        if x_count == other_count:
            split_str.append(str)
            x_count = 0
            other_count = 0
            str = ''

    if len(str) == 0:
        return len(split_str)
    else:
        return len(split_str) + 1