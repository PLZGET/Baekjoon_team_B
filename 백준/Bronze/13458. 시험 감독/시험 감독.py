import math

def calculate_supervisors(N, A, B, C):
    total_supervisors = 0

    for i in range(N):
        # 총감독관이 감독 가능한 인원만큼 감독
        A[i] -= B
        total_supervisors += 1

        # 남은 응시자가 있을 경우 부감독관이 감독
        if A[i] > 0:
            total_supervisors += math.ceil(A[i] / C)

    return total_supervisors

# 입력 받기
N = int(input())  # 시험장의 개수
A = list(map(int, input().split()))  # 각 시험장의 응시자 수
B, C = map(int, input().split())  # 총감독관과 부감독관이 감시 가능한 응시자 수

result = calculate_supervisors(N, A, B, C)

# 결과 출력
print(result)
