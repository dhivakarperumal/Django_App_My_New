from django.urls import path
from .import views

urlpatterns = [
    path('',views.home,name='home'),
    path('about/',views.about,name='about'),
    path('courses/',views.courses,name='courses'),
    path('course_details/<int:pk>/',views.course_details,name='course_details'),
    path('trainer/',views.trainer,name='trainer'),
    path('events/',views.events,name='events'),
    path('contact/',views.contact,name='contact'),
    path('contact_success_pages/',views.contact_success_pages, name='contact_success_pages'),

    
    path('register/',views.register,name="register"),
    path('login_page/',views.login_page,name="login_page"),
    path('logout_page/',views.logout_page,name="logout_page"),

   
    
]