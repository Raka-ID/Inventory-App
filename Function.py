from pathlib import Path

def check_data():
    filepath = Path(r'Data')
    datas = []
    for file in filepath.iterdir():
        if file.is_file():
            datas.append(file.name)
    return datas
