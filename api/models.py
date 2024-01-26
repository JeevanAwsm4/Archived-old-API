from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.utils import timezone

class DonorManager(BaseUserManager):
    def create_user(self, phone_no, password=None, **extra_fields):
        user = self.model(phone_no=phone_no, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone_no, password=None, **extra_fields):
        user = self.create_user(phone_no, password, **extra_fields)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class Donor(AbstractBaseUser):
    BLOOD_GROUPS = [
        ('', 'Select Blood Group'),
        ('A+', 'A+'),
        ('A-', 'A-'),
        ('B+', 'B+'),
        ('B-', 'B-'),
        ('AB+', 'AB+'),
        ('AB-', 'AB-'),
        ('O+', 'O+'),
        ('O-', 'O-'),
    ]

    TATTOO_CHOICES = [
        ('', 'any tattoo'),
        ('yes', 'Yes'),
        ('no', 'No'),
    ]

    name = models.CharField(max_length=255)
    blood_group = models.CharField(max_length=3, choices=BLOOD_GROUPS, default='')
    phone_no = models.CharField(max_length=10, unique=True ,null=True, blank=False)
    age = models.IntegerField()
    address = models.TextField()
    has_tattoo = models.CharField(max_length=3, choices=TATTOO_CHOICES, default='')
    district = models.ForeignKey('Districts', on_delete=models.CASCADE, blank=False, null=True)

    objects = DonorManager()

    USERNAME_FIELD = 'phone_no'

class Hospitals(models.Model):
    hospital = models.CharField(max_length=255)
    district = models.ForeignKey('Districts', on_delete=models.CASCADE, blank=False, null=True)

    def __str__(self):
        return self.hospital

class Districts(models.Model):
    district = models.CharField(max_length=255,blank=True, null=True)

    def __str__(self):
        return self.district

class Want(models.Model):
    BLOOD_GROUPS = [
        ('', 'Select Blood Group'),
        ('A+', 'A+'),
        ('A-', 'A-'),
        ('B+', 'B+'),
        ('B-', 'B-'),
        ('AB+', 'AB+'),
        ('AB-', 'AB-'),
        ('O+', 'O+'),
        ('O-', 'O-'),
    ]
    NO_OF_UNITS = [
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
    ]

    name = models.CharField(max_length=255)
    age = models.CharField(max_length=3, null=True, blank=True)
    blood_group = models.CharField(max_length=3, choices=BLOOD_GROUPS, default='')
    phone_no = models.CharField(max_length=15,)
    no_of_units_here = models.CharField(max_length=10, blank=False, null=True, choices=NO_OF_UNITS)
    hospital = models.CharField(max_length=255, null=True, blank=True)
    district = models.ForeignKey('Districts', on_delete=models.CASCADE, blank=False, null=True)
    created_at = models.DateTimeField(auto_now_add=True,null=True)
