from django.db import models
from django.contrib.auth.models import User


# # Create your models here.
# class Profile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     dp = models.ImageField(
#         upload_to='dp/', default='default.png', null=True, blank=True)
#     contact = models.CharField(max_length=50)
#     marital = models.BooleanField(default=False)

#     def __str__(self):
#         return self.user.username
