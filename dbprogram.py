'''
Dean Brennan
R00179510
dean.brennan1@mycit.ie
'''

import sqlite3
db = sqlite3.connect("dbOfElements.db")
cursor = db.cursor()

def modify():
	changeVars = ["atomWeight", "name", "symbol", "appearance"]
	chosenAtomNum = input("What is the atomic number?\n>>> ")
	#Print the data for that atomic number for reference to change
	cursor.execute('''
	SELECT * FROM periodicTable WHERE atomNum = ?
	''',(chosenAtomNum))
	elementsData= cursor.fetchall()
	for alldata in elementsData:
		print(alldata[0],alldata[1],alldata[2],alldata[3],alldata[4])
	choiceLoop = True
	#Loop to stay in menu untill user inputs are valid
	while choiceLoop:
		choiceLoop = False
		try:
			chosenChange = int(input("What would you like to modify?:\n"
				"1) Atomic weight\n"
				"2) Name\n"
				"3) Symbol\n"
				"4) Appearance\n>>> "))
			#setting old and new values for change
			oldVar = alldata[chosenChange]
			change = input("What would you like to change it to?:\t")
			#Changes the said value by the input
			#Could not automate a change - in document
			if chosenChange == 1:
				cursor.execute(''' 
					UPDATE periodicTable 
					SET atomWeight = ? 
					WHERE atomWeight = ?;
					''',(change,oldVar))
			elif chosenChange ==2:
				cursor.execute(''' 
					UPDATE periodicTable 
					SET name = ? 
					WHERE name = ?;
					''',(change,oldVar))
			elif chosenChange == 3:
				cursor.execute(''' 
					UPDATE periodicTable 
					SET symbol = ? 
					WHERE symbol = ?;
					''',(change,oldVar))
			elif chosenChange ==4:
				cursor.execute(''' 
					UPDATE periodicTable 
					SET appearance = ? 
					WHERE appearance = ?;
					''',(change,oldVar))
		except:
			print("Invalid input, Try again")
			choiceLoop = True
	menuSelect()

def addNew():
	print("Adding new element")
	atomNumCheckLoop = True
	while atomNumCheckLoop:
		atomNumCheckLoop = False
		#Checking users input against the data in db to see if num is already in use
		newAtomNum = input("What is the atomic number?:\t")
		dList = []
		cursor.execute('''
			SELECT atomNum FROM periodicTable
			''')
		data = cursor.fetchall()
		for data in data:
			for data in data:
				dList+= str(data)
		if newAtomNum in dList:
			print("\nAtomic Number already in use\n")
			atomNumCheckLoop = True
		else:
			newAtomWeight = input("What is the atomic weight?:\t")
			newName = input("What is the elements name?:\t")
			newSymbol = input("What is the symbol?:\t")
			newAppearance = input("Appearance of element (MAX 50 CHAR):\t")
			#All data in SQLITE needs to be a touple
			newElement = tuple([(newAtomNum),(newAtomWeight),(newName),(newSymbol),(newAppearance)])
			cursor.execute('''
			INSERT INTO periodicTable(atomNum, atomWeight, name, symbol, appearance)
			VALUES(?,?,?,?,?) ''',newElement)
			menuSelect()

def viewSpec():
	#Viewing the specific data by the atomic number
	chosenAtomNum = input("What is the atomic number?\n>>> ")
	cursor.execute('''
	SELECT * FROM periodicTable WHERE atomNum = ?
	''',(chosenAtomNum))
	elementsData= cursor.fetchall()
	for alldata in elementsData:
		print(alldata[0],alldata[1],alldata[2],alldata[3],alldata[4])
	input("Press anykey to continue")
	menuSelect()

def viewAllData():
	cursor.execute('''SELECT * FROM periodicTable''')
	elementsData = cursor.fetchall()
	for alldata in elementsData:
		print(alldata[0],alldata[1],alldata[2],alldata[3],alldata[4])
	input("Press anykey to continue")
	menuSelect()

def menuSelect():
	selectLoop = True
	while selectLoop:
		selectLoop = False
		try:
			selection = int(input("Please select an option:\n"
				"1) View all data\n"
				"2) View specific element\n"
				"3) Add new data\n"
				"4) Modify existing data\n"
				"5) Exit and save\n"
				"6) Exit without saving\n>>>>\t"))
			if selection == 1:
				viewAllData()
			elif selection == 2:
				viewSpec()
			elif selection == 3:
				addNew()
			elif selection == 4:
				modify()
			elif selection == 5:
				return True
			elif selection ==6:
				return False
		except:
			print("Error, invalid input")
			selectLoop = True

def main():
	print("#"*20+"\nElements Database\n"+"#"*20+"\n")
	saveChoice = menuSelect()
	if saveChoice == True:
		db.commit()
	else:
		db.rollback()
		db.close()
if __name__ == '__main__':
	main()