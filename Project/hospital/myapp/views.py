from django.shortcuts import render, get_object_or_404
from myapp.models import User, Observation

def login_view(request):
    return render(request, 'login.html', {})

def index_view(request):
    return render(request, 'index.html', {})


def register_view(request):
    return render(request, 'register.html', {})

def patient_details_view(request):
    name = request.POST.get('name')
    email = request.POST.get('email')
    address = request.POST.get('address')
    age = request.POST.get('age')
    blood_group = request.POST.get('blood_group')
    gender = request.POST.get('gender')
    weight = request.POST.get('weight')
    contact = request.POST.get('contact')
    print(name,address)
    
    user= User(name=name, address=address, email=email, age=age, blood_group=blood_group, gender=gender, weight=weight, contact=contact)
    user.save()
    
    return render(request, "index.html",{})


def consult_view(request):
    users = User.objects.all()  # Fetch all user records from the database
    context = {'users': users}
    return render(request, 'consult.html', context)

def user_details(request, user_id):
    user = get_object_or_404(User, id=user_id)
    return render(request, 'displaydetails.html', {'user': user})

def save_observation(request):
    user_id = request.POST.get('userid')
    print(user_id)
    user = get_object_or_404(User, id=user_id)
    
    if request.method == 'POST':
        observation_text = request.POST.get('observation')
        if observation_text:
            observation = Observation(user=user, text=observation_text)
            observation.save()
    users = User.objects.all()  # Fetch all user records from the database
    context = {'users': users}
    return render(request, 'consult.html', context)

