import FreeSimpleGUI as sg

# Pass Menu
pass_lable = sg.Text('Enter the password: ')
inp_pass = sg.Input(password_char="*", key="pass")
pass_button = sg.Button('Enter', key='pass_button')
exit_app = sg.Button('Exit', key='exit_app')

pass_layout = [[pass_lable], [inp_pass], [[pass_button, exit_app]]]

#Initial Password
password = 'Inventory001'

# Password Menu
pass_menu = sg.Window("Login Section", layout=pass_layout)

# Password Checker
while True:
    event_pass, values_pass = pass_menu.read()
    print(f'{event_pass}, and {values_pass}')
    match event_pass:
        case 'exit_app':
            sg.popup_timed('Bye!', )
            break
    if values_pass['pass'] == password:
        print('Password match!')
    else:
        sg.popup_ok('Password is incorrect!')


# File Opener


# Menu Title
the_title = sg.Text('Inventory-App', font=('Helvetica', 25), justification='center')

# the_table = sg.Table(value=, auto_size_columns=True)

# Button
add_button = sg.Button('Add', font=('Helvetica', 15), size=(10, 1), key='add')
edit_button = sg.Button('Edit', font=('Helvetica', 15), size=(10, 1), key='edit')
sold_button = sg.Button('Sold', font=('Helvetica', 15), size=(10, 1), key='sold')
delete_button = sg.Button('Delete', font=('Helvetica', 15), size=(10, 1), key='delete')
exit_button = sg.Button('Exit', font=('Helvetica', 15), size=(10, 1), key='exit')

# Layouts
layout_menu = []

# layout = [[the_title],
#            [the_table, [[add_button], [edit_button], [sold_button], [delete_button]]],
#            [exit_button]]

# window = sg.Window('Inventory-App', layout_menu)

# while True:
#     event_menu, values_menu = window.read()