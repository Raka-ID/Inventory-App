from pathlib import Path
import csv

def check_data():
    filepath = Path(r'Data')
    datas = []
    for file in filepath.iterdir():
        if file.is_file():
            datas.append(file.name)
    return datas

def get_data(filepath):
    with open(Path('Data', filepath),  newline="", encoding="utf-8-sig") as the_file:
        reader = csv.reader(the_file, delimiter=";")
        data = list(reader)
    return data