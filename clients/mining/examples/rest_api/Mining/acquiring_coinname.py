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


def acquiring_coinname():
    try:
        response = client.rest_api.acquiring_coinname()

        rate_limits = response.rate_limits
        logging.info(f"acquiring_coinname() rate limits: {rate_limits}")

        data = response.data()
        logging.info(f"acquiring_coinname() response: {data}")
    except Exception as e:
        logging.error(f"acquiring_coinname() error: {e}")


if __name__ == "__main__":
    acquiring_coinname()
