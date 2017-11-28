from django.shortcuts import render, redirect, reverse
from django.template.loader import render_to_string
from django.http import JsonResponse
from .models import Contact, Address, Image
from .forms import NewContact
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    session_id = request.session
    if request.user.is_authenticated:
        user = request.user
        contact = Contact.objects.filter(user_id=user.id)
        print(contact)
        context = {'contact_list': contact.values()}
        return redirect('dashboard/')
    else:
        return render(request, 'bizcontacts/index.html') 

@login_required()
def dashboard(request):
    user = request.user
    contact = Contact.objects.filter(user=user)
    print(contact)
    context = {'contact_list': contact.values()}
    return render(request,'bizcontacts/dashboard.html', context)
    
def signup(request):
    if (True):
        email = request.POST['signup_email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        if password == confirm_password:
            # we are good to make a user
            user = User.objects.create_user(email, email, password)
            user.save()
            user = authenticate(request, username=email, password=password)
            if (user is not None):
                login(request, user)
                return redirect('dashboard')

def login_view(request):
    username = request.POST['email']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    print(user)
    print(request)
    if (user is not None):
        login(request, user)
        return redirect(reverse('dashboard'))
    else:
        return redirect(reverse('index'))

def logout_view(request):
    logout(request)
    return redirect(reverse('index'))

def create_contact(request):
    form = NewContact()
    if request.method == 'GET':
        context = {'form': form}
        html_form = render_to_string('bizcontacts/partial_contact_create.html',
            context,
            request=request,
        )
        return JsonResponse({'html_form': html_form})
    else:
        # add some checks to make sure that the contact info is in the correct form
        # if it isn't we need to do something else
        name = request.POST['name']
        email = request.POST['email']
        business_name = request.POST['business_name']
        website = request.POST['website']
        cell_number = request.POST['cell_number']
        work_number = request.POST['work_number']
        notes = request.POST['notes']
        user = request.user
        contact = Contact(name=name, email=email, business_name=business_name, user=user, cell_number=cell_number, work_number=work_number, notes=notes)
        contact.save()
        return redirect(reverse('dashboard')) 