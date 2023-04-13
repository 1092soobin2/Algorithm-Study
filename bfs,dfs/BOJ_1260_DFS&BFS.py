# BOJ_1260_DFS&BFS
from collections import deque

# ===input===
N, M, V = map(int, input().split())  # N: nodes, M: edges, V: start node
edges = [list(map(int, input().split())) for _ in range(M)]

# ===algorithm===

# 1. adj list
adj_list = [list() for _ in range(N + 1)]
for edge in edges:
    adj_list[edge[0]].append(edge[1])
    adj_list[edge[1]].append(edge[0])


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


# 3. bfs - queue
def bfs(graph_list, start_node):
    # 기본 2개
    visited_list, not_visited_queue = [], deque([start_node])

    while not_visited_queue:
        curr_node = not_visited_queue.popleft()

        if curr_node not in visited_list:
            visited_list.append(curr_node)
            not_visited_queue.extend(sorted(set(graph_list[curr_node]) - set(visited_list)))
    return visited_list


# ===output===
ans1, ans2 = dfs(adj_list, V), bfs(adj_list, V)

print(' '.join(str(x) for x in ans1))
print(' '.join(str(x) for x in ans2))
