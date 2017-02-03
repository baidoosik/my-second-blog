from django.db import models
from django.utils import timezone

# Create your models here.

# 쿠폰
class TimeStampModel(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        abstract = True

class Category(TimeStampModel):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name

class Item(TimeStampModel):
    title = models.CharField(max_length=200,null=False)
    category = models.ForeignKey(Category, null=True)
    price = models.CharField(max_length=20,null=True ,name= "가격")
    image_file = models.ImageField(upload_to='static_files/uploaded/original/%Y/%m/%d')
    text = models.TextField()

    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title