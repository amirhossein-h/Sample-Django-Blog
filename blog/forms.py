from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model= Comment
        fields= ("text", )
        widgets={
            "text": forms.Textarea(attrs={'cols': 80, 'rows': 3, 'class': 'form-control'}),
        }
