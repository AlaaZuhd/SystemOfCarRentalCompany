
import re
import CarRental


def inquiryPerson (list):

    choice=input("Would you like to search using name(n) or ID number (id)? ")

    if(choice=='n'): # if the user want to search using the name
        listIds=[] # this list will contains the ids of every person whose name is identical to inputName
        inputName=input("Enter the name you would like to search for:")
        inputName=inputName.lower() # convert the inputName into lower case , beacse names in lower case or upper case are the same
        #valid characters in inputName are ( A-Z , a-z , - , _ ,"space" )
        obj = re.search(r"[^A-Za_z \-_]",inputName,re.M|re.I)

        if(obj): # if obj is not null , that's means the inputName contains invalid characters
            print("You can not enter a name with invalid characters!")
        else: # else the inoutName is valid
            for i in range(len(list)):
                if (inputName == list[i].getName().lower()): # if they are equal then add that element into the listIds
                    if (listIds.count(list[i].getId()) == 0):
                        listIds.append(list[i].getId())
            if (len(listIds) == 0): # if the length of the listIds is = 0 then there is no person with the entered name
                print("No such Name!")
            for i in range(len(listIds)):
                searchId(listIds[i], list)
    elif(choice=='id'): # if the user want to search using the id
        inputId = input("Enter the id you would like to search for:")
        if(inputId.isnumeric()):# checking if the id is consists of digits only
           searchId(inputId,list)
        else: # the entered id is not valid , because it have to consist digits only
           print("You can not enter an id with characters other than digits!")
    else:# the entered choice is invalid
        print("Wrong Choice!")


# search a person using it's id
def searchId(inputId,list):

    total = 0
    flag = 0
    # loops through the lsit
    for i in range(len(list)):
        # if the id is identical to inputId then print person information
        if (inputId == list[i].getId()):
            flag = 1
            # if total is 0 then that's means we need to first print the basic inforamtion of the person
            if (total == 0):
                print("Name searched for is: " + list[i].getName() + ", Id number is: " + list[
                    i].getId() + ", Date of birth is: " + list[i].getDob() + ", Mobile numerb is: " + list[
                          i].getMobile())
                print("Cars rented by that person are:")
            total += int(list[i].getRb())
            # now print the other information
            print("Car Licence is: " + list[i].getCl() + ", Car make is: " + list[
                i].getCm() + ", Year of manufacturing is: " + list[i].getYear() + ", Car rent start date is: " +
                  list[i].getSd() + ", Car rent end date is: " + list[i].getEd() + ", The amount paid is: " + list[
                      i].getRb())
    # printing the total amount paid by this person for renting the cars
    if (flag == 1):
        print("Total paid is: %f " % total)
    # there is no person with the specified id
    else:
        print("No such ID!Try AGAIN!")


# searching about car using it's cl number
def inquiryCar(list):

    inputCl = input("Enter the car license number you would like to search for:")
    if(inputCl.isalnum()):
        total = 0
        flag = 0
        for i in range(len(list)): # loops through the list

            # if the cl of the car is identical to the inputCl then print the information
            if (inputCl == list[i].getCl()):
                flag = 1
                # if total is zero then print the basic iformation (the basic information will be printed once )
                if (total == 0):
                    print("Car license searched for is: " + list[i].getCl() + ", Car make is: " + list[
                        i].getCm() + ",year of manufacturing is: " + list[i].getYear())
                    print("Persons rented this car are:")

                total += int(list[i].getRb()) # calculating the revenue mase by renting this car

                # printint the other information
                print("Person name is: " + list[i].getName() + " Person id is: " + list[i].getId() + " Person DOB is: " +
                      list[i].getDob() + " mobile number is: " + list[i].getMobile() + "\ncar rent start date is: " +
                      list[i].getSd() + " car rent end date is: " + list[i].getEd() + " the amount paid is: " + list[
                          i].getRb())
        if (flag == 1):
            print("Total paid is: %f " % total)
        else:
            print("No such Car!Try AGAIN!")
    else:
        print("the entered license number is not valid , it should contains letters and digits only ")

