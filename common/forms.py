from django import forms
from .models import User
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User

# class UserForm(UserCreationForm):
#     email = forms.EmailField(label="이메일")

#     class Meta:
#         model = User
#         fields = ("username", "email")



class RegisterForm(forms.ModelForm): 
    # 회원가입 폼 
    # 장고에서는 HTML 입력요소를 widget(위젯)이라고 말한다.  
    password = forms.CharField(label='password', widget=forms.PasswordInput) 
    confirm_password = forms.CharField(label='confirm password', widget=forms.PasswordInput) 
 
 
    class Meta: 
        model = User 
        fields = ['username', 'email', ] 
 
 
    def clean_confirm_password(self): 
        cd = self.cleaned_data 
        if cd['password'] != cd['confirm_password']: 
            raise forms.ValidationError('비밀번호가 일치하지 않습니다!') 
 
 
        return cd['confirm_password'] 
