from django.db.models.functions import datetime
from django.http import HttpResponse
from django.shortcuts import render
from django.db.models import Q
from pygments.lexer import combined

from listing.models import Dispenser, Matiere, Classe, Etudiant, Note
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

        return render(request, 'Enseignant/EnseignantSpace.html', {'user':request.user, 'id':3, 'classes': classes, 'matieres': matieres})
    return HttpResponse("Unauthorized", status=401)


def EnseignantNote(request, mc=None, id2=None):
    if len(mc) > 1:
        id1 = mc[1]
        id3 = mc[0]
    else:
        id1 = mc[0]
        id3 = None

    if not request.user.is_authenticated:
        return render(request, 'login')
    username = request.user.username
    matieres = Matiere.objects.filter(enseignant=username)
    classes = []
    noteE = []
    for matiere in matieres:
        classeProf = Dispenser.objects.filter(idMatiere=matiere.idMatiere).select_related('idClasse')
        classes.extend(classeProf)
    etudiantClasse = Etudiant.objects.filter(classe=id1)
    if id2 is not None:
        for etudiant in etudiantClasse:
            note = Note.objects.filter(Q(idEtudiant=etudiant.idEtudiant) & Q(n_Eval=id2))
            noteE.extend(note)
        if request.method == 'POST':
            for etudiant in etudiantClasse:
                NoteStudent = Note.objects.filter(idEtudiant=etudiant.idEtudiant, idMatiere=id3, n_Eval=id2)
                valeur= request.POST.get('valeurNote_' + str(etudiant.idEtudiant))
                remarque=request.POST.get('remarques_' + str(etudiant.idEtudiant))
                if len(NoteStudent) == 0 :
                    Note.objects.create(idEtudiant=etudiant.idEtudiant, idMatiere=id3, n_Eval=id2, valeur=valeur, remarques=remarque, dateEval='2024-11-12 12:00:00.000000', dateRemplissage= datetime.now())
                else:
                    NoteStudent.valeur = request.POST.get('valeurNote_'+str(etudiant.idEtudiant))
                    NoteStudent.remarques = request.POST.get('valeurNote_'+str(etudiant.idEtudiant))
                    NoteStudent.dateRemplissage = datetime.now()
                    NoteStudent.save()


                print(len(NoteStudent))
                print(etudiant.Nom)
                print(request.POST.get('valeurNote_'+str(etudiant.idEtudiant)))
                print(request.POST.get('remarques_'+str(etudiant.idEtudiant)))
    return render(request, 'Enseignant/EnseignantNote.html', {
        'user':request.user,
        'notes':noteE, 'id1':id1, 'id2':id2,
        'etudiants':etudiantClasse, 'classes': classes, 'matieres': matieres})


def EtudiantSpace(request):
    return render(request, 'Etudiant/EtudiantSpace.html', {'user':request.user})