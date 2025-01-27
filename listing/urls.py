from django.urls import path
from listing.views import EnseignantSpace, EtudiantSpace, EnseignantNote


urlpatterns = [
    path('EnseignantSpace/', EnseignantSpace, name='EnseignantSpace'),
    path('EtudiantSpace/', EtudiantSpace, name='EtudiantSpace'),
    path('EnseignantNote/<int:id>', EnseignantNote, name='EnseignantNote'),

]