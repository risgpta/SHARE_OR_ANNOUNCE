from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver


class Profiles(models.Model):
    meta = {
        "indexes": ["email"],
    }

    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    date_of_birth = models.DateField(blank=True)
    bio = models.TextField(blank=True)
    location = models.CharField(max_length=30, blank=True)
    email = models.EmailField()
    phone_number = models.CharField(max_length=12, blank=True)
    website = models.URLField(blank=True)

    def __str__(self):
        return self.first_name + self.last_name + self.email


@receiver(pre_save, sender=Profiles)
def set_sold(sender, instance, **kwargs):
    """
    Signal receiver function to set the published_at field just before saving the Book instance.
    """
    # Check if the published_at field is not already set
    if instance.first_name == 'SOLD':
        print(instance)
        instance.first_name = 'duplicate'
        instance.last_name = 'duplicate'
        instance.save()


# Connect the signal receiver to the pre_save signal
pre_save.connect(set_sold, sender=Profiles)


