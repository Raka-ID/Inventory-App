import FreeSimpleGUI as sg
import Function as fc
import csv

# Login Menu UI component
pass_label      = sg.Text('Enter the password: ')
inp_pass        = sg.Input(password_char="*", key="pass")
enter_button    = sg.Button('Enter', key='enter_button')
exit_app1       = sg.Button('Exit', key='exit_app')
password        = 'aaa' # Initial Password

login_layout    = [
                   [pass_label],
                   [inp_pass],
                   [enter_button, exit_app1]
                  ]

login_menu      = sg.Window("Login Section", layout=login_layout)

#-----------------------------------------------------------------------------------------------------------------------
# Main Menu UI Window
def main_menu():
    # Main Menu Components
    file_lists = fc.check_data_list()
    list_box = sg.Listbox(values=file_lists, key='sel_file', enable_events=True, size=(50, 10))
    sel_file_button = sg.Button('Select Data', key='sel_button')
    chg_pass_button = sg.Button('Change Password', key='chg_pass')
    exit_mm = sg.Button('Exit', key='exit_mm')

    # Main Menu Layout
    mm_layout = [
        [sg.Text('Select Data')],
        [list_box, sg.Column([[sel_file_button], [chg_pass_button], [exit_mm]])]
    ]

    return sg.Window('Main Menu', layout=mm_layout)

#-----------------------------------------------------------------------------------------------------------------------
# Inventory-App UI Window
def inventory_app(data):
    buttons_argument = [('Add', 'add', 'Add new data'),
                        ('Edit', 'edit', 'Please click the cell you want to edit'),
                        ('Complete', 'comp', 'Store and Delete Data From Table'),
                        ('Delete', 'delete', 'Delete data(row) permanently'),
                        ('Back', 'back', 'Back to main menu'),
                        ('Exit', 'exit', 'Exit application')]

              # List Comprehension for Buttons
    buttons = [[sg.Button(i, key=j, font=('Helvetica', 12), size=(10, 1), tooltip=k)] for i, j, k in buttons_argument]

    table = sg.Table(values=data[1:], headings=data[0], enable_click_events=True, num_rows=15, font=('Helvetica', 12),
                     key='the_table')
    layout = [
        [sg.Text(values["sel_file"][0].strip(".csv").replace("_", " ").title(),
                 font=('Helvetica', 15),
                 expand_x=True,
                 justification='center')],
        [table, sg.Column(buttons)]
    ]
    return sg.Window('Inventory App', layout)

#=======================================================================================================================
# THE MAIN CODE

# Login Menu / Password Checker
while True:
    event_login, values_login = login_menu.read()
    match event_login:
        case 'exit_app' | sg.WIN_CLOSED:
            break
        case 'enter_button':
            if values_login['pass'] == password:
                break
            else:
                sg.popup('Password is incorrect!')
login_menu.close()

window = main_menu()

while values_login['pass'] == password and event_login != 'exit_app':
    event, values = window.read()
    print(f'{event}, and {values}') # Delete this after Finished
    match event:

    # Main Menu
        case 'sel_button':
            try:
                data = fc.get_data(values['sel_file'][0])  # What if the data is not csv
                heading = data[0]
                filepath = values['sel_file'][0]
            except IndexError:
                sg.popup('Select data first!')
                continue

            window.close()
            window = inventory_app(data)

        # Change Password Menu
        case 'chg_pass':
            continue

        # Exit from Main Menu
        case 'exit_mm' | sg.WIN_CLOSED:
            sg.popup_timed('Bye!', auto_close_duration=0.5)
            exit()

# -----------------------------------------------------------------------------------------------------------------------
    # Inventory App
        case 'add':
            if filepath.endswith(".csv"):
                user_add_input = fc.add_data_csv(heading, filepath)
                window['the_table'].update(values=user_add_input)
            else:
                user_add_input = fc.add_data_other(filepath)
                window['the_table'].update(values=user_add_input)
        case 'edit':
            continue
        case 'comp':
            continue
        case 'delete':
            try:
                if filepath.endswith(".csv"):
                    user_del = fc.del_data_csv(filepath, del_row=values['the_table'][0])
                    window['the_table'].update(values=user_del)
            except IndexError:
                sg.popup('Select data first!')
        case 'back':
            window.close()
            window = main_menu()
        case 'exit' | sg.WIN_CLOSED:
            sg.popup_timed('Bye!', auto_close_duration=0.5)
            exit()