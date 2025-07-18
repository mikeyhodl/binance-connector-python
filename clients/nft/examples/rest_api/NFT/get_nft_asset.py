import os
import logging

from binance_sdk_nft.nft import NFT, ConfigurationRestAPI, NFT_REST_API_PROD_URL


# Configure logging
logging.basicConfig(level=logging.INFO)

# Create configuration for the REST API
configuration_rest_api = ConfigurationRestAPI(
    api_key=os.getenv("API_KEY", ""),
    api_secret=os.getenv("API_SECRET", ""),
    base_path=os.getenv("BASE_PATH", NFT_REST_API_PROD_URL),
)

# Initialize NFT client
client = NFT(config_rest_api=configuration_rest_api)


def get_nft_asset():
    try:
        response = client.rest_api.get_nft_asset()

        rate_limits = response.rate_limits
        logging.info(f"get_nft_asset() rate limits: {rate_limits}")

        data = response.data()
        logging.info(f"get_nft_asset() response: {data}")
    except Exception as e:
        logging.error(f"get_nft_asset() error: {e}")


if __name__ == "__main__":
    get_nft_asset()
