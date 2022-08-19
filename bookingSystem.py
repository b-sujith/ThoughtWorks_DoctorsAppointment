from patient import Patient
from doctor import Doctor
from datetime import time
from pydoc import doc
import string

class OnlineDoctorsAppointment:
    def __init__(self) -> None:
        self.__doctors=[]

    def addDoctor(self,id:int, specialization:string, day:string, availableStartTime:time,availableEndTime:time):
        doctorID = Doctor(id,specialization,day, availableStartTime,availableEndTime)
        self.__doctors.append(doctorID)
        return doctorID

    def deleteDoctor(self,doctorID:int):
        #searching for the doctor with doctorID and removing him/her in the doctors list,deleting that object
        for doctor in self.__doctors:
            if self.doctor.getID() == doctorID:
                self.__doctors.remove(doctor) #throws an error if this doc doesn't exist in the doctors list
                del doctor

    def updateDoctor(self,id:int,specialization:string,availableStartTime:time,availableEndTime:time):
        #searching for the doctor with doctorID and updating his/her timings if exists
        for doctor in self.__doctors:
            if doctor.getID() == id:
                newDoctor = Doctor(specialization,availableStartTime,availableEndTime)
                doctor = newDoctor

    def bookAppointment(self,specialist:string,day:string, requiredStartTime:time,requiredEndTime:time):
        patient = Patient(specialist,day,requiredStartTime,requiredEndTime)
        bool,id=self.isAnyDoctorAvailable(patient)
        if bool:
            return 'Appointment Booked with Doctor {doc} at {time}'.format(doc=id,time=requiredStartTime)
        return 'No slot available,please come back later'

    def isAnyDoctorAvailable(self,patient:Patient):
        requiredPatientSpecialist=patient.getSpecialist()
        requiredPatientDay=patient.getRequiredDay()
        requiredPatientStartTime=patient.getRequiredStartTime()
        requiredPatientEndTime=patient.getRequiredEndTime()
        #check for any specialist's availability and store all of them in a list
        availableSpecialists=[specialist for specialist in self.__doctors if specialist.getSpecialization()==requiredPatientSpecialist]
        #if those specialist is free at required timings,we return True
        for availableSpecialist in availableSpecialists:

            #checking whether specialist is available on that day of week
            if requiredPatientDay==availableSpecialist.getAvailableDay():
     
                #checking whether the patients required timings match with the doctors timings
                if requiredPatientStartTime >= availableSpecialist.getAvailableStartTime() and requiredPatientEndTime <= availableSpecialist.getAvailableEndTime():
            
                    #storing all the patients whom this specialist is attending
                    patientList = availableSpecialist.getPatientsList()
                    
                    #if no doctor has no patients
                    if not patientList:
                        availableSpecialist.addPatient(patient)
                        return (1,availableSpecialist.getID())
                        
                    #if atleast 1 patient is already present for this specialist
                    if patientList:
                        for oldPatient in patientList:
            
                            #check already alloted patient timings with current patient
                            if requiredPatientStartTime >= oldPatient.getRequiredEndTime() or requiredPatientEndTime <= oldPatient.getRequiredStartTime():

                                #adding patient to the doctor's patient list
                                availableSpecialist.addPatient(patient)
                                return (1,availableSpecialist.getID())
                    
                    #as there as no patients already,directly add patient
                
        return (0,0)
        
                
