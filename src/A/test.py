def game_result():
    S_set = set(S)
    last_symbols = set()
    for S_symbol, Q_symbol in zip(S, Q):
        if S_symbol == Q_symbol:
            last_symbols.add(Q_symbol)
            print("correct")
        elif Q_symbol in S_set \
                and Q_symbol not in last_symbols:
            last_symbols.add(Q_symbol)
            print("present")
        else:
            print("absent")


if __name__ == '__main__':
    S, Q = input().strip(), input().strip()
    game_result()


if __name__ == '__main__':
    symbols = set(S)
    black_symbols = set()
    for index, (w1, w2) in enumerate(zip(input().strip(), input().strip())):
        if w1 == w2:
            print("correct")
            black_symbols.add(w2)
        elif w2 in symbols and w2 not in black_symbols:
            print('present')
            black_symbols.add(w2)
        else:
            print('absent')

