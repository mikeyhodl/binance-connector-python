import os
import logging

from binance_sdk_spot.spot import Spot, ConfigurationRestAPI, SPOT_REST_API_PROD_URL


# Configure logging
logging.basicConfig(level=logging.INFO)

# Create configuration for the REST API
configuration_rest_api = ConfigurationRestAPI(
    api_key=os.getenv("API_KEY", ""),
    api_secret=os.getenv("API_SECRET", ""),
    base_path=os.getenv("BASE_PATH", SPOT_REST_API_PROD_URL),
)

# Initialize Spot client
client = Spot(config_rest_api=configuration_rest_api)


def delete_order():
    try:
        response = client.rest_api.delete_order(
            symbol="BNBUSDT",
        )

        rate_limits = response.rate_limits
        logging.info(f"delete_order() rate limits: {rate_limits}")

        data = response.data()
        logging.info(f"delete_order() response: {data}")
    except Exception as e:
        logging.error(f"delete_order() error: {e}")


if __name__ == "__main__":
    delete_order()
