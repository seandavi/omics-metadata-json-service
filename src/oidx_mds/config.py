from pydantic import BaseSettings, PostgresDsn
from google.cloud import secretmanager


class Settings(BaseSettings):
    """Settings for the app"""

    app_name: str = "oidx_mds"
    app_version: str = "0.1.0"
    app_description: str = "OIDX Metadata Service"
    app_author: str = "Sean Davis"
    app_author_email: str = "seandavi@gmail.com"
    app_license: str = "MIT"
    app_license_url: str = "https://opensource.org/licenses/MIT"
    app_author_orcid: str = "0000-0002-8991-6458"

    # Google Cloud
    gcp_project_id: str = "oidx_mds"

    # database
    pg_dsn: PostgresDsn = "postgresql://postgres:postgres@localhost:5433/oidx_mds"


settings = Settings()


def access_secret_version(secret_id, version_id="latest"):
    # Create the Secret Manager client.
    client = secretmanager.SecretManagerServiceClient()

    # Build the resource name of the secret version.
    name = (
        f"projects/{settings.gcp_project_id}/secrets/{secret_id}/versions/{version_id}"
    )

    # Access the secret version.
    response = client.access_secret_version(name=name)

    # Return the decoded payload.
    return response.payload.data.decode("UTF-8")  # type: ignore
