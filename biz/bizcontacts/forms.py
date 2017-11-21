from django import forms
from .models import Image, Contact

class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ('front_url', 'back_url')
        
class NewContact(forms.ModelForm):
    class Meta: 
        model = Contact
        fields = ('name', 'business_name', 'cell_number', 'work_number', 'email', 'notes', 'website')