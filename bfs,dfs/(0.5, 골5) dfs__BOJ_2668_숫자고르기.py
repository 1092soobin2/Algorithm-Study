

# === input ===
N = int(input())
ARRAY = [int(input()) - 1 for _ in range(N)]


# === algorithm ===
def solution():

    selected_set = set()

    def dfs(start):

        index_stack = [start]

        index_set = set()
        number_set = set()

        while index_stack:
            curr_idx = index_stack.pop()
            curr_num = ARRAY[curr_idx]

            index_set.add(curr_idx)
            number_set.add(curr_num)
            if curr_num not in index_set and curr_num not in selected_set:
                index_stack.append(curr_num)

            if number_set == index_set:
                return index_set

        if number_set == index_set:
            return index_set
        else:
            return set()

    for i in range(N):
        if i not in selected_set:
            selected_set |= dfs(i)
    return sorted(list(selected_set))


# === output ===
answer = list(map(lambda x: int(x) + 1, solution()))
print(len(answer))
print("\n".join(map(str, answer)))
