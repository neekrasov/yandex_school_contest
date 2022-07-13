def check_diff_len(big: str, less: str):
    count = 0
    for i in range(len(less)):
        if less[i] != big[i]:
            count += 1
            if less[i] == big[i + count]:
                i -= 1
    return count


def checkForMathes(w1: str, w2: str):
    len_w1 = len(w1)
    len_w2 = len(w2)

    if ((w1 in w2) or (w2 in w1)) and abs(len_w1 - len_w2) <= 1:
        return True
    elif len_w1 > len_w2:
        count = check_diff_len(w1, w2)
    elif len_w2 > len_w1:
        count = check_diff_len(w2, w1)
    elif len_w1 == len_w2:
        count = 0
        for i in range(len_w1):
            if w1[i] != w2[i]:
                count += 1

    return True if count <= 1 else False


if __name__ == "__main__":
    print(checkForMathes("hell", "hello"))
    print(checkForMathes("cat", "cut"))
    print(checkForMathes("cat", "at"))
    print(checkForMathes("cat", "caf"))
    print(checkForMathes("cat", "atc"))
    print(checkForMathes("cat", "fat"))
    print(checkForMathes("cat", "caft"))
