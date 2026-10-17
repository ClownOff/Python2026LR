"""Задача 3. Полное условие находится в README.md."""


def build_tag_index(documents):
    # TODO: реализуйте функцию по условию из README.md
    pass


def attach_tag(document, tag, index):
    # TODO: реализуйте функцию по условию из README.md
    pass

def build_tag_index(documents):
    # Для каждого тега - свой список документов.
    # Сами документы не копируем.
    index = {}
    for document in documents:
        for tag in document["tags"]:
            if tag not in index:
                index[tag] = []
            index[tag].append(document)
    return index

def attach_tag(document, tag, index):
    # Тег добавляем документу и документ добавляем в индекс по этому тегу.
    document["tags"].append(tag)
    if tag not in index:
        index[tag] = []
    index[tag].append(document)
    return index