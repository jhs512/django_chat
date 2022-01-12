from django.db import models


# Create your models here.
class ChatMessage(models.Model):
    reg_date = models.DateTimeField('작성날짜', auto_now_add=True)
    writer = models.CharField('작성자', max_length=20)
    body = models.CharField('내용', max_length=100)
