from django.db import models
from django.conf import settings
User= settings.AUTH_USER_MODEL

class Details(models.Model):
	#user = models.ForeignKey(User,on_delete=models.CASCADE)
	name = models.CharField(max_length = 50)
	dob = models.DateField(auto_now=False)
	email = models.EmailField(max_length=254)
	number = models.IntegerField()

	def __str__(self):
		return self.name

