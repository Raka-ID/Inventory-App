import FreeSimpleGUI as sg
import Function as fc
import csv

# Login Menu UI component
pass_label   = sg.Text('Enter the password: ')
inp_pass     = sg.Input(password_char="*", key="pass")
pass_button  = sg.Button('Enter', key='pass_button')
exit_app1    = sg.Button('Exit', key='exit_app')
password     = 'aaa' # Initial Password

#-----------------------------------------------------------------------------------------------------------------------
# Main Menu UI component
file_lists      = fc.check_data_list()
list_box        = sg.Listbox(values=file_lists, key='sel_file', enable_events=True, size=(50, 10))
sel_file_button = sg.Button('Select Data', key='sel_button')
chg_pass_button = sg.Button('Change Password', key='chg_pass')
exit_app2       = sg.Button('Exit', key='exit_app2')

#-----------------------------------------------------------------------------------------------------------------------
# Inventory-App UI component
buttons = [
    [sg.Button(texts, key=keys, font=('Helvetica', 12), size=(10, 1), tooltip=tt)] for texts, keys, tt in
        [('Add',      'add',    'Add new data'),
         ('Edit',     'edit',   'Please click the cell you want to edit'),
         ('Complete', 'comp',   'Store and Delete Data From Table'),
         ('Delete',   'delete', 'Delete data(row) permanently'),
         ('Back',     'back',   'Back to main menu'),
         ('Exit',     'exit',   'Exit application')]
] # List Comprehension

#-----------------------------------------------------------------------------------------------------------------------
# Layouts
login_layout    = [
                   [pass_label],
                   [inp_pass],
                   [pass_button, exit_app1]
                  ]

mm_layout       = [
                   [sg.Text('Select Data')],
                   [list_box, sg.Column([[sel_file_button], [chg_pass_button], [exit_app2]])]
                  ]

data_layout     = [
                   [sg.Column([[]], key='table_col')]
                  ]

layouts         = [[
                    sg.Column(mm_layout, key='mm_lay'),
                    sg.Column(data_layout, key='data_lay', visible=False)
                  ]]

# GUI Windows
login_menu = sg.Window("Login Section", layout=login_layout)
main_menu  = sg.Window('Inventory App', layout=layouts, resizable=True)

#=======================================================================================================================
# THE MAIN CODE

# Login Menu / Password Checker
while True:
    event_login, values_login = login_menu.read()
    match event_login:
        case 'exit_app' | sg.WIN_CLOSED:
            break
        case 'pass_button':
            if values_login['pass'] == password:
                break
            else:
                sg.popup('Password is incorrect!')
login_menu.close()

# Main Menu
while values_login['pass'] == password and event_login != 'exit_app':
    event, values = main_menu.read()
    print(f'{event}, and {values}') # Delete this after Finished
    # event_slicing = event[1]

    match event:
        # Change Password Menu
        case 'chg_pass':
            continue

        # Exit the App
        case 'exit_app2' | sg.WIN_CLOSED:
            sg.popup_timed('Bye!', auto_close_duration=0.5)
            exit()

        case 'sel_button':
            try:
                data = fc.get_data(values['sel_file'][0]) # What if the data is nott csv
                heading = data[0]
                table = sg.Table(values=data[1:],
                                 headings=heading,
                                 enable_events=True,
                                 enable_click_events=True,
                                 num_rows=15,
                                 font=('Helvetica', 12),
                                 key='nt')
                main_menu['mm_lay'].update(visible=False)
                main_menu['data_lay'].update(visible=True)
                main_menu.extend_layout(main_menu['data_lay'],
                                        [
                                         [sg.Text(values["sel_file"][0].strip(".csv").replace("_", " ").title(),
                                                  font=('Helvetica', 15),
                                                  expand_x=True,
                                                  justification='center')],
                                         [table, sg.Column(buttons)]
                                        ]
                                       )
            except IndexError:
                sg.popup('Select data first!')

        case 'add':
            if values['sel_file'][0].endswith(".csv"):
                user_add_input = fc.add_data_csv(heading=heading, filepath=values['sel_file'][0])
                main_menu['nt'].update(values=user_add_input)
            else:
                user_add_input = fc.add_data_other(filepath=values['sel_file'][0])
                main_menu['nt'].update(values=user_add_input)
        case 'edit':
            continue
        case 'comp':
            continue
        case 'delete':
            try:
                # print(values['nt'][0])  # Delete this if you have finished
                if values['sel_file'][0].endswith(".csv"):
                    user_del = fc.del_data_csv(filepath=values['sel_file'][0], del_row=values['nt'][0])
                    main_menu['nt'].update(values=user_del)
            except IndexError:
                sg.popup('Select data first!')
        case 'exit' | sg.WIN_CLOSED:
            sg.popup_timed('Bye!', auto_close_duration=0.5)
            exit()