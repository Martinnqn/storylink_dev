# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.

# <FirstCodeSnippet>
import msal
import os
import time
from django.conf import settings


def get_msal_app(cache=None):
    # Initialize the MSAL confidential client
    auth_app = msal.ConfidentialClientApplication(
        settings.AZURE_B2C_APP_ID,
        authority=settings.AZURE_AD_AUTHORITY,
        client_credential=settings.AZURE_B2C_APP_SECRET,
        token_cache=cache)
    return auth_app

# Method to generate a sign-in flow
def get_sign_in_flow():
    auth_app = get_msal_app()
    scopes = settings.AZURE_B2C_SCOPES.split(" ")
    return auth_app.initiate_auth_code_flow(scopes)

def get_access_token():
    auth_app = get_msal_app()
    scopes = settings.AZURE_B2C_SCOPES.split(" ")
    resp = auth_app.acquire_token_for_client(scopes)
    print(resp)
    return resp['access_token']
