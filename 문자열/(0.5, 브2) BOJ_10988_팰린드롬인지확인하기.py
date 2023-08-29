# (0.5, 브2) BOJ_10988_팰린드롬인지확인하기

def check_if_palindrome(string: str):

    len_string = len(string)
    for i in range(len_string // 2):
        if string[i] != string[-(i + 1)]:
            return False

    return True


word = input()
if check_if_palindrome(word):
    print(1)
else:
    print(0)
