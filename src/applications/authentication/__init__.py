"""
    Authentication Module
"""
import inspect

from django.apps import apps as django_apps
from django.core.exceptions import ImproperlyConfigured, PermissionDenied
from django.utils.module_loading import import_string
from core import settings


def load_backend(path):
    return import_string(path)()


def _get_backends(return_tuples=False):
    backends = []
    for backend_path in settings.CUSTOM_AUTHENTICATION_BACKENDS:
        backend = load_backend(backend_path)
        backends.append((backend, backend_path) if return_tuples else backend)
    if not backends:
        raise ImproperlyConfigured(
            'No authentication backends have been defined. Does '
            'AUTHENTICATION_BACKENDS contain anything?'
        )
    return backends


def authenticate(request=None, **credentials):
    """
    If the given credentials are valid, return a User object.
    """
    for backend, backend_path in _get_backends(return_tuples=True):
        try:
            inspect.getcallargs(backend.authenticate, request, **credentials)
        except TypeError:
            # This backend doesn't accept these credentials as arguments. Try the next one.
            continue
        try:
            user = backend.authenticate(request, **credentials)
        except PermissionDenied:
            # This backend says to stop in our tracks - this user should not be allowed in at all.
            break
        if user is None:
            continue
        # Annotate the user object with the path of the backend.
        user.backend = backend_path
        return user


def get_user_model():
    """
    Return the Account model that is active in this project.
    """
    try:
        return django_apps.get_model(settings.CUSTOM_AUTH_USER_MODEL, require_ready=False)
    except ValueError:
        raise ImproperlyConfigured("CUSTOM_AUTH_USER_MODEL must be of the form 'app_label.model__name")
    except LookupError:
        raise ImproperlyConfigured(
        "CUSTOM_AUTH_USER_MODEL refers to model'%s' that hast not been installed" % settings.CUSTOM_AUTH_USER_MODEL
    )
