# (1.5) Codetree_왕실의기사대결

# L*L board [1,1]~ [EMPTY, TRAP, WALL]

# N 기사 [위치(r, c), h*w, 체력: k]
# 자신의 마력으로 상대방을 밀쳐낼 수 있음

# 명령
# (

# 1. move_knight
# 인접 4칸 중 하나로 이동
# 이동하려는 위치에 다른 기사가 있다면 연쇄적으로 밀려남
# 이동 방향 끝에 벽이 있다면 모든 기사는 이동할 수 X
# 사라진 기사에게 명령을 내리면 반응 X

# 2. fight_damage
# 밀려난 기사들 피해를 입음
# 이동한 곳에 놓여 있는 TRAP 수만큼 피해
# 피해를 받은 만큼 체력 깎임
# 체력 이상의 피해를 받을 경우 사라짐

# answer: 생존 기사들이 받은 총 대미지의 합

from collections import deque
from typing import List


class Knight:
    def __init__(self, knight, idx):
        self.loc = knight[0] - 1, knight[1] - 1
        self.height, self.width = knight[2:4]
        self.stamina = knight[4]
        self.damage = 0
        self.dead = False
        self.idx = idx + 1

    def __str__(self):
        if not self.dead:
            return f"{self.idx} stamina:{self.stamina}, damage:{self.damage}\n"
        else:
            return f"{self.idx} is dead\n"

    def get_right_down_loc(self):
        r, c = self.loc
        return [r + self.height - 1, c + self.width - 1]

    def check_at_board(self, board):
        r, c = self.loc
        for dr in range(self.height):
            for dc in range(self.width):
                board[r + dr][c + dc] = self.idx

    def die(self, board):
        r, c = self.loc
        for dr in range(self.height):
            for dc in range(self.width):
                board[r + dr][c + dc] = 0

    def cal_damage_at_board(self, board):
        damage = 0
        print_debug(f"cal_damage {self.idx}, {self}")
        r, c = self.loc
        for dr in range(self.height):
            for dc in range(self.width):
                if BOARD[r + dr][c + dc] == TRAP:
                    damage += 1
        if damage >= self.stamina:
            self.dead = True
            self.die(board)
        else:
            self.stamina -= damage
            self.damage += damage


# === input ===
L, N, Q = map(int, input().split())
BOARD = [list(map(int, input().split())) for _ in range(L)]
knight_info_list = [list(map(int, input().split())) for _ in range(N)]
COMMAND_LIST = [list(map(int, input().split())) for _ in range(Q)]
DIRECTION_LIST = [[-1, 0], [0, 1], [1, 0], [0, -1]]
knight_list: List[Knight] = []
knight_board = []
EMPTY, TRAP, WALL = 0, 1, 2


# === algorithm ===
def init():
    global knight_list, knight_board

    knight_board = [[0]*L for _ in range(L)]
    knight_list.append(None)

    for idx in range(N):
        knight = Knight(knight_info_list[idx], idx)

        # board
        knight.check_at_board(knight_board)

        # list
        knight_list.append(knight)

    print_debug("after init")


def move_knight(knight_id, direction_id) -> list:
    global knight_board, knight_list

    def check_wall() -> bool:  # wall -> True
        if not ((0 <= left_r < L and 0 <= left_c < L) and
                (0 <= right_r < L and 0 <= right_c < L)):
            return True
        if direction_id == 1:
            return WALL in [BOARD[temp_r][right_c] for temp_r in range(left_r, right_r + 1)]
        elif direction_id == 3:
            return WALL in [BOARD[temp_r][left_c] for temp_r in range(left_r, right_r + 1)]
        elif direction_id == 0:
            return WALL in BOARD[left_r][left_c:right_c + 1]
        elif direction_id == 2:
            return WALL in BOARD[right_r][left_c:right_c + 1]

    def get_next_loc(loc) -> bool:
        return loc[0] + dr, loc[1] + dc

    new_knight_board = [[0] * L for _ in range(L)]
    dr, dc = DIRECTION_LIST[direction_id]

    pushed = [knight_id]
    pushed_set = {knight_id}
    to_be_pushed = deque([knight_id])

    while to_be_pushed:
        curr_knight_id = to_be_pushed.popleft()
        curr_knight = knight_list[curr_knight_id]

        left_r, left_c = get_next_loc(curr_knight.loc)
        right_r, right_c = get_next_loc(curr_knight.get_right_down_loc())

        if check_wall():
            print_debug(f"이 기사 다음에 벽이 있음: {curr_knight_id, (left_r, left_c, right_r, right_c)}")
            pushed.clear()
            break

        for r in range(left_r, right_r + 1):
            for c in range(left_c, right_c + 1):
                new_knight_board[r][c] = curr_knight_id
                if knight_board[r][c] != curr_knight_id and knight_board[r][c] != 0 \
                        and knight_board[r][c] not in pushed_set:
                    to_be_pushed.append(knight_board[r][c])
                    pushed.append(knight_board[r][c])
                    pushed_set.add(knight_board[r][c])

    if pushed:

        for unpushed_id in range(1, N + 1):
            if unpushed_id not in pushed_set and not knight_list[unpushed_id].dead:
                knight_list[unpushed_id].check_at_board(new_knight_board)

        knight_board = new_knight_board
        for pushed_id in pushed:
            knight_list[pushed_id].loc = get_next_loc(knight_list[pushed_id].loc)

        for pushed_id in pushed[1:]:
            knight_list[pushed_id].cal_damage_at_board(knight_board)

    print_debug(f"⭕move 끝: {knight_id}/{get_direction_char(direction_id)}, pushed:{pushed}")


def exec_command(knight_id, direction_id):

    if knight_list[knight_id].dead:
        return

    move_knight(knight_id, direction_id)


def solution():
    init()
    for command in COMMAND_LIST:
        exec_command(*command)

    answer = 0
    for knight in knight_list[1:]:
        if not knight.dead:
            answer += knight.damage

    return answer


def get_direction_char(direction_id):
    if direction_id == 0:
        return "⬆️"
    elif direction_id == 1:
        return "->"
    elif direction_id == 2:
        return "⬇️"
    elif direction_id == 3:
        return "<-"


def print_debug(title=""):
    if not DEBUG:
        return

    print("============================")
    print(title)
    print(*knight_list[1:])
    for r in range(L):
        for c in range(L):
            if BOARD[r][c] == EMPTY:
                print(f" ", end="")
            elif BOARD[r][c] == TRAP:
                print(f"^", end="")
            elif BOARD[r][c] == WALL:
                print(f"+", end="")
        print("|\t", end="")
        for c in range(L):
            if BOARD[r][c] == WALL:
                print(f"  +", end="")
            else:
                print(f"{knight_board[r][c]:3}", end="")
        print()
    print("============================")


# === output ===
DEBUG = False
# DEBUG = True

print(solution())
