from django.shortcuts import render, redirect, reverse
from django.template.loader import render_to_string
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from google.cloud import vision
from google.cloud.vision import types
import io
import os
from .models import Contact, Address, Image 
from .forms import ImageForm, NewContact
from biz.settings import BASE_DIR


#instantiates a client, specifying the project credentials (json file)
path_to_json = os.path.join(BASE_DIR, 'biz\\biz-contacts-service-account.json')
print(path_to_json)
vision_client = vision.Client.from_service_account_json(path_to_json, "biz-contacts")

# Create your views here.
def index(request):
    session_id = request.session
    if request.user.is_authenticated:
        return redirect('dashboard/')
    else:
        return render(request, 'bizcontacts/index.html') 

#@login_required()
def dashboard(request):
    user = request.user
    contacts = Contact.objects.filter(user=user)
    for contact in contacts:
        contact.cell_displayable = contact.make_displayable_phone_number(contact.cell_number)
        contact.work_displayable = contact.make_displayable_phone_number(contact.cell_number)        
    context = {'contact_list': contacts}
    return render(request,'bizcontacts/dashboard.html', context)

@login_required()
def dashboard_search(request):
    user = request.user
    search_term = request.GET['q']
    contact = Contact.objects.filter(user=user).filter(name__icontains=search_term)
    print(contact)
    context = {'contact_list': contact.values()}
    html = render_to_string('bizcontacts/cards.html',
            context,
            request=request,
        )
    return JsonResponse({'html': html})
        
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
        contact = Contact(name=name, email=email, business_name=business_name, user=user, cell_number=cell_number, work_number=work_number, notes=notes, website=website)
        contact.save()
        return redirect(reverse('dashboard')) 

def image_upload(request):
    print(request.FILES)
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            print(request.FILES['front_url'])
            parse_image(request.FILES['front_url'])
            return redirect(reverse('dashboard'))
    else:
        form = ImageForm()
    return render(request, 'bizcontacts/image_upload_form.html', {
        'form': form
    })
  
def parse_image(image_file):
    client = vision.ImageAnnotatorClient()
    file_name = os.path.join(os.path.dirname(__file__, image_file))
    with io.open(file_name, 'rb') as vision_file:
        content = vision_file.read()
    image = types.Image(content=content)
    response = client.label_detection(image=image)
    labels = response.label_annotations
    print('Labels')
    for label in labels:
        print(label.description)
