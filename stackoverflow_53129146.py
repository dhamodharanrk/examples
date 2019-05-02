#Link : https://stackoverflow.com/questions/53129146/python-beautifulsoup-unboundlocalerror

import os
from bs4 import BeautifulSoup
import ftfy

path_to_10k = "D:/10ks/list_missing_10k/"
path_to_saved_10k = "D:/10ks/list_missing_10kp/"
list_txt = os.listdir(path_to_10k)

for name in list_txt:
    file = open(path_to_10k + name, "r+", encoding="utf-8")
    file_read = file.read()
    textData = ftfy.fix_text(file_read)
    textData = ftfy.fix_text_encoding(textData)
    try: text = BeautifulSoup(textData, "html5lib")
    except: text = BeautifulSoup(textData)
    text = text.get_text("\n")
    file2 = open(path_to_saved_10k + name, "w+", encoding="utf-8")
    file2.write(str(text))
    file2.close()
    file.close()
