from django.db import models

class Person(models.Model):
   GENDER = [
      ('M', 'Man'),
      ('W', 'Woman'),
   ]
   name = models.CharField(max_length=100,blank=False)
   Age = models.CharField(max_length=10,blank=False)
   Email = models.EmailField(blank=False)
   Gender = models.CharField(blank=False, max_length=10, choices=GENDER, default='M')
   Phone = models.CharField(blank=False,max_length=15)
   Weight = models.FloatField(max_length=5,blank=False ,help_text="Enter your weight in kgs")
   Height = models.FloatField(max_length=5,blank=False, help_text="Enter your height in Cm")
   Password = models.CharField(max_length=100,blank=False)
   Image = models.ImageField(upload_to='images',null=True)

   def __str__(self):
      return self.name
