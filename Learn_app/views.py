from django.shortcuts import render,get_object_or_404,redirect
from  .models import Course,Events
from django.contrib.auth import authenticate,login,logout
from .forms import userCustomForm ,ContactForm


# Create your views here.
def home(request):
    trending_courses = Course.objects.filter(trending=True)
    courses_trending_trainer = Course.objects.filter(trending=True)
    return render(request,'index.html',{'trending_courses':trending_courses,'courses_trending_trainer':courses_trending_trainer})

def about(request):
    return render(request,'About/about.html')

def courses(request):
    course_view=Course.objects.all()
    return render(request,'Courses/course.html',{'course_view':course_view})

def course_details(request,pk):
    course_details= get_object_or_404(Course, id=pk)
    return render(request,'Courses/course_details.html',{'course_details':course_details})

def trainer(request):
    course_tainer=Course.objects.all()
    return render(request,'Trainers/trainers.html',{'course_tainer':course_tainer})

def events(request):
    evnt_items=Events.objects.all()
    return render(request,'EventsDetails/event.html',{'evnt_items':evnt_items})


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save() 
            return redirect('contact_success_pages') 
    else:
        form = ContactForm()
    return render(request,'ContactUs/contact.html',{'form':form})

def contact_success_pages(request):
    return render(request,'ContactUs/success.html')




def register(request):
    if request.method == 'POST':
        form = userCustomForm(request.POST)
        if form.is_valid():
            form.save()
            
            # messages.success(request, f'Account created for {username}!')
            return redirect('login_page')
    else:
        form =userCustomForm()
    return render(request, 'RegisterandLogin/register.html', {'form': form})

def login_page(request):
    if request.user.is_authenticated:
        redirect('/')
    else:
        if request.method=='POST':
            name=request.POST.get('username')
            pwd=request.POST.get('password')
            user=authenticate(request,username=name,password=pwd)
            if user is not None:
                login(request,user)
                return redirect('home')
            else:
                return redirect('/login_page')
    return render(request,'RegisterandLogin/login.html')

def logout_page(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect("/")


