from django.db import models


# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=64)

class Category(models.Model):
    CATEGORY_LIST = (
        ('[패키지]', '패키지'),
        ('[마케팅]', '마케팅')
    )
    name = models.CharField(max_length=64, choices=CATEGORY_LIST)