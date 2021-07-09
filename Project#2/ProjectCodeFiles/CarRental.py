class CarRental:
    #Constructor and attributes
    def __init__(self, name, id, dob, mobile,cl, cm, year, sd, ed, rb):
        self.__name = name
        self.__id = id
        self.__dob = dob
        self.__mobile = mobile
        self.__cl = cl
        self.__cm = cm
        self.__year = year
        self.__sd = sd
        self.__ed = ed
        self.__rb = rb
    #Getters
    def getName(self):
        return self.__name
    def getId(self):
        return self.__id
    def getDob(self):
        return self.__dob
    def getMobile(self):
        return self.__mobile
    def getCl(self):
        return self.__cl
    def getCm(self):
        return self.__cm
    def getYear(self):
        return self.__year
    def getSd(self):
        return self.__sd
    def getEd(self):
        return self.__ed
    def getRb(self):
        return self.__rb
    #Setters
    def setName(self, name):
        self.__name = name
    def setId(self, id):
        self.__id = id
    def setDob(self, dob):
        self.__dob = dob
    def setMobile(self, mobile):
        self.__mobile = mobile
    def setCl(self, cl):
        self.__cl = cl
    def setCm(self, cm):
        self.__cm= cm
    def setYear(self, year):
        self.__year = year
    def setSd(self, sd):
        self.__sd = sd
    def setEd(self, ed):
        self.__ed = ed
    def setRb(self, rb):
        self.__rb = rb

    #function to print the attributes of the instances of the class
    def printInfo(self):
        return(self.__name + " " + self.__id + " " + self.__dob + " " + self.__mobile + " " + self.__cl +
               " " + self.__cm + " " + self.__year + " " + self.__sd + " " + self.__ed + " " + self.__rb)


    def printFormatedInfo(self):
        return(self.__name + ";" + self.__id + ";" + self.__dob + ";" + self.__mobile + ";" + self.__cl +
               ";" + self.__cm + ";" + self.__year + ";" + self.__sd + ";" + self.__ed + ";" + self.__rb)
