from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
    ROLES=(
        ("manager","Manager"),
        ("user","User"),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='userprofile')
    profile_pic = models.ImageField(upload_to='profiles/', blank=True, null=True)
    role=models.CharField(max_length=10, choices=ROLES, default="user") 

    def __str__(self):
        return self.user.username

