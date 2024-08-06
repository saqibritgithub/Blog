from django.db import models
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator
# Create your models here.
class ProfileModel(models):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    image = models.ImageField(defaualt='default.png', upload_to= 'profile')

    def __str__(self):
        return self.user.username

    