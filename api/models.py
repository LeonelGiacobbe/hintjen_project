from django.db import models
from django.utils import timezone
from django.utils.text import slugify
from django.core.validators import MinLengthValidator

class Device(models.Model):
    name = models.CharField()
    is_online = models.BooleanField(default=True)
    last_seen = models.DateTimeField("last time the device was online", auto_now=True)

class Server(models.Model):
    # Used later in 'status' field
    STATUS_CHOICES = [
        ('stopped', 'Stopped'),
        ('starting', 'Starting'),
        ('running', 'Running'),
        ('error', 'Error'),
    ]

    name = models.CharField(
        max_length=50,  # maximum length
        validators=[MinLengthValidator(3)]  # minimum length
    )

    # subdomain is automatically generated when saved, will have format => name-{i}
    subdomain = models.SlugField(max_length=100, unique=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='stopped')
    # Populate upon creation
    created_at = models.DateTimeField(auto_now_add=True)
    # Establish relatonship with Device class
    device = models.ForeignKey(Device, null=True, blank=True, on_delete=models.SET_NULL)

    def save(self, *args, **kwargs):
        if not self.pk: # only create slug if this is a new object
            base_slug = slugify(self.name)
            slug = base_slug
            counter = 2
            
            # Iterate until name-{i} is not in database, and set that as subdomain
            # To ensure uniqueness in the db
            # using __iexact to make it case insensitive
            while Server.objects.filter(subdomain__iexact=slug).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
                
            self.subdomain = slug
        super().save(*args, **kwargs)


