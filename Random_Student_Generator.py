# Random student generator
# Jeff Mitchell
# Version 1.8 19 July 2017
# Takes a list of students and randomly selects the desired number from the list
# Saves the output to a user-defined text document
# Requires StudentDatabase.csv to be present in directory

import csv
import random

# Initialise variables
students = []
studentIdList = []
load = True
saveName = ""
studentDatabaseRaw = []
studentDatabaseConverted = {}
fileName = "StudentDatabase" #Student database file

# Read the contents of the text file for Student ID's
def LoadFile(loadName):
    studentIdListTemp = []
    try:
        FO = open(loadName, "r")
    except IOError:
        print("\nSorry, that file does not exist")
    else:
        for line in FO:
            studentIdListTemp.append(line.strip())
        FO.close()
        print("File is loaded")
        date = studentIdListTemp[0]
        sampler = studentIdListTemp[1]
        standard = studentIdListTemp[2]
        group = studentIdListTemp[3]
        size = int(studentIdListTemp[4])
        del studentIdListTemp[0:5]
    return studentIdListTemp, date, sampler, standard, group, size

# Load student database file into a list
def loadStudents(fileName):
    student_list = []
    try:
        file = open(fileName + '.csv', 'r')
    except IOError:
        print("The file does not exist. Check filename.")
    else:
        file.readline()
        reader = csv.reader(file, delimiter=',', quotechar='"')
        for row in reader:
            student_list.append(row)
        file.close()
        print("Student Database loaded.")
    return student_list

# get the length of a list
def listSize(list):
    length = len(list)
    return length
    
# Take a list and returns a list (allows a list to be created within a function)
def makingList(studentIdList):
    i = 0
    available = []
    while i < len(studentIdList):
        available.append(studentIdList[i])
        i += 1
    return available

# Convert to studentID and name
def convertNames(student_list):
    input_list = student_list
    new_database = {}
    t = tuple()
    name = ''
    i = 0
    while i < len(input_list):
        t = input_list[i]
        key = t[0]
        name = t[1] + ',' + t[2]
        new_database[key] = name
        i += 1
    return new_database

# Takes the list of students and returns a list of random ones (amount determined by size variable)
def pickSample(studentIdList, size):
    i = 0
    localSample = makingList(studentIdList)
    sampleList = []
    while i < (size):
        sampleLength = (len(localSample)-1)
        j = random.randint(0, sampleLength)
        value = localSample[j]
        #print(value)
        sampleList.append(value)
        del localSample[j]
        i +=1
    sortedList = sorted(sampleList)
    return sortedList

# get the length of a list
def listSize(list):
    length = len(list)
    return length

# compare length of list
def checkLength(size, supplied):
    if size < supplied:
        return 1
    elif size == supplied:
        print("They are the same size; just use the whole sample")
        return 2
    else:
        return 3

# Get the student's name from student database
def getName(student_data, student):
    #print("getName student value passed is: " + student)
    name = str(student_data.get(student))
    #print("getName student name is: " + name)
    return name

# Return a formatted string for student name and id for display
def unpackDisplay(studentID, studentName):
    firstName = getFirstName(studentName)
    lastName = getLastName(studentName)
    studentDetails = studentID + ' ' + firstName + ' ' + lastName
    return studentDetails
    
# Find the student's First Name (portion of string prior to ',')
def getFirstName(student):
    place = student.find(',')
    studentFirstName = student[0:place]
    return studentFirstName
    
# Find the student's Last Name (portion of string after ',')
def getLastName(student):
    place = student.find(',')
    place += 1
    studentLastName = student[place:]
    return studentLastName

# Display on screen selected students
def displayStudents(studentDatabaseConverted, selectedStudents):
    i = 0
    selectedStudentsList = []
    while i < len(selectedStudents):
        student = unpackDisplay(selectedStudents[i], getName(studentDatabaseConverted, selectedStudents[i]))
        print(student)
        selectedStudentsList.append(str(student))
        i += 1
    return selectedStudentsList

# Package selected student data for csv file format
def packageCSV(studentName):
    firstName = getFirstName(studentName)
    lastName = getLastName(studentName)
    return firstName, lastName 
        
