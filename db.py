'''
Dean Brennan
R00179510
dean.brennan1@mycit.ie

'''
import math
import sqlite3


atomNum = "atomNum"
atomNumTab = 11
atomWeight = "atomWeight"
atomWeightTab = 14
name = "name"
nameTab = 24
symbol = "symbol"
symbolTab = 8
appearance = "appearance"
appearanceTab = 54


db = sqlite3.connect("elements.db")
cursor = db.cursor()

def viewAllData():
	cursor.execute('''
		SELECT * from elements
		''')
	allData = cursor.fetchall()
	for data in allData:
		##Column Num
		print(type(str(data[0]))
			+str(data[1])
			+str(data[2])
			+str(data[3])
			+str(data[4]))
	input("\n\nAny Key to return to menu")
	menuSelect()

def viewSpec():
	# while True:
		# try:
	chosenAtomNum = int(input("What is the atomic number?>> "))
	cursor.execute('''
		SELECT * FROM elements WHERE atomNum = ?
		''',(chosenAtomNum))
	allData = cursor.fetchall()
	for data in allData:
		print(data[0],data[1],data[2],data[3],data[4])
	menuSelect()
		# except:
		# 	print("Invalid input, try again\n")
		# 	pass

def queery():
	#as
	print("")

def menuSelect():
	selectLoop = True
	while selectLoop:
		selectLoop = False
		selection = int(input("Please select an option:\n"
			"1) View all data\n"
			"2) View specific element\n"
			"3) Query by data\n"
			"4) Add new data\n"
			"5) Modify existing data\n"
			"6) Exit\n>>>>\t"))
		if selection == 1:
			viewAllData()
		elif selection == 2:
			viewSpec()
		elif selection ==3:
			queery()
		elif selection == 4:
			addNew()
		elif selection == 5:
			modify()
		elif selection == 6:
			return True


def main():
	print("#"*20+"\nElements Database\n"+"#"*20+"\n")
	saveChoice = menuSelect()
	if saveChoice == True:
		db.commit()
	else:
		pass
	db = sqlite3.connect("elements.db")
	cursor = db.cursor()
if __name__ == '__main__':
	main()
