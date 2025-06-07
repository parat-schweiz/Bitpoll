from mozilla_django_oidc.auth import OIDCAuthenticationBackend

class ParatOIDCOIDCAuthenticationBackend(OIDCAuthenticationBackend):
    def create_user(self, claims):
        user = super(ParatOIDCOIDCAuthenticationBackend, self).create_user(claims)

        user.username = claims.get('name', '')
        user.save()

        return user

    def update_user(self, user, claims):
        user.username = claims.get('name', '')
        user.save()

        return user
