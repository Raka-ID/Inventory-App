import FreeSimpleGUI as sg
import Function as fc

# Login Menu UI component
pass_label   = sg.Text('Enter the password: ')
inp_pass     = sg.Input(password_char="*", key="pass")
pass_button  = sg.Button('Enter', key='pass_button')
exit_app1    = sg.Button('Exit', key='exit_app')
password     = 'aaa' # Initial Password

#-----------------------------------------------------------------------------------------------------------------------
# Main Menu UI component
file_lists      = fc.check_data()
list_box        = sg.Listbox(values=file_lists, key='sel_file', enable_events=True, size=(50, 10))
sel_file_button = sg.Button('Select Data', key='sel_button')
chg_pass_button = sg.Button('Change Password', key='chg_pass')
exit_app2       = sg.Button('Exit', key='exit_app2')

#-----------------------------------------------------------------------------------------------------------------------
# Inventory-App UI component
buttons = [[sg.Button(texts, key=keys, font=('Helvetica', 12), size=(10, 1))] for texts, keys in [('Add',     'add'),
                                                                                                  ('Edit',    'edit'),
                                                                                                  ('Complete','comp'),
                                                                                                  ('Delete',  'delete'),
                                                                                                  ('Back',    'back'),
                                                                                                  ('Exit',    'exit')]
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
main_menu  = sg.Window('Main Menu', layout=layouts, resizable=True)

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
                data = fc.get_data(values['sel_file'][0])
                table = sg.Table(values=data[1:],
                                 headings=data[0],
                                 enable_click_events=True,
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
                                         [table]
                                        ]
                                       )
                match event:
                    case 'add':
                        print(event, values)
                    case 'edit':
                        continue
                    case 'comp':
                        continue
                    case 'delete':
                        continue
                    case 'exit':
                        continue
            except IndexError:
                sg.popup('Select data first!')