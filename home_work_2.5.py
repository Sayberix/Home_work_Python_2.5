# 4. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

from pathlib import Path
import os

# получение текста из файла
def recive_text_file (directory: str, filename: str) -> str:
    #path_dir = r'4/data_decrypted/'
    file_path = Path(os.getcwd() + directory, os.getcwd() + directory + filename)
    with open(file_path, 'r', encoding="utf-8") as read_data_str:
        read_data_str = read_data_str.read()
    return read_data_str

# запись текста в файл
def write_in_file(resault_str: str, directory: str, filename: str):
    #path_dir = r'4/data_encrypted/'
    file_path = Path(os.getcwd() + directory, os.getcwd() + directory + filename)
    with open(file_path,'w', encoding="utf-8") as str_write:
        str_write.write(str(resault_str))

# шифрование данных
def data_encrypted(text_string: str) -> list:
    #text_string = 'aaababbcbbb'
    list_elements = []
    if len(text_string) >= 2:
        count = 1
        symbol = text_string[0]
        for i in range(1, len(text_string)):
            if text_string[i] == symbol:
                count += 1
            else:
                list_elements.extend([text_string[i - 1],count])
                symbol = text_string[i]
                count = 1
            if i + 1 == len(text_string):
                list_elements.extend([text_string[i],count])
    return list_elements

# преобразование строки со списком в удобочитаемый формат
def format_str(text_string: str) -> str:
    #text_string = "['a', 3, 'b', 1, 'a', 1, 'b', 2, 'c', 1, 'b', 3]"
    text_resault = ""
    for i in range(1,len(text_string) - 1):
        if text_string[i] != "'" and text_string[i] != "," and text_string[i] != " ":
            text_resault += text_string[i]
    return text_resault

# расшифровка данных
def data_decrypted(data: str) -> str:
    #data = "a3b1a1b2c1b3"
    data = format_str(data) # преобразуем данные для работы над ними как над списком
    resault = ""
    for i in range(0, len(data), 2):
        for j in range(int(data[i + 1])):
            resault += data[i]
    return resault


# Сжатие данных и их запись в файл
data = recive_text_file('/4/data_decrypted/','data.txt')
write_in_file(data_encrypted(data),'/4/data_encrypted/','resault.txt')

# Распаковка данных и запись их в файл
data = recive_text_file('/4/data_encrypted/','data.txt')
write_in_file(data_decrypted(data),'/4/data_decrypted/','resault.txt')