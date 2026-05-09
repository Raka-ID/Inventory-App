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
                    conf_data.append([sg.Text(f"{j}: {add_values[j]}", font=('Helvetica', 12))])
                conf_layout = [
                               conf_data,
                               [sg.Button('Yes', key='yes'), sg.Button('No', key='no')]
                              ]
                confirmation = sg.Window('Confirmation', layout = conf_layout)
                conf_event, conf_values = confirmation.read()
                match conf_event:
                    case 'yes':
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
    new_data = list(add_values.values())
    with open(Path('Data', filepath), 'a', newline="", encoding="utf-8-sig") as the_file:
        writer = csv.writer(the_file, delimiter=";")
        writer.writerow(new_data)
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
                the_file.write(window['new_data'] + '\n')
        case 'cancel' | sg.WIN_CLOSED:
            window.close()
    return get_data(filepath)[1:]


# headinga = ['satu', 'dua', 'tiga']
#
# print(add_data_csv(headinga))