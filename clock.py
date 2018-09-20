import datetime as dt
import os,pytz
"""
this plays a selected file in the computer's hard disc at a certain time,
also includes a world time checker for major places in the world.
"""
class Clock:
    def __init__(self):
        self.local_time=dt.datetime.now().time()
        self.alarm_time=None
    def get_local_t(self):
        local__time=dt.datetime.now().time()
        local__time2=dt.time.strftime(local__time,"%H:%M")
        return local__time2
    @staticmethod
    def check_timezone():
        zones={
            '1 Shanghai':'Asia/Shanghai','2 New York':'US/Eastern','3 Madrid':'Europe/Madrid','4 Amsterdam':'Europe/Amsterdam',
            '5 London':'Europe/London','6 Johannesburg':'Africa/Johannesburg','7 Nairobi':'Africa/Nairobi','8 Moscow':'Europe/Moscow'}
        for k in zones:
            print(k)
        print('Choose a location for its current time')
        place = input('')
        for i in zones:
            if place == i[0]:
                real_place=i[1:]
                aw = pytz.timezone(zones[i])
                aw= dt.datetime.now(aw)
                aw=dt.datetime.strftime(aw,"%H:%M")
                print("The time in {} is {}".format(real_place.title(),aw))
                return
        return
    def set_alarm(self):
        try:
            print('Please input your time in hours and minutes  without spaces e.g 2245')
            alarm_time = input('Enter Alarm time here:')
            alarm_time = dt.datetime.strptime(alarm_time, '%H%M').time()
            self.alarm_time=alarm_time
            return self.alarm_time
        except ValueError:
            print('Please use only digits that are within the 24hour range')
            return
    def alarm(self):
        try:
            time_now=dt.datetime.now().time()
            alarm=self.alarm_time
            while time_now<alarm:
                time_now = dt.datetime.now().time()
            os.startfile(r'C:\Users\user\Music\GRADUATION\01 Good Morning (Intro).mp3')
        except TypeError:
            print('You have no alarm set')



    def interface(self):
        checker=True
        while True:
            print('WELCOME!!\n'
            'Press 1 to check Local Time \nPress 2 to set alarm time\n'
            'Press 3 to check local time in Major cities worldwide\n'
            'Press 4 to start alarm\n'
            'Press 5 to check current alarm time\n'
            'Press 6 to exit the console')
            choice=input(':')
            if choice=='1':
                print("The Time is ",self.get_local_t())
            elif choice=='2':
                self.set_alarm()
            elif choice=='3':
                self.check_timezone()
            elif choice =='4':
                print("Alarm Started")
                self.alarm()
            elif choice=='5':
                print(self.alarm_time)
            elif choice=='6':
                print('Goodbye')
                break
            else:
                print('Please choose a valid option')


        return
a=Clock()
a.interface()
# a.set_alarm()
# a.get_local_t()
# print(a.local_time)
# print(a.alarm_time)
# a.check_timezone()
# a.alarm()



