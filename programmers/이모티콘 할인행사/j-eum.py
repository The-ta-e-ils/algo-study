# import heapq


def solution(users, emoticons):
    # 할인율은 10%, 20%, 30%, 40% 중 하나로 설정됩니다.
    rate = [10, 20, 30, 40]
    discount = []

    def dfs(path, n):
        if len(path) == n:
            discount.append(path)
            return
        for r in rate:
            dfs(path + [r], n)

    dfs([], len(emoticons))

    result = [0, 0]
    # heap = []
    # heapq.heapify(heap)
    for rates in discount:
        cnt = 0  # 가입자수
        sales = 0  # 매출
        for user_rate, user_price in users:
            user_spent = 0
            for rate, price in zip(rates, emoticons):
                discounted_price = price * (100 - rate) / 100
                if rate >= user_rate:
                    user_spent += discounted_price
            # 일정가격 이상이면 가입
            if user_spent >= user_price:
                cnt += 1
            # 아니면 개별구매
            else:
                sales += user_spent

        # 2. 바로 대소비교
        if cnt > result[0]:
            result = [cnt, sales]
        elif cnt == result[0]:
            result[1] = max(result[1], sales)

    return result

    #     # 1. 힙 사용
    #     heapq.heappush(heap, [-cnt, -sales])
    # cnt, sales = heapq.heappop(heap)
    # return [-cnt, -sales]
