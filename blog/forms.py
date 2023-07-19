from django import forms
from django.forms import Textarea
from blog.models import Post, Comments

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = (
            "category",
            "title",
            "text",
            "published",

        )
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = (
            "text",

        )
        widget={
            'text': Textarea(attrs={'rows':4, 'cols':40}),
        }