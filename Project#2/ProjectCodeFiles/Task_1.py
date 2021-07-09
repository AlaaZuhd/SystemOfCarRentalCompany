import CarRental
import datetime
import re

monthName = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October',
             'November', 'December']


#modifying date format function
def modifyDate(entry):

    # We will be modifying:
    # 1)The date of birth of each object
    flag = 0
    object = re.search(r"[-/][0-9]*[-/]", entry.getDob(),re.M | re.S)  # if the date has the format of "/digit/" or "-digit-" it should be modified
    if object:
        replaceString = monthName[int(object.group()[1:len(object.group()) - 1]) - 1]  # the replace string is the monthName element indexed by the digit
        entry.setDob(re.sub(r"[-/][0-9]*[-/]", " " + replaceString + " ", entry.getDob()))
        flag = 1
    # 2)The start rental date of each object
    object = re.search(r"[-/][0-9]*[-/]", entry.getSd(), re.M | re.S)
    if object:
        replaceString = monthName[int(object.group()[1:len(object.group()) - 1]) - 1]
        entry.setSd(re.sub(r"[-/][0-9]*[-/]", " " + replaceString + " ", entry.getSd()))
        flag= 1
    # 3)The end rental date of each object
    object = re.search(r"[-/][0-9]*[-/]", entry.getEd(), re.M | re.S)
    if object:
        replaceString = monthName[int(object.group()[1:len(object.group()) - 1]) - 1]
        entry.setEd(re.sub(r"[-/][0-9]*[-/]", " " + replaceString + " ", entry.getEd()))
        flag = 1
    return flag

