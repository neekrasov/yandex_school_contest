def result_competition():
    result = []
    for position_title, people in candidates.items():
        people = sorted(people, key=lambda human: [human[1], -human[-1]], reverse=True)
        result += list(map(lambda x: x[0], people[:positions[position_title]]))
    print(*sorted(result), sep='\n')


if __name__ == "__main__":
    n, positions = int(input()), {}
    for i in range(n):
        position, count = input().split(',')
        positions[position] = positions.get(position, 0) + int(count)

    k, candidates = int(input()), {}
    for i in range(k):
        inp = input().split(',')
        name, position, count, fail = inp[0], inp[1], int(inp[2]), int(inp[3])
        value = candidates.get(position, [])
        value.append([name, count, fail])
        candidates[position] = value

    result_competition()
