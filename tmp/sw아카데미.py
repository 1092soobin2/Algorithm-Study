# ===input===
T = int(input())

# ===algorithm===
def sol():
    number, repeat = input().split()
    repeat = int(repeat)
    number = list(map(int, number))
    len_number = len(number)

    def find_max_index_back(start_i) -> int:
        max_i = start_i
        for num_i in range(start_i, len_number):
            if number[num_i] >= number[max_i]:
                max_i = num_i
        return max_i

    def find_same():
        for num_i in range(len_number - 1):
            if number[num_i] == number[num_i + 1]:
                return True
        return False

    for r in range(repeat):
        index = 0
        for i in range(0, repeat-r):
            if number[i] < number[index]:
                index = i
        max_index = index
        while True:
            max_index = find_max_index_back(index)
            if number[index] != number[max_index]:
                break
            index += 1
            if index == len_number:
                break

        if index == len_number:
            if not find_same():
                if (repeat - r) % 2 == 1:
                    index = len_number - 2
                    number[index], number[max_index] = number[max_index], number[index]
            break

        # print(index, max_index, number)

        number[index], number[max_index] = number[max_index], number[index]
        print(number)
        index += 1


    return "".join(list(map(str, number)))


# ===output===
for t in range(1, T + 1):
    print(f"#{t} {sol()}")