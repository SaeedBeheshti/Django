from django import forms
from website.models import Contact,Newsletter
from captcha.fields import CaptchaField
class NameForm(forms.Form):
    name =forms.CharField(max_length=255)
    email = forms.EmailField()
    subject = forms.CharField(max_length=255)
    message = forms.TimeField(widget=forms.Textarea)



class ContactForm(forms.ModelForm):
    captcha = CaptchaField()
    class Meta:
        model = Contact
        fields = '__all__'
        widgets = {
            'message': forms.Textarea(attrs={'rows': 5}),  # برای textarea
        }
class NewsletterForm(forms.ModelForm):
    captcha = CaptchaField()
    email = forms.EmailField()
    class Meta:
        model = Newsletter
        fields = '__all__'
