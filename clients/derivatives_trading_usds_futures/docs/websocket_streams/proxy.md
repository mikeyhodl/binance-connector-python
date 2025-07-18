import asyncio
import logging

from binance_common.configuration import ConfigurationWebSocketStreams
from binance_sdk_derivatives_trading_usds_futures.derivatives_trading_usds_futures import DerivativesTradingUsdsFutures


configuration_ws_streams = ConfigurationWebSocketStreams(
    proxy={
        "host": "localhost",
        "port": 8080,
        "protocol": "http",  # or 'https'
        "auth": {
            "username": "proxy-user",
            "password": "proxy-password",
        },
    },
)

client = DerivativesTradingUsdsFutures(config_ws_streams=configuration_ws_streams)


async def allBookTickersStream():
    connection = None
    try:
        connection = await client.websocket_streams.create_connection()

        stream = await connection.allBookTickersStream()
        stream.on("message", lambda data: print(f"{data}"))
        await asyncio.sleep(5)
    except Exception as e:
        logging.error(f"allBookTickersStream() error: {e}")
    finally:
        if connection:
            await connection.close_connection(close_session=True)


if __name__ == "__main__":
    asyncio.run(allBookTickersStream())
