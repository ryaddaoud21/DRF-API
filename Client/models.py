from django.db import models

class Person(models.Model):
   GENDER = [
      ('M', 'Male'),
      ('F', 'Female'),
   ]
   SPORT = [
      ('GE ', 'GYM EXERCISES'),
      ('CR', 'CROSSFIT'),
      ('SW', 'SWIMMING'),
      ('FB', 'FOOTBALL'),
      ('HB', 'HANDBALL'),
   ]
   EFFORT = [
      ('LA ', 'Lightly Active'),
      ('MA', 'Moderately Active'),
      ('HA', 'Highly Active'),

   ]
   GOAL = [
      ('L ', 'Lose Fat'),
      ('G', 'Gain Weight'),
      ('S', 'Stability on Weight'),

   ]
   GOAL_W = [
      ('1 ', '1/4 Kgs'),
      ('2', '1/2 Kgs'),
      ('3', '1 Kgs'),

   ]

   Name = models.CharField(max_length=100,blank=False,help_text="Enter your Full name")
   Username = models.CharField(max_length=100,blank=False ,help_text="Username")
   Age = models.CharField(max_length=10,blank=False)
   Email = models.EmailField(blank=False)
   Password = models.CharField(max_length=100,blank=False)
   Gender = models.CharField(blank=False, max_length=10, choices=GENDER, default='M')
   Sport = models.CharField(blank=False, max_length=10, choices=SPORT, default='GE')
   Train = models.FloatField(max_length=5,blank=False, help_text="number of times do you train per week",null=True)
   Weight = models.FloatField(max_length=5,blank=False ,help_text="Enter your weight in kgs")
   Height = models.FloatField(max_length=5,blank=False, help_text="Enter your height in Cm")
   Hours = models.FloatField(max_length=5,blank=False, help_text="Number of Hours at Work")
   Effort = models.CharField(blank=False, max_length=10, choices=EFFORT, default='LA',help_text="YOUR EFFORT AT WORK ")
   Goal_Type = models.CharField(blank=False, max_length=10, choices=GOAL, default='LA',help_text="THE GOAL YOU WANT TO ACHIEVE")
   Goal_Weight = models.CharField(blank=False, max_length=10, choices=GOAL_W, default='1')
   Image = models.ImageField(upload_to='images',null=True)

   def __str__(self):
      return self.name
