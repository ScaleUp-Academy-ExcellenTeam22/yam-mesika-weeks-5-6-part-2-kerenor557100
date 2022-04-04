#submitted by Keren Or Hadad 208025205
import time


def mahir_veamin():
    """

    :return: How long on average does the word search in the list and how much in the group.
    And so we will know what is faster.
    """
    sum_time_list = 0
    sum_time_set = 0
    my_file = open("words.txt", "r")
    content = my_file.read()
    content_list = content.split("\n")
    my_file.close()
    content_set = set(content_list)
    for i in range(1000):
        start_list = time.time()
        index_list = content_list.index("zwitterion")
        end_list = time.time()
        sum_time_list += end_list-start_list
        start_set = time.time()
        el_in_set = "zwitterion" in content_set
        end_set = time.time()
        sum_time_set += end_set - start_set
    average_time_list = sum_time_list/1000
    average_time_set = sum_time_set/1000
    print("average search time in list: ", average_time_list, ", average search time in set: ", average_time_set)
mahir_veamin()
"""
output:
average search time in list:  0.006536080121994019 , average search time in set:  2.728700637817383e-06

searching in set is much faster
"""
