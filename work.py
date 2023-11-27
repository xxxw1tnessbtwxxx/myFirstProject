def calculatedistance(days: int, dist: int) -> float:
    s = dist
    for i in range(1, days):
        dist += 1.1
        s += dist
    
    return s

print(calculatedistance(int(input()), int(input())))