from datetime import datetime
import string

from doctorsAppointment.patient import Patient


class Doctor:
    def __init__(self,id:int, specialization:string , day:string, availableStartTime:datetime ,availableEndTime:datetime) -> None:
        self.setID(id)
        self.setAvailableDay(day)
        self.setSpecialization(specialization)
        self.setAvailableStartTime(availableStartTime)
        self.setAvailableEndTime(availableEndTime)
        self.setPatientsList()

    def setID(self,id:int):
        self.__id=id

    def setAvailableDay(self,day:string):
        self.__day=day

    def setSpecialization(self,specialization:string):
        self.__specialization=specialization

    def setAvailableStartTime(self,availableStartTime:datetime):
        self.__availableStartTime=availableStartTime

    def setAvailableEndTime(self,availableEndTime:datetime):
        self.__availableEndTime=availableEndTime

    def setPatientsList(self):
        self.__patients=[]

    def addPatient(self,patient:Patient):
        self.__patients.append(patient)

    def getID(self):
        return self.__id

    def getSpecialization(self):
        return self.__specialization

    def getAvailableStartTime(self):
        return self.__availableStartTime

    def getAvailableEndTime(self):
        return self.__availableEndTime

    def getPatientsList(self):
        return self.__patients

    def getAvailableDay(self):
        return self.__day
