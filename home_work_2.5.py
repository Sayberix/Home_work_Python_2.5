# Напишите программу, удаляющую из текста все слова, содержащие "абв".

from pathlib import Path

def recive_text_file (filename: str) -> str:
    path_dir = r'1/data/'
    file_path = Path(path_dir, filename)
    with open(file_path,'r', encoding="utf-8") as data_str:
        data_str = data_str.read().split()
    return data_str

def write_in_file(resault_str: str, filename: str):
    path_dir = r'1/resault/'
    file_path = Path(path_dir, filename)
    with open(file_path,'w', encoding="utf-8") as str_write:
        str_write.write(str(resault_str))

write_in_file(' '.join(list(filter(lambda el: not "абв" in el, recive_text_file('data.txt')))),'resault.txt')