# function to try and complete the missing information
def completeMissing(list):
    missingList=[] # this is a list to put the elements which can't be completed
    completeList=[] # this is a list to put the elements which are completed
    printList1 = [0,0,0,0,0,0,0,0,0,0]   #this list will be counting data for printing summary for completed/recovered entries
    printList2 = [0,0,0,0,0,0,0,0,0,0]   #this list will be counting data for printing summary for uncompleted entries(either missing cl, or missing more than a field so that it can not be filled

    for i in list:
        countList = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0] #this list will be couting the data for printing summary for each entry seperately
        flag = modifyDate(i)    #if any date in the entry is modified, flag is set to one
        countList[1] = flag    #countList[1] represents if entry is with wrong date format
        if(i.getCl()!=""):      #if cl is missing, then this entry can not be completed
            if (i.getId() == "" or i.getName() == "" or i.getDob() == "" or i.getMobile() == "" or i.getCm() == "" or
                    i.getYear() == "" or i.getSd() == "" or i.getEd() == "" or i.getRb() == ""):
                for j in list:   #start searching the list, to fill the incompleted entry
                    if (i.getCl() == j.getCl()):
                        # get the missing cm from the j.getCm is it's exist
                        if (i.getCm() == ""):
                            countList[7] = 1   #countList[7] states whether a missing cm or not
                            if(j.getCm() != ""):
                              i.setCm(j.getCm())
                        # get the missing year from the j.getYear is it's exist
                        if (i.getYear() == ""):
                            countList[9] = 1   #countList[9] states whether the year is missing in this entry or not
                            if(j.getYear() != ""):
                              i.setYear(j.getYear())
                        if (i.getSd() == "" and j.getSd() != "" and i.getEd() != "" and compareDates(i.getEd(),j.getEd())==1): #trying to fill the start date,
                        #if missing start date, then need to check that end date is the same,
                        #if both dates are missing, then entry can not be completed
                            i.setSd(j.getSd())
                        if (i.getEd() == "" and j.getEd() != "" and i.getSd() != "" and compareDates(i.getSd(),j.getSd())==1): #trying to fill the end date
                        #if missing end  date, then start date should be checked before completing entry
                            i.setEd(j.getEd())
                        # get the missing rb from the j.getRb is it's exist
                        if (i.getRb() == "" and j.getRb() != "" and ( (i.getEd() != "" and compareDates(i.getEd(),j.getEd())==1)
                            or (i.getSd() != "" and compareDates(i.getSd(),j.getSd())==1) ) ):
                        #before completing the Rb entry, need to check the start or end date, to make sure we are dealing with same entries
                        #note: no two cars with same Cl and same start date and end date are not duplicates
                            i.setRb(j.getRb())
                        if (i.getId() == ""):
                            countList[3] = 1  #countList[3] states wether id is missing in the given entry
                            #if missing and before filling it, need to check that the cl and start date and end date are the same for this person
                            if(j.getId() != "" and i.getCl().upper() == j.getCl().upper() and i.getEd() != "" and compareDates(i.getEd(),j.getEd())==1
                                and i.getSd() != "" and compareDates(i.getSd(),j.getSd())==1):
                                i.setId(j.getId())
                    if (i.getName() == ""):
                            countList[2] = 1  #countList[2] states wether name is missing in the given entry
                            #if name is missing, check same id ( as cl is already checked) before filling,smae concept is used for Dob and mobile
                            if(j.getName() != "" and (i.getId()==j.getId())):
                              i.setName(j.getName())
                            # get the missing id from the j.getId if it's exist
                    if (i.getDob() == ""):
                            countList[4] = 1  #countList[4] states wether Dob is missing in the given entry
                            if(j.getDob() != "" and (i.getId()==j.getId())):
                               i.setDob(j.getDob())
                            # get the missing mobile from the j.getMobile if it's exist
                    if (i.getMobile() == ""):
                            countList[5] = 1  #countList[5] states wether id is missing in the given entry
                            if(j.getMobile() != ""  and (i.getId() == j.getId())):
                              i.setMobile(j.getMobile())


        else:
            if (i.getCm() == ""):
                countList[7] = 1
            if (i.getYear() == ""):
                countList[9] = 1
            if (i.getId() == ""):
                countList[3] = 1
            if (i.getName() == ""):
                countList[2] = 1
            if (i.getDob() == ""):
                countList[4] = 1
            if (i.getMobile() == ""):
                countList[5] = 1
            countList[8] = 1   #countList[8] states wether cl is missing in the given entry

        # now if there are still missing fields then move that element with missing fields into a list called missingList
        if (i.getCl() == "" or i.getId() == "" or i.getName() == "" or i.getDob() == "" or i.getMobile() == "" or i.getCm() == "" or i.getYear() == ""
            or i.getSd() == "" or i.getEd() == "" or i.getRb() == ""):
            if(i.getId() == "" or i.getName() == "" or i.getDob() == "" or i.getMobile() == ""):
               countList[6] = 1 #countList[6] states wether the personal information in this entry can't be recovered
            missingList.append(i)
            for k in range(0,10):
                printList2[k] += countList[k]
        # if the current entry dosn't have any missing fields then mve it into a list called completeList
        else:
            completeList.append(i)
            for k in range(0, 10):
                printList1[k] += countList[k]

    printList2[0] = calcNumOfDuplicates(list)

    #moving all not comlete entries to a new text file called(“CarRentalMissing.txt”)
    f=open("CarRentalMissing.txt","w")
    for i in missingList:
        f.write(str(i.printFormatedInfo()))
        f.write("\n")
    f.close()
    # moving all comlete entries to a new text file called(“CarRentalCompleted.txt”
    f=open("CarRentalCompleted.txt","w")
    for i in completeList:
        f.write(str(i.printFormatedInfo()))
        f.write("\n")
    f.close()

    l = removeDuplicate(completeList)
    completeList = l[0]
    printList1[0] = l[1]
    #printSummary(printList1, printList2)

    return [completeList,printList1,printList2]

def printSummary(printList1,printList2):
    #printing summary before recovering, requires printing the summation of printList1[i]+printList2[i] in most cases
    print("Summary of data missing in the database:")
    print("Number of duplicate entries in the database = " , printList2[0] )
    print("Number of entries with wrong date format in the database = " , (printList1[1] + printList2[1]))
    print("Number of entries where names are dropped from the database = " ,(printList1[2] + printList2[2]))
    print("Number of entries where Ids are dropped from the database = " , (printList1[3] + printList2[3]))
    print("Number of entries where dob are dropped from the database = ", (printList1[4] + printList2[4]))
    print("Number of entries where mobile numbers are dropped from the database = " , (printList1[5] + printList2[5]))
    print("Number of entries where personal entry can not be completed = " , printList2[6])
    print("Number of entries where car make is dropped from the database = " , (printList1[7] + printList2[7]))
    print("Number of entries where car Ids are dropped from the database = ", (printList2[8]))
    print("Number of entries where car models (year) are dropped from the database = " , (printList1[9] + printList2[9]))

    print("")

    #printing summary after recovery, requires printing the printList1 elements
    print("Summary of data recovered from the database:")
    print("Number of duplicate entries removed from the new database = " , printList1[0])
    print("Number of entries with wrong date format fixed in the new database = " , printList1[1])
    print("Number of entries with names recovered in the new database = " , printList1[2])
    print("Number of entries with Ids recovered in the new database = " , printList1[3])
    print("Number of entries with dob recovered in the new database = " , printList1[4])
    print("Number of entries with mobile numbers recovered in the new database = " , printList1[5])
    print("Number of entries with car make recovered in the new database = " , printList1[7])
    print("Number of entries with car models (year) recovered in the new database = " , printList1[9])


