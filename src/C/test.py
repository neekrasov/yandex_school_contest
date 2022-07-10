def sort_products(json: dict, *args) -> str:
    return dumps(sorted(filter(
        lambda p: args[0] in p['name'].lower().strip()
                  and args[1] <= p['price'] <= args[2]
                  and args[3] <= datetime.strptime(p['date'], "%d.%m.%Y") <= args[4], json),
        key=lambda x: x['id']),
    )


if __name__ == '__main__':
    from datetime import datetime
    from json import loads, dumps

    json = loads(input())
    NAME_CONTAINS = input().split()[1].lower().strip()
    PRICE_GREATER_THAN, PRICE_LESS_THAN = int(input().split()[1]), int(input().split()[1])
    DATE_AFTER = datetime.strptime(input().split()[1], "%d.%m.%Y")
    DATE_BEFORE = datetime.strptime(input().split()[1], "%d.%m.%Y")
    print(sort_products(json, NAME_CONTAINS, PRICE_GREATER_THAN, PRICE_LESS_THAN, DATE_AFTER, DATE_BEFORE))


