def solution(operations):
    answer = []
    for op in operations:
        operation, value = op.split()
        if operation == 'I':
            answer.append(int(value))
        else:
            if answer and value == '1':
                answer.pop()
            elif answer and value == '-1':
                answer.pop(0)
        answer.sort()
        
    return [answer.pop(), answer.pop(0)] if answer else [0, 0]