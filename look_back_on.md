~ 0710 (스니펫1)Codetree_생명과학부랩인턴,(스니펫2)20057, 21611
# Format

```python
# ===input===

# ===algorithm===

# ===output===
```

Why) python

[Python](https://www.notion.so/Python-9f2326caab5e45f8abb8a017ef1b82f1?pvs=21)

- 면접관이 쉽게 이해할 수 있다. pseudo-code로도 굳
- 언어 레벨에서 풍부한 기능을 지원한다.
- 유연한 언어이다.

# 시간제한

1초에 2000만번 (20M)

시간제한 1초인 문제 

![Screenshot 2023-03-15 at 1.21.48 PM.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/7cbbee93-200d-4ea9-a622-b48226c3c539/Screenshot_2023-03-15_at_1.21.48_PM.png)

- ?!
    1. 604ms
    
    ```python
    # inline 계산
    min_ = 1e9
    for _ in combinations(_, M):
        sum_of_dist = 0
        # calculate
        min_ = min(min_, sum_of_dist)
    ```
    
    1. 348ms
    
    ```python
    def cal():
    	...
    
    # function call
    min_ = 1e9
    for _ in combinations(_, M):
        min_ = min(min_, cal())
    ```
    

# SNIPPET

그래프 문제 → 탐색

최단 거리 문제 → 탐색, 다익스트라

호텔 대실 → 그리디

리스트 탐색 → (N)선형 탐색, (logN)이분 탐색

### 1. MIN, MAX at 차례로 조회

```jsx
minimum = MAX_NUM
for ...
	current_value = ...
	minimim = min(minimum, current_value)
```

### 2. DFS (스택 | 재귀)

1) 스택

```powershell
스택

# 2. dfs - stack
def dfs(graph_list, start_node):
    # 기본 2개 자료 구조
    visited_list, not_visited_stack = [], deque([start_node])

    # 스택 이용
    while not_visited_stack:
        curr_node = not_visited_stack.pop()

        if curr_node not in visited_list:
            visited_list.append(curr_node)
            not_visited_stack.extend(sorted(set(graph_list[curr_node]) - set(visited_list), reverse=True))

    return visited_list
```

2) 재귀

```python

def FUNC_NAME:
		answer = []

		def dfs(arr, curr_r, curr_c, acc_list):
				if len(acc_list) == MAX_LEN:
						answer.append(acc_list)
						return 
				
				for dr, dc in DIRECTION_LIST:
						nr, nc = curr_r+dr, curr_c+dc
						if check_boundary(nr, nc):
								dfs(arr, nr, nc, acc_list + [arr[nr][nc]])
```

		

### 3. 튜플이 들어있는 list 정렬

`sorted(LIST, key=lambda x: (x[0], x[1]))`

### 4. Combination(nCr)

```powershell
# nCr
def comb(array, r):
    combs = []
    n = len(array)

    def dfs(start_i, acc_list):
        if len(acc_list) == r:
            combs.append(acc_list[:])
            return

        for i in range(start_i+2, n):
            acc_list.append(array[i])
            dfs(i+1, acc_list)
            acc_list.pop()

    dfs(0, [])
    return combs
```
## 5. 다익스트라
```python
def dijkstra(start):

    pq = []
    distances = [int(1e9)] * (N + 1)

    # start node
    distances[start] = 0
    heapq.heappush(pq, (distances[start], start))

    # repeat
    while pq:
        curr_dist, curr_vertex = heapq.heappop(pq)
				
				# 거리가
        if distances[curr_vertex] < curr_dist:
            continue

        for next_vertex, w in adj_list[curr_vertex]:
            next_dist = curr_dist + w
						# next_dist가 더 작으면 갱신
            if distances[next_vertex] > next_dist:
                distances[next_vertex] = next_dist
                heapq.heappush(pq, (next_dist, next_vertex))

    return distances
```

### 6. 크루스칼

```python
parent = list(range(n))
    
def find_parent(node): 
    if parent[node] != node:
        parent[node] = find_parent(parent[node])
    return parent[node]

def union_parent(n1, n2):
		root1 = find_parent(n1)
		root2 = find_parent(n2)
		new_root = min(root1, root2)
		parent[root1] = new_root
		parent[root2] = new_root
```

### 7. 회전

```python
# 1) 점의 시계 방향 회전
# dr = abs(기준_r - r)
# dc = abs(기준_c - c)
nr, nc = r + dc, c - dr
```

### 8. 벽에 부딪히며 핑퐁

```python
    def move_one_mold(start_r, start_c) -> (int, int):
        speed, direction = board[start_r][start_c][0][SPEED], board[start_r][start_c][0][DIRECTION]

        direction = [direction]

        def move_one_elem(elem, forward, d, max_elem) -> int:
            while forward > 0:
                # max elem쪽으로 이동
                if d == 1:
                    can_go = max_elem - elem
                    if can_go >= forward:
                        elem += forward
                        forward = 0
                    else:
                        forward -= can_go
                        elem = max_elem
                        d = -1
                        direction[0] = (direction[0] + 2) % 4
                # 0쪽으로 이동
                else:
                    can_go = elem - 0
                    if can_go >= forward:
                        elem -= forward
                        forward = 0
                    else:
                        forward -= can_go
                        elem = 0
                        d = 1
                        direction[0] = (direction[0] + 2) % 4
            return elem

        dr, dc = DIRECTION_LIST[direction[0]]
        if dr != 0:
            next_r, next_c = move_one_elem(start_r, speed % (2 * (N - 1)), dr, N - 1), start_c,
        else:
            next_r, next_c = start_r, move_one_elem(start_c, speed % (2 * (M - 1)), dc, M - 1)

        return next_r, next_c, direction[0]
```

