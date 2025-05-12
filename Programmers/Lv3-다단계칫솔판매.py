import math

def solution(enroll, referral, seller, amount):

		# {이름: 추천인 이름} 인 딕셔너리
    parentTree = dict(zip(enroll, referral))
    # {이름: 인덱스 번호} 인 딕셔너리
    answer = dict(zip(enroll, [0 for i in range(len(enroll))]))

    
    for i in range(len(seller)):
        earn = amount[i] * 100
        target = seller[i]

        while True :
		        # 나눠 줄 필요가 없는 경우
            if earn < 10 : 
                answer[target] += earn
                break
            # 나눠줘야 하는 경우
            else : 
                answer[target] += math.ceil(earn * 0.9)
                # 나눠 줄 사람이 없으면 종료
                if parentTree[target] == "-": 
                    break
                earn = math.floor(earn*0.1)
                target = parentTree[target]

    return list(answer.values())