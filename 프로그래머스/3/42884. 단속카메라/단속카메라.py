def solution(routes):
    answer = 1
    routes.sort()
    print(routes)

    car = len(routes)
    cam = routes[0][1]
    for i in range(1, car):
        if routes[i][0] > cam:
            answer += 1
            cam = routes[i][1]
        else:
            cam = min(routes[i][1], cam)
    
    return answer