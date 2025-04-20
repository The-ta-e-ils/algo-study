def comb(m):
    rates = [10, 20, 30, 40]
    result = [[] for _ in range(4 ** m)]
    
    for i in range(len(result)):
        for j in range(1, m + 1):
            ind = i // (4 ** (m - j))
            result[i].append(rates[ind % 4])
    
    return result
        

def solution(users, emoticons):
    n = len(users)
    m = len(emoticons)
    emos = comb(m)
    answer = [0, 0]
    
    for com in emos:
        member = 0
        profit = 0
        
        for i in range(len(users)):
            standard = users[i][1]
            rate = users[i][0]
            purchase = 0
            for j in range(len(emoticons)):
                if com[j] >= rate:
                    purchase += emoticons[j] * (1 - com[j] / 100)
            if purchase >= standard:
                member += 1
            else:
                profit += purchase
        
        if member > answer[0]:
            answer = [member, profit]
        elif member == answer[0] and profit > answer[1]:
            answer = [member, profit]
    
    return answer
