#Tool zum Scannen von Servern und deren Verzeichnis um alte Daten zu finden die z.b. weg können oder lange nicht genutzt worden sind#
import os
import pandas as pd
import time

input_path = input("Gebe deinen Pfad ein:")
check_path = os.path.exists(input_path)

while check_path is False:
    input_path = input("Pfad exestiert nicht. Bitte versuche es erneut.")

Start_Path = input_path


def get_Path(Start_Path):
    Path = []
    for file in os.listdir(Start_Path):
        file_path = os.path.join(Start_Path,file)
        Path.append(file_path)

    return Path

def get_Time(Full_Path):
    Time = []
    for file in Full_Path:
        get_time_code = os.path.getmtime(file)
        get_time = time.ctime(get_time_code)
        Time.append(get_time)

    return Time

def get_Size(Full_Path):
    Size_Byte = []
    for file in Full_Path:
        get_Size = os.path.getsize(file)
        Size_Byte.append(get_Size)

    return Size_Byte

def convert_bytes(Full_Size_in_Byte):
    converted_list = []
    for size in Full_Size_in_Byte:
        for unit in ['bytes', 'KB', 'MB', 'GB', 'TB']:
            if size < 1024:
                converted_list.append(f"{size:.1f} {unit}")
                break
            size /= 1024
    return converted_list

def concat_data(Full_Path, Full_Time, Full_Size):
    Data_Concat = {
        "Path" : Full_Path,
        "Time" : Full_Time,
        "Size" : Full_Size
    }

    return Data_Concat

def write_excel(Data_Concat):
    excel = pd.DataFrame(Data_Concat)
    excel.to_excel("new.xlsx", index = False)

Full_Path = get_Path(Start_Path)
Full_Time = get_Time(Full_Path)
Full_Size_in_Byte = get_Size(Full_Path)
Convert_Size = convert_bytes(Full_Size_in_Byte)
Data_Concat = concat_data(Full_Path, Full_Time, Convert_Size)
result_excel = write_excel(Data_Concat)