### 9. 나선형 구조


```python
def init_loc_list():
    global loc_list
    direction_list = [[0, -1], [1, 0], [0, 1], [-1, 0]]

    repeat = 2

    # start
    r, c, d = N // 2, N // 2, 0

    # go
    for forward in range(1, N):
        if forward == N - 1:
            repeat = 3
        # change direction
        for _ in range(repeat):
            # go forward
            dr, dc = direction_list[d]
            for _ in range(forward):
                r, c = r + dr, c + dc
                loc_list.append([r, c])
            d = (d + 1) % 4
```
# Trouble Shooting

### General

(구현-업데이트) 배열에서 존나 이상한 데가 바뀐다 했더니.. 알고보니 내가 변경한 데에 `[ ]` 가 들어가서 뒤에 것들이 땡겨진 거였음.
-> sol) `from typing import List`

(2차원 배열) R, C 크로스
- `r, c = r, r` ㅇㅈㄹ 좀 하지말라거…
- `r < N, c < M` 좀… `r < M, c < N`  ㅇㅈㄹ..

(시발) 상, 하, 좌, 우 literal을 내가 잘못 쓰는 경우가 있음 ;;; 
(변수 업데이트) 원래 값 보존 여부 판단. ex) 자리가 안 바뀌었는데 바뀌었다고 생각하고 덮어써버림
(초기화) 반복문 간의 위치 주의.
(dfs) 재귀 dfs에서 continue vs. return 구분하기

(구현) 다른 경우 한 번에 처리
→ 🥲 pb) not clean, 오류 가능성 ↑
→ sol) 무적권. 따로 처리. 절대. 사수해. 중복되도 따로 처리.

(재귀) 런타임 에러: 재귀 사용 시 sys.setrecursionlimit 필요

(구현) c_list, c_dict 같이 비슷한 이름 가진 자료구조 자동완성 하다가 뻑남 ㅜ
-> sol) 이런 네이밍 관습이 없는 듯 하다,, 타입 힌트를 써보쟈 ㅜㅜ

(구현) 여러 가지 경우를 일반화하려다가 잘못된 알고리즘. 
-> e.g.) 업데이트 구문 일반화하다가 덮어써버리기.

(구현, 초기 시작) 헷갈리는 부분 무작정 구현 -> 잘못 이해해서 잘못된 알고리즘 -> 디버깅에 시간 더 걸림;;
(구현) 하드 코딩 부분 나중에 -> 흐름 끊김

(구현, 비교) 다차원 배열 접근 시 3 차 접근인데 1차 접근 같은 문제. 비교 조건에서 자주 발생
(구현, bfs,dfs) 함수 내부 함수 정의 시에 curr_r과 r 혼용하다가 실수
## 효율성
(수학) 순회가 아니라 나누기로 가능한 경우!!!
(리스트) 메모리를 희생해서 효율성을 재고하자.. remove → O(N) → bool_list

## 예외
(수학) 0인 경우 `if` 써 줘야지
(배열-조회) 배열의 길이가 0인 경우
(배열-비교) 요소들끼리 비교하는 경우 길이가 0, 1, 2인 구간에서 조심하기

(예외) 예외 경우 하나만 찾고 홀라당 좋아하지 않기
→ 예외 경우는 `# TODO:` 로 기록하기
→ 완벽하게 기록하지 않아도 된다. 대충이라도!!!!

## ERR
‘int’ is not subscriptable → 정수에 슬라이싱, 인덱싱 하는 경우

# DONE

## General

### 변수 사용 중에 바꾸지 않기

ex) for문에서 `range(VAR_NAME)`에 들어가는 매개변수(`VAR_NAME`) 바꾸지 않기

### 하드코딩 문제 (tq)

### 변수 갱신 관련
(구현) 분산된 정보 함께 업데이트
(구현) 업데이트할 정보 유념하기 `TODO` 활용

- [ ]  아니면 아예 객체로 만들어버리까

## Python 문법

### String
스트링은 리스트처럼 수정 못함.
수정 시에는 str → list → str (by `join`) 과정을 거져주어야 함.

### 함수 인자 copy vs. reference
python에서 함수 인자로 전달되는 mutable object는 참조된다 -> 재귀 dfs같은 경우는 deepcopy 필요.

### 리스트 * 연산

`[0] * 3` Literal이 복사되므로 따로 수정 가능

`[[0]]` Object가 복사되므로 하나를 수정하면 다른 것도 수정된다.

### list slicing

**`a`**

a의 copy 객채:**`a[:]`**

### Literal list는 사라진다.

```powershell
list(map(list, num_count_dict.items())).sort(key=lambda x: (x[1], x[0]))
```

이지랄 하면 list()로 생성된 객체는 참조할 수가 없어서. None.sort() 이지랄 남.

# 벼락치기

IndexError - 인덱스 조회 시에 `len(배열)` 확인

- (배열-조회) 배열의 길이가 0인 경우

(배열-비교) 요소들끼리 비교하는 경우 길이가 0, 1, 2인 구간에서 조심하기

구현

- 분산된 정보 함꼐 업데이트→ `TODO`를 활용해야징.

다 썼으면 초기화. 초기화 필요없어도 초기화


