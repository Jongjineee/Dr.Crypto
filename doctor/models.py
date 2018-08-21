from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from sorl.thumbnail import ImageField


# Create your models here.

class Category(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_category')
    sort = models.CharField(max_length=20, blank =True)

    def __str__(self):
        return '{} {}'.format(self.sort, self.user)


class Doctor(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_doctor')
    name = models.CharField(max_length=30, blank=False)
    medical_name = models.CharField(max_length=30, blank=False)
    address = models.CharField(max_length=200, blank=False)
    phone_number = models.CharField(max_length=20, blank=False)
    license_number = models.IntegerField(blank=False)
    certification = models.FileField(upload_to='documents/%Y/%m/%d/')
    uploaded_at = models.DateTimeField(auto_now_add=True)


class Enterprise(models.Model):
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='enterprise_user')
    enterprise_name = models.CharField(max_length=20, blank=True)
    enterprise_category = models.CharField(max_length=30, blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=20, blank=False)
    birth = models.CharField(max_length=30, blank=False)
    wallet_address = models.CharField(max_length=50, blank=True)
    image = models.ImageField(blank=True)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()