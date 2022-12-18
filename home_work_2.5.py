# 4. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

from pathlib import Path
import os

def recive_text_file (directory: str, filename: str) -> str:
    #path_dir = r'4/data_decrypted/'
    file_path = Path(os.getcwd() + directory, os.getcwd() + directory + filename)
    with open(file_path, encoding="utf-8") as data_str:
        data_str = data_str.read()
    return data_str



def write_in_file(resault_str: str, filename: str):
    path_dir = r'4/data_encrypted/'
    file_path = Path(path_dir, filename)
    with open(file_path,'w', encoding="utf-8") as str_write:
        str_write.write(str(resault_str))

def data_encrypted(text_string: str) -> list:
    #text_string = 'aaababbcbbb'
    list_elements = []

    if len(text_string) >= 2:
        #count_index = 0
        count = 1
        symbol = text_string[0]
        for i in range(1, len(text_string)):
            if text_string[i] == symbol:
                count += 1
            else:
                #list_elements.insert(count_index,[text_string[i - 1],count])
                list_elements.extend([text_string[i - 1],count])
                symbol = text_string[i]
                #count_index += 1
                count = 1
            if i + 1 == len(text_string):
                list_elements.extend([text_string[i],count])
    #print(list_elements)
    return list_elements

#def data_decrypted(text_string: str) -> str:

def format_str(text_string: str) -> str:
    #text_string = "['a', 3, 'b', 1, 'a', 1, 'b', 2, 'c', 1, 'b', 3]"
    text_resault = ""
    for i in range(1,len(text_string) - 1):
        if text_string[i] != "'" and text_string[i] != "," and text_string[i] != " ":
            text_resault += text_string[i]
    return text_resault

#text_str = format_str(recive_text_file('/4/data_decrypted/','data.txt'))
#print(text_str)
#for i in range(len(text_resault)):
#    print(text_resault[i])
#text_list = text_string[1 : -1].split()
#print(text_list)

#for i in range(len(text_string)):
#    text_string[i].replace("'", "")
#    if i % 2 == 0:
#print(text_string[1 : -1].split())


# Сжатие данных и их запись в файл
write_in_file(data_encrypted(recive_text_file('/4/data_decrypted/','data.txt')),'resault.txt')