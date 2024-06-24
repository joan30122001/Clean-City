from django import forms
from django.contrib.auth.models import User
from .models import EmergencyCollection, Profile, CompanyProfile, IllegalDeposit


class RegisterForm(forms.Form):
    TOWN_CHOICES = [
        ('Yaounde, Bastos', 'Yaounde, Bastos'),
        ('Yaounde, Nkolbisson', 'Yaounde, Nkolbisson'),
        ('Yaounde, Ngoa-Ekelle', 'Yaounde, Ngoa-Ekelle'),
        ('Yaounde, Mvog-Ada', 'Yaounde, Mvog-Ada'),
        ('Yaounde, Mvog-Mbi', 'Yaounde, Mvog-Mbi'),
        ('Yaounde, Etoudi', 'Yaounde, Etoudi'),
        ('Yaounde, Nsam', 'Yaounde, Nsam'),
        ('Yaounde, Essos', 'Yaounde, Essos'),
        ('Yaounde, Biyemassi', 'Yaounde, Biyemassi'),
        ('Yaounde, Mendong', 'Yaounde, Mendong'),
        ('Yaounde, Emana', 'Yaounde, Emana'),
        ('Yaounde, Ahala', 'Yaounde, Ahala'),
        ('Yaounde, Oyom-Abang', 'Yaounde, Oyom-Abang'),
        ('Yaounde, Nkolndongo', 'Yaounde, Nkolndongo'),
        ('Yaounde, Ekounou', 'Yaounde, Ekounou'),
        ('Yaounde, Obili', 'Yaounde, Obili'),
        ('Yaounde, Etoa-Meki', 'Yaounde, Etoa-Meki'),
        ('Yaounde, Melen', 'Yaounde, Melen'),
        ('Yaounde, Odza', 'Yaounde, Odza'),
        ('Yaounde, Mfandena', 'Yaounde, Mfandena'),
        ('Yaounde, Biyem-Assi', 'Yaounde, Biyem-Assi'),
        ('Yaounde, Nkol-Eton', 'Yaounde, Nkol-Eton'),
        ('Yaounde, Mvan', 'Yaounde, Mvan'),
        ('Yaounde, Tsinga', 'Yaounde, Tsinga'),
        ('Yaounde, Messa', 'Yaounde, Messa'),
        ('Yaounde, Simbock', 'Yaounde, Simbock'),
        ('Yaounde, Ngousso', 'Yaounde, Ngousso'),
        ('Yaounde, Etoug-Ebe', 'Yaounde, Etoug-Ebe'),
        ('Yaounde, Anguissa', 'Yaounde, Anguissa'),
        ('Yaounde, Awae', 'Yaounde, Awae'),
        ('Yaounde, Nfandena', 'Yaounde, Nfandena'),
        ('Yaounde, Biassi', 'Yaounde, Biassi'),
        ('Yaounde, Efoulan', 'Yaounde, Efoulan'),
        ('Yaounde, Essomba', 'Yaounde, Essomba'),
        ('Yaounde, Olezoa', 'Yaounde, Olezoa'),
        ('Yaounde, Nyom', 'Yaounde, Nyom'),
        ('Yaounde, Mimboman', 'Yaounde, Mimboman'),
        ('Yaounde, Nkolmesseng', 'Yaounde, Nkolmesseng'),
        ('Yaounde, Madagascar', 'Yaounde, Madagascar'),
        ('Yaounde, Tsinga', 'Yaounde, Tsinga'),
        ('Yaounde, Elig-Essono', 'Yaounde, Elig-Essono'),
        ('Yaounde, Simbok', 'Yaounde, Simbok'),
        ('Yaounde, Mbankolo', 'Yaounde, Mbankolo'),
        ('Yaounde, Ekoumdoum', 'Yaounde, Ekoumdoum'),
        ('Yaounde, Nkoabang', 'Yaounde, Nkoabang'),
        ('Yaounde, Nkoldongo', 'Yaounde, Nkoldongo'),
        ('Yaounde, Abattoir', 'Yaounde, Abattoir'),
        ('Yaounde, Odza', 'Yaounde, Odza'),
        ('Yaounde, Cite Verte', 'Yaounde, Cite Verte'),
        ('Yaounde, Ngousso', 'Yaounde, Ngousso'),
        ('Yaounde, Nkomo', 'Yaounde, Nkomo'),
        ('Douala, Nkomo', 'Douala, Nkomo'),
    ]

    FREQUENCY_CHOICES = [
        ('once a week -- 1000 XAF', 'once a week -- 1000 XAF'),
        ('twice a week -- 2500 XAF', 'twice a week -- 2500 XAF'),
        ('three times a week -- 5000 XAF', 'three times a week -- 5000 XAF'),
    ]

    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password_repeat = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
    phone_number = forms.CharField(widget=forms.NumberInput(attrs={'class':'form-control'}), required=False)
    town_street = forms.ChoiceField(choices=TOWN_CHOICES, widget=forms.Select(attrs={'class':'form-control'}))
    street_detail = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    frequency = forms.ChoiceField(choices=FREQUENCY_CHOICES, widget=forms.Select(attrs={'class':'form-control'}))



class CompanyRegisterForm(forms.Form):
    LOCATION_CHOICES = [
        ('Yaounde', 'Yaounde'),
        ('Douala', 'Douala'),
    ]
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password_repeat = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
    company_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    phone_number = forms.CharField(widget=forms.NumberInput(attrs={'class':'form-control'}), required=False)
    location = forms.ChoiceField(choices=LOCATION_CHOICES, widget=forms.Select(attrs={'class':'form-control'}))



class EmergencyCollectionForm(forms.ModelForm):
    class Meta:
        model = EmergencyCollection
        fields = ['image', 'description', 'town_street', 'street_detail']



class IllegalDepositForm(forms.ModelForm):
    class Meta:
        model = IllegalDeposit
        fields = ['image', 'description', 'town_street', 'street_detail']



class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'username', 
            'first_name', 
            'last_name', 
            'email', 
        ]



class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [
            'phone_number',
            'frequency',
            'town_street',
            'street_detail',
            'profile_image'
        ]
    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'



class CompanyUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'username', 
            'first_name', 
            'last_name', 
            'email', 
        ]



class CompanyProfileForm(forms.ModelForm):
    class Meta:
        model = CompanyProfile
        fields = [
            'phone_number',
            'location',
            'company_name',
            'profile_image'
        ]
    def __init__(self, *args, **kwargs):
        super(CompanyProfileForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'