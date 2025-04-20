import heapq

def solution(genres, plays):
    song_dict = {}
    answer = []
    
    for i in range(len(genres)):
        cur_gen = genres[i]
        cur_play = plays[i]
        
        if cur_gen not in song_dict:
            song_dict[cur_gen] = [cur_play, [(-cur_play, i)]]
            heapq.heapify(song_dict[cur_gen][1])
        else:
            song_dict[cur_gen][0] += cur_play
            heapq.heappush(song_dict[cur_gen][1], (-cur_play, i))
    
    # 최대 총 재생회수를 가진 장르부터~ 
    for gen in sorted(song_dict.keys(), key=lambda x: -song_dict[x][0]):
        for _ in range(2):
            if song_dict[gen][1]:
                answer.append(heapq.heappop(song_dict[gen][1])[1])
    
    return answer
