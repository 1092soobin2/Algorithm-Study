# 30

# ShiftRow
# Rotate

from collections import deque

def solution(rc, operations):
    
    ROW, COL = len(rc), len(rc[0])
    
    col0 = deque([row[0] for row in rc])                #|
    coln = deque([row[-1] for row in rc])               #|
    rows = deque([deque(row[1:-1]) for row in rc])      #=
    
    def print_rc():
        print(col0, coln, rows)
        # for r in range(ROW):
        #     print(list([col0[r]]) + list(rows[r]) + list([coln[r]]))
    
    def rotate():
        # row 0, ROW-1   -  -
        rows[0].appendleft(col0.popleft())
        rows[-1].append(coln.pop())
        # col 0, COL-1
        col0.append(rows[-1].popleft())
        coln.appendleft(rows[0].pop())
        
    def shift_row():
        rows.appendleft(rows.pop())
        col0.appendleft(col0.pop())
        coln.appendleft(coln.pop())
    
    # print_rc()
    for op in operations:
        if op == "ShiftRow":
            shift_row()
        elif op == "Rotate":
            rotate()
        # print_rc()
        
    rc = [list([col0[r]]) + list(rows[r]) + list([coln[r]]) for r in range(ROW)]
    
    return rc
