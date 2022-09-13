from django import forms
from django.core import validators

def ends_with_gmail(value):
    if not value.endswith('@gmail.com'):
        raise forms.ValidationError('gmail id only allowed')

class Registration(forms.Form):
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(required=False)
    email = forms.EmailField(max_length=40,validators=[ends_with_gmail])
    address = forms.CharField(widget=forms.Textarea(attrs={'cols':20,'rows':5}),validators=[validators.MaxLengthValidator(10),validators.MinLengthValidator(5)])
    age = forms.IntegerField()
    password=forms.CharField(widget=forms.PasswordInput)
    retype_password=forms.CharField(widget=forms.PasswordInput)
    bot_handler=forms.CharField(required=False,widget=forms.HiddenInput)

    # def clean_first_name(self):
    #     fname=self.cleaned_data['first_name']
    #     if len(fname)<3:
    #         raise forms.ValidationError('The min char should be 3')
    #     return fname

    # def clean_age(self):
    #     inputage=self.cleaned_data['age']
    #     if inputage < 20 and inputage > 30:
    #         raise forms.ValidationError('age should be 20 to 30')
    #     return inputage

    # def clean_email(self):
    #     mail = self.cleaned_data['email']
    #     if not mail.endswith('@gmail.com'):
    #         raise forms.ValidationError('email domain should be gmail.com')
    #     return mail
    def clean(self):
        cleaned_data = super(Registration,self).clean()
        pwd1 = cleaned_data.get("password")
        pwd2 = cleaned_data.get("retype_password")
        if pwd1 != pwd2:
            raise forms.ValidationError("Passwords not matching")

        lname=cleaned_data.get('last_name')
        if lname == '':
            raise forms.ValidationError("last name should not be null")

        bot_value=cleaned_data['bot_handler']
        if len(bot_value)>0:
            raise forms.ValidationError('Request from BOT...cannot be submitted')
