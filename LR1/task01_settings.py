"""Задача 1. Полное условие находится в README.md."""


def add_change(key, value, changes=None):
    # TODO: реализуйте функцию по условию из README.md
    pass


def apply_changes(settings, changes):
    # TODO: реализуйте функцию по условию из README.md
    pass


def build_settings(base, changes):
    # TODO: реализуйте функцию по условию из README.md
    pass

import copy



def add_change(key, value, changes=None):
    # Если список не передали - делаем новый.
    if changes is None:
        changes = []
    changes.append((key,value))
    return changes


def apply_changes(settings, changes):
    # Применяем изменения к тому же словарю.
    for key, value in changes:
        settings[key] = value
    return settings


def build_settings(base,changes):
    # Делаем полную копию, чтоюы не менять base.
    # deepcopy - т.к. внутри могут быть вложенные списки/словари
    result = copy.deepcopy(base)
    for key, value in changes:
        result[key] = value
    return result
    