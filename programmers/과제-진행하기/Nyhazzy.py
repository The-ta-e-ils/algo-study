
# 분으로 변환
def time_to_minutes(time):
    h, m = map(int, time.split(":"))
    return h*60+m

def solution(plans):
    
    # plans[:][1]은 과제 시작 시각
    # 과제 시각 정렬
    plans = [(name, time_to_minutes(start), int(playtime)) for name, start, playtime in plans]
    plans.sort(key=lambda x: x[1])
    
    answer = []
    stack = []
    
    # 코드 내에서 +1으로 다음 과제랑 비교할 거라서 하나 뺀 길이만큼 반복
    # 길이 그대로 사용하면 마지막 요소는 비교 대상이 없음
    for i in range(len(plans) - 1):
        # 과제명과 소요시간을 stack에 추가
        stack.append([plans[i][0], plans[i][2]])
        # 다음 과제 시작 시각과 현재 과제 시작 시각 차이
        # 현재 과제에 사용가능한 시간
        gap = plans[i+1][1] - plans[i][1]
        
        while stack and gap:
            now_name = stack[-1][0]
            now_time = stack[-1][1]
            
            if now_time <= gap: # 과제 소요시간이 다음 과제의 시작 시각 차이 보다 작거나 같아면
                stack.pop() # 과제 완료, 스텍에서 제거
                answer.append(now_name) # 과제를 끝냈으니 정답 리스트에 추가
                gap -= now_time # 과제를 끝내고 남은 시간
            else: # 과제 소요시간 내에 과제를 끝내지 못할 경우
                stack[-1][1] -= gap # 과제 소요시간에서 시간 차이 빼기 (과제를 끝내는데 필요한 추가 시간 계산), 스텍에 업데이트
                gap = 0 # 더이상 여유 시간 없음.
                
    stack.append([plans[-1][0], plans[-1][2]]) # 마지막 과제의 이름과 소요시간
    while stack:
        # 완료하지 못한 과제들을 가장 최근에 멈춘 과제들부터 처리
        answer.append(stack.pop()[0])
           
    return answer