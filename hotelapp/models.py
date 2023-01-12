from django.db import models

# Create your models here.
class add_user(models.Model):
    Name=models.CharField(max_length=20)
    Id_name=models.TextField(max_length=20)
    Mail=models.EmailField(max_length=150)
    Mobile_number=models.CharField(max_length=12)
    
    def __str__(self):
        return self.Name
    
class add_room(models.Model):
    roomnumber=models.IntegerField()
    roomfloor=models.IntegerField()
    roomtype=models.CharField( max_length=50)
    select=models.CharField( max_length=50)
    roomprice=models.IntegerField()
    
    def __str__(self) -> str:
        return  str(self.roomnumber)
    
    
    
