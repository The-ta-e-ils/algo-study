def solution(phone_book):
    # res = 1
    # f = lambda s1, s2 : 1 if len(s1) > len(s2) else 0
    # for i in range(len(phone_book)):
    #     for j in range(i, len(phone_book)):
    #         if i != j:
    #             bigger = f(phone_book[i], phone_book[j])
    #             if bigger:
    #                 if phone_book[i][:len(phone_book[j])] == phone_book[j]:
    #                     res *= 0
    #             else:
    #                 if phone_book[j][:len(phone_book[i])] == phone_book[i]:
    #                     res *= 0  
    # return bool(res)

    # sorting = comparison relief
    phone_book.sort()
    print(f"sorted: {phone_book}")
    for i in range(len(phone_book) - 1):
        print(f"compare{phone_book[i]} and {phone_book[i + 1][:len(phone_book[i])]}")
        # check prefix
        if phone_book[i] == phone_book[i + 1][:len(phone_book[i])]:
            # WHY FALSE tho??
            return False
    return True