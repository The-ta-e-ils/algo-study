def solution(phone_book):
    # 1. 전화번호부를 정렬
    phone_book.sort()
    
    # 2. 인접한 전화번호끼리 접두사 관계 확인
    for i in range(len(phone_book) - 1):
        if phone_book[i+1].startswith(phone_book[i]):  # 접두어 검사
            return False
    return True
