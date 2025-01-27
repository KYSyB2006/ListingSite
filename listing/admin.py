from django.contrib import admin
from listing.models import Etudiant, Matiere, Classe, Dispenser

# Register your models here.

admin.site.register(Etudiant)
admin.site.register(Classe)
admin.site.register(Dispenser)
admin.site.register(Matiere)


