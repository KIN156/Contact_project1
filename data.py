import sqlite3

db = sqlite3.connect('contact.db')
cur = db.cursor()
cur.execute('create table if not exists contacts(name text,phone text)')

def add_data():
	name = input("Enter the contact's name : ")
	phone_no = input("Enter the phone number : ")
	cur.execute('insert into contacts values(?,?)',(name,phone_no))
	print('Data insert successfully..')	
	
		
def delete_data():
	s = input('Write number or name to delete contact : ')
	if s == 'name':
		name_d = input("Enter the name to deleted from contacts : ")
		cur.execute('delete from contacts where name = (?)',(name_d,))
		print('Data delete successfully..')	
	elif s == 'number':
		p_n = input('Enter the phone number to deleted from contacts : ')
		cur.execute('delete from contacts where name = (?)',(name_d,))
		print('Data delete successfully..')	
	else:
		print('invalid choice..')
		
def view_data():
	cur.execute('select * from contacts')
	cts = cur.fetchall()
	print('contact List : ',cts)


def edit_data():
	s = input('Write phone number or name to edit contact : ')
	if s == 'name':
		n = input('Enter the name : ')
		p = input('Enter the phone number which is edited : ')
		cur.execute('update contacts set phone = (?) where name = (?)', (p, n))
		print('Data update successfully..')	
	elif s == 'number':
		n1 = input('Enter the phone number : ')
		p1 = input('Enter the name which is edited : ')
		cur.execute('update contacts set name = (?) where phone = (?)',(p1,n1))
		print('Data update successfully..')
	else:
		print('Update Failed')

		
def search():
	s = input('Write number or name to edit contact : ')
	if s == 'name':
		n = input('Enter the name : ')
		cur.execute('select * from contacts where name == (?)',(n,))
		cts = cur.fetchone()
		print('contact List : ',cts)
	elif s == 'number':
		n1 = input('Enter the phone number : ')
		cur.execute('select * from contacts where phone == (?)', (n1,))
		cts = cur.fetchone()
		print('contact List : ',cts)
	else:
		print('Invalid search...')



