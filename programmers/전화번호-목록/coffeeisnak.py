def solution(phone_book):
    l = len(phone_book)
    phone_book.sort()  # 전화번호를 사전순 정렬 => O(NlogN)

    for i in range(l - 1):
        l_string = phone_book[i]
        r_string = phone_book[i + 1]

        # 바로 뒤만 접두어로 확인 (N^2 은 N <= 100만이므로 절대 불가) => 사전순이라면 바로 앞뒤가 포함하지 않으면 가망성이없음.
        if len(l_string) >= len(r_string):
            if r_string == l_string[: len(r_string)]:
                return False
        else:
            if l_string == r_string[: len(l_string)]:
                return False

    return True