# Write student sample to csv file (not currently used)
def writeStudentData(saveFile, student_data, students):
    # Take students and turn into a list
    i = 0
    myList = []
    while i < len(students):
        firstName, lastName = packageCSV(getName(student_data, students[i]))
        entry = students[i]
        myList.append(entry)
        myList.append(firstName)
        myList.append(lastName)
        i += 1
    with open(saveFile + '.csv', 'w') as csv_file:
        print(myList)
        writer = csv.writer(csv_file, delimiter=',', quotechar='|', lineterminator='\n', quoting=csv.QUOTE_MINIMAL)     
        for item in myList:
            writer.writerow([item])

# Program to run if sample size is less than size of list supplied
def process(studentDatabaseConverted, date, sampler, standard, length, group, size, studentIdList, saveName):
    sample = []
    sampleToSave = []
    print("\nDate: " + date)
    print("Sampler: " + sampler)
    print("The standard is: ", standard)
    print("Length of supplied list is: ", length)
    print("The group is: ", group)
    print("Sample size is: ", size)
    sample = pickSample(studentIdList, size)
    print("\nThe selected students are: \n")
    sampleToSave = displayStudents(studentDatabaseConverted, sample)
    #printList(sample)
    print("")
    saveList(sampleToSave, date, sampler, standard, group, size, saveName)
    print("List saved to: " + saveName)

# check if they wish to sample for another standard
def anotherStandard(saveName):
    load_again = "" #reset to check if want to load another file
    while load_again == "": #check if would like to load another file
        load_again = input("\nDo you want to sample another standard? y/n: ")
        if load_again != "y" and load_again != "n":
            print("\nThat is not a valid answer! Please try again")
            load_again = ""
        elif load_again == "y":
            keepSaveName = "" #use to check if they want to keep the same file name
            while keepSaveName == "":
                keepSaveName = input("Do you want to use the same save file? y/n: ")
                if keepSaveName != "y" and keepSaveName != "n":
                    print("\nThat is not a valid answer! Please try again")
                    keepSaveName = ""
                elif keepSaveName == "y":
                    break
                else: saveName = ""                    
            return True, saveName
        else:
            return False, saveName

# Print out items in a list
def printList(list):
    i = 0
    length = listSize(list)
    while i < length:
        print(list[i])
        i += 1

# Save a list
def saveList(selectedStudentsList, date, sampler, standard, group, size, saveName):
    fo = open(saveName, "a")
    fo.write("Date sampled: " + date + "\n")
    fo.write("Sampler: " + sampler + "\n")
    fo.write("Standard: " + standard + "\n")
    fo.write("Group: " + group + "\n")
    fo.write("Sample size: " + str(size) + "\n\n")
    fo.write("The selected students are:\n\n")
    list_save = ""
    for item in selectedStudentsList:
        list_save = list_save + str(item) + "\n"
    list_save = list_save + "\n"

    fo.write(list_save)
    fo.close()

# Find the student ID (portion of string prior to ',')
def getID(student):
    studentID = student.strip()
    place = student.find(',')
    studentID = student[0:place]
    return student
    
# Find the student name (portion of string after ',')
def getDefinition(student):
    studentName = student.strip()
    place = student.find(',')
    place += 1
    studentName = student[place:]
    return studentName

# Create a dictionary with student ID numbers and names
def defineStudents (studentList):
    i = 0
    listLength = listSize(studentList)
    students = {}
    tempKey = ""
    tempDefinition = ""
    while i < listLength:
        tempKey = getID(studentList[i])
        tempDefinition = getDefinition(studentList[i])
        students[tempKey] = tempDefinition
        i += 1
    return students

# Main program
print("\n\n************=============================*************")
print("\nRandom Student Generator version 1.8")
print("Created by Jeff Mitchell, 2017")
print("Randomly selects the desired number of students from a supplied list\n")

# Load student database
studentDatabaseRaw = loadStudents(fileName)
studentDatabaseConverted = convertNames(studentDatabaseRaw)

while load == True:
    loadName = input("What file would you like to load? ") + ".txt"
    if saveName == "":
        saveName = input("What file would you like to save to? ") + ".txt"
    studentIdList, date, sampler, standard, group, size = LoadFile(loadName)
    length = listSize(studentIdList)
    check = True
    while check == True:
        if checkLength(size, length) == 1:
            process(studentDatabaseConverted, date, sampler, standard, length, group, size, studentIdList, saveName)
            check = False
        else:
            print('''Sorry but you have not supplied enough Student ID's to process
a sample. Please make sure the sample size is less than the size of the list
that you are choosing from''')
            check = False
    repeat, saveName = anotherStandard(saveName);
    if repeat == True:
        load == True
    else:
        load = False
input("\nPress ENTER to exit")
    
