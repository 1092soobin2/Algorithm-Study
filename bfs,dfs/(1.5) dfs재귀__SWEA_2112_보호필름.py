# (1.5) dfs재귀__SWEA_2112_보호필름

# D*W     protection film
# A(0)|B(1)     attribute

# K       criteria
    # col에서 K개 이상 같은 attribute가 연속되어야 한다.

# ans: min of projection_count

def test_film(film, depth, width, criteria):
    entire_pass = True

    for c in range(width):
        same_attr = 1
        col_pass = False
        for r in range(1, depth):
            if film[r][c] == film[r-1][c]:
                same_attr += 1
            else:
                same_attr = 1
            if same_attr >= criteria:
                col_pass = True
                break
        if not col_pass:
            entire_pass = False
            break

    return entire_pass


def print_film(film, depth, width, title=""):
    print("================")
    print(title)
    for r in range(depth):
        for c in range(width):
            print(film[r][c], end=' ')
        print()
    print("================\n")


def min_projection_count(film, depth, width, criteria) -> int:

    if test_film(film, depth, width, criteria):
        return 0

    def dfs(start_i, count, max_count) -> bool:
        if test_film(film, depth, width, criteria):
            # print_film(film, depth, width, f"count {count} / {max_count}")
            return True
        if count == max_count:
            return False

        for i in range(start_i, depth):
            curr_row = film[i]
            # A
            film[i] = [0]*width
            if dfs(i+1, count+1, max_count):
                film[i] = curr_row
                return True
            # B
            film[i] = [1]*width
            if dfs(i+1, count+1, max_count):
                film[i] = curr_row
                return True
            film[i] = curr_row

    for num_of_row in range(1, depth+1):
        if dfs(0, 0, num_of_row):
            return num_of_row

    return depth


T = int(input())
for test_case in range(1, T + 1):
    # ===input===
    D, W, K = map(int, input().split())
    film = [list(map(int, input().split())) for _ in range(D)]

    # ===algorithm===
    ans = min_projection_count(film, D, W, K)

    # ===output===
    print(f"#{test_case} {ans}")