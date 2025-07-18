import os
import logging

from binance_sdk_mining.mining import (
    Mining,
    ConfigurationRestAPI,
    MINING_REST_API_PROD_URL,
)


# Configure logging
logging.basicConfig(level=logging.INFO)

# Create configuration for the REST API
configuration_rest_api = ConfigurationRestAPI(
    api_key=os.getenv("API_KEY", ""),
    api_secret=os.getenv("API_SECRET", ""),
    base_path=os.getenv("BASE_PATH", MINING_REST_API_PROD_URL),
)

# Initialize Mining client
client = Mining(config_rest_api=configuration_rest_api)


def cancel_hashrate_resale_configuration():
    try:
        response = client.rest_api.cancel_hashrate_resale_configuration(
            config_id=1,
            user_name="user_name_example",
        )

        rate_limits = response.rate_limits
        logging.info(
            f"cancel_hashrate_resale_configuration() rate limits: {rate_limits}"
        )

        data = response.data()
        logging.info(f"cancel_hashrate_resale_configuration() response: {data}")
    except Exception as e:
        logging.error(f"cancel_hashrate_resale_configuration() error: {e}")


if __name__ == "__main__":
    cancel_hashrate_resale_configuration()
