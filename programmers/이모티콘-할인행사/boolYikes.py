from itertools import product
def solution(users, emoticons):
    discounts = [10, 20, 30, 40]
    l_emot = len(emoticons)
    discounts_product = product(discounts, repeat=l_emot) # worst case: 4 ^ 7 = 16384

    possibilites = set() # remove dupes cuz this is an aggregation-combination
    for discounts in discounts_product:
        sales = 0
        converted = 0
        for user in users: # worst case perm 16384 * users 100 = 1638400 ... so far so good ?
            discount_threshold, price_threshold = user
            # policies : always buy things that meet discount criteria
            sale = sum(emoticons[i] - int((discount / 100) * emoticons[i]) for i, discount in enumerate(discounts) if discount >= discount_threshold) # 1638400 * 7 ????
            if sale >= price_threshold:
                converted += 1
            else:
                sales += sale
        possibilites.add((converted, sales))# , discounts))
    # possibilities: Set[Tuple[Total sales, Total converted]]]
    return list(max(possibilites, key=lambda case: (case[0], case[1])))