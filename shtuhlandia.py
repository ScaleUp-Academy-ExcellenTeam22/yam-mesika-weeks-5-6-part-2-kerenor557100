#submitted by Keren Or Hadad 208025205

def shtuhlandia():
    """
    Of the names of all the countries in the United States,
    there is only one country name that can be typed with just one line on the keyboard.
    :return: The function returns the name of the country that can be assembled
    using the letters that appear on the same line on the keyboard.
    """
    special_states = []
    keyboard1 = {'q','w','e','r','t','y','u','i','o','p'}
    keyboard2 = {'a','s','d','f','g','h','j','k','l'}
    keyboard3 = {'z','x','c','v','b','n','m'}
    my_file = open("states.txt", "r")
    states = my_file.read()
    states_list = states.split("\n")
    my_file.close()
    for state in states_list:
        letters = set(list(state))
        if letters.issubset(keyboard1) or letters.issubset(keyboard2) or letters.issubset(keyboard3):
            special_states.append(state)
    print(special_states)


shtuhlandia()
"""
output:
['alaska']
"""