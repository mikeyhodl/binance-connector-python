import os
import logging

from binance_sdk_sub_account.sub_account import (
    SubAccount,
    ConfigurationRestAPI,
    SUB_ACCOUNT_REST_API_PROD_URL,
)


# Configure logging
logging.basicConfig(level=logging.INFO)

# Create configuration for the REST API
configuration_rest_api = ConfigurationRestAPI(
    api_key=os.getenv("API_KEY", ""),
    api_secret=os.getenv("API_SECRET", ""),
    base_path=os.getenv("BASE_PATH", SUB_ACCOUNT_REST_API_PROD_URL),
)

# Initialize SubAccount client
client = SubAccount(config_rest_api=configuration_rest_api)


def enable_futures_for_sub_account():
    try:
        response = client.rest_api.enable_futures_for_sub_account(
            email="sub-account-email@email.com",
        )

        rate_limits = response.rate_limits
        logging.info(f"enable_futures_for_sub_account() rate limits: {rate_limits}")

        data = response.data()
        logging.info(f"enable_futures_for_sub_account() response: {data}")
    except Exception as e:
        logging.error(f"enable_futures_for_sub_account() error: {e}")


if __name__ == "__main__":
    enable_futures_for_sub_account()
