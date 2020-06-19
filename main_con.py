import sqlite3

from project_contact import data

db = sqlite3.connect('contact.db')

def con_main():
	ch = ''
	while ch != 0:
		ch = int(input('0..for Exit\n1..for Add\n2..for Delete\n3..for View\n4..for Edit\n5..for Search......:'))
		if ch == 1:
			data.add_data()
		elif ch == 2:
			data.delete_data()
		elif ch == 3:
			data.view_data()
		elif ch == 4:
			data.edit_data()
		elif ch == 5:
			data.search()
		elif ch == 0:
			print('Thank you for visite..')
		else:
			print('choice is invalid')

con_main()
db.commit()
db.close()
