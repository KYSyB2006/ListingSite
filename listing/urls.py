from django.urls import path
from listing.views import EnseignantSpace, EtudiantSpace


urlpatterns = [
    path('EnseignantSpace/', EnseignantSpace, name='EnseignantSpace'),
    path('EtudiantSpace/', EtudiantSpace, name='EtudiantSpace'),


]