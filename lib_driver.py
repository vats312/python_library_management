from library_master import library
import os
lib=library("marwadi")
cl= lambda : os.system("clear")
code=0
cl()
while code!=7:
	print(lib)
	print("""\noptions
\n1.show books 2.add book 3.show users 
4.add user 5.issue book 6.return book 
7.exit""")
	code=int(input("enter choice"))	
	if(code==1):
		cl()
		lib.show_books()
	elif(code==2):
		cl()
		lib.add_book()
	elif(code==3):
		cl()
		lib.show_users()
	elif(code==4):
		cl()
		lib.add_user()
	elif(code==5):
		cl()
		lib.issue_book()	
	elif(code==6):
		cl()
		lib.return_book()
	elif(code==7):
		break
	

