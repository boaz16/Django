from django.shortcuts import render
from myapp.models import Student

# Create your views here.

def home_view(request):
    return render(request, 'home.html', {})

def about_view(request):
    return render(request, 'about.html', {})

def form_view (request):
    return render(request, 'form.html', {})

def addstudentdetails_view(request):
    address = request.POST.get('address')
    course = request.POST.get('course')
    age = request.POST.get('age')
    name = request.POST.get('name')
    print(name,address)
    
    stud= Student(name=name, address=address, course=course, age=age)
    stud.save()
    
    return render(request, "form.html",{})

def viewstudentdetails_view(request):
    stud = Student.objects.all()
    print(stud)
    context = {
        'students' : stud
    }
    return render(request, "student_view.html",context)


def getstudent_view(request, pk):
    stud = Student.objects.get(pk=pk)
    print(stud)
    context = {
        'students' : stud
    }
    return render(request, "single_student_view.html",context)

def deletestudent_view(request, pk):
    print("In delete")
    Student.objects.filter(pk=pk).delete()

    stud = Student.objects.all()
    print(stud)
    context = {
        'students' : stud
    }
    return render(request, "student_view.html",context)


