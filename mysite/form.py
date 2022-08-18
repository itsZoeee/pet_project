from socket import fromshare
from django import forms
from django.forms import ModelForm
from matplotlib import widgets
from mysite.models import Adopt, Lost
from django.forms import ModelChoiceField

class AdoptForm(ModelForm):
    class Meta:
        model = Adopt
        species=(('貓','貓'),('狗','狗'),('其他','其他'))
        sex = (('公','公'),('母','母'))
        Ligation = (('已結紮','是'),('未結紮','否'))
        Vaccine= (('已施打','是'),('未施打','否'))
        pic = forms.FileField()
         
        # fields = '__all__'
        fields = ('species','breed','sex','size','color','age','location','ligation','vaccine','picUpload')
        labels ={
            'species': '寵物種類',
            'breed': '品種',
            'sex':'性別',
            'ligation':'是否已結紮',
            'vaccine':'是否已施打疫苗',
            'size':'體型',
            'color':'花色',
            'age':'年齡',
            'location':'地點',
            'picUpload':'照片上傳'
        }
        widgets ={
            'species': forms.Select(choices=species,attrs={'class':'form-select form-select-sm','style':'width:8rem; margin-right: 10px;'}),
            'sex' : forms.Select(choices=sex,attrs={'class':'form-select form-select-sm','style':'width:8rem; margin-right: 10px;'}),
            'ligation' : forms.Select(choices=Ligation,attrs={'class':'form-select form-select-sm','style':'width:8rem; margin-right: 10px;'}),
            'vaccine': forms.Select(choices=Vaccine,attrs={'class':'form-select form-select-sm','style':'width:8rem; margin-right: 10px;'}),
            'breed': forms.TextInput(attrs={'class':'form-control'}),
            'size': forms.TextInput(attrs={'class':'form-control'}),
            'color': forms.TextInput(attrs={'class':'form-control'}),
            'age': forms.TextInput(attrs={'class':'form-control'}),
            'location': forms.TextInput(attrs={'class':'form-control'}),
        }

class LostForm(ModelForm):
    class Meta:
        model = Lost
        variety=(('鳥','鳥'),('貓','貓'),('狗','狗'),('兔','兔'),('鼠','鼠'),('其他','其他'))
        gender = (('公','公'),('母','母'))
         
        # fields = '__all__'
        fields = ('variety','name','species','gender','body','color','age','lostdate','area','picUpload')
        labels ={
            'name': '寵物名',
            'variety': '寵物種類',
            'species': '品種',
            'gender':'性別',
            'body':'體型',
            'color':'花色',
            'age':'年齡',
            'area':'走失地點',
            'picUpload':'照片上傳',
            'lostdate':'走失日期',
        }
        widgets ={
            'variety': forms.Select(choices=variety,attrs={'class':'form-select form-select-sm','style':'width:8rem; margin-right: 10px;'}),
            'gender' : forms.Select(choices=gender,attrs={'class':'form-select form-select-sm','style':'width:8rem; margin-right: 10px;'}),
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'species': forms.TextInput(attrs={'class':'form-control'}),
            'body': forms.TextInput(attrs={'class':'form-control'}),
            'color': forms.TextInput(attrs={'class':'form-control'}),
            'age': forms.TextInput(attrs={'class':'form-control'}),
            'area': forms.TextInput(attrs={'class':'form-control'}),
            'lostdate': forms.DateInput(format=('%Y-%m-%d'),
                    attrs={'class': 'form-control', 'placeholder': 'Select a date','type': 'date'}),
        }