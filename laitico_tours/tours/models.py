from django.db import models
from django.utils.text import slugify
from tinymce.models import HTMLField

# Create your models here.
class Destination(models.Model):
    name = models.CharField(max_length=255, unique=True)
    slug=models.SlugField(unique=True, blank=True)
    description = HTMLField()
    image = models.ImageField(upload_to='destinations/')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    is_popular = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

class Booking(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    destination = models.ForeignKey("Destination", on_delete=models.CASCADE)
    booking_date = models.DateTimeField(auto_now_add=True)
    from_date = models.DateField()
    to_date = models.DateField()
    pax = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2, editable=False)

    def save(self, *args, **kwargs):
        """Automatically fetch price from the selected destination before saving."""
        if self.destination:
            self.price = self.destination.price
        super().save(*args, **kwargs)

    def total_price(self):
        """Calculate total price based on pax and destination price."""
        return self.pax * self.price

    def __str__(self):
        return f"{self.name} - {self.destination.name} ({self.from_date} to {self.to_date})"
    
class Inquiry(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    phone = models.CharField(max_length=20)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.subject