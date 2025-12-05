import os
# TODO: fix docs

def word_frequency(string: str) -> dict[str, int]:
    """
    Counts the amount of each word in a string.
    :param string: the string to count words in.
    :return: a dictionary with the structure of {'word': count}
    """
    characters_to_clear = '.,:;?!@#$%^&*-+/~`=_'
    clean_string = string.strip(characters_to_clear)
    words = clean_string.split()
    ret = {}
    for word in words:
        ret[word] = ret.get(word, 0) + 1
    return ret

def move_file(fname: str, category: str, dir: str = 'archive') -> None:
    """
    Moves a file from the unsorted directory to the sorted directory into the specified category.
    :param fname: the file to move from the unsorted folder
    :param category: the category name to move the file to
    :param dir: the working directory of sorting, 'archive' by default
    :raises ValueError: if ``dir`` does not exist in ``.``
    :raises ValueError: if ``fname`` does not exist in ``./archive/unsorted``
    :return:
    """
    path_to_file = f'./{dir}/unsorted/{fname}'
    path_to_category = f'./{dir}/sorted/{category}'
    path_to_new_file = f'{path_to_category}/{fname}'
    if not os.path.exists(path_to_file):
        raise ValueError('File to move does not exist.')
    if not os.path.exists(f'./{dir}'):
        raise ValueError('Working directory does not exist.')
    if not os.path.exists(path_to_category):
        os.mkdir(path_to_category)
    os.rename(path_to_file, path_to_new_file)

def move_all(info: dict[str, str], dir: str = 'archive') -> None:
    """
    Moves all files from ./archive/unsorted into ./archive/sorted by using info in ``info`` dict.
    :param info: the dictionary to be used as a reference for sorting. 'file_name': 'category_name'
    :param dir: the working directory of sorting, 'archive' by default
    :raises ValueError: if ``dir`` does not exist in ``.``
    :return:
    """
    if not os.path.exists(f'./{dir}'):
        raise ValueError('Working directory does not exist.')
    for file, category in info:
        move_file(file, category)


def smart_sort_files(path: str) -> None:
    """
    Sorts all files by categories into different folders from ./(path)/unsorted/ into ./(path)/sorted
    :param path: the working directory of the sorting.
    :raises ValueError: if ``path`` does not exist in ``.``.
    :return:
    """
    ...

def check_accuracy(path: str) -> None:
    """
    Checks accuracy of an already performed sorting in ./(path)/sorted by using ./(path)/labels.txt as a reference.
    :param path: the working directory of previously performed sorting.
    :raises ValueError: if ``path`` does not exist in ``.``.
    :return:
    """
    ...

move_file('test.txt', 'test')