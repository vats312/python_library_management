import os
class library(object):
	#initialized lists
	books=[{"name":"book1","isavailable":1},{"name":"book2","isavailable":1}]
	issued_books=[{"user":"vatsal","book":"book1"},{"user":"vatsal","book":"book2"},{"user":"mihir","book":"book1"},{"user":"mihir","book":"book2"},{"user":"mihir","book":"book3"}]
	users=[{"name":"vatsal","id":1,"issued":2},{"name":"mihir","id":2,"issued":3}]	
	
	#for setting the library name	
	def __init__(self,name):
		self.name=name

	#return print
	def __str__(self):
		return "WELCOME TO %s"%(self.name)

	#shows books in library
	def show_books(self):
		print('list of available books is below')
		for book in self.books:
			if book["isavailable"]==1:
				print(book["name"]) 

	#to add book in library	
	def add_book(self):
		book=dict()
		book.update(name=input("enter books name"),isavailable=1)
		self.books.append(book)	

	#add users in library	
	def add_user(self):
		user=dict()
		user.update(name=input("enter users name"),id=input("enter id"),issued=0)
		self.users.append(user)

	#show users list	
	def show_users(self):
		print("list of users")
		for user in self.users:
			print("name:- %s issued books %d"%(user["name"],user["issued"]))

	#issue book to user	
	def issue_book(self):
		self.show_books()
		b=input("book issue console\nenter name of book: ")
		self.show_users()
		u=input("enter users name: ")
		for book in self.books:
			if book["name"]==b and book["isavailable"]==1:
				print("\nissueing %s"%(book["name"]))				
				book["isavailable"]=0
		for user in self.users:
			if user["name"]==u:
				print("to %s"%(user["name"]))
				user["issued"]=user["issued"]+1
		issued_book=dict()
		issued_book.update(user=u,book=b)
		self.issued_books.append(issued_book) 

	#return book to library
	def return_book(self):
		u=input("enter the name of user")
		for book in self.issued_books:
			if(book["user"]==u):
				print(book["book"]) 
		b=input("enter book you want to return")
		for book in self.issued_books:
			if(book["user"]==u and book["book"]==b):
				b=dict()
				b.update(name=book["book"],isavailable=1)
				self.books.append(b)
			for user in self.users:
				if(user["name"]==u):
					user["issued"]=user["issued"]-1
		print("book returned sucessfully")
