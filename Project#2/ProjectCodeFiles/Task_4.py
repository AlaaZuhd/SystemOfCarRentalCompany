
import datetime

# function to print the number of days a car was rented , the revenue made by each car , and the average price per day for renting each car
def printStatisticsAboutCars(list,setOfCars):

    print("---------------statistics about each car----------------")
    # loops through all cars in setOfCars ( sedOfCars contains the cl number of each car in the completed database )
    for i in setOfCars:
        # calcNumOfRentedDays will return a list the first element in it will be the number of days the car was rented ,
        # and the second element is the revenue made by the car .
        l = calcNumOfRentedAndRevenueDays(list,i)

        # printing the statistics of the car
        print("--------------------------------------------------------")
        print("Number of Days car \""+ i + "\" was rented : " + str(l[0]) )
        print("Revenue made by renting the car : " + str(l[1]))
        # the average price per day for renting a car = Revenue made by the car / number of rented days
        print("Average price per day for renting the car : " + str(float(l[1])/l[0]))
        print("--------------------------------------------------------\n")

# this function take the list that contains the completed database , and the cl of the car we want to search about
# then it calculates how many days the given car was rented , and the revenue made by this car .
def calcNumOfRentedAndRevenueDays(list,car):

    num = 0
    revenue = 0
    # loops through the list
    for i in list:

        if(i.getCl() == car):
            # convert the dates from this format (dayNum nonthName yearNum) to this format (yearNum-monthNum-dayNum)
            sd = datetime.datetime.strptime(i.getSd(), "%d %B %Y")
            ed = datetime.datetime.strptime(i.getEd(), "%d %B %Y")
            # (ed-sd).days will return how many days are between this two dates
            days = (ed-sd).days
            num += days
            revenue += int(i.getRb())

    # return a list contains the number of days the car was rented , and the revenue made by renting this car
    return [num,revenue]
