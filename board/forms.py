from django import forms
from board.models import Post, Comment




class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['subject','head_image', 'content', ]

        # widgets = {
        #     'subject': forms.TextInput(attrs={'class': 'form-control'}),
        #     'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 10}),
        # }

        labels = {
            'subject': '제목',
            'head_image': '이미지',
            'content': '내용',
            
         
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        labels = {
            'content': '답변내용',
        }