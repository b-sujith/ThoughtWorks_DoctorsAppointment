from datetime import datetime
from bookingSystem import OnlineDoctorsAppointment


admin = OnlineDoctorsAppointment()
admin.addDoctor(1,'Pediatrician','Tuesday', datetime(2020,6,9,14,0,0), datetime(2020,6,16,16,0,0))
admin.addDoctor(2,'Pediatrician', 'Tuesday', datetime(2020,6,9,13,0,0), datetime(2020,6,16,16,0,0))
admin.addDoctor(3,'Pediatrician', 'Monday', datetime(2020,6,9,13,0,0), datetime(2020,6,16,16,0,0))
admin.addDoctor(4,'ENT', 'Wednesday', datetime(2020,6,9,13,0,0), datetime(2020,6,16,16,0,0))
admin.addDoctor(5,'ENT', 'Thursday', datetime(2020,6,9,13,0,0), datetime(2020,6,16,16,0,0))

print(admin.bookAppointment('Pediatrician', 'Tuesday', datetime(2020,6,9,14,0,0), datetime(2020,6,9,14,30,0) ) )
print(admin.bookAppointment('Pediatrician', 'Tuesday', datetime(2020,6,9,14,0,0), datetime(2020,6,9,14,30,0) ) )
print(admin.bookAppointment('Pediatrician', 'Tuesday', datetime(2020,6,9,14,0,0), datetime(2020,6,9,14,30,0) ) )