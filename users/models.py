from django.db import models
from django.contrib.auth.models import AbstractUser


# 使用django自带的表   1、需要先继承AbstractUser   2、在setting当中设置#继承django自带的用户类  第二步AUTH_USER_MODEL = "users.User_k"
class UserProfile(AbstractUser):
    sex = models.BooleanField(null=True)
    phone = models.CharField(max_length=50,null=True)
    address = models.CharField(max_length=50,null=True)
    content = models.CharField(max_length=500,null=True)
    age = models.IntegerField(null=True)
    img_url= models.ImageField(upload_to='imgs')
    class Meta:
        db_table = "user_myself"


# 使用django自带的表   1、需要先继承AbstractUser   2、在setting当中设置#继承django自带的用户类  第二步AUTH_USER_MODEL = "users.User_k"
# class Friend_Message(models.Model):
#     who = models.ForeignKey(UserProfile,verbose_name="个人信息", on_delete=models.CASCADE)
#     date = models.DateTimeField(auto_now_add=True)
#     photo = models.ImageField(upload_to='imgs')
#     content = models.TextField(null=True)
#     class Meta:
#         db_table = "dynamic_message"