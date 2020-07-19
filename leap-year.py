from tkinter import Tk
from tkinter import Entry
from tkinter import Button
from tkinter import Label 
from tkinter import messagebox

root = Tk()
root.configure(bg="#f0f0f0")
root.title('Leap Year Checker')
root.geometry('200x200')

def validate_as_int():
	'''
	Checks if the input is a integer
	and calls the display_result() function.
	Warning is shown if input is not a integer.  

	'''
	try:
		year = int(entry_box.get())
		display_result(year)
	except ValueError:
		messagebox.showwarning('Warning','Please Enter a Integer')
		entry_box.delete(0,'end')

def check_leap_year(year):
	"""
	Checks if the year is a leap year or not
	Input: year (int)
	Output: Return True if year is a leap year
			or return False.
	"""
	if (year % 400) == 0:
		return True
	elif (year % 100) == 0:
		return False
	elif (year % 4) == 0 : 
		return True
	else :
		return False 
		

def display_result(year):
	if check_leap_year(year):
		lbl_display['text'] = ' Year {} : Leap Year'.format(year)
	else:
		lbl_display['text'] = 'Year {} : Not a Leap Year'.format(year)
	entry_box.delete(0,'end')

def on_return(event):
	validate_as_int()

def  bye():
	'''
	Closes the application.
	'''
	msg = messagebox.askyesno('Confirm Exit','Do you want to leave?')
	if msg:
		root.destroy()

#setup
lbl_title = Label(root,text='Leap Year Checker',bg='White')
lbl_title.pack(pady=5)

lbl_display = Label(root,text='',bg='white')
lbl_display.pack(pady=5)

entry_box = Entry(root,width = 15)
entry_box.bind('<Return>',on_return)
entry_box.pack(pady=5)

enter_button = Button(root, text ='Enter',fg='blue',command=validate_as_int)
enter_button.pack(pady=5)

exit_button = Button(root,text = 'Exit',fg='red',command=bye)
exit_button.pack(pady=5)

root.mainloop()