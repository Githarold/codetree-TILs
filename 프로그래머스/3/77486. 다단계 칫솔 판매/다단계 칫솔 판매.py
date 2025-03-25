def solution(enroll, referral, seller, amount):
    refer_dict = {}
    for i in range(len(enroll)):
        refer_dict[enroll[i]] = referral[i]
    
    profit = {name: 0 for name in enroll}
    
    for i in range(len(seller)):
        person = seller[i]
        curr_amount = amount[i] * 100
        
        current = person
        while True:
            fee = curr_amount // 10
            remaining = curr_amount - fee
            
            if fee == 0:
                profit[current] += curr_amount
                break
            else:
                profit[current] += remaining
            
            parent = refer_dict[current]
            if parent == '-':
                break
                
            curr_amount = fee
            current = parent
    
    return [profit[name] for name in enroll]