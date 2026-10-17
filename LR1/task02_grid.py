"""Задача 2. Полное условие находится в README.md."""


def make_grid(rows, columns, template):
    # TODO: реализуйте функцию по условию из README.md
    pass


def update_cell(grid, row, column, field, value):
    # TODO: реализуйте функцию по условию из README.md
    pass


def replace_cell(grid, row, column, new_cell):
    # TODO: реализуйте функцию по условию из README.md
    pass

import copy

def make_grid(rows, columns, template):
    # Каждую ячейку делаем отдельной копией шаблона.
    grid = []
    for _ in range(rows):
        row = []
        for _ in range(columns):
         row.append(copy.deepcopy(template))
        grid.append(row)
    return grid

def update_cell(grid, row, column, field, value):
    # Меняем поле внутри словаря, а не саму ячейку.
    grid[row][column][field] = value
    return grid

def replace_cell(grid, row, column, new_cell):
    # Запоминаем старую ячейку, кладем новую, возвращаем старую.
    old_cell = grid[row][column]
    grid[row][column] = new_cell
    return old_cell