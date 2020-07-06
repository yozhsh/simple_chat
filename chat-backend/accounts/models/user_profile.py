from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from accounts.utils import get_private_user_id


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    visible_name = models.CharField(max_length=50)
    user_own_id = models.CharField(max_length=20, unique=True, null=True, blank=True, db_index=True)
    private_user_id = models.CharField(max_length=16, default=get_private_user_id, unique=True, db_index=True)

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()
