from django.db import models

# Create your models here.
# class Player 는 선수의 포지션(FW, MF, DF, GK 중에 선택), 이름, 나이, 국적, 선호하는 발이 들어가게 한다 
class Player(models.Model):
    POSITION_CHOICES = (
        ('FW', 'Forward'),
        ('MF', 'Midfielder'),
        ('DF', 'Defender'),
        ('GK', 'Goalkeeper'),
    )

    FOOT_CHOICES = (
        ('R', 'Right'),
        ('L', 'Left'),
        ('Both', 'Both'),
    )

    name = models.CharField(max_length=200)
    backnumber = models.CharField(max_length=2)
    position = models.CharField(max_length=2, choices=POSITION_CHOICES)
    age = models.CharField(max_length=2)
    nationality = models.CharField(max_length=200)
    foot = models.CharField(max_length=4, choices=FOOT_CHOICES)
# template에서 나타낼 때는 {{ player.position }}
    def __str__(self):
        return self.name


# class Match는 몇 라운드인지, 홈or어웨이 인지, 심판 이름, 승무패, 스코어, 득점자(ForeignKey)
# class Match(models.Model) :
#     def __str__(self):
#         return self.name


