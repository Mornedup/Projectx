from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from datetime import date

# Create your models here.
def profile_img_path(instance, filename):
    return 'user_{0}/profile_image/{1}/{2}'.format(instance.user.id, date.today(), instance.profile_image.name)

class UserProfile(models.Model):
    user=models.OneToOneField(User)
    city=models.CharField(default='', max_length=100, blank=True)
    phone=models.IntegerField(default=0, blank=True)
    website=models.URLField(default='', blank=True)
    profile_image=models.ImageField(upload_to=profile_img_path, blank=True)
    description=models.TextField(blank=True)

    def __str__(self):
        return self.user.username

def create_profile(sender, **kwargs):
    if kwargs['created']:
        user_profile = UserProfile.objects.create(user=kwargs['instance'])

post_save.connect(create_profile, sender=User)
