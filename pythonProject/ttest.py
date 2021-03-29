
import CarRental
import datetime
import re


def ValidDates(list,setOfCars,sd,ed):

    setOfValidCars = setOfCars
    ssd = datetime.datetime.strptime(sd, "%d %B %Y")
    eed = datetime.datetime.strptime(ed, "%d %B %Y")

    for i in range(len(list)):

        # if the car from list is in setOfValidCars then check the dates to know if it's will still valid or not
        if (list[i].getCl() in setOfValidCars ):
            # if there is any intersection between dates then remove the car from the setOfValidCars
            currentSd = datetime.datetime.strptime(list[i].getSd(), "%d %B %Y")
            currentEd = datetime.datetime.strptime(list[i].getEd(), "%d %B %Y")

            if(ssd == currentSd or (ssd > currentSd and ssd < currentEd)
               or eed == currentEd or ( eed < currentEd and eed > currentSd)):
                # this car is not available
                # remove this car from setOfValidCars
                setOfValidCars.remove(list[i].getCl())

    # if there isn't any car avaialbe at these date
    if (len(setOfValidCars)==0):
        print("There isn't any car available at these dates (" + sd + "-->" + ed +") ")
    else:
        print ("The cars that are available during these dates are :")
        for i in setOfValidCars:
            print(i)

def readDates(list,setOfCars):
    flag1=0
    flag2 = 0
    while(flag1==0 and flag2==0):
        while (flag1 == 0):
            inputSd = input("Enter the start rental date:(dd mm yy): ")
            inputSd=modifyDate(inputSd)
            # checking that no negative number is entered
            flag1 = 1
            split1 = inputSd.split(" ")
            if ((int(split1[0]) < 0) or (int(split1[2]) < 0)):  # split[0] and split[2] represents the day and year
                print("Not a Valid date, no minus sign in dates!Try AGAIN!")
                flag1 = 0
        while (flag2 == 0):
            inputEd = input("Enter the end rental date:(dd mm yy): ")
            inputEd = modifyDate(inputEd)
            flag2 = 1
            # checking that no negative number is entered
            split2 = inputEd.split(" ")
            if ((int(split2[0]) < 0) or (int(split2[2]) < 0)):  # split[0] and split[2] represents the day and year
                print("Not a Valid date, no minus sign in dates!Try AGAIN!")
                flag2 = 0
            # checking that the entered dates are logical:
            # if same month and year, then day of end date should be greater than day of start
        if ((split1[1] == split2[1]) & (split1[2] == split2[2])):
            if (int(split2[0]) < int(split1[0])):
                print("Illogical date!")
                flag1=0
                flag2=0
        #if we would like to add more cases
    ValidDates(list,setOfCars,inputSd,inputEd)


#here we use this function to modify all entered dates in differed formats to the desired format
def modifyDate(date):
    monthName = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    object = re.search(r"[-/][0-9]*[-/]", date, re.M | re.S)  # if the date has the format of "/digit/" or "-digit-" it should be modified
    if object:
        replaceString = monthName[int(object.group()[1:len(object.group()) - 1]) - 1]  # the replace string is the monthName element indexed by the digit
        date=re.sub(r"[-/][0-9]*[-/]", " " + replaceString + " ", date)
    return date

def addInfoToList(list,setOfValidCars,sd,ed):

    while True :

      cl = input("Please enter  car license number you want to rent from the above vlaid cars : ")
      cl = cl.upper()
      if (cl in setOfValidCars):
          # add the information
          name = input("Enter the name : ")
          id = input("Enter the id : ")
          dob = input("Enter the date of birth :")
          mobile = input("Enter the mobile number : ")
          #obj = CarRental.CarRental(name,id,dob,mobile,cl,)
          break
      else:
          choice  = input("The car license number is not valid if you want to try agin enter (y) else enter (n)")
          if (choice != "y" or choice != "Y"):
              break


import datetime

d1 = datetime.date.today()
d2 = datetime.date(2020,8,1)

print((d1-d2).days)





















Dic = {'January':1, 'February':2, 'March':3, 'April':4, 'May':5, 'June':6, 'July':7, 'August':8, 'September':9, 'October':10, 'November':11, 'December':12}

day = input("Please enter day ")
month = input("please enter the month ")
if(month.isalpha()):
    month = month.capitalize()
    month = Dic[month]
year = input("Please enter the year")
date = str(day) + " " + str(month) + " " + str(year)
try:
    date = datetime.datetime.strptime(date,"%d %m %Y")
    currentDate = datetime.date.today()
    date = datetime.date(date.year,date.month,date.day)
    DateBecfor16Years = datetime.date(currentDate.year-16,currentDate.month,currentDate.day)
    if(DateBecfor16Years < date):
        print("your age acording to the entered DOB is under 16 , so you can't rent a car ")
        choice = input("if you have missed in entering your DOB and want to try again please enter(y) , if you want to finsh the process of renting a car please enter (t) ")
    if(choice == "Y" or choice =="y"):
        continue
    else:
        break;

except Exception:
    print("Not valid")
    # error massege like the above one

