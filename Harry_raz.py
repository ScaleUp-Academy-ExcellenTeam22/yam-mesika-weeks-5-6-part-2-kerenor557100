#submitted by Keren Or Hadad 208025205

import os
import codecs
import re


def harry_raz():
    """
    The resources folder contains a compressed file with all the chapters of the story,
    but unfortunately the name of the files does not match their contents.
    In this exercise I renamed the files to suit their contents
    :return: Each file is returned so that its new name will be a three-digit number that describes the chapter number,
     followed by the chapter name.
    """
    for it in range(122):
        itt = it + 1
        it_b = str(itt) + ".html"
        codecs.register_error("strict", codecs.ignore_errors)
        f = codecs.open("potter/" + it_b, 'r').read()
        match = re.search('<title>(.*?)</title>', f)
        title = match.group(1) if match else 'No title'
        title = title.split("Chapter ")
        title = title[1].split(":")
        if eval(title[0]) < 10:
            title[0] = "00" + title[0]
        elif eval(title[0]) < 100:
            title[0] = "0" + title[0]
        title_new = ''
        for i in title:
            title_new += i
        title_new += ".html"
        os.rename("potter/" + it_b, title_new)


harry_raz()
