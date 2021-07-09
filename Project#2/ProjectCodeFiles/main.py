import Car
import CarRental
import Task_1
import Task_2
import Task_3
import Task_4
import datetime
import re


list=[]


#read the whole file, and store the result is info
with open('CarRentalOld.txt')as f:
    info=f.read()
#infoList is the read text from file, having each line seperately
infoList=info.split("\n")
#Here we will be creating objects of the class after splitting each line by the ";", where each splitted field represents an attribute of the object
for i in range(len(infoList)):
    obj = re.search(r"[A-Za-z0-9\-/;]", infoList[i], re.M) # if object is exist then the line is not empty
    if (not obj):  # empty line
        continue
    data = infoList[i].split(";")
    obj=CarRental.CarRental(data[0],data[1],data[2],data[3],data[4],data[5],data[6],data[7],data[8],data[9])
    list.append(obj)



setOfCars = set() # this set will include all the cl number of all valid cars in the database
carsDict = {} # this dictionary will include the basic information of the cars with the key considered to be the cl number of the car


# call completeMissing from Task_1 to do Task 1
l = Task_1.completeMissing(list)
list = l[0]
# this function add the unique cl into setOfCars , and then add the basic information of this car into carsDict because we will use them later
for i in range(len(list)):
    if not( list[i].getCl() in setOfCars):
        setOfCars.add(list[i].getCl())
        carsDict[list[i].getCl()] = "manufacturing car : " + list[i].getYear() + " Car maker : " + list[i].getCm()
print("Note : We have implemented task 1 because it's the base of the other tasks inorder to get the completed database")

while True :

    choice = input("Please Enter the number of the task you would like to do :")

    # Task 1 is chosen
    if(choice == "1"):
        print("Printing Summary : ")
        Task_1.printSummary(l[1],l[2])

    # Task 2 is chosen
    elif(choice == "2"):
        choice = input("Would you like to inquire about person (p) or about car (c) ? ")
        if(choice == "P" or choice == "p"):
            Task_2.inquiryPerson(list)
            print("Task 2 done successfully ")
        elif(choice == "C" or choice == "c"):
            Task_2.inquiryCar(list)
            print("Task 2 done successfully")
        else:
            print("This is not a valid option !")

    # Task 3 is chosen
    elif(choice == "3"):
        Task_3.readDates(list,setOfCars,carsDict)
        print("Task 3 done successfully ")

    # Task 4 is chosen
    elif(choice == "4"):
        Task_4.printStatisticsAboutCars(list,setOfCars)

    # invalid choice
    else:
        print("Your choice is not valid !")

    # ask the user if he/she wants to do more tasks or want to terminate
    choice = input("Do you want to try again (y) , or terminate (t) ? ")

    if(choice == "Y" or choice == "y"):
        continue
    else:
        print("Bye!")
        break
