#submitted by Keren Or Hadad 208025205
# part 5.4
import itertools


def interleave(*lists):
    """
    The function gets a list of lists and returns a list where the first items are the first items in every list,
    then the seconds etc.
    :param lists: list of input lists
    :return: reorganized list (as described above)
    """
    if len(set(len(_) for _ in lists)) > 1:
        raise ValueError("Lists are not all the same length!")
    reorganized_list = list(itertools.chain(*lists))
    for list_index, word in enumerate(lists):
        reorganized_list[list_index::len(lists)] = word
    return reorganized_list


print(interleave('abc', [1, 2, 3], ('!', '@', '#')))
"""
output:
['a', 1, '!', 'b', 2, '@', 'c', 3, '#']
"""