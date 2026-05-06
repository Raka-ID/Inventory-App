import FreeSimpleGUI as sg
import Function as fc

# Login Menu UI component
pass_lable = sg.Text('Enter the password: ')
inp_pass = sg.Input(password_char="*", key="pass")
pass_button = sg.Button('Enter', key='pass_button')
exit_app1 = sg.Button('Exit', key='exit_app')

password = 'aaa' # Initial Password
login_layout = [[pass_lable], [inp_pass], [[pass_button, exit_app1]]]
login_menu = sg.Window("Login Section", layout=login_layout)
#-----------------------------------------------------------------------------------------------------------------------
# Main Menu UI component
file_lists = fc.check_data()
list_box = sg.Listbox(values=file_lists, key='selected_file', enable_events=True, size=(50, 10))
sel_file_button = sg.Button('Select Data', key='sel_file')
chg_pass_button = sg.Button('Change Password', key='chg_pass')
exit_app2 = sg.Button('Exit', key='exit_app2')

mm_layout = [
    [sg.Text('Select Data')],
    [
        list_box,
        sg.Column([
            [sel_file_button],
            [chg_pass_button],
            [exit_app2]
        ])
    ]
]
main_menu = sg.Window('Main Menu', layout=mm_layout, resizable=True)
#-----------------------------------------------------------------------------------------------------------------------
# Inventory-App UI component
the_title = sg.Text('Inventory-App', font=('Helvetica', 25), justification='center')
# the_table = sg.Table(values=fc.get_data(values_mm['selected_file'][0], auto_size_columns=True))

# Button
add_button = sg.Button('Add', font=('Helvetica', 15), size=(10, 1), key='add')
edit_button = sg.Button('Edit', font=('Helvetica', 15), size=(10, 1), key='edit')
sold_button = sg.Button('Sold', font=('Helvetica', 15), size=(10, 1), key='sold')
delete_button = sg.Button('Delete', font=('Helvetica', 15), size=(10, 1), key='delete')
exit_button = sg.Button('Exit', font=('Helvetica', 15), size=(10, 1), key='exit')

# layout = [[the_title],
#            [the_table, [[add_button], [edit_button], [sold_button], [delete_button]]],
#            [exit_button]]
#=======================================================================================================================
# The Main Code

# Password Checker
while True:
    event_pass, values_pass = login_menu.read()
    print(f'{event_pass}, and {values_pass}') # Delete this when finished
    match event_pass:
        case 'exit_app':
            sg.popup_timed('Bye!', auto_close_duration = 0.5)
            break

    # Main Menu
    if values_pass['pass'] == password:
        login_menu.close()
        while True:
            event_mm, values_mm = main_menu.read()
            print(f'{event_mm}, and {values_mm}') # Delete this after Finished
            match event_mm:
                case 'sel_file':
                    data = fc.get_data(values_mm['selected_file'][0])
                    print(data)
                    table = sg.Window(f'{values_mm['selected_file'][0].strip(".csv")}',
                                      layout= [[sg.Text(values_mm['selected_file'][0].strip('.csv').replace('_', ' '),
                                               font=('Helvetica', 22))],
                                              [sg.Table(values=data[1:],
                                                        auto_size_columns=True,
                                                        headings=data[0],
                                                        key="table",
                                                        enable_events=True,
                                                        expand_x=True,
                                                        expand_y=True),
                                               sg.Column([[add_button],
                                                          [edit_button],
                                                          [sold_button],
                                                          [delete_button],
                                                          [exit_button]
                                                         ])
                                               ]
                                             ]
                                     )
                    event_data, values_data = table.read()
                    print(event_data, values_data)
                case 'chg_pass':
                    continue
                case 'exit_app2':
                    sg.popup_timed('Bye!', auto_close_duration=0.5)
                    exit()

    else:
        sg.popup_error('Password is incorrect!')


# File Opener


# Menu Title


# Layouts


# window = sg.Window('Inventory-App', layout_menu)

# while True:
#     event_menu, values_menu = window.read()