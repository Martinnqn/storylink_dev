from apps.users.models import CustomUser
from rest_framework import authentication
from rest_framework import exceptions
from azure_ad_verify_token import verify_jwt


class AzureADAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):
        user_data = getPayload(self, request)

        if not user_data.username:
            return None

        try:
            # obtener un id de usuario, nombre, apellido, email desde los
            # claim del token.
            # crear un user con CustomUser(username=username, email=email,....)
            # y retornar ese usuario sin guardarlo en la base de datos
            user = CustomUser.objects.get(username=user_data.username)
        except CustomUser.DoesNotExist:
            raise exceptions.AuthenticationFailed('No such user')

        return (user, None)


def getPayload(self, request):
    azure_ad_app_id = 'c23486d4-c9ee-4e7f-b0ef-8a5222db50b5'
    azure_ad_issuer = 'https://storylinkb2c.b2clogin.com/tfp/8f366d86-6d3f-43f5-81e1-d84cd7bd349b/b2c_1_reactjs_susin/v2.0/'
    azure_ad_jwks_uri = 'https://storylinkb2c.b2clogin.com/storylinkb2c.onmicrosoft.com/b2c_1_reactjs_susin/discovery/v2.0/keys'
    return verify_jwt(
        token="eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImtpZCI6Ilg1ZVhrNHh5b2pORnVtMWtsMll0djhkbE5QNC1jNTdkTzZRR1RWQndhTmsifQ.eyJpc3MiOiJodHRwczovL3N0b3J5bGlua2IyYy5iMmNsb2dpbi5jb20vdGZwLzhmMzY2ZDg2LTZkM2YtNDNmNS04MWUxLWQ4NGNkN2JkMzQ5Yi9iMmNfMV9yZWFjdGpzX3N1c2luL3YyLjAvIiwiZXhwIjoxNjEyMDE2Mzc3LCJuYmYiOjE2MTIwMTI3NzcsImF1ZCI6ImMyMzQ4NmQ0LWM5ZWUtNGU3Zi1iMGVmLThhNTIyMmRiNTBiNSIsIm9pZCI6IjNmODZhZDI0LTJkNjUtNDZkZi05YWQyLTNjYjViMDg2M2IzMCIsInN1YiI6IjNmODZhZDI0LTJkNjUtNDZkZi05YWQyLTNjYjViMDg2M2IzMCIsImdpdmVuX25hbWUiOiJNYXJ0aW4iLCJmYW1pbHlfbmFtZSI6IkJlcm11ZGV6IiwibmFtZSI6InVua25vd24iLCJlbWFpbHMiOlsiYmVybXVkZXpfbWFydGluLm5xbkBob3RtYWlsLmNvbSJdLCJ0ZnAiOiJCMkNfMV9yZWFjdGpzX3N1c2luIiwibm9uY2UiOiI4YTU2M2FmNi0xMmNlLTQ3YTItYTI0Ni0wNjQzZWEwMzUwMDkiLCJzY3AiOiJGaWxlcy5SZWFkIiwiYXpwIjoiY2JjYTJkMzgtZmE2OC00MjM2LWJkYmEtZjk3ZmMwY2ZmYjlkIiwidmVyIjoiMS4wIiwiaWF0IjoxNjEyMDEyNzc3fQ.fbkzxgVhbcnJisHHbapBsbMI5gGFlx0K4U2A_Dti7atzVMx_YqhXKYupMdWL-cVlxHUgrN9dxaL9WmO6YatLWhj4ykQzt91EjUGn9iDkXHn3BPK7mxnHHkt1MtVqE4D-5L1cDYG__W5ws2Q-PRwF5Wgt8Ry7g1CgG0GBSKIqXQYLcmhqz8vf7QI9tc7KqqzncwEmaIMRxDqGAELm17wvxMixtVq5-VAkTdPnR55C_2bdBv2PefPbgndOUjcWGfdK8vnZwAXqSUDGCc3Jo03yV7X79uVUS4C8C2daw4woeg37vUi1s3s6Dm2U1bMUSyfw-zu910K3Gr9gZGG8YiAEZg",
        valid_audiences=[azure_ad_app_id],
        issuer=azure_ad_issuer,
        jwks_uri=azure_ad_jwks_uri,
    )
