def solution(genres, plays):
    answer = []
    # 장르, 고유번호, 재생수를 담는 배열 선언
    genres_plays = []
    for i in range(len(genres)):
        genres_plays.append([genres[i], i, plays[i]])
    
    # 중복을 제거한 장르
    genres_set = list(set(genres))
    # 장르별 재생 횟수 저장
    count_plays = [[genres_set[i], 0] for i in range(len(genres_set))]
    
    for i in range(len(genres_set)):
        for j in range(len(genres_plays)):
            # 장르가 같으면
            if count_plays[i][0] == genres_plays[j][0]:
                # 해당 장르 재생 횟수 더해주기
                count_plays[i][1] += int(genres_plays[j][2])
    # 재생 횟수가 가장 큰 순서대로 정렬
    count_plays.sort(key=lambda x: x[1], reverse = True)
    
    # 재생 횟수가 가장 큰 순서대로 정렬
    genres_plays.sort(key=lambda x:x[2], reverse = True)
    
    # 장르가 맞는지 확인 -> 맞으면 고유번호수록
    for i in range(len(count_plays)):
        count = 0
        for j in range(len(genres_plays)):
            if count == 2:
                break
            genre = count_plays[i][0]
            if genre == genres_plays[j][0]:
                answer.append(genres_plays[j][1])
                count += 1
    return answer