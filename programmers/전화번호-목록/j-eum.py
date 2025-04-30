def solution(phone_book):
    phone_book.sort()
    # for i in range(len(phone_book) - 1):
    #     n = len(phone_book[i])
    #     if phone_book[i] == phone_book[i + 1][:n]:
    #         return False
    for p1, p2 in zip(phone_book, phone_book[1:]):
        if p2.startswith(p1):
            return False
    return True
