"""Задача 4. Полное условие находится в README.md."""


def make_card(code, labels=None):
    # TODO: реализуйте функцию по условию из README.md
    pass


def add_label(card, label):
    # TODO: реализуйте функцию по условию из README.md
    pass


def change_code(card, new_code):
    # TODO: реализуйте функцию по условию из README.md
    pass


def clone_card(card):
    # TODO: реализуйте функцию по условию из README.md
    pass

def make_card(code, labels=None):
    # Без labels - каждый раз новый пустой список.
    # С labels - используем именно его, без копии.
    if labels is None:
        labels = []
    return (code, labels)

def add_label(card, label):
    # Меняем список внутри кортежа, но не трогаем его.
    card[1].append(label)
    return card

def change_code(card, new_code):
    # Новый кортеж с новым кодом, но список меток - тот же.
    return (new_code, card[1])

def clone_card(card):
    # Новый кортеж и новая копия списка.
    return (card[0], list(card[1]))

    