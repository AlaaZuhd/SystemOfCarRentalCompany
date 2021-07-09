
import CarRental
import Car
import datetime
import re

def ValidCars(list,setOfCars,carsDict,SD,ED):

    setOfValidCars = setOfCars

    sd = datetime.datetime.strptime(SD, "%d %B %Y")
    ed = datetime.datetime.strptime(ED, "%d %B %Y")

    for i in range(len(list)):
        # if the car from list is in setOfValidCars then cheack the dates to know if it's will still valid or not
        if (list[i].getCl() in setOfValidCars):
            # if there is any intersection between dates then remove the car from the setOfValidCars
            currentSd = datetime.datetime.strptime(list[i].getSd(), "%d %B %Y")
            currentEd = datetime.datetime.strptime(list[i].getEd(), "%d %B %Y")
            if (sd == currentSd or (sd > currentSd and sd < currentEd)
                    or ed == currentEd or (ed < currentEd and ed > currentSd)):
                # this car is not available
                # remove this car from setOfValidCars
                setOfValidCars.remove(list[i].getCl())

    # if there isn't any car avaialbe at these date
    if (len(setOfValidCars) == 0):
        print("There isn't any car available at these dates (" + sd + "-->" + ed + ") ")
    else:
        print("The cars that are available during these dates are :")

        for i in setOfValidCars:
            print("Car license number: " + i + " " + carsDict[i])

    addInfoToList(list, setOfValidCars, carsDict, SD, ED)


def readDates(list,setOfCars,carsDict):
    flag1=0
    flag2 = 0
    while True :
        inputSd = input("Enter the start rental date:(dd mm yy): ")
        inputSd = modifyDate(inputSd)
        inputEd = input("Enter the end rental date:(dd mm yy): ")
        inputEd = modifyDate(inputEd)
        inputSd = modifyDate(inputSd)
        inputEd = modifyDate(inputEd)
        try :
            sd = datetime.datetime.strptime(inputSd, "%d %B %Y")
            ed = datetime.datetime.strptime(inputEd, "%d %B %Y")
            if(ed < sd):
                print("end date must be more than the start date !")
                raise  Exception
            today = datetime.datetime.today()
            if (today.date() > sd.date()):
                print("You can not rent a car on a day that is over!")
                raise Exception
            break

        except Exception:
            choice = input("Dates are not valid ! Do you want to try again (y) ot finish the task (f) ? ")
            if(choice == "y" or choice == "Y"):
                continue
            else:
                return;

        #if we would like to add more cases
    ValidCars(list,setOfCars,carsDict,inputSd,inputEd)

#here we use this function to modify all entered dates in differed formats to the desired format
def modifyDate(date):
    monthName = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    object = re.search(r"[-/][0-9]*[-/]", date, re.M | re.S)  # if the date has the format of "/digit/" or "-digit-" it should be modified
    if object:
        replaceString = monthName[int(object.group()[1:len(object.group()) - 1]) - 1]  # the replace string is the monthName element indexed by the digit
        date=re.sub(r"[-/][0-9]*[-/]", " " + replaceString + " ", date)
    return date


def addInfoToList(list,setOfValidCars,carsDict,sd,ed):
    flag=0
    while True :
      cl = input("Please enter the car license number you want to rent from the above valid cars : ")
      cl = cl.upper()
      for i in setOfValidCars:
          if (cl == i):
              flag=0
              # add the information
              while(True):
                name = input("Enter the name : ")
                id = input("Enter the id : ")
                print("Note: the valid date formates allowed to enter here are dd-mm-yy , dd/mm/yy , or dd monthName yy")
                dob = input("Enter the date of birth :")
                dob = modifyDate(dob)
                mobile = input("Enter the mobile number : ")
                rb = input("Enter the rental money need to be paid : ")
                splitString = carsDict[cl].split(" ")
                year = splitString[3]
                cm = splitString[7]

                obj = re.search(r"[^A-Za-z \-_]",name,re.M|re.I)
                if (obj):
                    print("name is not valid , name should contains letters , - , _ , or space ")
                    choice = input("Do you want to try again (y) or finish this task(f) ? ")
                elif(not id.isnumeric()):
                    print("Id is not valid , id should contains digits only !")
                    choice = input("Do you want to try again (y) or finish this task(f) ? ")
                elif(not mobile.isnumeric()):
                    print("mobile number is not valid , it should contains digits only !")
                    choice = input("Do you want to try again (y) or finish this task(f) ? ")
                elif(not rb.isnumeric()):
                    print("money need to be paid is not valid , it should contains digits only !")
                    choice = input("Do you want to try again (y) or finish this task(f) ? ")

                else:
                    choice = isDOBValid(dob)
                    flag = choice # will be 1 if there is no error in the date of birth
                    if(flag==1):
                       break;

                if(choice == "y" or choice == "Y"):
                    continue
                else:
                  return ;
              if(flag):
                  obj = CarRental.CarRental(name, id, dob, mobile, cl, cm, year, sd, ed, rb)
                  list.append(obj)
                  file = open("CarRentalCompleted.txt","a")
                  file.write(obj.printFormatedInfo())
                  file.write("\n")
                  break
      if(flag==0):
          choice  = input("The car license number is not valid if you want to try again enter (y) else enter (n) ")
          if (choice == "y" or choice == "Y"):
              continue
          else:
              break
      else:
          break



def isDOBValid(birthDate):
    try:

        birthDate = datetime.datetime.strptime(birthDate, "%d %B %Y")

        currentDate = datetime.date.today()
        DateBecfor16Years = datetime.date(currentDate.year - 16, currentDate.month, currentDate.day)

        # to cheack that the age of the user is valid to rent a car
        if (DateBecfor16Years < birthDate.date()):
            print("according to you DOB you are under 16 , so you can't rent a car ")
            choice = input("If you made a mistake in entering your DOB , you can try again (y) or ending the task (f) ")
            return choice

    except Exception:
        choice = input("Yor date not valid")
        return choice

    # summary if the return value is "Y" or "y" then that is mean there is an error in the date formate and the user want to try again
    # if the return valus is 1 that means there is'nt any error in the dateFormate
    # else means there is an error in the dateFormate and the user choice to finish the task .
    return 1
