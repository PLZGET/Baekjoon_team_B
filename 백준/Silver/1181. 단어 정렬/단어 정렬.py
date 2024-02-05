# 단어의 개수 N 입력 받기
N = int(input())

# 단어들을 저장할 리스트 생성
words = []

# N개의 단어를 입력 받아 리스트에 저장
for i in range(N):
    word = input()
    words.append(word)

# 중복 제거 및 정렬 조건에 따라 정렬
sorted_words = sorted(list(set(words)), key=lambda x: (len(x), x))

# 정렬된 결과 출력
for word in sorted_words:
    print(word)