from django import forms
from common.models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["text"]

        widgets = {
            "text": forms.Textarea(
                attrs={
                    "placeholder": "Add a comment...",
                    "cols": 40,
                    "rows": 10,
                }
            )
        }
