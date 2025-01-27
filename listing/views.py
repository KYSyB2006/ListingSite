from django.shortcuts import render
from listing.models import Dispenser, Matiere, Classe
from authentication.models import Userlisting
# Create your views here.
def EnseignantSpace(request):
    if request.user.is_authenticated:
        username = request.user.username
        matieres = Matiere.objects.filter(enseignant=username)
        classes = []
        for matiere in matieres:
            classeProf = Dispenser.objects.filter(idMatiere=matiere.idMatiere).select_related('idClasse')
            classes.extend(classeProf)
        # for classe in classes:
        #     print(classe.idClasse.Filiere+''+classe.idClasse.niveau)
    return render(request, 'Enseignant/EnseignantSpace.html', {'user':request.user, 'classes': classes, 'matieres': matieres})

def EtudiantSpace(request):
    return render(request, 'Etudiant/EtudiantSpace.html', {'user':request.user})