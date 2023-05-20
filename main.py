#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Main file for the project
"""

from utils import get_folder_content, to_path
from constants import folder_structure


file_path = input('Enter the path of the file: ')

all_datas = get_folder_content(file_path)

for file in all_datas:
    file.glob('*.mp4')
    if file.is_file():
        for folder, extensions in folder_structure.items():
            if file.suffix[1:] in extensions:
                to_path(file_path + "/" + folder).mkdir(exist_ok=True)
                print(f"Moving {file.name} to {folder}")
                file.rename(file_path + "/" + folder + "/" + file.name)
                break

            else:
                to_path(file_path + "/others").mkdir(exist_ok=True)
                print(f"Moving {file.name} to others")
                file.rename(file_path + "/others/" + file.name)
                break
    else:
        print(f"{file.name} is a folder")
