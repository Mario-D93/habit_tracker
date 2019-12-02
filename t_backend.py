import sqlite3

class Database():
	'''
	The Database object contains functions to handle operations such as adding, 
	viewing, searching, updating, & deleting values from the sqlite3 database

	The object takes one argument: name of sqlite3 database

	Class is imported to the frontend script (t_fronted.py) 
	'''
	def __init__(self,db):
		'''
		Database Class Constractor to initialize the object and
		connect to the database if exists.
		IF not, new database will be created and will contain columns:
		id, work, wake_up, training, bedtime, sleep
		'''
		self.conn=sqlite3.connect(db)
		self.curs=self.conn.cursor()
		self.curs.execute("CREATE TABLE IF NOT EXISTS trackerdata(id INTEGER PRIMARY KEY, dt TEXT, work INTEGER, wake_up INTEGER,\
			training TEXT, bedtime INTEGER, sleep INTEGER)")
		self.conn.commit()

	def insert(self,dt,work,wake_up,training,bedtime,sleep):
		self.curs.execute("INSERT INTO trackerdata VALUES(NULL,?,?,?,?,?,?)",(dt,work,wake_up,training,bedtime,sleep))
		self.conn.commit()
		
	def view_all(self):
		self.curs.execute("SELECT * FROM trackerdata")
		view_all=self.curs.fetchall()
		return view_all

	def search(self,dt="",work="",wake_up="",training="",bedtime="",sleep=""):
		self.curs.execute("SELECT * FROM trackerdata WHERE dt=? OR work=? OR wake_up=? OR training=? OR bedtime=? OR sleep=?",\
			(dt,work,wake_up,training,bedtime,sleep))
		view_all=self.curs.fetchall()
		return view_all

	def delete(self,id):
		self.curs.execute("DELETE FROM trackerdata WHERE id=?",(id,))
		self.conn.commit()
		
	def update(self,id,dt,work,wake_up,training,bedtime,sleep):
		self.curs.execute("UPDATE trackerdata SET dt=?,work=?,wake_up=?,\
			training=?,bedtime=?,sleep=? WHERE id=?",(dt,work,wake_up,\
				training,bedtime,sleep,id))
		self.conn.commit()
		
	def __del__(self):
		#function closes the connection with the sqlite3 database
		self.conn.close()