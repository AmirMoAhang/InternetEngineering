from django.db import models
import uuid

# Create your models here.

class User(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    created = models.DateTimeField(auto_now_add=True)
    userName = models.CharField(max_length=400)
    firstName = models.CharField(max_length=400)
    lastName = models.CharField(max_length=400)
    password = models.CharField(max_length=1000)
    
    def __str__(self) -> str:
        return self.userName
    

class Task(models.Model):
    PRIORITY_TYPE = (
        (0 , 'High'),
        (1 , 'default'),
        (2 , 'Low'),
    )
    
    STATE_TYPE =(
        (0 , 'Done'),
        (1 , 'In Progress'),
        (2 , 'Todo'),
    )
    
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    priority = models.IntegerField(choices=PRIORITY_TYPE)
    state = models.IntegerField(choices=STATE_TYPE)
    deadLine = models.DateTimeField(null=True, blank=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    
    def __str__(self) -> str:
        return self.title
    
    
    
class Comment(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    created = models.DateTimeField(auto_now_add=True)
    description = models.TextField(null=True, blank=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    task = models.ForeignKey(Task, on_delete=models.CASCADE, null=False)



    
