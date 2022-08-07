from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from .models import Answer,Question,CustomUser

class RegisterForm(UserCreationForm):
    class Meta:
        model=CustomUser
        fields = ('username',)

class AnswerForm(ModelForm):
    class Meta:
        model=Answer
        fields=('detail',)

class QuestionForm(ModelForm):
    class Meta:
        model=Question
        fields=('title','detail','tags')

class ProfileForm(ModelForm):
    class Meta:
        model=CustomUser
        fields=('first_name','last_name','username','bio','location')