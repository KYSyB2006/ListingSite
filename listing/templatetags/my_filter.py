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
    return str(mat)+str(id1)

@register.filter
def noteMat(notes,matiere):
    return notes.filter(idMatiere=matiere.idMatiere)

@register.filter
def nbrDs(notes):
    for i in range(1,4):
        if len(notes.filter(n_Eval=i))>0:
            return i
    return 0

@register.filter
def noteMatDScum(noteMat,ds):
    noteDS=0
    notedsi = noteMat.filter(n_Eval=ds)
    if len(notedsi) > 0:
        for notem in noteMat:
            if notem.n_Eval <= ds :
                noteDS += notem.valeur
        return round(noteDS/ds, 2)
    return '-'

@register.filter
def noteMatDSi(noteMat,ds):
    notedsi = noteMat.filter(n_Eval=ds)
    if len(notedsi) > 0:
        return round(notedsi[0].valeur, 2)
    return '-'

@register.filter
def noteCoefMatDSi(noteMat,ds):
    coef=noteMat[0].idMatiere.Coef
    notedsi = noteMat.filter(n_Eval=ds)
    if len(notedsi) > 0:
        return round(coef*notedsi[0].valeur, 2)
    return '-'

@register.filter
def noteApprec(notes, matiere):
    b=noteMat(notes, matiere)
    c=nbrDs(notes)
    a =noteMatDScum(b, c)
    if a!='-':
        a=int(a)
        if 0 < a < 6:
            return 'non valide,    Mediocre'
        elif 6 <= a < 12:
            return 'non valide,   insuffisant'
        elif 12 <= a < 13.5:
            return '  valide,      passable'
        elif 13.5 <= a < 15:
            return '  valide,     assez bien'
        elif 15 <= a < 16.5:
            return '  valide,        Bien'
        elif 16.5 <= a < 18.5:
            return '  valide,      Tres bien'
        elif 18.5 <= a < 20:
            return '  valide,      Excellent'
    return a

@register.filter
def NoteRemarque(noteMat,ds):
    notedsi = noteMat.filter(n_Eval=ds)
    if len(notedsi) == 1:
         return notedsi[0].remarques
    return "Rien n'est encore perdu, suffit juste d'y mettre du sien"

@register.filter
def noteApprecdsi(noteMat, ds):
    a =noteMatDSi(noteMat,ds)
    if a!='-':
        a=int(a)
        if 0 < a < 6:
            return 'non valide,    Mediocre'
        elif 6 <= a < 12:
            return 'non valide,   insuffisant'
        elif 12 <= a < 13.5:
            return '  valide,      passable'
        elif 13.5 <= a < 15:
            return '  valide,     assez bien'
        elif 15 <= a < 16.5:
            return '  valide,        Bien'
        elif 16.5 <= a < 18.5:
            return '  valide,      Tres bien'
        elif 18.5 <= a < 20:
            return '  valide,      Excellent'
    return a

@register.filter
def TotalCredit(matieres):
    Tcredits=0
    for matiere in matieres:
        Tcredits+=matiere.Coef
    if Tcredits > 0:
        return Tcredits
    return '-'

@register.filter
def MatObtenudsi(notes, id1):
    note=notes.filter(n_Eval=id1)
    return note

@register.filter
def TotalCreditObtenu(MatObtenudsi):
    Tcredits=0
    notes=MatObtenudsi
    for note in notes:
        if note.valeur>=12:
            Tcredits+=note.idMatiere.Coef
    if Tcredits>0:
        return Tcredits
    return '-'

@register.filter
def notesMatsdsi(notes,id1):
    return notes.filter(n_Eval=id1)

@register.filter
def TotalPoints(notesMatsdsi):
    Tpoints=0
    for note in notesMatsdsi:
        if note.valeur!=0:
            Tpoints+=(note.valeur)*(note.idMatiere.Coef)
    if Tpoints>0:
        return int(Tpoints)
    return '-'


@register.filter
def Moyenne(notesMatsdsi,matieres):
    a=TotalPoints(notesMatsdsi)
    b=TotalCredit(matieres)
    if a!='-' and b!='-':
        a=int(a)
        b=int(b)
        return round(a/b, 2)
    return'-'

@register.filter
def moyenneApprecdsi(notesMatsdsi,matieres):
    a =Moyenne(notesMatsdsi,matieres)
    if a!='-':
        a=int(a)
        if 0 < a < 6:
            return 'non valide,    Mediocre'
        elif 6 <= a < 12:
            return 'non valide,   insuffisant'
        elif 12 <= a < 13.5:
            return '  valide,      passable'
        elif 13.5 <= a < 15:
            return '  valide,     assez bien'
        elif 15 <= a < 16.5:
            return '  valide,        Bien'
        elif 16.5 <= a < 18.5:
            return '  valide,      Tres bien'
        elif 18.5 <= a < 20:
            return '  valide,      Excellent'
    return a

@register.filter
def NoteEtu(notes,etudiant):
    noteE = notes.filter(idEtudiant=etudiant)
    if notes.filter(idEtudiant=etudiant).count()>0:
        return noteE
    return 0

@register.filter
def TotalCreditCumObtenu(NoteEtu,matieres):
    Tcredits=0
    notes=NoteEtu
    for i in range(1,4):
        if len(notes.filter(n_Eval=i))>0:
            ds=i
    for matiere in matieres:
        noteDS = 0
        notesF=notes.filter(idMatiere=matiere.idMatiere)
        for note in notesF:
            if note.n_Eval <= ds:
                noteDS += note.valeur
        if noteDS/ds >= 12:
            Tcredits+=matiere.Coef
    if Tcredits>0:
        return Tcredits
    return '-'

@register.filter
def TotalPointsCum(NoteEtu,matieres):
    notes = NoteEtu
    for i in range(1, 4):
        if len(notes.filter(n_Eval=i)) > 0:
            ds = i
    Tpoints = 0
    for matiere in matieres:
        notesF=notes.filter(idMatiere=matiere)
        noteDS = 0
        for note in notesF:
            if note.n_Eval <= ds:
                noteDS += note.valeur
        noteCum=noteDS/ds
        if noteCum != 0:
            Tpoints += (noteCum) * (matiere.Coef)
    if Tpoints > 0:
        return round(Tpoints,2)
    return '-'

@register.filter
def MoyenneCum(NoteEtu,matieres):
    a=TotalPointsCum(NoteEtu,matieres)
    b = TotalCredit(matieres)
    if a != '-' and b != '-':
        a = int(a)
        b = int(b)
        return round(a / b, 2)
    return '-'

@register.filter
def moyenneApprecdsiCum(MoyenneCum):
    a =MoyenneCum
    if a!='-':
        a=int(a)
        if 0 < a < 6:
            return 'non valide,    Mediocre'
        elif 6 <= a < 12:
            return 'non valide,   insuffisant'
        elif 12 <= a < 13.5:
            return '  valide,      passable'
        elif 13.5 <= a < 15:
            return '  valide,     assez bien'
        elif 15 <= a < 16.5:
            return '  valide,        Bien'
        elif 16.5 <= a < 18.5:
            return '  valide,      Tres bien'
        elif 18.5 <= a < 20:
            return '  valide,      Excellent'
    return a