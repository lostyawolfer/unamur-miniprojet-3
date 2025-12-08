import os


def clean_text(string:str):
    """
    Receives a text/string, changes all upper-case into lower_case letters, removes all punctuations and returns  the resulting string
    
    Parameters
    ----------
    string: string to be cleanes(str)
    
    Returns
    -------
    Result: clean_Up string
    """
    signs=["(",")","{","}","'",",","[","]","/","'",".",":",";","?","!","@","#","$","%","^","&","*","-","+","/","~","`","=","_"]
    string = string.lower()
    for sign in signs:
        string = string.replace(sign," ")
        string=string.replace("  "," ")
    string = string.strip()      
    return string

def word_frequency(string: str) -> dict[str, int]:
    """Counts the amount of each word in a string.

    Parameters
    ----------
    string : the string to count words in (str)

    Returns
    -------
    a dictionary with the structure of {'word': count}
    """
    clean_string = clean_text(string)
    words = clean_string.split()
    ret = {}
    for word in words:
        ret[word] = ret.get(word, 0) + 1
    return ret

def move_file(fname: str, category: str, dir: str = 'archive') -> None:
    """Moves a file from the unsorted directory to the sorted directory into the specified category.

    Parameters
    ----------
    fname : the file to move from the unsorted folder (str)
    category : the category name to move the file to (str)
    dir : the working directory of sorting, 'archive' by default (str)

    Raises
    ------
    ValueError
        if ``dir`` does not exist in ``.``
    ValueError
        if ``fname`` does not exist in ``./archive/unsorted``
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
    """Moves all files from ./archive/unsorted into ./archive/sorted by using info in ``info`` dict.

    Parameters
    ----------
    info : the dictionary to be used as a reference for sorting. 'file_name': 'category_name' (dict[str, str])
    dir : the working directory of sorting, 'archive' by default (str)

    Raises
    ------
    ValueError
        if ``dir`` does not exist in ``.``
    """
    if not os.path.exists(f'./{dir}'):
        raise ValueError('Working directory does not exist.')
    for file, category in info:
        move_file(file, category)


def smart_sort_files(path: str) -> None:
    """Sorts all files by categories into different folders from ./(path)/unsorted/ into ./(path)/sorted.

    Parameters
    ----------
    path : the working directory of the sorting (str)

    Raises
    ------
    ValueError
        if ``path`` does not exist in ``.``.
    """
    ...

def check_accuracy(path: str) -> None:
    """Checks accuracy of an already performed sorting in ./(path)/sorted by using ./(path)/labels.txt as a reference.

    Parameters
    ----------
    path : the working directory of previously performed sorting (str)

    Raises
    ------
    ValueError
        if ``path`` does not exist in ``.``.
    """
    ...


test_string = "Hello, my name Hello"

print(word_frequency(test_string))
