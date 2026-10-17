"""Задача 6. Полное условие находится в README.md."""


def make_request_key(request):
    # TODO: реализуйте функцию по условию из README.md
    pass


def group_requests(requests):
    # TODO: реализуйте функцию по условию из README.md
    pass

def make_request_key(request):
    # Собираем ключ так, чтобы одинаковые по смыслу запросы давали одинаковый ключ.
    return (
        request["path"],
        tuple(request["fields"]),
        frozenset(request["tags"]),
        tuple(sorted(request["options"].items())),
    )

def group_requests(requests):
    # Складываем запросы в словарь: ключ => список запросов.
    groups = {}
    for request in requests:
        key = make_request_key(request)
        if key not in groups:
            groups[key] = []
        groups[key].append(request)
    return groups
