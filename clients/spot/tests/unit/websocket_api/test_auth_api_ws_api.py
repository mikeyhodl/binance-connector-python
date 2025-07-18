"""
Binance Spot WebSocket API

OpenAPI Specifications for the Binance Spot WebSocket API

API documents:
  - [Github web-socket-api documentation file](https://github.com/binance/binance-spot-api-docs/blob/master/web-socket-api.md)
  - [General API information for web-socket-api on website](https://developers.binance.com/docs/binance-spot-api-docs/web-socket-api/general-api-information)

The version of the OpenAPI document: 1.0.0
Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""

import pytest

from unittest.mock import AsyncMock, MagicMock

from binance_common.models import WebsocketApiResponse
from binance_common.utils import parse_ws_rate_limit_headers
from binance_sdk_spot.websocket_api.api import AuthApi


from binance_sdk_spot.websocket_api.models import SessionLogonResponse
from binance_sdk_spot.websocket_api.models import SessionLogoutResponse
from binance_sdk_spot.websocket_api.models import SessionStatusResponse


class TestWebSocketAuthApi:
    @pytest.fixture(autouse=True)
    def setup_method(self):
        self.mock_websocket_api = MagicMock()
        self.websocket_api = AuthApi(websocket_api=self.mock_websocket_api)

    @pytest.mark.asyncio
    async def test_session_logon_success(self):
        """Test session_logon() successfully with required parameters only."""

        expected_response = {
            "id": "c174a2b1-3f51-4580-b200-8528bd237cb7",
            "status": 200,
            "result": {
                "apiKey": "vmPUZE6mv9SD5VNHk4HlWFsOr6aKE2zvsw0MuIgwCIPy6utIco14y7Ju91duEh8A",
                "authorizedSince": 1649729878532,
                "connectedSince": 1649729873021,
                "returnRateLimits": False,
                "serverTime": 1649729878630,
                "userDataStream": False,
            },
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
        result = await self.websocket_api.session_logon()

        actual_call_args = self.mock_websocket_api.send_signed_message.call_args
        request_kwargs = actual_call_args.kwargs

        assert "payload" in request_kwargs
        assert "method" in request_kwargs["payload"]
        assert request_kwargs["payload"]["method"] == "/session.logon".replace("/", "")

        assert result is not None
        assert result.data() == expected_response
        self.mock_websocket_api.send_signed_message.assert_called_once_with(
            payload={"method": "/session.logon".replace("/", ""), "params": {}},
            response_model=SessionLogonResponse,
            signer=None,
        )

    @pytest.mark.asyncio
    async def test_session_logon_success_with_optional_params(self):
        """Test session_logon() successfully with optional parameters."""

        params = {"id": "e9d6b4349871b40611412680b3445fac", "recv_window": 5000}

        expected_response = {
            "id": "c174a2b1-3f51-4580-b200-8528bd237cb7",
            "status": 200,
            "result": {
                "apiKey": "vmPUZE6mv9SD5VNHk4HlWFsOr6aKE2zvsw0MuIgwCIPy6utIco14y7Ju91duEh8A",
                "authorizedSince": 1649729878532,
                "connectedSince": 1649729873021,
                "returnRateLimits": False,
                "serverTime": 1649729878630,
                "userDataStream": False,
            },
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

        result = await self.websocket_api.session_logon(**params)

        actual_call_args = self.mock_websocket_api.send_signed_message.call_args
        request_kwargs = actual_call_args.kwargs

        assert "payload" in request_kwargs
        assert "method" in request_kwargs["payload"]
        assert request_kwargs["payload"]["method"] == "/session.logon".replace("/", "")
        assert "params" in request_kwargs["payload"]
        params = request_kwargs["payload"]["params"]
        assert params["id"] == "e9d6b4349871b40611412680b3445fac"
        assert params["recv_window"] == 5000

        assert result is not None
        assert result.data() == expected_response
        self.mock_websocket_api.send_signed_message.assert_called_once_with(
            payload={"method": "/session.logon".replace("/", ""), "params": params},
            response_model=SessionLogonResponse,
            signer=None,
        )

    @pytest.mark.asyncio
    async def test_session_logon_server_error(self):
        """Test that session_logon() raises an error when the server returns an error."""

        mock_error = Exception("ResponseError")
        self.mock_websocket_api.send_signed_message.side_effect = mock_error

        with pytest.raises(Exception, match="ResponseError"):
            await self.websocket_api.session_logon()

    @pytest.mark.asyncio
    async def test_session_logout_success(self):
        """Test session_logout() successfully with required parameters only."""

        expected_response = {
            "id": "c174a2b1-3f51-4580-b200-8528bd237cb7",
            "status": 200,
            "result": {
                "apiKey": "CAvIjXy3F44yW6Pou5k8Dy1swsYDWJZLeoK2r8G4cFDnE9nosRppc2eKc1T8TRTQ",
                "authorizedSince": 1649729878532,
                "connectedSince": 1649729873021,
                "returnRateLimits": False,
                "serverTime": 1649730611671,
                "userDataStream": False,
            },
        }

        self.mock_websocket_api.send_message = AsyncMock(
            return_value=WebsocketApiResponse(
                data_function=lambda: expected_response,
                rate_limits=(
                    parse_ws_rate_limit_headers(expected_response["rateLimits"])
                    if "rateLimits" in expected_response
                    else None
                ),
            )
        )
        result = await self.websocket_api.session_logout()

        actual_call_args = self.mock_websocket_api.send_message.call_args
        request_kwargs = actual_call_args.kwargs

        assert "payload" in request_kwargs
        assert "method" in request_kwargs["payload"]
        assert request_kwargs["payload"]["method"] == "/session.logout".replace("/", "")

        assert result is not None
        assert result.data() == expected_response
        self.mock_websocket_api.send_message.assert_called_once_with(
            payload={"method": "/session.logout".replace("/", ""), "params": {}},
            response_model=SessionLogoutResponse,
        )

    @pytest.mark.asyncio
    async def test_session_logout_success_with_optional_params(self):
        """Test session_logout() successfully with optional parameters."""

        params = {"id": "e9d6b4349871b40611412680b3445fac"}

        expected_response = {
            "id": "c174a2b1-3f51-4580-b200-8528bd237cb7",
            "status": 200,
            "result": {
                "apiKey": "CAvIjXy3F44yW6Pou5k8Dy1swsYDWJZLeoK2r8G4cFDnE9nosRppc2eKc1T8TRTQ",
                "authorizedSince": 1649729878532,
                "connectedSince": 1649729873021,
                "returnRateLimits": False,
                "serverTime": 1649730611671,
                "userDataStream": False,
            },
        }

        self.mock_websocket_api.send_message = AsyncMock(
            return_value=WebsocketApiResponse(
                data_function=lambda: expected_response,
                rate_limits=(
                    parse_ws_rate_limit_headers(expected_response["rateLimits"])
                    if "rateLimits" in expected_response
                    else None
                ),
            )
        )

        result = await self.websocket_api.session_logout(**params)

        actual_call_args = self.mock_websocket_api.send_message.call_args
        request_kwargs = actual_call_args.kwargs

        assert "payload" in request_kwargs
        assert "method" in request_kwargs["payload"]
        assert request_kwargs["payload"]["method"] == "/session.logout".replace("/", "")
        assert params["id"] == "e9d6b4349871b40611412680b3445fac"

        assert result is not None
        assert result.data() == expected_response
        self.mock_websocket_api.send_message.assert_called_once_with(
            payload={"method": "/session.logout".replace("/", ""), "params": params},
            response_model=SessionLogoutResponse,
        )

    @pytest.mark.asyncio
    async def test_session_logout_server_error(self):
        """Test that session_logout() raises an error when the server returns an error."""

        mock_error = Exception("ResponseError")
        self.mock_websocket_api.send_message.side_effect = mock_error

        with pytest.raises(Exception, match="ResponseError"):
            await self.websocket_api.session_logout()

    @pytest.mark.asyncio
    async def test_session_status_success(self):
        """Test session_status() successfully with required parameters only."""

        expected_response = {
            "id": "b50c16cd-62c9-4e29-89e4-37f10111f5bf",
            "status": 200,
            "result": {
                "apiKey": "vmPUZE6mv9SD5VNHk4HlWFsOr6aKE2zvsw0MuIgwCIPy6utIco14y7Ju91duEh8A",
                "authorizedSince": 1649729878532,
                "connectedSince": 1649729873021,
                "returnRateLimits": False,
                "serverTime": 1649730611671,
                "userDataStream": True,
            },
        }

        self.mock_websocket_api.send_message = AsyncMock(
            return_value=WebsocketApiResponse(
                data_function=lambda: expected_response,
                rate_limits=(
                    parse_ws_rate_limit_headers(expected_response["rateLimits"])
                    if "rateLimits" in expected_response
                    else None
                ),
            )
        )
        result = await self.websocket_api.session_status()

        actual_call_args = self.mock_websocket_api.send_message.call_args
        request_kwargs = actual_call_args.kwargs

        assert "payload" in request_kwargs
        assert "method" in request_kwargs["payload"]
        assert request_kwargs["payload"]["method"] == "/session.status".replace("/", "")

        assert result is not None
        assert result.data() == expected_response
        self.mock_websocket_api.send_message.assert_called_once_with(
            payload={"method": "/session.status".replace("/", ""), "params": {}},
            response_model=SessionStatusResponse,
        )

    @pytest.mark.asyncio
    async def test_session_status_success_with_optional_params(self):
        """Test session_status() successfully with optional parameters."""

        params = {"id": "e9d6b4349871b40611412680b3445fac"}

        expected_response = {
            "id": "b50c16cd-62c9-4e29-89e4-37f10111f5bf",
            "status": 200,
            "result": {
                "apiKey": "vmPUZE6mv9SD5VNHk4HlWFsOr6aKE2zvsw0MuIgwCIPy6utIco14y7Ju91duEh8A",
                "authorizedSince": 1649729878532,
                "connectedSince": 1649729873021,
                "returnRateLimits": False,
                "serverTime": 1649730611671,
                "userDataStream": True,
            },
        }

        self.mock_websocket_api.send_message = AsyncMock(
            return_value=WebsocketApiResponse(
                data_function=lambda: expected_response,
                rate_limits=(
                    parse_ws_rate_limit_headers(expected_response["rateLimits"])
                    if "rateLimits" in expected_response
                    else None
                ),
            )
        )

        result = await self.websocket_api.session_status(**params)

        actual_call_args = self.mock_websocket_api.send_message.call_args
        request_kwargs = actual_call_args.kwargs

        assert "payload" in request_kwargs
        assert "method" in request_kwargs["payload"]
        assert request_kwargs["payload"]["method"] == "/session.status".replace("/", "")
        assert params["id"] == "e9d6b4349871b40611412680b3445fac"

        assert result is not None
        assert result.data() == expected_response
        self.mock_websocket_api.send_message.assert_called_once_with(
            payload={"method": "/session.status".replace("/", ""), "params": params},
            response_model=SessionStatusResponse,
        )

    @pytest.mark.asyncio
    async def test_session_status_server_error(self):
        """Test that session_status() raises an error when the server returns an error."""

        mock_error = Exception("ResponseError")
        self.mock_websocket_api.send_message.side_effect = mock_error

        with pytest.raises(Exception, match="ResponseError"):
            await self.websocket_api.session_status()
