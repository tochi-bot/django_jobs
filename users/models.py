from django.db import models
from django.contrib.auth.models import AbstractUser
from cloudinary.models import CloudinaryField

class user(AbstractUser):
    email=models.EmailField(unique=True)
    is_recruiter=models.BooleanField(default=False)
    is_applicant=models.BooleanField(default=False)

    has_resume=models.BooleanField(default=False)
    has_company=models.BooleanField(default=False)

