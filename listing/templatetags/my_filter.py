from django import template
from django.shortcuts import redirect

register = template.Library()

@register.filter
def dictionnary(tab1,tab2):
    tab = {
        'tab1':tab1,
        'tab2':tab2
    }
    return  tab

@register.filter
def PlaceholderNote(etudiant, notes):
    for note in notes:
        if note.idEtudiant.idEtudiant == etudiant.idEtudiant:
            return note.valeur
    return 0

@register.filter
def PlaceholderNoteRemarque(etudiant, notes):
    for note in notes:
        if note.idEtudiant.idEtudiant == etudiant.idEtudiant:
            return note.remarques
    return 'Ajouter une remarque'

@register.filter
def urlStr(mat, id1):
    print('mat',mat)
    print('id1', id1)
    print(str(mat)+str(id1))
    return str(mat)+str(id1)


