from django.db import models

# Create your models here.
"""
    我们的模型类需要继承制model.Model
    系统回味我们自动添加一个主键 ID
    字段名等于model的类型(选项)
    属性名==数据表的字段名
"""
class BookInfo(models.Model):
    name = models.CharField(max_length=50)

class PeopleInfo(models.Model):
    name = models.CharField(max_length=50)
    gender = models.BooleanField()
    book = models.ForeignKey(BookInfo, on_delete=models.CASCADE)
