from django.contrib.auth.models import AbstractUser
from django.db import models

class Userlisting(AbstractUser):

    ROLE_CHOICES = (
        ('IADMINISTRATOR', 'IAdministrateur'),
        ('PROFESSEUR', 'Professeur'),
        ('ETUDIANT', 'Etudiant'),
    )
    profile_photo = models.ImageField(upload_to="profile_pics",  verbose_name='Photo de profil', default='photo_profil_base.jpg')
    role = models.CharField(max_length=30, choices=ROLE_CHOICES, verbose_name='Role')
    Matricule = models.CharField(max_length=30, default='iuc')

    def __str__(self):
        return self.username

    def save(self, *args, **kwargs):
        if self.role == 'IADMINISTRATOR':
           self.is_superuser = True
           self.is_staff = True
           self.set_password(self.password)
        elif self.role == '':
           self.is_superuser = True
           self.is_staff = True
        elif self.role == 'PROFESSEUR':
           self.is_superuser = False
           self.is_staff = True
           self.set_password(self.password)
        else:
           self.is_superuser = False
           self.is_staff = False
           self.set_password(self.password)

        super().save(*args, **kwargs)

