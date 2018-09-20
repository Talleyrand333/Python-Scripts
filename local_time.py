<<<<<<< HEAD
import datetime as  dt
#Here we will try to convert a string to a datetime object using a string input
# date_now=dt.date.today()
# local_time=dt.datetime.now().time()
# loco=local_time.strftime("%H:%M:%S")
# print(loco)
# print(date_now)
alar=input("Enter your alarm")
print(alar)
ala=dt.datetime.strptime(alar,"%H%M").time()
print(ala)
=======
import datetime as  dt
#Here we will try to convert a string to a datetime object using a string input
# date_now=dt.date.today()
# local_time=dt.datetime.now().time()
# loco=local_time.strftime("%H:%M:%S")
# print(loco)
# print(date_now)
alar=input("Enter your alarm")
print(alar)
ala=dt.datetime.strptime(alar,"%H%M").time()
print(ala)
>>>>>>> 2cfe30de2f685ec458c182ee58d1beb7e4d61c15
