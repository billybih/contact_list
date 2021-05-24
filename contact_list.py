import sqlite3
from tabulate import tabulate

con = sqlite3.connect('./contact_list.db')

c = con.cursor()

# c.execute("""CREATE TABLE contacts (
#             first_name text,
#             last_name text,
#             age integer,
#             address text,
#             phone_number text,
#             email text
#             )""")

def new_contact():
    first_name = input('Enter first_name')
    last_name = input('Enter last_name')
    age = input('Enter age')
    address = input('Enter address')
    phone_number = input('Enter phone number')
    email = input('Enter email')
    params = (first_name, last_name, age, address, phone_number, email)
    c.execute("INSERT INTO contacts VALUES (?, ?, ?, ?, ?, ?)", params)
    con.commit()

def delete_contact():
    first = input('Enter first_name ')
    last = input('Enter last_name ')
    print('')
    c.execute("DELETE FROM contacts WHERE first_name = ? AND last_name = ?", (first, last))
    con.commit()


def edit_contact():
    first = input('Enter first_name ')
    last = input('Enter last_name ')
    print('')
    infos = {'1': "first_name", '2': 'last_name', '3': 'age', '4': 'address', '5': 'phone_number', '6': 'email'}
    choice = str(input("""==> What do you want to edit:
press 1 - first name
press 2 - last name
press 3 - age
press 4 - address
press 5 - phone number
press 6 - email
"""))
    info2 = input("Enter {} ".format(infos[choice]))
    print('')
    c.execute('UPDATE contacts SET {} = ? WHERE {} = ? AND {} = ?'.format(infos[choice], infos['1'], infos['2']), (info2, first, last))
    con.commit()

def list_contacts():
    contacts_first = []
    for i in c.fetchall():
        contact = [x for x in i]
        contacts_first.append(contact)
    con.commit()
    print(tabulate(contacts_first, headers = ['First name', 'Last name', 'Age', 'Address', 'Phone number', 'email']))

def find():
    infos = {'1': "first_name", '2': 'last_name', '3': 'age', '4': 'address', '5': 'phone_number', '6': 'email', '7': 'full_name'}
    choice = str(input("""==> Search by:
first name - press 1
last name - press 2
age - press 3
address - press 4
phone number - press 5
email - press 6
full name - press 7
"""))
    if choice == '7':
        info2 = input('Enter full name ').split(' ')
        c.execute('SELECT * FROM contacts WHERE first_name = ? AND last_name = ?', (info2[0], info2[1]))
        list_contacts()
        return
    else:
        info2 = input("Enter {} ".format(infos[choice]))
        print('')
    c.execute('SELECT * FROM contacts WHERE {} = ?'.format(infos[choice]), (info2, ))
    list_contacts()

def initialize():
    choice = str(input("""==> What do you want to do?
new contact - press 1
delete contact - press 2
edit contact - press 3
list all contacts - press 4
find contact - press 5
exit - press 6
"""))
    if choice == '1':
        new_contact()
        print("Successfully added new contact!")
        print('')
    if choice == '2':
        delete_contact()
        print("Contact successfully deleted!")
        print('')
    if choice == '3':
        edit_contact()
        print("Contact successfully edited!")
        print('')
    if choice == '4':
        c.execute("SELECT * FROM contacts")
        list_contacts()
        print('')
    if choice == '5':
        find()
        print('')
    if choice == '6':
        con.close()
        exit()
    initialize()

initialize()
