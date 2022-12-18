import math

def solution(fees, records):
    cars = {}
    result = []
    for row in records:
        time, num, state = row.split()
        if num not in cars:
            cars[num] = [time]
        else:
            cars[num].append(time)
            
    cars = sorted(cars.items(), key=lambda x:x[0])
    
    for car in cars:
        money = 0
        tmp = 0
        for i in range(1,len(car[1]),2):
            tmp += (int(car[1][i].split(':')[0])*60 + int(car[1][i].split(':')[1])) -\
            (int(car[1][i-1].split(':')[0])*60 + int(car[1][i-1].split(':')[1]))
        
        if len(car[1])%2 == 1:
            tmp += 23*60+59 - (int(car[1][-1].split(':')[0])*60 + int(car[1][-1].split(':')[1]))
                
        if fees[0] < tmp:
            money = fees[1] + math.ceil((tmp-fees[0])/fees[2])*fees[3]
        else:
            money = fees[1]
        result.append(money)
    return result