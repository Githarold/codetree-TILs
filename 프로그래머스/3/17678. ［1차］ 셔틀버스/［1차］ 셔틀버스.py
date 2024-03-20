def solution(n, t, m, timetable):
    time = sorted([int(ti.split(':')[0]) * 60 + int(ti.split(':')[1]) for ti in timetable])

    bus_arrive_time = 540
    last_crew_time = 0

    for _ in range(n):
        passengers = 0
        while passengers < m and time and time[0] <= bus_arrive_time:
            last_crew_time = time.pop(0)
            passengers += 1
        bus_arrive_time += t

    if passengers < m:
        answer_time = bus_arrive_time - t
    else:
        answer_time = last_crew_time - 1

    answer = '{:02d}:{:02d}'.format(answer_time // 60, answer_time % 60)
    return answer
