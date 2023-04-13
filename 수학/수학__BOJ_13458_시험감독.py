# 수학__BOJ_13458_시험감독

'''
N개 시험장
A_i: i번 시험장 응시자 수
- 총감독관 - B명
- 부감독관 - C명

- 총감독관 오직 1명
- 부감독관 여러 명 가능

각 시험장마다 응시생을 모두 감독하기 위해 필요한 감독관의 최소 수
'''
# ===input===
N = int(input())
A = list(map(int, input().split()))    # TODO: A[i-1]: i번 시험장 응시자 수
B, C = map(int, input().split())


# ===algorithm===
def count_supervisor(num_of_people: int) -> int:

    # 1) 총감독관 1명
    num_of_people -= B
    total_supervisor = 1
    # 2) 부감독관
    if num_of_people > 0:
        sub_supervisors = int(num_of_people / C)
        total_supervisor += sub_supervisors if sub_supervisors == num_of_people / C else sub_supervisors + 1
    # while num_of_people > 0 :
    #     num_of_people -= C
    #     total_supervisor += 1

    return total_supervisor


# ===output===
ans = 0
for people in A:
    ans += count_supervisor(people)
print(ans)
