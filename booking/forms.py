from allauth.account.forms import SignupForm
from django import forms
from .models import UserProfile, Schedule

class CustomSignupForm(SignupForm):
    first_name = forms.CharField(max_length=30, label='First Name')
    last_name = forms.CharField(max_length=30, label='Last Name')
    date_of_birth = forms.DateField(label='Date of Birth', widget=forms.DateInput(attrs={
            'type': 'date',  
            'placeholder': 'YYYY-MM-DD',  
        }),
        input_formats=['%Y-%m-%d'])    
    

    def save(self, request):
        user = super(CustomSignupForm, self).save(request)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.save()        

        UserProfile.objects.create(
            user=user,
            first_name=self.cleaned_data['first_name'],
            last_name=self.cleaned_data['last_name'],
            date_of_birth=self.cleaned_data['date_of_birth'],                       
        )

        return user


class ScheduleForm(forms.ModelForm):
    class Meta:
        model = Schedule
        fields = ['date', 'time']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'time': forms.Select(),
        }

        