from django.http import HttpResponseForbidden
from functools import wraps


class BlockSuperuserMixin:
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_superuser or request.user.is_staff:
            return HttpResponseForbidden(f"Espace Etudiant réservé, administrateur { request.user.username }")
        return super().dispatch(request, *args, **kwargs)

def block_superuser(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if request.user.is_superuser :
            return HttpResponseForbidden(f"Espace Etudiant réservé, administrateur { request.user.username }")
        return view_func(request, *args, **kwargs)
    return _wrapped_view

def role_required(required_roles):
    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view(request, *args, **kwargs):
            if not request.user.is_authenticated:
                return HttpResponseForbidden("Bien vouloir vous connecté.")
            if request.user.role not in required_roles:
                return HttpResponseForbidden("Désolé, accès refusé! Espace professeur réservé." )
            return view_func(request, *args, **kwargs)
        return _wrapped_view
    return decorator

def etudiant_required(nonrequired_etudiant):
    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view(request, *args, **kwargs):
            if not request.user.is_authenticated:
                return HttpResponseForbidden("Bien vouloir vous connecté.")
            if request.user.role in nonrequired_etudiant:
                return HttpResponseForbidden("Accès refusé! Espace Etudiant réservé." )
            return view_func(request, *args, **kwargs)
        return _wrapped_view
    return decorator

