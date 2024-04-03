from django.db import models

# Create your models here.
class Login(models.Model):
   
    password=models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    is_police = models.BooleanField(default=False)

class Police(models.Model):
    login_id= models.CharField(max_length=255)
    policestation=models.CharField(max_length=255)
    address=models.CharField(max_length=255)
    location=models.CharField(max_length=255)
    phnnum=models.CharField(max_length=255)
   

class User(models.Model):
     login_id= models.CharField(max_length=255)
     name=models.CharField(max_length=255)
     phn_num=models.CharField(max_length=255)
    
   

    
    

class MissingPerson(models.Model):
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Others', 'Others'),
    ]

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    date_of_birth = models.DateField()
    address = models.TextField()
    aadhar_number = models.CharField(max_length=12, unique=True)  # Aadhar number is 12 digits and should be unique
    image = models.ImageField(upload_to='missing_persons/')  # Store images in a 'missing_persons' directory
    missing_from = models.DateField()
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    location= models.CharField(max_length=255)
    reported_by =  models.CharField(max_length=255)# Reference to the user who reported the case
    investigating_police = models.CharField(max_length=255)  # Reference to the police station that reported the case

    def __str__(self):
        return f"{self.first_name} {self.last_name}"



