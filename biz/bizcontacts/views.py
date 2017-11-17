from django.shortcuts import render
from .models import Contact, Address, Image 
from django.contrib.auth.models import User

# Create your views here.
def index(request):
    return render(request, 'bizcontacts/index.html')

def dashboard(request):
    user = User.objects.get(username='birdy')
    contact = Contact.objects.filter(user=user)
    print(contact)
    context = {'contact_list': contact.values()}
    return render(request,'bizcontacts/dashboard.html', context)
    
