from django import forms
from .models import Comment
from django_recaptcha.fields import ReCaptchaField
from django_recaptcha.widgets import ReCaptchaV3


class CommentForm(forms.ModelForm):
    honeypot = forms.CharField(required=False, widget=forms.HiddenInput)
    captcha = ReCaptchaField(widget=ReCaptchaV3, required=True)

    class Meta:
        model = Comment
        fields = ['name', 'content', 'honeypot']

    def clean_honeypot(self):
        data = self.cleaned_data['honeypot']
        if data:
            raise forms.ValidationError("Spam detected!")
        return data
