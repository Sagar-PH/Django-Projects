from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
#from phonenumber_field.modelfields import PhoneNumberField
from PIL import Image

# Create your models here.

class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	phone_number = models.CharField(default='+91', max_length=13, blank=True)
	profession = models.CharField(default='', max_length= 30, blank=True)
	image = models.ImageField(default='default.jpg', upload_to='profile_pics')

	def __str__(self):
		return self.user.username

	def save(self, *args, **kwargs):
		super().save(*args, **kwargs)

		img = Image.open(self.image.path)
		
		if img.height > 300 or img.width > 300:
			output_size = (300,300)
			img.thumbnail(output_size)
			img.save(self.image.path)

class FrontEnd(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    img_link = models.CharField(max_length=1000)
    html = models.TextField()
    css = models.TextField()
    javascript = models.TextField()
    
    def __str__(self):
	    return self.title

class Items(models.Model):
	name = models.CharField(default='', max_length=100)
	image = models.ImageField(default='default.jpg', upload_to='items')

	def __str__(self):
		return self.name

	def save(self, *args, **kwargs):
		super().save(*args, **kwargs)

		img = Image.open(self.image.path)
		
		if img.height > 300 or img.width > 300:
			output_size = (300,300)
			img.thumbnail(output_size)
			img.save(self.image.path)

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
	if created:
		Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_profile(sender, instance, created, **kwargs):
	instance.profile.save()