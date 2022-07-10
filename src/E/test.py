import os

result = []
size, read_limit = os.path.getsize('input.txt'), 100
with open('input.txt') as f:
    for _ in range(0, size, read_limit):
        expression = f.read(read_limit)
        for index, symbol in enumerate(expression):
            if symbol == '(':
                result.append(index)
            elif symbol == ')':
                if not result:
                    result.append(index)
                else:
                    result.pop()
if not result or len(result) >= 2:
    print('-1')
else:
    print(result.pop() + 1)

