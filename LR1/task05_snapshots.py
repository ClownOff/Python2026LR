"""Задача 5. Полное условие находится в README.md."""


def save_shallow(history, state):
    # TODO: реализуйте функцию по условию из README.md
    pass


def save_deep(history, state):
    # TODO: реализуйте функцию по условию из README.md
    pass


def restore(history, index):
    # TODO: реализуйте функцию по условию из README.md
    pass

import copy

def save_shallow(history, state):
    # Копия только снаружи.
    history.append(copy.copy(state))
    return history

def save_deep(history, state):
    # Полная копия.
    history.append(copy.deepcopy(state))
    return history

def restore(history, index):
    # Возвращаем копию.
    return copy.deepcopy(history[index])