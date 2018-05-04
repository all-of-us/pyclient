"""OAuth against the AoU Workbench API using bearer tokens.

The credentials are obtained by oauth2client, from one of:
*   Google application default credentials (expected case, from notebook servers).
*   A private key file, path specified in GOOGLE_APPLICATION_CREDENTIALS environment variable.

GoogleCredentials.create_scoped() is a noop for application-default credentials. (However, it is
used when GOOGLE_APPLICATION_CREDENTIALS is defined and they key is read from a file.) For
application default credentials, the service account's scopes are set ahead of time, like:

  SCOPES="https://www.googleapis.com/auth/userinfo.profile"
  SCOPES+=",https://www.googleapis.com/auth/userinfo.email"
  gcloud compute instances set-service-account $INSTANCE_ID --zone us-west1-b \
      --service-account $PET_SA_NAME@$PROJECT.iam.gserviceaccount.com \
      --scopes "$SCOPES"

See https://www.googleapis.com/oauth2/v3/tokeninfo?access_token= for debugging.
"""

import time

from oauth2client.client import GoogleCredentials

from aou_workbench_client.config import all_of_us_config
from aou_workbench_client.swagger_client.api_client import ApiClient
from aou_workbench_client.swagger_client.configuration import Configuration

# These are sometimes ignored, see module doc.
CLIENT_OAUTH_SCOPES = (
      'https://www.googleapis.com/auth/userinfo.profile',
      'https://www.googleapis.com/auth/userinfo.email',
)


class OauthConfiguration(Configuration):
    """Self-refreshing oauth API client configuration."""
    def __init__(self, force=False, **kwargs):
        Configuration.__init__(self, **kwargs)
        self.force = force
        self.token_expiration = None

    def auth_settings(self):
        # check expiry
        if (not self.access_token or
            self.force or (time.time() >= self.token_expiration)):
            self.access_token, self.token_expiration = _get_bearer_token_and_expiration()
        return Configuration.auth_settings(self)


# TODO: This ApiClient should self-refresh its credentials. Currently this
# ApiClient must not be cached, as this will lead to token expiration.
def get_authenticated_swagger_client(force=False, debug=False):
    """Returns a Swagger ApiClient set up to make authenticated calls to the Workbench API.
    """
    conf = OauthConfiguration(force)
    conf.debug = debug
    conf.host = all_of_us_config.api_host
    return ApiClient(conf)


def _get_bearer_token_and_expiration():
    """Fetches a new token. Returns (token string, expiration time epoch seconds)."""
    # Conservatively estimate token expiration time by recording token fetch time before initiating
    # the request.
    t = int(time.time())

    # The default, unscoped credentials provide an access token.
    creds = GoogleCredentials.get_application_default()
    # Scoped credentials provide the bearer token we need. However, create_scoped is sometimes
    # ignored, see the module doc.
    scoped_creds = creds.create_scoped(CLIENT_OAUTH_SCOPES)
    token_info = scoped_creds.get_access_token()

    return token_info.access_token, t + token_info.expires_in
