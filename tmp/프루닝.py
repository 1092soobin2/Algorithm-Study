# 1-n 카드
# coin개 동전

# 카드 뽑는 순서가 정해져 있다.
# 1. n/3 장을 뽑아 모두 가진다 (n = 6k), coin개 교환 가능한 동전
# 2. 라운드, 시작할 때 카드 2장
    # 1) 카드 뭉치에 카드가 없다면 게임 종료
    # 2) 가지기(카드 1장당 동전 1 소모) || 버리기 (동전 0 소모)
# 3. 적힌 수의 합이 n+1이 되도록 카드 두장을 내고 다음 라운드로 진행
    # 1) 낼 수 없다면 종료

# answer: 게임에서 도달 가능한 최대 라운드 수

from collections import deque

answer = 1


def find_pair_with_sum(curr_card: dict, n) -> list:
    elements = set(curr_card)

    possible_pair_list = []

    # 합 (n+1)을 만족하는 원소 쌍
    for element in curr_card:
        if curr_card[element]:
            complement = (n + 1 - element)
            if complement in elements:
                possible_pair_list.append({element, complement})
                elements.remove(element)
                elements.remove(complement)

    return possible_pair_list


def dfs(curr_card: set, rest_card: deque, coin, acc, n):
    global answer

    pair_list = find_pair_with_sum(curr_card, n)

    # print(f"현재 라운드: {acc} --- 카드: {curr_card} -- 현재 정답: {answer}")
    # print(f"rest: {rest_card} coin: {coin}")
    # print(f"possible: {pair_list}")
    # print()

    # 카드가 없거나, 다음 라운드로 진행할 수 없다면 종료
    if not curr_card or not pair_list:
        answer = max(answer, acc)
        return

    # pruning
    if coin == 0:
        answer = max(answer, len(pair_list) + acc)
        return

    rest_card = deque(rest_card)

    # 다음 라운드
    for pair in pair_list:
        # curr_card = curr_card - pair

        if not rest_card:
            answer = max(answer, acc + 1)
            return

        c1 = rest_card.popleft()
        c2 = rest_card.popleft()
        next_card = [c1, c2]

        # 1) 카드 0장
        dfs(curr_card, rest_card, coin, acc + 1, n)

        # 2) 카드 1장
        if coin >= 1 and next_card:
            dfs(curr_card | set(next_card[:1]), rest_card, coin - 1, acc + 1, n)
            dfs(curr_card | set(next_card[1:]), rest_card, coin - 1, acc + 1, n)
        # 3) 카드 2장
        if coin >= 2 and next_card:
            dfs(curr_card | set(next_card[:2]), rest_card, coin - 2, acc + 1, n)


def solution(coin, cards):
    n = len(cards)
    curr_card = dict([(card, True) for card in cards[:(n // 3)]])

    rest_card = deque(cards[(n // 3):])

    c1 = rest_card.popleft()
    c2 = rest_card.popleft()
    next_card = [c1, c2]

    # 1) 카드 0장
    dfs(curr_card, rest_card, coin, 1, n)
    # 2) 카드 1장
    if coin >= 1 and next_card:
        dfs(curr_card | set(next_card[:1]), rest_card, coin - 1, 1, n)
        dfs(curr_card | set(next_card[1:]), rest_card, coin - 1, 1, n)
    # 3) 카드 2장
    if coin >= 2 and next_card:
        dfs(curr_card | set(next_card[:2]), rest_card, coin - 2, 1, n)

    return answer