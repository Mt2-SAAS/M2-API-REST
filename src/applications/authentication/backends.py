from applications.authentication import get_user_model


UserModel = get_user_model()


class BaseBackend:
    def authenticate(self, request, **kwargs):
        return None

    def get_user(self, user_id):
        return None


class ModelBackend(BaseBackend):
    """
    Authenticates against settings.AUTH_USER_MODEL.
    """

    def authenticate(self, request, username=None, password=None, **kwargs):
        if username is None:
            username = kwargs.get(UserModel.USERNAME_FIELD)
        if username is None or password is None:
            return
        try:
            user = UserModel.user = UserModel.objects.get(login=username)
        except UserModel.DoesNotExist:
            # Run the default password hasher once to reduce the timing
            # difference between an existing and a nonexistent user (#20760).
            UserModel().set_password(password)
        else:
            if user.check_password(password) and not user.is_banned:
                return user

    # def user_can_authenticate(self, user):
    #     """
    #     Reject users with is_active=False. Custom user models that don't have
    #     that attribute are allowed.
    #     """
    #     is_active = getattr(user, 'status', None)
    #     if is_active == 'OK':
    #         return True
    #     return False

