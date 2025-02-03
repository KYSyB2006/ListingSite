from django.db import models
from django.core.validators import MinLengthValidator
from django.core.validators import MaxValueValidator, MinValueValidator


class Matiere(models.Model):
    idMatiere = models.fields.AutoField(primary_key=True)
    Id_UE = models.fields.CharField( max_length=50)
    Coef = models.fields.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(20)], default=0)
    enseignant = models.fields.CharField(max_length=50)

    def __str__(self):
     return f'{self.Id_UE}'

class Classe(models.Model):

    class Niveau(models.TextChoices):
        Niveau_1 = '1'
        Niveau_2 = '2'
        Niveau_3 = '3'
        Niveau_4 = '4'
        Niveau_5 = '5'

    idClasse = models.fields.AutoField(primary_key=True)
    Code = models.fields.CharField( max_length=20)
    Filiere = models.fields.CharField(max_length=20)
    niveau = models.fields.TextField(choices=Niveau.choices, default='0')

    def __str__(self):
        return f'{self.Filiere} {self.niveau}'

class Etudiant(models.Model):
    class Sexe(models.TextChoices):
        Feminin = 'F'
        Masculin = 'M'

    idEtudiant = models.fields.AutoField(primary_key=True)
    Matricule = models.fields.CharField(  max_length=20, unique=True)
    Nom = models.fields.CharField(max_length=50)
    Prenom = models.fields.CharField(max_length=50)
    classe = models.ForeignKey(Classe, on_delete=models.CASCADE, related_name='etudiants')
    Sexe = models.fields.TextField(choices=Sexe.choices, default='')
    image = models.ImageField(default='C:/Users/YONTA/Desktop/PROJET IUC/projetPy/projetPy/photo_profil_base.jpg')
    last_login = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.Nom}  {self.Matricule}'

class Dispenser(models.Model):
    idClasse = models.ForeignKey(Classe, related_name='dispenser', default='iuc', on_delete=models.CASCADE)
    idMatiere = models.ForeignKey(Matiere, on_delete=models.CASCADE, default='cours')
    semestre = models.fields.IntegerField()


class Note(models.Model):
    class N_Eval(models.IntegerChoices):
        Evaluation_1 = 1
        Evaluation_2 = 2
        Evaluation_3 = 3

    idEtudiant = models.ForeignKey(Etudiant, on_delete=models.CASCADE)
    idMatiere = models.ForeignKey(Matiere, on_delete=models.CASCADE)
    n_Eval = models.fields.IntegerField(choices=N_Eval.choices, default=0)
    valeur = models.fields.FloatField(validators=[MinValueValidator(0), MaxValueValidator(20)], null=True, blank=True)
    remarques = models.fields.TextField(max_length=100, default="la reussite s'arrache")
    dateEval = models.fields.DateTimeField()
    dateRemplissage = models.fields.DateTimeField()

class Meta:
        unique_together = ('etudiants', 'classe')
