import os
import pickle
#from pathlib import Path

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

def move_file(fname: str, category: str) -> None:
    """
    Moves a file from the unsorted directory to the sorted directory into the specified category.
    :param fname: the file to move from the unsorted folder
    :param category: the category name to move the file to
    :raises ValueError: if ``fname`` does not exist in ``./archive/unsorted``
    :return:
    """
    path_to_file = f'./archive/unsorted/{fname}'
    path_to_category = f'./archive/sorted/{category}'
    path_to_new_file = f'{path_to_category}/{fname}'
    if not os.path.exists(path_to_file):
        raise ValueError('File to move does not exist.')
    if not os.path.exists(path_to_category):
        os.mkdir(path_to_category)
    os.rename(path_to_file, path_to_new_file)



# def sort_one_file(fpath: str, sort_dir: str):
#     """
#
#     :param fpath: a string of path leading to the file to be sorted
#     :param sort_dir: a string of path leading to the directory that contains directories to sort the file to
#     :raises ValueError: if ``path`` or ``sort_dir`` does not exist
#     :return: ...
#     """
#     if not os.path.exists(fpath):
#         raise ValueError('Path does not exist')
#     file = open(fpath, 'r')
#     content = file.read()
#     file.close()
#     word_count = word_frequency(content)
#     if word_count['test'] and word_count['test'] >= 3:
#
#     return ...
#
#
# res = sort_one_file('archive/unsorted/test.txt')
# print(res)

move_file('test.txt', 'test')