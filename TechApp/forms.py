from django import forms
from .models import Comment
from django_recaptcha.fields import ReCaptchaField


class CommentForm(forms.ModelForm):
    honeypot = forms.CharField(required=False, widget=forms.HiddenInput)
    captcha = ReCaptchaField()

    class Meta:
        model = Comment
        fields = ['name', 'content', 'honeypot']

    def clean_honeypot(self):
        data = self.cleaned_data['honeypot']
        if data:
            raise forms.ValidationError("Spam detected!")
        return data
