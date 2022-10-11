import datetime
from multiprocessing.sharedctypes import Value
from django import forms

from Recruit.models import Experience


class Skills_Form(forms.Form):
    skill_name = forms.CharField(max_length = 100 , required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    experience = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
    skill_level = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control'}))


class Expr_Form(forms.Form):
    title = forms.CharField(max_length = 100 , required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    company = forms.CharField(max_length = 100 , required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    years = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
    months = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
    from_date = forms.DateField( initial=datetime.date.today, widget=forms.DateInput(attrs={'class': 'form-control','type':'date'}))
    to_date = forms.DateField( initial=datetime.date.today, widget=forms.DateInput(attrs={'class': 'form-control','type':'date'}))
    

class Quali_Form(forms.Form):
    cert_choice =(
        ('10th', "High School"),
        ('12th', "Higher Secondary"),
        ('Graduation','Bachelor'),
        ('PostGraduation','Masters'),
        ('Ph.D','Doctorate')
    )

    qualification = forms.ChoiceField(choices=cert_choice, widget=forms.Select(attrs={'class': 'form-control'}))
    university_name = forms.CharField(max_length = 100 , required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    institute_name = forms.CharField(max_length = 100 , required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    from_date = forms.DateField( initial=datetime.date.today, widget=forms.DateInput(attrs={'class': 'form-control','type':'date'}))
    to_date = forms.DateField( initial=datetime.date.today, widget=forms.DateInput(attrs={'class': 'form-control','type':'date'}))
    percentage = forms.FloatField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
    grade = forms.CharField(max_length = 50, required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    year = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
    

class Reg_Frm(forms.Form):
    EXP_CHOICES =(
    ("1", "0-1 years"),
    ("2", "1-2 years"),
    ("3", "2-4 years"),
    ("4", "4+ years"), 
    )                        

    FirstName = forms.CharField(max_length = 100 , required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    LirstName = forms.CharField(max_length = 100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    Contact = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
    UserID = forms.CharField(max_length = 50, required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    Password = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'type':'password'}))
    E_mail = forms.EmailField(max_length = 100, widget=forms.EmailInput(attrs={'class': 'form-control','type':'email'}))
    Date_of_Birth = forms.DateField( initial=datetime.date.today, widget=forms.DateInput(attrs={'class': 'form-control','type':'date'}))
    Address1 = forms.CharField(max_length = 100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    Address2 = forms.CharField(max_length = 100, required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    Address3 = forms.CharField(max_length = 100, required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    Pincode = forms.CharField(max_length = 15, widget=forms.TextInput(attrs={'class': 'form-control'}))
    City = forms.CharField(max_length = 100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    country = forms.ChoiceField(widget=forms.Select(attrs={'class':'form-control'}))
    state = forms.ChoiceField(widget=forms.Select(attrs={'class': 'form-control'}))
    Previous_Organization = forms.CharField(max_length = 200, widget=forms.TextInput(attrs={'class': 'form-control'}))
    Experience = forms.ChoiceField(choices=EXP_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    UI_Developer = forms.BooleanField(required=False)
    Python_Developer = forms.BooleanField(required=False)
    Full_Stack_Developer = forms.BooleanField(required=False)
    IJP = forms.BooleanField(required=False)
    #ijp_app = forms.BooleanField()

    # class Meta:
    #     widgets = {
    #         'FirstName' : forms.CharField(attrs={'class':'form-control;'}),
    #     }
    
