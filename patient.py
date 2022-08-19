from datetime import datetime
import string


class Patient:
    def __init__(self,specialist:string,day:string,requiredStartTime:datetime,requiredEndTime:datetime) -> None:
        self.setSpecialist(specialist)
        self.setDay(day)
        self.setRequiredStartTime(requiredStartTime)
        self.setRequiredEndTime(requiredEndTime)

    def setSpecialist(self,specialist:string):
        self.__specialist=specialist

    def setDay(self,day:string):
        self.__day=day

    def setRequiredStartTime(self,requiredStartTime:datetime):
        self.__requiredStartTime=requiredStartTime
    
    def setRequiredEndTime(self,requiredEndTime:datetime):
        self.__requiredEndTime=requiredEndTime

    def getSpecialist(self):
        return self.__specialist

    def getRequiredDay(self):
        return self.__day

    def getRequiredStartTime(self):
        return self.__requiredStartTime

    def getRequiredEndTime(self):
        return self.__requiredEndTime