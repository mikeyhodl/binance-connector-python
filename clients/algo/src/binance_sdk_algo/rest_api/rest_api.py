"""
Binance Algo REST API

OpenAPI Specification for the Binance Algo REST API
The version of the OpenAPI document: 1.0.0
Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""

import requests
from typing import Optional, TypeVar
from binance_common.configuration import ConfigurationRestAPI
from binance_common.models import ApiResponse
from binance_common.signature import Signers
from binance_common.utils import send_request
from .api.future_algo_api import FutureAlgoApi
from .api.spot_algo_api import SpotAlgoApi

from .models import CancelAlgoOrderFutureAlgoResponse
from .models import QueryCurrentAlgoOpenOrdersFutureAlgoResponse
from .models import QueryHistoricalAlgoOrdersFutureAlgoResponse
from .models import QuerySubOrdersFutureAlgoResponse
from .models import TimeWeightedAveragePriceFutureAlgoResponse
from .models import VolumeParticipationFutureAlgoResponse
from .models import CancelAlgoOrderSpotAlgoResponse
from .models import QueryCurrentAlgoOpenOrdersSpotAlgoResponse
from .models import QueryHistoricalAlgoOrdersSpotAlgoResponse
from .models import QuerySubOrdersSpotAlgoResponse
from .models import TimeWeightedAveragePriceSpotAlgoResponse


T = TypeVar("T")


class AlgoRestAPI:
    def __init__(
        self,
        configuration: ConfigurationRestAPI,
    ) -> None:
        self.configuration = configuration
        self._session = requests.Session()
        self._signer = (
            Signers.get_signer(
                configuration.private_key, configuration.private_key_passphrase
            )
            if configuration.private_key is not None
            else None
        )

        self._futureAlgoApi = FutureAlgoApi(
            self.configuration, self._session, self._signer
        )
        self._spotAlgoApi = SpotAlgoApi(self.configuration, self._session, self._signer)

    def send_request(
        self, endpoint: str, method: str, params: Optional[dict] = None
    ) -> ApiResponse[T]:
        """
        Sends an request to the Binance REST API.

        Args:
            endpoint (str): The API endpoint path to send the request to.
            method (str): The HTTP method to use for the request (e.g. "GET", "POST", "PUT", "DELETE").
            params (Optional[dict]): The request payload as a dictionary, or None if no payload is required.

        Returns:
            ApiResponse[T]: The API response, where T is the expected response type.
        """
        return send_request[T](
            self._session, self.configuration, method, endpoint, params
        )

    def send_signed_request(
        self, endpoint: str, method: str, params: Optional[dict] = None
    ) -> ApiResponse[T]:
        """
        Sends a signed request to the Binance REST API.

        Args:
            endpoint (str): The API endpoint path to send the request to.
            method (str): The HTTP method to use for the request (e.g. "GET", "POST", "PUT", "DELETE").
            params (Optional[dict]): The request payload as a dictionary, or None if no payload is required.

        Returns:
            ApiResponse[T]: The API response, where T is the expected response type.
        """
        return send_request[T](
            self._session,
            self.configuration,
            method,
            endpoint,
            params,
            is_signed=True,
            signer=self._signer,
        )

    def cancel_algo_order_future_algo(
        self,
        algo_id: int = None,
        recv_window: Optional[int] = None,
    ) -> ApiResponse[CancelAlgoOrderFutureAlgoResponse]:
        """
                Cancel Algo Order(TRADE)

                Cancel an active order.

        * You need to enable `Futures Trading Permission` for the api key which requests this endpoint.
        * Base URL: https://api.binance.com

        Weight: 1

                Args:
                    algo_id (int): eg. 14511
                    recv_window (Optional[int]):

                Returns:
                    ApiResponse[CancelAlgoOrderFutureAlgoResponse]

                Raises:
                    RequiredError: If a required parameter is missing.

        """

        return self._futureAlgoApi.cancel_algo_order_future_algo(algo_id, recv_window)

    def query_current_algo_open_orders_future_algo(
        self,
        recv_window: Optional[int] = None,
    ) -> ApiResponse[QueryCurrentAlgoOpenOrdersFutureAlgoResponse]:
        """
                Query Current Algo Open Orders(USER_DATA)

                Query Current Algo Open Orders

        * You need to enable `Futures Trading Permission` for the api key which requests this endpoint.
        * Base URL: https://api.binance.com

        Weight: 1

                Args:
                    recv_window (Optional[int]):

                Returns:
                    ApiResponse[QueryCurrentAlgoOpenOrdersFutureAlgoResponse]

                Raises:
                    RequiredError: If a required parameter is missing.

        """

        return self._futureAlgoApi.query_current_algo_open_orders_future_algo(
            recv_window
        )

    def query_historical_algo_orders_future_algo(
        self,
        symbol: Optional[str] = None,
        side: Optional[str] = None,
        start_time: Optional[int] = None,
        end_time: Optional[int] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        recv_window: Optional[int] = None,
    ) -> ApiResponse[QueryHistoricalAlgoOrdersFutureAlgoResponse]:
        """
                Query Historical Algo Orders(USER_DATA)

                Query Historical Algo Order

        * You need to enable `Futures Trading Permission` for the api key which requests this endpoint.
        * Base URL: https://api.binance.com

        Weight: 1

                Args:
                    symbol (Optional[str]): Trading symbol eg. BTCUSDT
                    side (Optional[str]): BUY or SELL
                    start_time (Optional[int]): in milliseconds  eg.1641522717552
                    end_time (Optional[int]): in milliseconds  eg.1641522526562
                    page (Optional[int]): Default is 1
                    page_size (Optional[int]): MIN 1, MAX 100; Default 100
                    recv_window (Optional[int]):

                Returns:
                    ApiResponse[QueryHistoricalAlgoOrdersFutureAlgoResponse]

                Raises:
                    RequiredError: If a required parameter is missing.

        """

        return self._futureAlgoApi.query_historical_algo_orders_future_algo(
            symbol, side, start_time, end_time, page, page_size, recv_window
        )

    def query_sub_orders_future_algo(
        self,
        algo_id: int = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        recv_window: Optional[int] = None,
    ) -> ApiResponse[QuerySubOrdersFutureAlgoResponse]:
        """
                Query Sub Orders(USER_DATA)

                Get respective sub orders for a specified algoId

        * You need to enable `Futures Trading Permission` for the api key which requests this endpoint.
        * Base URL: https://api.binance.com

        Weight: 1

                Args:
                    algo_id (int): eg. 14511
                    page (Optional[int]): Default is 1
                    page_size (Optional[int]): MIN 1, MAX 100; Default 100
                    recv_window (Optional[int]):

                Returns:
                    ApiResponse[QuerySubOrdersFutureAlgoResponse]

                Raises:
                    RequiredError: If a required parameter is missing.

        """

        return self._futureAlgoApi.query_sub_orders_future_algo(
            algo_id, page, page_size, recv_window
        )

    def time_weighted_average_price_future_algo(
        self,
        symbol: str = None,
        side: str = None,
        quantity: float = None,
        duration: int = None,
        position_side: Optional[str] = None,
        client_algo_id: Optional[str] = None,
        reduce_only: Optional[bool] = None,
        limit_price: Optional[float] = None,
        recv_window: Optional[int] = None,
    ) -> ApiResponse[TimeWeightedAveragePriceFutureAlgoResponse]:
        """
                Time-Weighted Average Price(Twap) New Order(TRADE)

                Send in a Twap new order.
        Only support on USDⓈ-M Contracts.

        * Total Algo open orders max allowed: `30` orders.
        * Leverage of symbols and position mode will be the same as your futures account settings. You can set up through the trading page or fapi.
        * Receiving `"success": true` does not mean that your order will be executed. Please use the query order endpoints（`GET sapi/v1/algo/futures/openOrders` or `GET sapi/v1/algo/futures/historicalOrders`） to check the order status.
        For example: Your futures balance is insufficient, or open position with reduce only or position side is inconsistent with your own setting. In these cases you will receive `"success": true`, but the order status will be `expired` after we check it.
        * `quantity` * 60 / `duration` should be larger than minQty
        * `duration` cannot be less than 5 mins or more than 24 hours.
        * For delivery contracts, TWAP end time should be one hour earlier than the delivery time of the symbol.
        * You need to enable `Futures Trading Permission` for the api key which requests this endpoint.
        * Base URL: https://api.binance.com

        Weight: 3000

                Args:
                    symbol (str): Trading symbol eg. BTCUSDT
                    side (str): Trading side ( BUY or SELL )
                    quantity (float): Quantity of base asset; Maximum notional per order is 200k, 2mm or 10mm, depending on symbol. Please reduce your size if you order is above the maximum notional per order.
                    duration (int): Duration for TWAP orders in seconds. [300, 86400]
                    position_side (Optional[str]): Default `BOTH` for One-way Mode ; `LONG` or `SHORT` for Hedge Mode. It must be sent in Hedge Mode.
                    client_algo_id (Optional[str]): A unique id among Algo orders (length should be 32 characters)， If it is not sent, we will give default value
                    reduce_only (Optional[bool]): "true" or "false". Default "false"; Cannot be sent in Hedge Mode; Cannot be sent when you open a position
                    limit_price (Optional[float]): Limit price of the order; If it is not sent, will place order by market price by default
                    recv_window (Optional[int]):

                Returns:
                    ApiResponse[TimeWeightedAveragePriceFutureAlgoResponse]

                Raises:
                    RequiredError: If a required parameter is missing.

        """

        return self._futureAlgoApi.time_weighted_average_price_future_algo(
            symbol,
            side,
            quantity,
            duration,
            position_side,
            client_algo_id,
            reduce_only,
            limit_price,
            recv_window,
        )

    def volume_participation_future_algo(
        self,
        symbol: str = None,
        side: str = None,
        quantity: float = None,
        urgency: str = None,
        position_side: Optional[str] = None,
        client_algo_id: Optional[str] = None,
        reduce_only: Optional[bool] = None,
        limit_price: Optional[float] = None,
        recv_window: Optional[int] = None,
    ) -> ApiResponse[VolumeParticipationFutureAlgoResponse]:
        """
                Volume Participation(VP) New Order (TRADE)

                Send in a VP new order.
        Only support on USDⓈ-M Contracts.

        * Total Algo open orders max allowed: `10` orders.
        * Leverage of symbols and position mode will be the same as your futures account settings. You can set up through the trading page or fapi.
        * Receiving `"success": true` does not mean that your order will be executed. Please use the query order endpoints（`GET sapi/v1/algo/futures/openOrders` or `GET sapi/v1/algo/futures/historicalOrders`） to check the order status.
        For example: Your futures balance is insufficient, or open position with reduce only or position side is inconsistent with your own setting. In these cases you will receive `"success": true`, but the order status will be `expired` after we check it.
        * You need to enable `Futures Trading Permission` for the api key which requests this endpoint.
        * Base URL: https://api.binance.com

        Weight: 300

                Args:
                    symbol (str): Trading symbol eg. BTCUSDT
                    side (str): Trading side ( BUY or SELL )
                    quantity (float): Quantity of base asset; Maximum notional per order is 200k, 2mm or 10mm, depending on symbol. Please reduce your size if you order is above the maximum notional per order.
                    urgency (str): Represent the relative speed of the current execution; ENUM: LOW, MEDIUM, HIGH
                    position_side (Optional[str]): Default `BOTH` for One-way Mode ; `LONG` or `SHORT` for Hedge Mode. It must be sent in Hedge Mode.
                    client_algo_id (Optional[str]): A unique id among Algo orders (length should be 32 characters)， If it is not sent, we will give default value
                    reduce_only (Optional[bool]): "true" or "false". Default "false"; Cannot be sent in Hedge Mode; Cannot be sent when you open a position
                    limit_price (Optional[float]): Limit price of the order; If it is not sent, will place order by market price by default
                    recv_window (Optional[int]):

                Returns:
                    ApiResponse[VolumeParticipationFutureAlgoResponse]

                Raises:
                    RequiredError: If a required parameter is missing.

        """

        return self._futureAlgoApi.volume_participation_future_algo(
            symbol,
            side,
            quantity,
            urgency,
            position_side,
            client_algo_id,
            reduce_only,
            limit_price,
            recv_window,
        )

    def cancel_algo_order_spot_algo(
        self,
        algo_id: int = None,
        recv_window: Optional[int] = None,
    ) -> ApiResponse[CancelAlgoOrderSpotAlgoResponse]:
        """
                Cancel Algo Order(TRADE)

                Cancel an open TWAP order

        Weight: 1

                Args:
                    algo_id (int): eg. 14511
                    recv_window (Optional[int]):

                Returns:
                    ApiResponse[CancelAlgoOrderSpotAlgoResponse]

                Raises:
                    RequiredError: If a required parameter is missing.

        """

        return self._spotAlgoApi.cancel_algo_order_spot_algo(algo_id, recv_window)

    def query_current_algo_open_orders_spot_algo(
        self,
        recv_window: Optional[int] = None,
    ) -> ApiResponse[QueryCurrentAlgoOpenOrdersSpotAlgoResponse]:
        """
                Query Current Algo Open Orders(USER_DATA)

                Get all open SPOT TWAP orders

        Weight: 1

                Args:
                    recv_window (Optional[int]):

                Returns:
                    ApiResponse[QueryCurrentAlgoOpenOrdersSpotAlgoResponse]

                Raises:
                    RequiredError: If a required parameter is missing.

        """

        return self._spotAlgoApi.query_current_algo_open_orders_spot_algo(recv_window)

    def query_historical_algo_orders_spot_algo(
        self,
        symbol: Optional[str] = None,
        side: Optional[str] = None,
        start_time: Optional[int] = None,
        end_time: Optional[int] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        recv_window: Optional[int] = None,
    ) -> ApiResponse[QueryHistoricalAlgoOrdersSpotAlgoResponse]:
        """
                Query Historical Algo Orders(USER_DATA)

                Get all historical SPOT TWAP orders

        Weight: 1

                Args:
                    symbol (Optional[str]): Trading symbol eg. BTCUSDT
                    side (Optional[str]): BUY or SELL
                    start_time (Optional[int]): in milliseconds  eg.1641522717552
                    end_time (Optional[int]): in milliseconds  eg.1641522526562
                    page (Optional[int]): Default is 1
                    page_size (Optional[int]): MIN 1, MAX 100; Default 100
                    recv_window (Optional[int]):

                Returns:
                    ApiResponse[QueryHistoricalAlgoOrdersSpotAlgoResponse]

                Raises:
                    RequiredError: If a required parameter is missing.

        """

        return self._spotAlgoApi.query_historical_algo_orders_spot_algo(
            symbol, side, start_time, end_time, page, page_size, recv_window
        )

    def query_sub_orders_spot_algo(
        self,
        algo_id: int = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        recv_window: Optional[int] = None,
    ) -> ApiResponse[QuerySubOrdersSpotAlgoResponse]:
        """
                Query Sub Orders(USER_DATA)

                Get respective sub orders for a specified algoId

        Weight: 1

                Args:
                    algo_id (int): eg. 14511
                    page (Optional[int]): Default is 1
                    page_size (Optional[int]): MIN 1, MAX 100; Default 100
                    recv_window (Optional[int]):

                Returns:
                    ApiResponse[QuerySubOrdersSpotAlgoResponse]

                Raises:
                    RequiredError: If a required parameter is missing.

        """

        return self._spotAlgoApi.query_sub_orders_spot_algo(
            algo_id, page, page_size, recv_window
        )

    def time_weighted_average_price_spot_algo(
        self,
        symbol: str = None,
        side: str = None,
        quantity: float = None,
        duration: int = None,
        client_algo_id: Optional[str] = None,
        limit_price: Optional[float] = None,
    ) -> ApiResponse[TimeWeightedAveragePriceSpotAlgoResponse]:
        """
                Time-Weighted Average Price(Twap) New Order(TRADE)

                Place a new spot TWAP order with Algo service.

        * Total Algo open orders max allowed: `20` orders.

        Weight: 3000

                Args:
                    symbol (str): Trading symbol eg. BTCUSDT
                    side (str): Trading side ( BUY or SELL )
                    quantity (float): Quantity of base asset; Maximum notional per order is 200k, 2mm or 10mm, depending on symbol. Please reduce your size if you order is above the maximum notional per order.
                    duration (int): Duration for TWAP orders in seconds. [300, 86400]
                    client_algo_id (Optional[str]): A unique id among Algo orders (length should be 32 characters)， If it is not sent, we will give default value
                    limit_price (Optional[float]): Limit price of the order; If it is not sent, will place order by market price by default

                Returns:
                    ApiResponse[TimeWeightedAveragePriceSpotAlgoResponse]

                Raises:
                    RequiredError: If a required parameter is missing.

        """

        return self._spotAlgoApi.time_weighted_average_price_spot_algo(
            symbol, side, quantity, duration, client_algo_id, limit_price
        )
