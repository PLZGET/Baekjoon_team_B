def min_supervisors(test_rooms, examinees, B, C):
    total_supervisors = 0

    for i in range(test_rooms):
        # 각 시험장의 응시자 수
        students = examinees[i]

        # 총감독관이 감시할 수 있는 응시자 수를 뺀 나머지 응시자 수
        remaining_students = students - B

        # 총감독관은 무조건 1명 필요
        total_supervisors += 1

        # 남은 응시자 수가 양수일 경우 부감독관이 필요
        if remaining_students > 0:
            # 부감독관이 감시할 수 있는 응시자 수로 나누어 필요한 부감독관 수 계산
            # 7//4 = 1 이니까 +1 해서 부감독관 수 맞쳐줌
            if(remaining_students % C == 0):
                additional_supervisors = (remaining_students // C)
            else:
                additional_supervisors = (remaining_students // C) + 1
            
            total_supervisors += additional_supervisors

    return total_supervisors


# 시험장 개수(N) 입력
test_rooms = int(input())

# 각 시험장에 있는 응시자수 Ai(1<=Ai<=1,000,000)
examinees = list(map(int, input().split()))

# 총감독관, 부감독관 감시가능한 응시자수 B, C
B, C = map(int, input().split())

# 결과 출력
result = min_supervisors(test_rooms, examinees, B, C)
print(result)