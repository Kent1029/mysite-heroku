from django.db import models
from django.utils import timezone

class Post(models.Model):
	title = models.CharField(max_length=200)
	content = models.TextField() #Textfield不限制文字數量的大量文字
	pub_date = models.DateTimeField(default=timezone.now)

	class Meta:
		ordering = ('-pub_date',)

	def __str__(self):
		return self.title


class Country(models.Model):
	country_id = models.IntegerField() #國家id(index)為整數interger
	name = models.CharField(max_length=50) #國家名稱char
	def __str__(self):
		return self.name


class City(models.Model):
	name=models.CharField(max_length=50)
	population= models.IntegerField()
	country = models.ForeignKey(Country, on_delete=models.CASCADE)
	def __str__(self):
		return self.name

class Note(models.Model):
	title = models.CharField(max_length=200)
	pub_date = models.DateTimeField(default=timezone.now)
	def __str__(self):
		return self.title
 
