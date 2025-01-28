from django.db.models.signals import post_save
from django.dispatch import receiver

from listing.models import Etudiant, Dispenser, Matiere
from authentication.models import Userlisting


@receiver(post_save, sender=Etudiant)
def create_user_for_new_etudiant(sender, instance, created, **kwargs):
    if created:
       userlisting = Userlisting.objects.create(username=instance.Nom+' '+instance.Prenom, role='Etudiant', profile_photo=instance.image, Matricule=instance.Matricule)
       userlisting.set_password(instance.Matricule)
       userlisting.save()

@receiver(post_save, sender=Etudiant)
def create_user_for_new_etudiant(sender, instance, created, **kwargs):
    if created:
       userlisting = Userlisting.objects.create(username=instance.Nom+' '+instance.Prenom, role='Etudiant', profile_photo=instance.image, Matricule=instance.Matricule)
       userlisting.set_password(instance.Matricule)
       userlisting.save()

# @receiver(post_save, sender=Etudiant)
# def create_listing(sender, instance, created, **kwargs):
#     if created:
#         dispensers = Dispenser.objects.all().filter(idClasse=instance.classe)
#         matieres = Matiere.objects.all()
#         for dispenser in dispensers:
#             for matiere in matieres:
#                 if matiere.idMatiere == dispenser.idMatiere:
#                     Note.objects.create()
            