from tkinter import*
from t_backend import Database

database = Database("track_data.db")

class Window(object):
	'''
	The Window class creates the Tkinter GUI window containing:
	Labels, Entries, Buttons and List Box to show datas from the database.

	Methods:
			__init__(self,window)
			view_command(self)
			search_command(self)
			insert_command(self)
			delete_command(self)
			update_command(self)
			get_selected_row(self,event)
	'''
	def __init__(self,window):
		'''
		Window Class Constractor to initialize the object
		'''
		self.window = window
		self.window.wm_title("Tracker")

		self.list_box = Listbox(window,heigh = 20,width = 50)
		self.list_box.grid(row = 3,column = 0,rowspan = 6,columnspan = 2)

		scr_bar = Scrollbar(window)
		scr_bar.grid(row = 3,column = 2,rowspan = 6 )

		self.list_box.configure(yscrollcommand = scr_bar.set)
		scr_bar.configure(command = self.list_box.yview)

		self.list_box.bind('<<ListboxSelect>>',self.get_selected_row)

		#DEFINE LABELS
		l1 = Label(window,text = "Date")
		l1.grid(row = 0,column = 0)

		l2 = Label(window,text = "Deep Work")
		l2.grid(row = 0,column = 2)

		l3 = Label(window,text = "Wake up")
		l3.grid(row = 1,column = 0)

		l4 = Label(window,text = "Workout")
		l4.grid(row = 1,column = 2)

		l5 = Label(window,text = "Bedtime")
		l5.grid(row = 2,column = 0)

		l6 = Label(window,text = "Sleep")
		l6.grid(row = 2,column = 2)

		#DEFINE BUTTONS
		b1 = Button(window, width=12, text = "Add Entry",command=self.insert_command)
		b1.grid(row=3,column=3)

		b2 = Button(window, width=12,text = "View All",command=self.view_command)
		b2.grid(row=4,column=3)

		b3 = Button(window, width=12, text = "Search Entry",command=self.search_command)
		b3.grid(row=5,column=3)

		b4 = Button(window, width=12, text = "Update",command=self.update_command)
		b4.grid(row=6,column=3)

		b5 = Button(window, width=12, text = "Delete",command=self.delete_command)
		b5.grid(row=7,column=3)

		#window.destroy parameter of the command argument automaticli ends the app
		b6 = Button(window, width=12, text = "Close",command=window.destroy)
		b6.grid(row = 8,column = 3)

		#DEFINE ENTRIES
		self.dt = StringVar()
		self.e1 = Entry(window,width = 12, textvariable = self.dt)
		self.e1.grid(row = 0,column = 1)

		self.work = StringVar()
		self.e2 = Entry(window,width = 6,textvariable = self.work)
		self.e2.grid(row = 0,column = 3)

		self.wake_up = StringVar()
		self.e3 = Entry(window,width = 12,textvariable = self.wake_up)
		self.e3.grid(row = 1,column = 1)

		self.training = StringVar()
		self.e4 = Entry(window,width = 6,textvariable = self.training)
		self.e4.grid(row = 1,column = 3)

		self.bedtime = StringVar()
		self.e5 = Entry(window,width = 12,textvariable = self.bedtime)
		self.e5.grid(row = 2,column = 1)

		self.sleep = StringVar()
		self.e6 = Entry(window,width = 6,textvariable = self.sleep)
		self.e6.grid(row = 2,column = 3)

	def get_selected_row(self,event):
		'''
		Function displays values in the entry windows when a user clicks on a row in the list box
		'''
		try:
			global selected_values
			index = self.list_box.curselection()[0]
			selected_values = self.list_box.get(index)

			self.e1.delete(0,END)
			self.e1.insert(END,selected_values[1])
			self.e2.delete(0,END)
			self.e2.insert(END,selected_values[2])
			self.e3.delete(0,END)
			self.e3.insert(END,selected_values[3])
			self.e4.delete(0,END)
			self.e4.insert(END,selected_values[4])
			self.e5.delete(0,END)
			self.e5.insert(END,selected_values[5])
			self.e6.delete(0,END)
			self.e6.insert(END,selected_values[6])
		except IndexError:
			pass

	def view_command(self):
		self.list_box.delete(0,END)
		for row in database.view_all():
			self.list_box.insert(END,row)

	def search_command(self):
		self.list_box.delete(0,END)
		for row in database.search(dt.get(),work.get(),wake_up.get(),training.get(),bedtime.get(),sleep.get()):
			self.list_box.insert(END,row)

	def insert_command(self):
		database.insert(self.dt.get(),self.work.get(),self.wake_up.get(),self.training.get(),self.bedtime.get(),self.sleep.get())
		self.list_box.delete(0,END)
		self.list_box.insert(END,(self.dt.get(),self.work.get(),self.wake_up.get(),self.training.get(),self.bedtime.get(),self.sleep.get()))
		self.view_command()

	def delete_command(self):
		database.delete(selected_values[0])
		self.view_command()

	def update_command(self):
		database.update(selected_values[0],self.dt.get(),self.work.get(),self.wake_up.get(),self.training.get(),self.bedtime.get(),self.sleep.get())
		self.view_command()

window = Tk()
Window(window)
window.mainloop()