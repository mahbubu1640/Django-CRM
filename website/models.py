from django.db import models

# Create a model named with Record 
# - created_at/first_name/last_name/email/phone/address/city/state/zipcode

class Record(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    address = models.CharField(max_length=164)
    city = models.CharField(max_length=64)
    state = models.CharField(max_length=64)
    zipcode = models.CharField(max_length=10)
    
    def __str__(self):
        return (f"{self.first_name} {self.last_name}")
    
# from django.db import models


# class Record(models.Model):
# 	created_at = models.DateTimeField(auto_now_add=True)
# 	first_name = models.CharField(max_length=50)
# 	last_name =  models.CharField(max_length=50)
# 	email =  models.CharField(max_length=100)
# 	phone = models.CharField(max_length=15)
# 	address =  models.CharField(max_length=100)
# 	city =  models.CharField(max_length=50)
# 	state =  models.CharField(max_length=50)
# 	zipcode =  models.CharField(max_length=20)

# 	def __str__(self):
# 		return(f"{self.first_name} {self.last_name}")