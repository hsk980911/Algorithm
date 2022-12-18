def solution(fees, records):
    cars = {}
    result = []
    for row in records:
        time, num, state = row.split()
        if num not in cars:
            cars[num] = [time]
        else:
            if state = 'OUT':
                cars[num][-1] = 
            cars[num].append(time)
            
    cars = sorted(cars.items(), key=lambda x:x[0])
    
    for car in cars:
        for t in car[1]:
            
    return 