import asyncio
import os
import logging

from binance_sdk_derivatives_trading_coin_futures.derivatives_trading_coin_futures import (
    DerivativesTradingCoinFutures,
    DERIVATIVES_TRADING_COIN_FUTURES_WS_API_PROD_URL,
    ConfigurationWebSocketAPI,
)


# Configure logging
logging.basicConfig(level=logging.INFO)

# Create configuration for the WebSocket API
configuration_ws_api = ConfigurationWebSocketAPI(
    api_key=os.getenv("API_KEY", ""),
    api_secret=os.getenv("API_SECRET", ""),
    stream_url=os.getenv(
        "STREAM_URL", DERIVATIVES_TRADING_COIN_FUTURES_WS_API_PROD_URL
    ),
)

# Initialize DerivativesTradingCoinFutures client
client = DerivativesTradingCoinFutures(config_ws_api=configuration_ws_api)


async def query_order():
    connection = None
    try:
        connection = await client.websocket_api.create_connection()

        response = await connection.query_order(
            symbol="symbol_example",
        )

        rate_limits = response.rate_limits
        logging.info(f"query_order() rate limits: {rate_limits}")

        data = response.data()
        logging.info(f"query_order() response: {data}")
    except Exception as e:
        logging.error(f"query_order() error: {e}")
    finally:
        if connection:
            await connection.close_connection(close_session=True)


if __name__ == "__main__":
    asyncio.run(query_order())
