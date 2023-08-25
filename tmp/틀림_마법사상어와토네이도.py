# __BOJ_20057_마법사상어와토네이도

# === input ===
N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]


# === algorithm ===
def move_tornado(r, c, dr, dc) -> int:
    out_boundary = 0
    loc_list = []
    loc_list += [[(r + 3*dr, c + 3*dc), 0.05]]
    loc_list += [[(r + 2*dr, c + 2*dc), 0.55]]

    if dr == 0:
        loc_list += [[(r + 1, c + 2*dc), 0.10], [(r - 1, c + 2*dc), 0.10]]
        loc_list += [[(r + 1, c + dc), 0.07], [(r - 1, c + dc), 0.07]]
        loc_list += [[(r + 2, c + dc), 0.02], [(r - 2, c + dc), 0.02]]
        loc_list += [[(r + 1, c), 0.01], [(r - 1, c), 0.01]]
    elif dc == 0:
        loc_list += [[(r + 2*dr, c + 1), 0.10], [(r + 2*dr, c - 1), 0.10]]
        loc_list += [[(r + dr, c + 1), 0.07], [(r + dr, c - 1), 0.07]]
        loc_list += [[(r + dr, c + 2), 0.02], [(r + dr, c - 2), 0.02]]
        loc_list += [[(r, c + 1), 0.01], [(r, c - 1), 0.01]]
    else:
        print("EXIT_FAILURE: n/a direction")
        exit()

    total = A[r+dr][c+dc]
    A[r+dr][c+dc] = 0
    for [(ar, ac), percent] in loc_list:
        if 0 <= ar < N and 0 <= ac < N:
            A[ar][ac] += int(total * percent)
        else:
            out_boundary += int(total * percent)
    return out_boundary


def move():
    global answer

    direction_list = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    direction_id = 0
    r, c = N // 2, N // 2
    dr, dc = direction_list[direction_id]

    for go_forward in range(1, N):
        repeat = 2
        if go_forward == N-1:
            repeat = 3
        for _ in range(repeat):
            for _ in range(go_forward):
                # print(r, c)
                move_tornado(r, c, dr, dc)
                r, c = r+dr, c+dc
            direction_id = (direction_id + 1) % 4
            dr, dc = direction_list[direction_id]
            # print_arr()


def print_arr():
    for r in range(N):
        print(*A[r])


# === output ===
prev_send = sum(map(sum, A))
move()
answer = prev_send - sum(map(sum, A))
print(answer)
