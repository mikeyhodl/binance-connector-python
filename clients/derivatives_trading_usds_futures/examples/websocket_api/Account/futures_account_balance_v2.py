import asyncio
import os
import logging

from binance_sdk_derivatives_trading_usds_futures.derivatives_trading_usds_futures import (
    DerivativesTradingUsdsFutures,
    DERIVATIVES_TRADING_USDS_FUTURES_WS_API_PROD_URL,
    ConfigurationWebSocketAPI,
)


# Configure logging
logging.basicConfig(level=logging.INFO)

# Create configuration for the WebSocket API
configuration_ws_api = ConfigurationWebSocketAPI(
    api_key=os.getenv("API_KEY", ""),
    api_secret=os.getenv("API_SECRET", ""),
    stream_url=os.getenv(
        "STREAM_URL", DERIVATIVES_TRADING_USDS_FUTURES_WS_API_PROD_URL
    ),
)

# Initialize DerivativesTradingUsdsFutures client
client = DerivativesTradingUsdsFutures(config_ws_api=configuration_ws_api)


async def futures_account_balance_v2():
    connection = None
    try:
        connection = await client.websocket_api.create_connection()

        response = await connection.futures_account_balance_v2()

        rate_limits = response.rate_limits
        logging.info(f"futures_account_balance_v2() rate limits: {rate_limits}")

        data = response.data()
        logging.info(f"futures_account_balance_v2() response: {data}")
    except Exception as e:
        logging.error(f"futures_account_balance_v2() error: {e}")
    finally:
        if connection:
            await connection.close_connection(close_session=True)


if __name__ == "__main__":
    asyncio.run(futures_account_balance_v2())
