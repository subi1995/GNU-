from django.db import models
from django.utils import timezone
# Create your models here.


# 회의실 예약
class Reservation (models.Model):
    FirstROOM = 0
    SecondROOM = 1
    ThirdROOM = 2
    STATUS = (
            (FirstROOM, ("회의실 1")),
            (SecondROOM, ("회의실 2")),
            (ThirdROOM, ("회의실 3")),             
    )
    
    author = models.ForeignKey('auth.User')
    tel_num = models.IntegerField()
    major = models.CharField(max_length = 30)
    rend_date = models.DateTimeField()
    return_date = models.DateTimeField()
    room_number = models.SmallIntegerField(choices=STATUS,default = FirstROOM)
    reservation_accept = models.BooleanField(default = False) #BooleanField의 기본 양식 위젯은 CheckboxInput
    updated_date = models.DateTimeField(blank = True, null = True)
    
    def publish(self):
        self.updated_date = timezone.now()
        self.save()


    def __int__(self):
        return self.room_number

