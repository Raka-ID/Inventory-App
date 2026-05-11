from pathlib import Path
import FreeSimpleGUI as sg
import csv

def check_data_list():
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

def add_data_csv(heading, filepath):
    while True:
        layouts = [
                   [[sg.Text(i), sg.Input(key=i)] for i in heading],
                   [sg.Button('Submit', key='submit'), sg.Button('Cancel', key='cancel')]
                  ]
        window = sg.Window('Input your Data', layout=layouts)
        add_event, add_values = window.read()
        match add_event:
            case 'submit':
                conf_data = []
                for j in heading:
                    conf_data.append([sg.Text(f"{j}\t: {add_values[j]}", font=('Helvetica', 12))])
                conf_layout = [
                               conf_data,
                               [sg.Button('Yes', key='yes'), sg.Button('No', key='no')]
                              ]
                confirmation = sg.Window('Confirmation', layout = conf_layout)
                conf_event, conf_values = confirmation.read()
                match conf_event:
                    case 'yes':
                        new_data = list(add_values.values())
                        with open(Path('Data', filepath), 'a', newline="", encoding="utf-8-sig") as the_file:
                            writer = csv.writer(the_file, delimiter=";")
                            writer.writerow(new_data)
                        confirmation.close()
                        window.close()
                        break
                    case 'no':
                        confirmation.close()
                        window.close()
                        continue
            case 'cancel' | sg.WIN_CLOSED:
                window.close()
                break
    print(len(add_values.values()))
    return get_data(filepath)[1:]

def add_data_other(filepath):
    layouts = [
        [sg.Text('Please input your new data: ')],
        [sg.Input(key='new_data')],
        [sg.Button('Submit', key='submit'), sg.Button('Cancel', key='cancel')]
    ]
    window = sg.Window('Input new data', layout=layouts)

    add_event, add_values = window.read()
    match add_event:
        case 'submit':
            with open(Path('Data', filepath), 'a', newline="", encoding="utf-8-sig") as the_file:
                the_file.write(f'\n{values["new_data"]}')
            window.close()
        case 'cancel' | sg.WIN_CLOSED:
            window.close()
    return get_data(filepath)[1:]

# heading = ['satu', 'dua', 'tiga']
#
# print(add_data_csv(heading))

def del_data_csv(filepath, del_row):
    with open(Path('Data', filepath), 'r', newline="", encoding="utf-8-sig") as the_file:
        data = the_file.readlines()
        heading = data[0].strip().split(';')
        del_data = data[del_row+1].strip().split(';')

    while True:
        layout = [
            [sg.Text('Are you sure you want to delete this data?', font=('Helvetica', 14))],
            [sg.Column([[sg.Text(f'{i}\t: {j}', font=('Helvetica', 12))] for i, j in zip(heading, del_data)])],
            [sg.Button('Yes', key='Yes'), sg.Button('Cancel', key='Cancel')]
        ]
        window = sg.Window('Data Deletion Confirmation', layout=layout)
        event, values = window.read()
        match event:
            case 'Yes':
                del data[del_row+1]
                with open(Path('Data', filepath), 'w', newline="", encoding="utf-8-sig") as the_file:
                    the_file.writelines(data)
                window.close()
                break
            case 'Cancel' | sg.WIN_CLOSED:
                window.close()
                break
    return get_data(filepath)[1:]