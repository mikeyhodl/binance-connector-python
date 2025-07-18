"""
Binance Derivatives Trading Options REST API

OpenAPI Specification for the Binance Derivatives Trading Options REST API
The version of the OpenAPI document: 1.0.0
Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""

import json
import pytest
import requests

from unittest.mock import MagicMock, patch
from urllib.parse import parse_qs

from binance_common.configuration import ConfigurationRestAPI
from binance_common.errors import RequiredError
from binance_common.utils import normalize_query_values, is_one_of_model, snake_to_camel

from binance_sdk_derivatives_trading_options.rest_api.api import MarketMakerEndpointsApi
from binance_sdk_derivatives_trading_options.rest_api.models import (
    AutoCancelAllOpenOrdersResponse,
)
from binance_sdk_derivatives_trading_options.rest_api.models import (
    GetAutoCancelAllOpenOrdersResponse,
)
from binance_sdk_derivatives_trading_options.rest_api.models import (
    GetMarketMakerProtectionConfigResponse,
)
from binance_sdk_derivatives_trading_options.rest_api.models import (
    OptionMarginAccountInformationResponse,
)
from binance_sdk_derivatives_trading_options.rest_api.models import (
    ResetMarketMakerProtectionConfigResponse,
)
from binance_sdk_derivatives_trading_options.rest_api.models import (
    SetAutoCancelAllOpenOrdersResponse,
)
from binance_sdk_derivatives_trading_options.rest_api.models import (
    SetMarketMakerProtectionConfigResponse,
)


class TestMarketMakerEndpointsApi:
    @pytest.fixture(autouse=True)
    def setup_client(self):
        """Setup a client instance with mocked session before each test method."""
        self.mock_session = MagicMock(spec=requests.Session)
        config = ConfigurationRestAPI(
            api_key="test-api-key",
            api_secret="test-api-secret",
        )
        self.client = MarketMakerEndpointsApi(
            configuration=config, session=self.mock_session
        )

    def set_mock_response(self, data: dict = {}, status_code=200, headers=None):
        """Helper method to setup mock response for the client's session request."""
        if headers is None:
            headers = {}

        mock_response = MagicMock()
        mock_response.status_code = status_code
        mock_response.json.return_value = data
        mock_response.text = json.dumps(data)
        mock_response.headers = headers

        self.mock_session.request.return_value = mock_response

    @patch("binance_common.utils.get_signature")
    def test_auto_cancel_all_open_orders_success(self, mock_get_signature):
        """Test auto_cancel_all_open_orders() successfully with required parameters only."""

        params = {
            "underlyings": "underlyings_example",
        }

        expected_response = {"underlyings": ["BTCUSDT", "ETHUSDT"]}
        mock_get_signature.return_value = "mocked_signature"
        self.set_mock_response(expected_response)

        response = self.client.auto_cancel_all_open_orders(**params)

        actual_call_args = self.mock_session.request.call_args
        request_kwargs = actual_call_args.kwargs
        parsed_params = parse_qs(request_kwargs["params"])
        camel_case_params = {snake_to_camel(k): v for k, v in params.items()}
        normalized = normalize_query_values(parsed_params, camel_case_params)

        self.mock_session.request.assert_called_once()
        mock_get_signature.assert_called_once()

        assert "url" in request_kwargs
        assert "signature" in parse_qs(request_kwargs["params"])
        assert "/eapi/v1/countdownCancelAllHeartBeat" in request_kwargs["url"]
        assert request_kwargs["method"] == "POST"
        assert normalized["underlyings"] == "underlyings_example"

        assert response is not None
        is_list = isinstance(expected_response, list)
        is_flat_list = (
            is_list and not isinstance(expected_response[0], list) if is_list else False
        )
        is_oneof = is_one_of_model(AutoCancelAllOpenOrdersResponse)

        if is_list and not is_flat_list:
            expected = expected_response
        elif is_oneof or is_list:
            expected = AutoCancelAllOpenOrdersResponse.from_dict(expected_response)
        else:
            expected = AutoCancelAllOpenOrdersResponse.model_validate_json(
                json.dumps(expected_response)
            )

        assert response.data() == expected

    @patch("binance_common.utils.get_signature")
    def test_auto_cancel_all_open_orders_success_with_optional_params(
        self, mock_get_signature
    ):
        """Test auto_cancel_all_open_orders() successfully with optional parameters."""

        params = {"underlyings": "underlyings_example", "recv_window": 5000}

        expected_response = {"underlyings": ["BTCUSDT", "ETHUSDT"]}
        mock_get_signature.return_value = "mocked_signature"
        self.set_mock_response(expected_response)

        response = self.client.auto_cancel_all_open_orders(**params)

        actual_call_args = self.mock_session.request.call_args
        request_kwargs = actual_call_args.kwargs

        assert "url" in request_kwargs
        assert "signature" in parse_qs(request_kwargs["params"])
        assert "/eapi/v1/countdownCancelAllHeartBeat" in request_kwargs["url"]
        assert request_kwargs["method"] == "POST"

        self.mock_session.request.assert_called_once()
        assert response is not None
        is_list = isinstance(expected_response, list)
        is_flat_list = (
            is_list and not isinstance(expected_response[0], list) if is_list else False
        )
        is_oneof = is_one_of_model(AutoCancelAllOpenOrdersResponse)

        if is_list and not is_flat_list:
            expected = expected_response
        elif is_oneof or is_list:
            expected = AutoCancelAllOpenOrdersResponse.from_dict(expected_response)
        else:
            expected = AutoCancelAllOpenOrdersResponse.model_validate_json(
                json.dumps(expected_response)
            )

        assert response.data() == expected

    def test_auto_cancel_all_open_orders_missing_required_param_underlyings(self):
        """Test that auto_cancel_all_open_orders() raises RequiredError when 'underlyings' is missing."""
        params = {
            "underlyings": "underlyings_example",
        }
        del params["underlyings"]

        with pytest.raises(
            RequiredError, match="Missing required parameter 'underlyings'"
        ):
            self.client.auto_cancel_all_open_orders(**params)

    def test_auto_cancel_all_open_orders_server_error(self):
        """Test that auto_cancel_all_open_orders() raises an error when the server returns an error."""

        params = {
            "underlyings": "underlyings_example",
        }

        mock_error = Exception("ResponseError")
        self.client.auto_cancel_all_open_orders = MagicMock(side_effect=mock_error)

        with pytest.raises(Exception, match="ResponseError"):
            self.client.auto_cancel_all_open_orders(**params)

    @patch("binance_common.utils.get_signature")
    def test_get_auto_cancel_all_open_orders_success(self, mock_get_signature):
        """Test get_auto_cancel_all_open_orders() successfully with required parameters only."""

        expected_response = {"underlying": "ETHUSDT", "countdownTime": 100000}
        mock_get_signature.return_value = "mocked_signature"
        self.set_mock_response(expected_response)

        response = self.client.get_auto_cancel_all_open_orders()

        actual_call_args = self.mock_session.request.call_args
        request_kwargs = actual_call_args.kwargs

        self.mock_session.request.assert_called_once()
        mock_get_signature.assert_called_once()

        assert "url" in request_kwargs
        assert "signature" in parse_qs(request_kwargs["params"])
        assert "/eapi/v1/countdownCancelAll" in request_kwargs["url"]
        assert request_kwargs["method"] == "GET"

        assert response is not None
        is_list = isinstance(expected_response, list)
        is_flat_list = (
            is_list and not isinstance(expected_response[0], list) if is_list else False
        )
        is_oneof = is_one_of_model(GetAutoCancelAllOpenOrdersResponse)

        if is_list and not is_flat_list:
            expected = expected_response
        elif is_oneof or is_list:
            expected = GetAutoCancelAllOpenOrdersResponse.from_dict(expected_response)
        else:
            expected = GetAutoCancelAllOpenOrdersResponse.model_validate_json(
                json.dumps(expected_response)
            )

        assert response.data() == expected

    @patch("binance_common.utils.get_signature")
    def test_get_auto_cancel_all_open_orders_success_with_optional_params(
        self, mock_get_signature
    ):
        """Test get_auto_cancel_all_open_orders() successfully with optional parameters."""

        params = {"underlying": "underlying_example", "recv_window": 5000}

        expected_response = {"underlying": "ETHUSDT", "countdownTime": 100000}
        mock_get_signature.return_value = "mocked_signature"
        self.set_mock_response(expected_response)

        response = self.client.get_auto_cancel_all_open_orders(**params)

        actual_call_args = self.mock_session.request.call_args
        request_kwargs = actual_call_args.kwargs

        assert "url" in request_kwargs
        assert "signature" in parse_qs(request_kwargs["params"])
        assert "/eapi/v1/countdownCancelAll" in request_kwargs["url"]
        assert request_kwargs["method"] == "GET"

        self.mock_session.request.assert_called_once()
        assert response is not None
        is_list = isinstance(expected_response, list)
        is_flat_list = (
            is_list and not isinstance(expected_response[0], list) if is_list else False
        )
        is_oneof = is_one_of_model(GetAutoCancelAllOpenOrdersResponse)

        if is_list and not is_flat_list:
            expected = expected_response
        elif is_oneof or is_list:
            expected = GetAutoCancelAllOpenOrdersResponse.from_dict(expected_response)
        else:
            expected = GetAutoCancelAllOpenOrdersResponse.model_validate_json(
                json.dumps(expected_response)
            )

        assert response.data() == expected

    def test_get_auto_cancel_all_open_orders_server_error(self):
        """Test that get_auto_cancel_all_open_orders() raises an error when the server returns an error."""

        mock_error = Exception("ResponseError")
        self.client.get_auto_cancel_all_open_orders = MagicMock(side_effect=mock_error)

        with pytest.raises(Exception, match="ResponseError"):
            self.client.get_auto_cancel_all_open_orders()

    @patch("binance_common.utils.get_signature")
    def test_get_market_maker_protection_config_success(self, mock_get_signature):
        """Test get_market_maker_protection_config() successfully with required parameters only."""

        expected_response = {
            "underlyingId": 2,
            "underlying": "BTCUSDT",
            "windowTimeInMilliseconds": 3000,
            "frozenTimeInMilliseconds": 300000,
            "qtyLimit": "2",
            "deltaLimit": "2.3",
            "lastTriggerTime": 0,
        }
        mock_get_signature.return_value = "mocked_signature"
        self.set_mock_response(expected_response)

        response = self.client.get_market_maker_protection_config()

        actual_call_args = self.mock_session.request.call_args
        request_kwargs = actual_call_args.kwargs

        self.mock_session.request.assert_called_once()
        mock_get_signature.assert_called_once()

        assert "url" in request_kwargs
        assert "signature" in parse_qs(request_kwargs["params"])
        assert "/eapi/v1/mmp" in request_kwargs["url"]
        assert request_kwargs["method"] == "GET"

        assert response is not None
        is_list = isinstance(expected_response, list)
        is_flat_list = (
            is_list and not isinstance(expected_response[0], list) if is_list else False
        )
        is_oneof = is_one_of_model(GetMarketMakerProtectionConfigResponse)

        if is_list and not is_flat_list:
            expected = expected_response
        elif is_oneof or is_list:
            expected = GetMarketMakerProtectionConfigResponse.from_dict(
                expected_response
            )
        else:
            expected = GetMarketMakerProtectionConfigResponse.model_validate_json(
                json.dumps(expected_response)
            )

        assert response.data() == expected

    @patch("binance_common.utils.get_signature")
    def test_get_market_maker_protection_config_success_with_optional_params(
        self, mock_get_signature
    ):
        """Test get_market_maker_protection_config() successfully with optional parameters."""

        params = {"underlying": "underlying_example", "recv_window": 5000}

        expected_response = {
            "underlyingId": 2,
            "underlying": "BTCUSDT",
            "windowTimeInMilliseconds": 3000,
            "frozenTimeInMilliseconds": 300000,
            "qtyLimit": "2",
            "deltaLimit": "2.3",
            "lastTriggerTime": 0,
        }
        mock_get_signature.return_value = "mocked_signature"
        self.set_mock_response(expected_response)

        response = self.client.get_market_maker_protection_config(**params)

        actual_call_args = self.mock_session.request.call_args
        request_kwargs = actual_call_args.kwargs

        assert "url" in request_kwargs
        assert "signature" in parse_qs(request_kwargs["params"])
        assert "/eapi/v1/mmp" in request_kwargs["url"]
        assert request_kwargs["method"] == "GET"

        self.mock_session.request.assert_called_once()
        assert response is not None
        is_list = isinstance(expected_response, list)
        is_flat_list = (
            is_list and not isinstance(expected_response[0], list) if is_list else False
        )
        is_oneof = is_one_of_model(GetMarketMakerProtectionConfigResponse)

        if is_list and not is_flat_list:
            expected = expected_response
        elif is_oneof or is_list:
            expected = GetMarketMakerProtectionConfigResponse.from_dict(
                expected_response
            )
        else:
            expected = GetMarketMakerProtectionConfigResponse.model_validate_json(
                json.dumps(expected_response)
            )

        assert response.data() == expected

    def test_get_market_maker_protection_config_server_error(self):
        """Test that get_market_maker_protection_config() raises an error when the server returns an error."""

        mock_error = Exception("ResponseError")
        self.client.get_market_maker_protection_config = MagicMock(
            side_effect=mock_error
        )

        with pytest.raises(Exception, match="ResponseError"):
            self.client.get_market_maker_protection_config()

    @patch("binance_common.utils.get_signature")
    def test_option_margin_account_information_success(self, mock_get_signature):
        """Test option_margin_account_information() successfully with required parameters only."""

        expected_response = {
            "asset": [
                {
                    "asset": "USDT",
                    "marginBalance": "10099.448",
                    "equity": "10094.44662",
                    "available": "8725.92524",
                    "initialMargin": "1084.52138",
                    "maintMargin": "151.00138",
                    "unrealizedPNL": "-5.00138",
                    "lpProfit": "-5.00138",
                }
            ],
            "greek": [
                {
                    "underlying": "BTCUSDT",
                    "delta": "-0.05",
                    "gamma": "-0.002",
                    "theta": "-0.05",
                    "vega": "-0.002",
                }
            ],
            "time": 1592449455993,
        }
        mock_get_signature.return_value = "mocked_signature"
        self.set_mock_response(expected_response)

        response = self.client.option_margin_account_information()

        actual_call_args = self.mock_session.request.call_args
        request_kwargs = actual_call_args.kwargs

        self.mock_session.request.assert_called_once()
        mock_get_signature.assert_called_once()

        assert "url" in request_kwargs
        assert "signature" in parse_qs(request_kwargs["params"])
        assert "/eapi/v1/marginAccount" in request_kwargs["url"]
        assert request_kwargs["method"] == "GET"

        assert response is not None
        is_list = isinstance(expected_response, list)
        is_flat_list = (
            is_list and not isinstance(expected_response[0], list) if is_list else False
        )
        is_oneof = is_one_of_model(OptionMarginAccountInformationResponse)

        if is_list and not is_flat_list:
            expected = expected_response
        elif is_oneof or is_list:
            expected = OptionMarginAccountInformationResponse.from_dict(
                expected_response
            )
        else:
            expected = OptionMarginAccountInformationResponse.model_validate_json(
                json.dumps(expected_response)
            )

        assert response.data() == expected

    @patch("binance_common.utils.get_signature")
    def test_option_margin_account_information_success_with_optional_params(
        self, mock_get_signature
    ):
        """Test option_margin_account_information() successfully with optional parameters."""

        params = {"recv_window": 5000}

        expected_response = {
            "asset": [
                {
                    "asset": "USDT",
                    "marginBalance": "10099.448",
                    "equity": "10094.44662",
                    "available": "8725.92524",
                    "initialMargin": "1084.52138",
                    "maintMargin": "151.00138",
                    "unrealizedPNL": "-5.00138",
                    "lpProfit": "-5.00138",
                }
            ],
            "greek": [
                {
                    "underlying": "BTCUSDT",
                    "delta": "-0.05",
                    "gamma": "-0.002",
                    "theta": "-0.05",
                    "vega": "-0.002",
                }
            ],
            "time": 1592449455993,
        }
        mock_get_signature.return_value = "mocked_signature"
        self.set_mock_response(expected_response)

        response = self.client.option_margin_account_information(**params)

        actual_call_args = self.mock_session.request.call_args
        request_kwargs = actual_call_args.kwargs

        assert "url" in request_kwargs
        assert "signature" in parse_qs(request_kwargs["params"])
        assert "/eapi/v1/marginAccount" in request_kwargs["url"]
        assert request_kwargs["method"] == "GET"

        self.mock_session.request.assert_called_once()
        assert response is not None
        is_list = isinstance(expected_response, list)
        is_flat_list = (
            is_list and not isinstance(expected_response[0], list) if is_list else False
        )
        is_oneof = is_one_of_model(OptionMarginAccountInformationResponse)

        if is_list and not is_flat_list:
            expected = expected_response
        elif is_oneof or is_list:
            expected = OptionMarginAccountInformationResponse.from_dict(
                expected_response
            )
        else:
            expected = OptionMarginAccountInformationResponse.model_validate_json(
                json.dumps(expected_response)
            )

        assert response.data() == expected

    def test_option_margin_account_information_server_error(self):
        """Test that option_margin_account_information() raises an error when the server returns an error."""

        mock_error = Exception("ResponseError")
        self.client.option_margin_account_information = MagicMock(
            side_effect=mock_error
        )

        with pytest.raises(Exception, match="ResponseError"):
            self.client.option_margin_account_information()

    @patch("binance_common.utils.get_signature")
    def test_reset_market_maker_protection_config_success(self, mock_get_signature):
        """Test reset_market_maker_protection_config() successfully with required parameters only."""

        expected_response = {
            "underlyingId": 2,
            "underlying": "BTCUSDT",
            "windowTimeInMilliseconds": 3000,
            "frozenTimeInMilliseconds": 300000,
            "qtyLimit": "2",
            "deltaLimit": "2.3",
            "lastTriggerTime": 0,
        }
        mock_get_signature.return_value = "mocked_signature"
        self.set_mock_response(expected_response)

        response = self.client.reset_market_maker_protection_config()

        actual_call_args = self.mock_session.request.call_args
        request_kwargs = actual_call_args.kwargs

        self.mock_session.request.assert_called_once()
        mock_get_signature.assert_called_once()

        assert "url" in request_kwargs
        assert "signature" in parse_qs(request_kwargs["params"])
        assert "/eapi/v1/mmpReset" in request_kwargs["url"]
        assert request_kwargs["method"] == "POST"

        assert response is not None
        is_list = isinstance(expected_response, list)
        is_flat_list = (
            is_list and not isinstance(expected_response[0], list) if is_list else False
        )
        is_oneof = is_one_of_model(ResetMarketMakerProtectionConfigResponse)

        if is_list and not is_flat_list:
            expected = expected_response
        elif is_oneof or is_list:
            expected = ResetMarketMakerProtectionConfigResponse.from_dict(
                expected_response
            )
        else:
            expected = ResetMarketMakerProtectionConfigResponse.model_validate_json(
                json.dumps(expected_response)
            )

        assert response.data() == expected

    @patch("binance_common.utils.get_signature")
    def test_reset_market_maker_protection_config_success_with_optional_params(
        self, mock_get_signature
    ):
        """Test reset_market_maker_protection_config() successfully with optional parameters."""

        params = {"underlying": "underlying_example", "recv_window": 5000}

        expected_response = {
            "underlyingId": 2,
            "underlying": "BTCUSDT",
            "windowTimeInMilliseconds": 3000,
            "frozenTimeInMilliseconds": 300000,
            "qtyLimit": "2",
            "deltaLimit": "2.3",
            "lastTriggerTime": 0,
        }
        mock_get_signature.return_value = "mocked_signature"
        self.set_mock_response(expected_response)

        response = self.client.reset_market_maker_protection_config(**params)

        actual_call_args = self.mock_session.request.call_args
        request_kwargs = actual_call_args.kwargs

        assert "url" in request_kwargs
        assert "signature" in parse_qs(request_kwargs["params"])
        assert "/eapi/v1/mmpReset" in request_kwargs["url"]
        assert request_kwargs["method"] == "POST"

        self.mock_session.request.assert_called_once()
        assert response is not None
        is_list = isinstance(expected_response, list)
        is_flat_list = (
            is_list and not isinstance(expected_response[0], list) if is_list else False
        )
        is_oneof = is_one_of_model(ResetMarketMakerProtectionConfigResponse)

        if is_list and not is_flat_list:
            expected = expected_response
        elif is_oneof or is_list:
            expected = ResetMarketMakerProtectionConfigResponse.from_dict(
                expected_response
            )
        else:
            expected = ResetMarketMakerProtectionConfigResponse.model_validate_json(
                json.dumps(expected_response)
            )

        assert response.data() == expected

    def test_reset_market_maker_protection_config_server_error(self):
        """Test that reset_market_maker_protection_config() raises an error when the server returns an error."""

        mock_error = Exception("ResponseError")
        self.client.reset_market_maker_protection_config = MagicMock(
            side_effect=mock_error
        )

        with pytest.raises(Exception, match="ResponseError"):
            self.client.reset_market_maker_protection_config()

    @patch("binance_common.utils.get_signature")
    def test_set_auto_cancel_all_open_orders_success(self, mock_get_signature):
        """Test set_auto_cancel_all_open_orders() successfully with required parameters only."""

        params = {
            "underlying": "underlying_example",
            "countdown_time": 56,
        }

        expected_response = {"underlying": "ETHUSDT", "countdownTime": 30000}
        mock_get_signature.return_value = "mocked_signature"
        self.set_mock_response(expected_response)

        response = self.client.set_auto_cancel_all_open_orders(**params)

        actual_call_args = self.mock_session.request.call_args
        request_kwargs = actual_call_args.kwargs
        parsed_params = parse_qs(request_kwargs["params"])
        camel_case_params = {snake_to_camel(k): v for k, v in params.items()}
        normalized = normalize_query_values(parsed_params, camel_case_params)

        self.mock_session.request.assert_called_once()
        mock_get_signature.assert_called_once()

        assert "url" in request_kwargs
        assert "signature" in parse_qs(request_kwargs["params"])
        assert "/eapi/v1/countdownCancelAll" in request_kwargs["url"]
        assert request_kwargs["method"] == "POST"
        assert normalized["underlying"] == "underlying_example"
        assert normalized["countdownTime"] == 56

        assert response is not None
        is_list = isinstance(expected_response, list)
        is_flat_list = (
            is_list and not isinstance(expected_response[0], list) if is_list else False
        )
        is_oneof = is_one_of_model(SetAutoCancelAllOpenOrdersResponse)

        if is_list and not is_flat_list:
            expected = expected_response
        elif is_oneof or is_list:
            expected = SetAutoCancelAllOpenOrdersResponse.from_dict(expected_response)
        else:
            expected = SetAutoCancelAllOpenOrdersResponse.model_validate_json(
                json.dumps(expected_response)
            )

        assert response.data() == expected

    @patch("binance_common.utils.get_signature")
    def test_set_auto_cancel_all_open_orders_success_with_optional_params(
        self, mock_get_signature
    ):
        """Test set_auto_cancel_all_open_orders() successfully with optional parameters."""

        params = {
            "underlying": "underlying_example",
            "countdown_time": 56,
            "recv_window": 5000,
        }

        expected_response = {"underlying": "ETHUSDT", "countdownTime": 30000}
        mock_get_signature.return_value = "mocked_signature"
        self.set_mock_response(expected_response)

        response = self.client.set_auto_cancel_all_open_orders(**params)

        actual_call_args = self.mock_session.request.call_args
        request_kwargs = actual_call_args.kwargs

        assert "url" in request_kwargs
        assert "signature" in parse_qs(request_kwargs["params"])
        assert "/eapi/v1/countdownCancelAll" in request_kwargs["url"]
        assert request_kwargs["method"] == "POST"

        self.mock_session.request.assert_called_once()
        assert response is not None
        is_list = isinstance(expected_response, list)
        is_flat_list = (
            is_list and not isinstance(expected_response[0], list) if is_list else False
        )
        is_oneof = is_one_of_model(SetAutoCancelAllOpenOrdersResponse)

        if is_list and not is_flat_list:
            expected = expected_response
        elif is_oneof or is_list:
            expected = SetAutoCancelAllOpenOrdersResponse.from_dict(expected_response)
        else:
            expected = SetAutoCancelAllOpenOrdersResponse.model_validate_json(
                json.dumps(expected_response)
            )

        assert response.data() == expected

    def test_set_auto_cancel_all_open_orders_missing_required_param_underlying(self):
        """Test that set_auto_cancel_all_open_orders() raises RequiredError when 'underlying' is missing."""
        params = {
            "underlying": "underlying_example",
            "countdown_time": 56,
        }
        del params["underlying"]

        with pytest.raises(
            RequiredError, match="Missing required parameter 'underlying'"
        ):
            self.client.set_auto_cancel_all_open_orders(**params)

    def test_set_auto_cancel_all_open_orders_missing_required_param_countdown_time(
        self,
    ):
        """Test that set_auto_cancel_all_open_orders() raises RequiredError when 'countdown_time' is missing."""
        params = {
            "underlying": "underlying_example",
            "countdown_time": 56,
        }
        del params["countdown_time"]

        with pytest.raises(
            RequiredError, match="Missing required parameter 'countdown_time'"
        ):
            self.client.set_auto_cancel_all_open_orders(**params)

    def test_set_auto_cancel_all_open_orders_server_error(self):
        """Test that set_auto_cancel_all_open_orders() raises an error when the server returns an error."""

        params = {
            "underlying": "underlying_example",
            "countdown_time": 56,
        }

        mock_error = Exception("ResponseError")
        self.client.set_auto_cancel_all_open_orders = MagicMock(side_effect=mock_error)

        with pytest.raises(Exception, match="ResponseError"):
            self.client.set_auto_cancel_all_open_orders(**params)

    @patch("binance_common.utils.get_signature")
    def test_set_market_maker_protection_config_success(self, mock_get_signature):
        """Test set_market_maker_protection_config() successfully with required parameters only."""

        expected_response = {
            "underlyingId": 2,
            "underlying": "BTCUSDT",
            "windowTimeInMilliseconds": 3000,
            "frozenTimeInMilliseconds": 300000,
            "qtyLimit": "2",
            "deltaLimit": "2.3",
            "lastTriggerTime": 0,
        }
        mock_get_signature.return_value = "mocked_signature"
        self.set_mock_response(expected_response)

        response = self.client.set_market_maker_protection_config()

        actual_call_args = self.mock_session.request.call_args
        request_kwargs = actual_call_args.kwargs

        self.mock_session.request.assert_called_once()
        mock_get_signature.assert_called_once()

        assert "url" in request_kwargs
        assert "signature" in parse_qs(request_kwargs["params"])
        assert "/eapi/v1/mmpSet" in request_kwargs["url"]
        assert request_kwargs["method"] == "POST"

        assert response is not None
        is_list = isinstance(expected_response, list)
        is_flat_list = (
            is_list and not isinstance(expected_response[0], list) if is_list else False
        )
        is_oneof = is_one_of_model(SetMarketMakerProtectionConfigResponse)

        if is_list and not is_flat_list:
            expected = expected_response
        elif is_oneof or is_list:
            expected = SetMarketMakerProtectionConfigResponse.from_dict(
                expected_response
            )
        else:
            expected = SetMarketMakerProtectionConfigResponse.model_validate_json(
                json.dumps(expected_response)
            )

        assert response.data() == expected

    @patch("binance_common.utils.get_signature")
    def test_set_market_maker_protection_config_success_with_optional_params(
        self, mock_get_signature
    ):
        """Test set_market_maker_protection_config() successfully with optional parameters."""

        params = {
            "underlying": "underlying_example",
            "window_time_in_milliseconds": 56,
            "frozen_time_in_milliseconds": 56,
            "qty_limit": 1.0,
            "delta_limit": 1.0,
            "recv_window": 5000,
        }

        expected_response = {
            "underlyingId": 2,
            "underlying": "BTCUSDT",
            "windowTimeInMilliseconds": 3000,
            "frozenTimeInMilliseconds": 300000,
            "qtyLimit": "2",
            "deltaLimit": "2.3",
            "lastTriggerTime": 0,
        }
        mock_get_signature.return_value = "mocked_signature"
        self.set_mock_response(expected_response)

        response = self.client.set_market_maker_protection_config(**params)

        actual_call_args = self.mock_session.request.call_args
        request_kwargs = actual_call_args.kwargs

        assert "url" in request_kwargs
        assert "signature" in parse_qs(request_kwargs["params"])
        assert "/eapi/v1/mmpSet" in request_kwargs["url"]
        assert request_kwargs["method"] == "POST"

        self.mock_session.request.assert_called_once()
        assert response is not None
        is_list = isinstance(expected_response, list)
        is_flat_list = (
            is_list and not isinstance(expected_response[0], list) if is_list else False
        )
        is_oneof = is_one_of_model(SetMarketMakerProtectionConfigResponse)

        if is_list and not is_flat_list:
            expected = expected_response
        elif is_oneof or is_list:
            expected = SetMarketMakerProtectionConfigResponse.from_dict(
                expected_response
            )
        else:
            expected = SetMarketMakerProtectionConfigResponse.model_validate_json(
                json.dumps(expected_response)
            )

        assert response.data() == expected

    def test_set_market_maker_protection_config_server_error(self):
        """Test that set_market_maker_protection_config() raises an error when the server returns an error."""

        mock_error = Exception("ResponseError")
        self.client.set_market_maker_protection_config = MagicMock(
            side_effect=mock_error
        )

        with pytest.raises(Exception, match="ResponseError"):
            self.client.set_market_maker_protection_config()
