
def solution(key, lock):      
    
    # RO variables
    len_key, len_lock = len(key), len(lock)
    lock_hole_set = set()
    for tr in range(len_lock):
        for tc in range(len_lock):
            if lock[tr][tc] == 0:
                lock_hole_set.add((tr,tc))
        
    def rotate_key(old_key) -> list:
        new_key = [[0]*len_key for _ in range(len_key)]
        for r in range(len_key):
            for c in range(len_key):
                new_key[c][len_key - 1 - r] = old_key[r][c]
        return new_key
        
    def check_at_lock(lock_loc):
        
        def check_at_key(key_loc):
            # print(f"lock:{lock_loc}, key{key_loc}")
            lock_holes = set()
            for dr in range(key_loc[0]):
                for dc in range(key_loc[1]):
                    lr, lc, kr, kc = lock_loc[0]-dr, lock_loc[1]-dc, key_loc[0]-dr, key_loc[1]-dc
                    if 0 <= lr < len_lock and 0 <= lc < len_lock:
                        # (돌기, 돌기) || (홈, 홈)
                        if key[kr][kc] == lock[lr][lc]:
                            return False
                        # (돌기, 홈) || (홈, 돌기)
                        else:
                            # 자물쇠가 홈인 경우 위치 체크
                            if lock[lr][lc] == 0:
                                lock_holes.add((lr, lc))
                                
            for dr in range(len_key-key_loc[0]):
                for dc in range(len_key-key_loc[1]):
                    lr, lc, kr, kc  = lock_loc[0]+dr, lock_loc[1]+dc, key_loc[0]+dr, key_loc[1]+dc
                    # 자물쇠의 범위 안이면 체크, 자물쇠의 범위 밖이면 상관없다.
                    if 0 <= lr < len_lock and 0 <= lc < len_lock:
                        # (돌기, 돌기) || (홈, 홈)
                        if key[kr][kc] == lock[lr][lc]:
                            return False
                        # (돌기, 홈) || (홈, 돌기)
                        else:
                            # 자물쇠가 홈인 경우 위치 체크
                            if lock[lr][lc] == 0:
                                lock_holes.add((lr, lc))
            if lock_holes == lock_hole_set:
                return True
            else:
                return False            
            
        for k_r in range(len_key):
            for k_c in range(len_key):
                if check_at_key([k_r, k_c]):
                    return True
        return False
                    
    # lock의 각 칸마다 반복
    for l_r in range(len_lock):
        for l_c in range(len_lock):
            for _ in range(4):
                # key와 비교
                if check_at_lock([l_r, l_c]):
                    return True
                # 회전하여 반복
                key = rotate_key(key)
    
        
    return False
