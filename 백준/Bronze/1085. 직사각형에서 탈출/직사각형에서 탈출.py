x, y, w, h = map(int, input().split())

# 각 변까지의 거리를 계산하여 리스트에 저장
#w-x는 직사각형의 오른쪽 변과 현재 점 x의 위치 사이의 거리
#h-y는 직사각형의 윗변과 현재 점 y의 위치 사이의 거리
dis = [x, y, w-x, h-y]

# 거리 중 최솟값을 출력
print(min(dis))
