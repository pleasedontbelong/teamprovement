from django.contrib.auth import get_user_model

UserModel = get_user_model()


class SimpleAuthBackend:
    """
    Authenticates against settings.AUTH_USER_MODEL.
    """

    def authenticate(self, request, **kwargs):
        username = kwargs.get(UserModel.USERNAME_FIELD)
        user, _ = UserModel._default_manager.get_or_create(username=username)
        return user

    def get_user(self, user_id):
        try:
            user = UserModel._default_manager.get(pk=user_id)
        except UserModel.DoesNotExist:
            return None
        return user
