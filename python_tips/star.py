# 삼각형 별찍기
# 문제 설명
# 이 문제에는 표준 입력으로 정수 n이 주어집니다.
# 별(*) 문자를 이용해 높이가 n인 삼각형을 출력해보세요.

# 제한 조건
# n은 100 이하인 자연수입니다.
# 예시
# 입력

# 3
# 출력

# *
# **
# ***

# -------------------------------------------------------------

# 명답

# 설명
n = int(input().strip())
answer= [123, 456]*n
print(answer)

# -------------------------------------------------------------

# 내 코드
n = int(input().strip())
for i in range(n):
    print('*'*(i+1))