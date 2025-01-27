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
            if self.id is None or self.has_usable_password():
                self.set_password(self.password)
            if self.role == 'IADMINISTRATOR' or self.role == '':
               self.is_superuser = True
               self.is_staff = True
            elif self.role == 'PROFESSEUR':
               self.is_superuser = False
               self.is_staff = True
            else:
               self.is_superuser = False
               self.is_staff = False

            super().save(*args, **kwargs)

