from django.forms import ModelForm
from .models import Comment,Task,User

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = '__all__'
   
        
class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = '__all__'


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = '__all__'