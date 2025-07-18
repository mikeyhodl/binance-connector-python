import os
import logging

from binance_sdk_fiat.fiat import Fiat, ConfigurationRestAPI, FIAT_REST_API_PROD_URL


# Configure logging
logging.basicConfig(level=logging.INFO)

# Create configuration for the REST API
configuration_rest_api = ConfigurationRestAPI(
    api_key=os.getenv("API_KEY", ""),
    api_secret=os.getenv("API_SECRET", ""),
    base_path=os.getenv("BASE_PATH", FIAT_REST_API_PROD_URL),
)

# Initialize Fiat client
client = Fiat(config_rest_api=configuration_rest_api)


def get_fiat_payments_history():
    try:
        response = client.rest_api.get_fiat_payments_history(
            transaction_type="transaction_type_example",
        )

        rate_limits = response.rate_limits
        logging.info(f"get_fiat_payments_history() rate limits: {rate_limits}")

        data = response.data()
        logging.info(f"get_fiat_payments_history() response: {data}")
    except Exception as e:
        logging.error(f"get_fiat_payments_history() error: {e}")


if __name__ == "__main__":
    get_fiat_payments_history()
