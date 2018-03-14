from django.db import models
from django.utils import timezone
# Create your models here.


# 회의실 예약
class Reservation (models.Model):

    FirstTIME = 0
    SecondTIME = 1
    ThirdTIME = 2
    ForthTIME = 3
    FifthTIME = 4
    SixthTIME = 5
    SevenTIME = 6
    EighthTIME = 7
    NinethTIME = 8 
    TenthTIME = 9 
    EleventhTIME = 10
    STATUS = (
            (FirstTIME, ("9:00 ~ 10:00")),
            (SecondTIME, ("10:00 ~ 11:00")),
            (ThirdTIME, ("11:00 ~ 12:00")),
            (ForthTIME, ("12:00 ~ 13:00")),
            (FifthTIME, ("13:00 ~ 14:00")),
            (SixthTIME, ("14:00 ~ 15:00")),
            (SevenTIME, ("15:00 ~ 16:00")),
            (EighthTIME, ("16:00 ~ 17:00")),
            (NinethTIME, ("17:00 ~ 18:00")),
            (TenthTIME, ("18:00 ~ 19:00")),
            (EleventhTIME, ("19:00 ~ 20:00")),
         )
    
    author = models.ForeignKey('auth.User')
    name = models.CharField(max_length = 10)    
    major = models.CharField(max_length = 30)
    tel_num = models.IntegerField()
    num_people = models.IntegerField()

    rend_date = models.DateTimeField()
    rend_time = models.SmallIntegerField(choices=STATUS,default = FirstTIME)

    return_date = models.DateTimeField()
    return_time = models.SmallIntegerField(choices=STATUS,default = FirstTIME)
    
    room_number = models.SmallIntegerField()
    
    reservation_accept = models.BooleanField(default = False) #BooleanField의 기본 양식 위젯은 CheckboxInput
    updated_date = models.DateTimeField(blank = True, null = True)
    
    def publish(self):
        self.updated_date = timezone.now()
        self.save()


    def __int__(self):
        return self.room_number