#This function will encounter the number of duplicates in the whole database
def calcNumOfDuplicates(list):

    # this list will be a flag to help as know wether this entry is encountered as a duplicates or not
    # so we have initailzed it with zeros
    flagList = []
    for i in range(len(list)):
        flagList.append(0)
    # sum variable will contains the number of duplicates in the whole database
    sum = 0

    for i in range(len(list)):
        # if this entry is considered as a duplicate of anther antry or it's cl is not exist or bot the start and end dats are not exist
        # then we can't know if it have a duplicates or not so continue looping
        if(flagList[i]==0 and ( list[i].getCl()=="" or (list[i].getSd()=="" and list[i].getEd()=="") ) ):
            continue
        # this loop will check the duplicate of the current entry starting from the next of this current entry
        for j in range(i+1,len(list)):
            # if this entry is not a duplicate of another entry , and the cars ids are identical and some of the start or end dates
            # are identical and not empty then this entry is a duplicate of the current entry
            if(flagList[j]==0 and list[i].getCl()==list[j].getCl() and
            ((list[i].getSd()!="" and list[i].getSd()==list[j].getSd()) or (list[i].getEd()!="" and list[i].getEd()==list[j].getEd())) ):
                sum += 1
                flagList[j] = 1


    return sum

# function to remove the duplicates from the completed database
def removeDuplicate(list):
    i=0
    sum=0
    while (i < len(list)): # loops through the list
        j=i+1
        # loops through the list starting from the first element in the list after the element obtained from the first loop
        while (j < len(list)):
            #if the ids are idenetical then cheack the other field and if they are all identical then remove the second element
            if (list[i].getCl() == list[j].getCl() and compareDates(list[i].getSd(),list[j].getSd())==1 and compareDates(list[i].getEd(),list[j].getEd())==1 and
                list[i].getName().lower() == list[j].getName().lower() and compareDates(list[j].getDob(),list[i].getDob()) ==1
                 and list[i].getMobile() == list[j].getMobile() and list[i].getCm().lower() == list[j].getCm().lower()
                 and list[i].getYear() == list[j].getYear() and list[i].getRb() == list[j].getRb()):
                    sum += 1
                    list.pop(j)
                    j-=1
            j+=1
        i+=1

    return [list , sum ]


def compareDates(date1, date2):
    # if the date has the format of "/digit/" or "-digit-" it should be modified
    object1 = re.search(r"[-/][0-9]*[-/]", date1, re.M | re.S)
    if object1:
        # the replace string is the monthName element indexed by the digit
        replaceString = monthName[int(object1.group()[1:len(object1.group()) - 1]) - 1]
        date1 = re.sub(r"[-/][0-9]*[-/]", " " + replaceString + " ", date1)

    object2 = re.search(r"[-/][0-9]*[-/]", date2, re.M | re.S)
    if object2:
        # the replace string is the monthName element indexed by the digit
        replaceString = monthName[int(object2.group()[1:len(object2.group()) - 1]) - 1]
        date2 = re.sub(r"[-/][0-9]*[-/]", " " + replaceString + " ", date2)
    date1 = datetime.datetime.strptime(date1,"%d %B %Y")
    # we have created a date object to comaper the dates , because maybe date1 = 1 May 2020 and date2 = 01 May 2020
    # then comparing them as string will yield to be not identical , so using date objects will solve the problem
    date2 = datetime.datetime.strptime(date2,"%d %B %Y")

    if (date1 == date2):
        return 1
    else:
        return 0
