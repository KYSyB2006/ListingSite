from django.urls import path
from listing.views import EnseignantSpace, EtudiantSpace, EnseignantNote, EtudiantListing


urlpatterns = [
    path('EnseignantSpace/', EnseignantSpace, name='EnseignantSpace'),

    path('EtudiantSpace/', EtudiantSpace, name='EtudiantSpace'),

    path('EnseignantNote/<slug:mc>/<int:id2>/', EnseignantNote, name='EnseignantNote'),
    path('EtudiantListing/<int:id1>', EtudiantListing, name='EtudiantListing'),

]