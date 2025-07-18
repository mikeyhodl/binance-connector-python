"""
Binance Derivatives Trading Options REST API

OpenAPI Specification for the Binance Derivatives Trading Options REST API
The version of the OpenAPI document: 1.0.0
Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""

from typing import List, Optional
from requests import Session
from binance_common.configuration import ConfigurationRestAPI
from binance_common.errors import RequiredError
from binance_common.models import ApiResponse
from binance_common.signature import Signers
from binance_common.utils import send_request

from ..models import AcceptBlockTradeOrderResponse
from ..models import AccountBlockTradeListResponse

from ..models import ExtendBlockTradeOrderResponse
from ..models import NewBlockTradeOrderResponse
from ..models import QueryBlockTradeDetailsResponse
from ..models import QueryBlockTradeOrderResponse


from ..models import NewBlockTradeOrderSideEnum


class MarketMakerBlockTradeApi:
    """API Client for MarketMakerBlockTradeApi endpoints."""

    def __init__(
        self,
        configuration: ConfigurationRestAPI = None,
        session: Session = None,
        signer: Signers = None,
    ) -> None:
        self._configuration = configuration
        self._session = session
        self._signer = signer

    def accept_block_trade_order(
        self,
        block_order_matching_key: str = None,
        recv_window: Optional[int] = None,
    ) -> ApiResponse[AcceptBlockTradeOrderResponse]:
        """
                Accept Block Trade Order (TRADE)
                POST /eapi/v1/block/order/execute
                https://developers.binance.com/docs/derivatives/option/market-maker-block-trade/Accept-Block-Trade-Order

                Accept a block trade order

        Weight: 5

                Args:
                    block_order_matching_key (str):
                    recv_window (Optional[int]):

                Returns:
                    ApiResponse[AcceptBlockTradeOrderResponse]

                Raises:
                    RequiredError: If a required parameter is missing.

        """

        if block_order_matching_key is None:
            raise RequiredError(
                field="block_order_matching_key",
                error_message="Missing required parameter 'block_order_matching_key'",
            )

        payload = {
            "block_order_matching_key": block_order_matching_key,
            "recv_window": recv_window,
        }

        return send_request(
            self._session,
            self._configuration,
            method="POST",
            path="/eapi/v1/block/order/execute",
            payload=payload,
            time_unit=self._configuration.time_unit,
            response_model=AcceptBlockTradeOrderResponse,
            is_signed=True,
            signer=self._signer,
        )

    def account_block_trade_list(
        self,
        end_time: Optional[int] = None,
        start_time: Optional[int] = None,
        underlying: Optional[str] = None,
        recv_window: Optional[int] = None,
    ) -> ApiResponse[AccountBlockTradeListResponse]:
        """
                Account Block Trade List (USER_DATA)
                GET /eapi/v1/block/user-trades
                https://developers.binance.com/docs/derivatives/option/market-maker-block-trade/Account-Block-Trade-List

                Gets block trades for a specific account.

        Weight: 5

                Args:
                    end_time (Optional[int]): End Time, e.g 1593512200000
                    start_time (Optional[int]): Start Time, e.g 1593511200000
                    underlying (Optional[str]): underlying, e.g BTCUSDT
                    recv_window (Optional[int]):

                Returns:
                    ApiResponse[AccountBlockTradeListResponse]

                Raises:
                    RequiredError: If a required parameter is missing.

        """

        payload = {
            "end_time": end_time,
            "start_time": start_time,
            "underlying": underlying,
            "recv_window": recv_window,
        }

        return send_request(
            self._session,
            self._configuration,
            method="GET",
            path="/eapi/v1/block/user-trades",
            payload=payload,
            time_unit=self._configuration.time_unit,
            response_model=AccountBlockTradeListResponse,
            is_signed=True,
            signer=self._signer,
        )

    def cancel_block_trade_order(
        self,
        block_order_matching_key: str = None,
        recv_window: Optional[int] = None,
    ) -> ApiResponse[None]:
        """
                Cancel Block Trade Order (TRADE)
                DELETE /eapi/v1/block/order/create
                https://developers.binance.com/docs/derivatives/option/market-maker-block-trade/Cancel-Block-Trade-Order

                Cancel a block trade order.

        Weight: 5

                Args:
                    block_order_matching_key (str):
                    recv_window (Optional[int]):

                Returns:
                    ApiResponse[None]

                Raises:
                    RequiredError: If a required parameter is missing.

        """

        if block_order_matching_key is None:
            raise RequiredError(
                field="block_order_matching_key",
                error_message="Missing required parameter 'block_order_matching_key'",
            )

        payload = {
            "block_order_matching_key": block_order_matching_key,
            "recv_window": recv_window,
        }

        return send_request(
            self._session,
            self._configuration,
            method="DELETE",
            path="/eapi/v1/block/order/create",
            payload=payload,
            time_unit=self._configuration.time_unit,
            is_signed=True,
            signer=self._signer,
        )

    def extend_block_trade_order(
        self,
        block_order_matching_key: str = None,
        recv_window: Optional[int] = None,
    ) -> ApiResponse[ExtendBlockTradeOrderResponse]:
        """
                Extend Block Trade Order (TRADE)
                PUT /eapi/v1/block/order/create
                https://developers.binance.com/docs/derivatives/option/market-maker-block-trade/Extend-Block-Trade-Order

                Extends a block trade expire time by 30 mins from the current time.

        Weight: 5

                Args:
                    block_order_matching_key (str):
                    recv_window (Optional[int]):

                Returns:
                    ApiResponse[ExtendBlockTradeOrderResponse]

                Raises:
                    RequiredError: If a required parameter is missing.

        """

        if block_order_matching_key is None:
            raise RequiredError(
                field="block_order_matching_key",
                error_message="Missing required parameter 'block_order_matching_key'",
            )

        payload = {
            "block_order_matching_key": block_order_matching_key,
            "recv_window": recv_window,
        }

        return send_request(
            self._session,
            self._configuration,
            method="PUT",
            path="/eapi/v1/block/order/create",
            payload=payload,
            time_unit=self._configuration.time_unit,
            response_model=ExtendBlockTradeOrderResponse,
            is_signed=True,
            signer=self._signer,
        )

    def new_block_trade_order(
        self,
        liquidity: str = None,
        legs: List[object] = None,
        symbol: str = None,
        side: NewBlockTradeOrderSideEnum = None,
        price: float = None,
        quantity: float = None,
        recv_window: Optional[int] = None,
    ) -> ApiResponse[NewBlockTradeOrderResponse]:
        """
                New Block Trade Order (TRADE)
                POST /eapi/v1/block/order/create
                https://developers.binance.com/docs/derivatives/option/market-maker-block-trade/New-Block-Trade-Order

                Send in a new block trade order.

        Weight: 5

                Args:
                    liquidity (str): Taker or Maker
                    legs (List[object]): Max 1 (only single leg supported), list of legs parameters in JSON; example: eapi/v1/block/order/create?orders=[{"symbol":"BTC-210115-35000-C", "price":"100","quantity":"0.0002","side":"BUY","type":"LIMIT"}]
                    symbol (str): Option trading pair, e.g BTC-200730-9000-C
                    side (NewBlockTradeOrderSideEnum): BUY or SELL
                    price (float): Order Price
                    quantity (float): Order Quantity
                    recv_window (Optional[int]):

                Returns:
                    ApiResponse[NewBlockTradeOrderResponse]

                Raises:
                    RequiredError: If a required parameter is missing.

        """

        if liquidity is None:
            raise RequiredError(
                field="liquidity",
                error_message="Missing required parameter 'liquidity'",
            )
        if legs is None:
            raise RequiredError(
                field="legs", error_message="Missing required parameter 'legs'"
            )
        if symbol is None:
            raise RequiredError(
                field="symbol", error_message="Missing required parameter 'symbol'"
            )
        if side is None:
            raise RequiredError(
                field="side", error_message="Missing required parameter 'side'"
            )
        if price is None:
            raise RequiredError(
                field="price", error_message="Missing required parameter 'price'"
            )
        if quantity is None:
            raise RequiredError(
                field="quantity", error_message="Missing required parameter 'quantity'"
            )

        payload = {
            "liquidity": liquidity,
            "legs": legs,
            "symbol": symbol,
            "side": side,
            "price": price,
            "quantity": quantity,
            "recv_window": recv_window,
        }

        return send_request(
            self._session,
            self._configuration,
            method="POST",
            path="/eapi/v1/block/order/create",
            payload=payload,
            time_unit=self._configuration.time_unit,
            response_model=NewBlockTradeOrderResponse,
            is_signed=True,
            signer=self._signer,
        )

    def query_block_trade_details(
        self,
        block_order_matching_key: str = None,
        recv_window: Optional[int] = None,
    ) -> ApiResponse[QueryBlockTradeDetailsResponse]:
        """
                Query Block Trade Details (USER_DATA)
                GET /eapi/v1/block/order/execute
                https://developers.binance.com/docs/derivatives/option/market-maker-block-trade/Query-Block-Trade-Detail

                Query block trade details; returns block trade details from counterparty's perspective.

        Weight: 5

                Args:
                    block_order_matching_key (str):
                    recv_window (Optional[int]):

                Returns:
                    ApiResponse[QueryBlockTradeDetailsResponse]

                Raises:
                    RequiredError: If a required parameter is missing.

        """

        if block_order_matching_key is None:
            raise RequiredError(
                field="block_order_matching_key",
                error_message="Missing required parameter 'block_order_matching_key'",
            )

        payload = {
            "block_order_matching_key": block_order_matching_key,
            "recv_window": recv_window,
        }

        return send_request(
            self._session,
            self._configuration,
            method="GET",
            path="/eapi/v1/block/order/execute",
            payload=payload,
            time_unit=self._configuration.time_unit,
            response_model=QueryBlockTradeDetailsResponse,
            is_signed=True,
            signer=self._signer,
        )

    def query_block_trade_order(
        self,
        block_order_matching_key: Optional[str] = None,
        end_time: Optional[int] = None,
        start_time: Optional[int] = None,
        underlying: Optional[str] = None,
        recv_window: Optional[int] = None,
    ) -> ApiResponse[QueryBlockTradeOrderResponse]:
        """
                Query Block Trade Order (TRADE)
                GET /eapi/v1/block/order/orders
                https://developers.binance.com/docs/derivatives/option/market-maker-block-trade/Query-Block-Trade-Order

                Check block trade order status.

        Weight: 5

                Args:
                    block_order_matching_key (Optional[str]): If specified, returns the specific block trade associated with the blockOrderMatchingKey
                    end_time (Optional[int]): End Time, e.g 1593512200000
                    start_time (Optional[int]): Start Time, e.g 1593511200000
                    underlying (Optional[str]): underlying, e.g BTCUSDT
                    recv_window (Optional[int]):

                Returns:
                    ApiResponse[QueryBlockTradeOrderResponse]

                Raises:
                    RequiredError: If a required parameter is missing.

        """

        payload = {
            "block_order_matching_key": block_order_matching_key,
            "end_time": end_time,
            "start_time": start_time,
            "underlying": underlying,
            "recv_window": recv_window,
        }

        return send_request(
            self._session,
            self._configuration,
            method="GET",
            path="/eapi/v1/block/order/orders",
            payload=payload,
            time_unit=self._configuration.time_unit,
            response_model=QueryBlockTradeOrderResponse,
            is_signed=True,
            signer=self._signer,
        )
