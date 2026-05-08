import FreeSimpleGUI as sg
import Function as fc

# Login Menu UI component
pass_lable  = sg.Text('Enter the password: ')
inp_pass    = sg.Input(password_char="*", key="pass")
pass_button = sg.Button('Enter', key='pass_button')
exit_app1   = sg.Button('Exit', key='exit_app')

password        = 'aaa' # Initial Password
login_layout    = [[pass_lable], [inp_pass], [[pass_button, exit_app1]]]
login_menu      = sg.Window("Login Section", layout=login_layout)
#-----------------------------------------------------------------------------------------------------------------------
# Main Menu UI component
file_lists      = fc.check_data()
list_box        = sg.Listbox(values=file_lists, key='sel_file', enable_events=True, size=(50, 10))
sel_file_button = sg.Button('Select Data', key='sel_button')
chg_pass_button = sg.Button('Change Password', key='chg_pass')
exit_app2       = sg.Button('Exit', key='exit_app2')

mm_layout = [[sg.Text('Select Data')], [list_box, sg.Column([[sel_file_button],
                                                             [chg_pass_button],
                                                             [exit_app2]
                                                            ])
            ]]
main_menu = sg.Window('Main Menu', layout=mm_layout, resizable=True)
#-----------------------------------------------------------------------------------------------------------------------
# Inventory-App UI component
buttons = [[sg.Button(texts, key=keys, font=('Helvetica', 12), size=(10, 1))] for texts, keys in [('Add', 'add'),
                                                                                                  ('Edit', 'edit'),
                                                                                                  ('Sold', 'sold'),
                                                                                                  ('Delete', 'delete'),
                                                                                                  ('Exit', 'exit')]
          ]
print(buttons)
#=======================================================================================================================
# The Main Code

# Login  Menu / Password Checker
while True:
    event_login, values_login = login_menu.read()
    print(f'{event_login}, and {values_login}')  # Delete this when finished
    match event_login:
        case 'exit_app' | sg.WIN_CLOSED:
            print(f'{event_login}, and {values_login}') # Delete this when finished
            break
        case 'pass_button':
            if values_login['pass'] == password:
                break
            else:
                sg.popup('Password is incorrect!')
login_menu.close()

# Main Menu
while values_login['pass'] == password and event_login != 'exit_app':
    event_mm, values_mm = main_menu.read()
    print(f'{event_mm}, and {values_mm}') # Delete this after Finished
    match event_mm:
        # Change Password Menu
        case 'chg_pass':
            continue

        # Exit the App
        case 'exit_app2':
            sg.popup_timed('Bye!', auto_close_duration=0.5)
            exit()

        case 'sel_button':
            # main_menu.close()
            data = fc.get_data(values_mm['sel_file'][0])
            table = sg.Window(title = f'{values_mm['sel_file'][0].strip(".csv")}',
                              layout = [[sg.Text(values_mm['sel_file'][0].strip('.csv').replace('_', ' '),
                                         font=('Helvetica', 22))],
                                        [sg.Table(values=data[1:], auto_size_columns=True,
                                                  headings=data[0], key="table", enable_events=True,
                                                  expand_x=True, expand_y=True
                                                 ),
                                         sg.Column(buttons)
                                        ]
                                       ]
                             )
            event_data, values_data = table.read()
            print(event_data, values_data)
            match event_data:
                case 'add':
                    continue
                case 'edit':
                    continue
                case 'sold':
                    continue
                case 'delete':
                    continue
                case 'exit':
                    continue