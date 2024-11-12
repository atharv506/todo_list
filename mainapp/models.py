from django.db import models

# Create your models here.

from django.contrib.auth.models import User 



class Task(models.Model):
    
    user = models.ForeignKey(User,on_delete = models.CASCADE, null = True , blank =True) # foreign key = many-to-one relationship. Each Task object is linked to one User object, while each User can be linked to multiple Task objects
    title = models.CharField(max_length = 200,null = True)
    description = models.TextField(null = True)
    complete = models.BooleanField(default= False) 
    created = models.DateTimeField(auto_now_add= True)#only set once when the object is created and won’t change on future updates to the object.

    def __str__(self):
        return self.title #method lets you see each task by its title.
    class Meta:
        ordering = ['complete'] # class organizes your tasks with incomplete ones first, so you don’t miss any tasks that still need to be done.

