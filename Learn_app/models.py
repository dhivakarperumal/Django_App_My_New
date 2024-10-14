from django.db import models
from django.contrib.auth.models import User 


class Course(models.Model):
    course_img = models.ImageField(upload_to='course_images/')
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=300, blank=True)
    description = models.TextField()
    trainer_img = models.ImageField(upload_to='trainer_images/')
    trainer_name = models.CharField(max_length=200)
    course_price = models.DecimalField(max_digits=10, decimal_places=2)
    seat_available = models.IntegerField()
    schedule_time = models.DateTimeField()
    course_video = models.FileField(upload_to='course_videos/')
    trending = models.BooleanField(default=False)
    

    def __str__(self):
        return self.title

class Events(models.Model):
    event_img = models.ImageField(upload_to='event_images/', blank=True, null=True)
    title = models.CharField(max_length=200)
    event_date = models.DateTimeField()
    descriptions = models.TextField()

    def __str__(self):
        return self.title
    
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name} - {self.subject}"

