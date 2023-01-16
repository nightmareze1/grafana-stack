import os
from dotenv import load_dotenv

load_dotenv()


class BaseConfig(object):

    # AWS_COUNTRY_ROLES = {
    #     "n/a": "n/a",
    # }

    AWS_COUNTRY_ROLES = {
        "dev": os.environ["DEV_ROLE_AWS"],
        "stg": os.environ["STG_ROLE_AWS"],
        "prd": os.environ["PRD_ROLE_AWS"],
    }

    REGION = {"dev": "us-west-2", "stg": "us-west-2", "prd": "us-west-2"}

    PROFILES = {"dev": "hdw-dev-tf", "stg": "hdw-stg-tf", "prd": "hdw-prd-tf"}

    AVAILABLES_ENVIRONMENT = ["dev", "stg", "prd"]
