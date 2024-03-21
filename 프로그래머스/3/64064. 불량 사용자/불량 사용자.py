def solution(user_id, banned_id):
    suspect = []
    for b in banned_id:
        suspect.append([i for i, u in enumerate(user_id) if can_banned(b, u)])
    suspect.sort(key=len)

    global total_case
    total_case = set()
    add_case(suspect, set())
    return len(total_case)

def can_banned(ban_id, user_id):
    if len(ban_id) != len(user_id):
        return False
    for b, u in zip(ban_id, user_id):
        if b != '*' and b != u:
            return False
    return True

def add_case(suspect, banned_user):
    global total_case
    if not suspect:
        total_case.add(tuple(sorted(banned_user)))
        return
    for i in suspect[0]:
        if i not in banned_user:
            add_case(suspect[1:], banned_user | {i})