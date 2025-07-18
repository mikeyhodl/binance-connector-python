"""
Binance Derivatives Trading COIN Futures WebSocket API

OpenAPI Specification for the Binance Derivatives Trading COIN Futures WebSocket API
The version of the OpenAPI document: 1.0.0
Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""

import pytest

from unittest.mock import AsyncMock, MagicMock

from binance_common.models import WebsocketApiResponse
from binance_common.utils import parse_ws_rate_limit_headers
from binance_sdk_derivatives_trading_coin_futures.websocket_api.api import AccountApi


from binance_sdk_derivatives_trading_coin_futures.websocket_api.models import (
    AccountInformationResponse,
)
from binance_sdk_derivatives_trading_coin_futures.websocket_api.models import (
    FuturesAccountBalanceResponse,
)


class TestWebSocketAccountApi:
    @pytest.fixture(autouse=True)
    def setup_method(self):
        self.mock_websocket_api = MagicMock()
        self.websocket_api = AccountApi(websocket_api=self.mock_websocket_api)

    @pytest.mark.asyncio
    async def test_account_information_success(self):
        """Test account_information() successfully with required parameters only."""

        expected_response = {
            "id": "baaec739-c5cf-4920-b448-c0b9c5431410",
            "status": 200,
            "result": {
                "feeTier": 0,
                "canTrade": True,
                "canDeposit": True,
                "canWithdraw": True,
                "updateTime": 0,
                "assets": [
                    {
                        "asset": "WLD",
                        "walletBalance": "0.00000000",
                        "unrealizedProfit": "0.00000000",
                        "marginBalance": "0.00000000",
                        "maintMargin": "0.00000000",
                        "initialMargin": "0.00000000",
                        "positionInitialMargin": "0.00000000",
                        "openOrderInitialMargin": "0.00000000",
                        "maxWithdrawAmount": "0.00000000",
                        "crossWalletBalance": "0.00000000",
                        "crossUnPnl": "0.00000000",
                        "availableBalance": "0.00000000",
                        "updateTime": 0,
                    }
                ],
                "positions": [
                    {
                        "symbol": "ETHUSD_220930",
                        "initialMargin": "0",
                        "maintMargin": "0",
                        "unrealizedProfit": "0.00000000",
                        "positionInitialMargin": "0",
                        "openOrderInitialMargin": "0",
                        "leverage": "7",
                        "isolated": False,
                        "positionSide": "BOTH",
                        "entryPrice": "0.00000000",
                        "maxQty": "1000",
                        "notionalValue": "0",
                        "isolatedWallet": "0",
                        "updateTime": 0,
                        "positionAmt": "0",
                        "breakEvenPrice": "0.00000000",
                    }
                ],
            },
            "rateLimits": [
                {
                    "rateLimitType": "REQUEST_WEIGHT",
                    "interval": "MINUTE",
                    "intervalNum": 1,
                    "limit": 2400,
                    "count": 10,
                }
            ],
        }

        self.mock_websocket_api.send_signed_message = AsyncMock(
            return_value=WebsocketApiResponse(
                data_function=lambda: expected_response,
                rate_limits=(
                    parse_ws_rate_limit_headers(expected_response["rateLimits"])
                    if "rateLimits" in expected_response
                    else None
                ),
            )
        )
        result = await self.websocket_api.account_information()

        actual_call_args = self.mock_websocket_api.send_signed_message.call_args
        request_kwargs = actual_call_args.kwargs

        assert "payload" in request_kwargs
        assert "method" in request_kwargs["payload"]
        assert request_kwargs["payload"]["method"] == "/account.status".replace("/", "")

        assert result is not None
        assert result.data() == expected_response
        self.mock_websocket_api.send_signed_message.assert_called_once_with(
            payload={"method": "/account.status".replace("/", ""), "params": {}},
            response_model=AccountInformationResponse,
            signer=None,
        )

    @pytest.mark.asyncio
    async def test_account_information_success_with_optional_params(self):
        """Test account_information() successfully with optional parameters."""

        params = {"id": "e9d6b4349871b40611412680b3445fac", "recv_window": 5000}

        expected_response = {
            "id": "baaec739-c5cf-4920-b448-c0b9c5431410",
            "status": 200,
            "result": {
                "feeTier": 0,
                "canTrade": True,
                "canDeposit": True,
                "canWithdraw": True,
                "updateTime": 0,
                "assets": [
                    {
                        "asset": "WLD",
                        "walletBalance": "0.00000000",
                        "unrealizedProfit": "0.00000000",
                        "marginBalance": "0.00000000",
                        "maintMargin": "0.00000000",
                        "initialMargin": "0.00000000",
                        "positionInitialMargin": "0.00000000",
                        "openOrderInitialMargin": "0.00000000",
                        "maxWithdrawAmount": "0.00000000",
                        "crossWalletBalance": "0.00000000",
                        "crossUnPnl": "0.00000000",
                        "availableBalance": "0.00000000",
                        "updateTime": 0,
                    }
                ],
                "positions": [
                    {
                        "symbol": "ETHUSD_220930",
                        "initialMargin": "0",
                        "maintMargin": "0",
                        "unrealizedProfit": "0.00000000",
                        "positionInitialMargin": "0",
                        "openOrderInitialMargin": "0",
                        "leverage": "7",
                        "isolated": False,
                        "positionSide": "BOTH",
                        "entryPrice": "0.00000000",
                        "maxQty": "1000",
                        "notionalValue": "0",
                        "isolatedWallet": "0",
                        "updateTime": 0,
                        "positionAmt": "0",
                        "breakEvenPrice": "0.00000000",
                    }
                ],
            },
            "rateLimits": [
                {
                    "rateLimitType": "REQUEST_WEIGHT",
                    "interval": "MINUTE",
                    "intervalNum": 1,
                    "limit": 2400,
                    "count": 10,
                }
            ],
        }

        self.mock_websocket_api.send_signed_message = AsyncMock(
            return_value=WebsocketApiResponse(
                data_function=lambda: expected_response,
                rate_limits=(
                    parse_ws_rate_limit_headers(expected_response["rateLimits"])
                    if "rateLimits" in expected_response
                    else None
                ),
            )
        )

        result = await self.websocket_api.account_information(**params)

        actual_call_args = self.mock_websocket_api.send_signed_message.call_args
        request_kwargs = actual_call_args.kwargs

        assert "payload" in request_kwargs
        assert "method" in request_kwargs["payload"]
        assert request_kwargs["payload"]["method"] == "/account.status".replace("/", "")
        assert "params" in request_kwargs["payload"]
        params = request_kwargs["payload"]["params"]
        assert params["id"] == "e9d6b4349871b40611412680b3445fac"
        assert params["recv_window"] == 5000

        assert result is not None
        assert result.data() == expected_response
        self.mock_websocket_api.send_signed_message.assert_called_once_with(
            payload={"method": "/account.status".replace("/", ""), "params": params},
            response_model=AccountInformationResponse,
            signer=None,
        )

    @pytest.mark.asyncio
    async def test_account_information_server_error(self):
        """Test that account_information() raises an error when the server returns an error."""

        mock_error = Exception("ResponseError")
        self.mock_websocket_api.send_signed_message.side_effect = mock_error

        with pytest.raises(Exception, match="ResponseError"):
            await self.websocket_api.account_information()

    @pytest.mark.asyncio
    async def test_futures_account_balance_success(self):
        """Test futures_account_balance() successfully with required parameters only."""

        expected_response = {
            "id": "9328e612-1560-4108-979e-283bf85b5acb",
            "status": 200,
            "result": [
                {
                    "accountAlias": "fWAuTiuXoCuXmY",
                    "asset": "WLD",
                    "balance": "0.00000000",
                    "withdrawAvailable": "0.00000000",
                    "crossWalletBalance": "0.00000000",
                    "crossUnPnl": "0.00000000",
                    "availableBalance": "0.00000000",
                    "updateTime": 0,
                }
            ],
            "rateLimits": [
                {
                    "rateLimitType": "REQUEST_WEIGHT",
                    "interval": "MINUTE",
                    "intervalNum": 1,
                    "limit": 2400,
                    "count": 10,
                }
            ],
        }

        self.mock_websocket_api.send_signed_message = AsyncMock(
            return_value=WebsocketApiResponse(
                data_function=lambda: expected_response,
                rate_limits=(
                    parse_ws_rate_limit_headers(expected_response["rateLimits"])
                    if "rateLimits" in expected_response
                    else None
                ),
            )
        )
        result = await self.websocket_api.futures_account_balance()

        actual_call_args = self.mock_websocket_api.send_signed_message.call_args
        request_kwargs = actual_call_args.kwargs

        assert "payload" in request_kwargs
        assert "method" in request_kwargs["payload"]
        assert request_kwargs["payload"]["method"] == "/account.balance".replace(
            "/", ""
        )

        assert result is not None
        assert result.data() == expected_response
        self.mock_websocket_api.send_signed_message.assert_called_once_with(
            payload={"method": "/account.balance".replace("/", ""), "params": {}},
            response_model=FuturesAccountBalanceResponse,
            signer=None,
        )

    @pytest.mark.asyncio
    async def test_futures_account_balance_success_with_optional_params(self):
        """Test futures_account_balance() successfully with optional parameters."""

        params = {"id": "e9d6b4349871b40611412680b3445fac", "recv_window": 5000}

        expected_response = {
            "id": "9328e612-1560-4108-979e-283bf85b5acb",
            "status": 200,
            "result": [
                {
                    "accountAlias": "fWAuTiuXoCuXmY",
                    "asset": "WLD",
                    "balance": "0.00000000",
                    "withdrawAvailable": "0.00000000",
                    "crossWalletBalance": "0.00000000",
                    "crossUnPnl": "0.00000000",
                    "availableBalance": "0.00000000",
                    "updateTime": 0,
                }
            ],
            "rateLimits": [
                {
                    "rateLimitType": "REQUEST_WEIGHT",
                    "interval": "MINUTE",
                    "intervalNum": 1,
                    "limit": 2400,
                    "count": 10,
                }
            ],
        }

        self.mock_websocket_api.send_signed_message = AsyncMock(
            return_value=WebsocketApiResponse(
                data_function=lambda: expected_response,
                rate_limits=(
                    parse_ws_rate_limit_headers(expected_response["rateLimits"])
                    if "rateLimits" in expected_response
                    else None
                ),
            )
        )

        result = await self.websocket_api.futures_account_balance(**params)

        actual_call_args = self.mock_websocket_api.send_signed_message.call_args
        request_kwargs = actual_call_args.kwargs

        assert "payload" in request_kwargs
        assert "method" in request_kwargs["payload"]
        assert request_kwargs["payload"]["method"] == "/account.balance".replace(
            "/", ""
        )
        assert params["id"] == "e9d6b4349871b40611412680b3445fac"
        assert params["recv_window"] == 5000

        assert result is not None
        assert result.data() == expected_response
        self.mock_websocket_api.send_signed_message.assert_called_once_with(
            payload={"method": "/account.balance".replace("/", ""), "params": params},
            response_model=FuturesAccountBalanceResponse,
            signer=None,
        )

    @pytest.mark.asyncio
    async def test_futures_account_balance_server_error(self):
        """Test that futures_account_balance() raises an error when the server returns an error."""

        mock_error = Exception("ResponseError")
        self.mock_websocket_api.send_signed_message.side_effect = mock_error

        with pytest.raises(Exception, match="ResponseError"):
            await self.websocket_api.futures_account_balance()
