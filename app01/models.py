from django.db import models

# Create your models here.



class User(models.Model):
    """用户"""
    username = models.CharField(max_length=50)



class UserScore(models.Model):
    """用户得分"""
    score = models.IntegerField()
    time = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)