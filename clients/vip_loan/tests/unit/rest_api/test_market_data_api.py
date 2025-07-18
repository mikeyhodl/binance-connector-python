"""
Binance VIP Loan REST API

OpenAPI Specification for the Binance VIP Loan REST API
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

from binance_sdk_vip_loan.rest_api.api import MarketDataApi
from binance_sdk_vip_loan.rest_api.models import GetBorrowInterestRateResponse
from binance_sdk_vip_loan.rest_api.models import GetCollateralAssetDataResponse
from binance_sdk_vip_loan.rest_api.models import GetLoanableAssetsDataResponse


class TestMarketDataApi:
    @pytest.fixture(autouse=True)
    def setup_client(self):
        """Setup a client instance with mocked session before each test method."""
        self.mock_session = MagicMock(spec=requests.Session)
        config = ConfigurationRestAPI(
            api_key="test-api-key",
            api_secret="test-api-secret",
        )
        self.client = MarketDataApi(configuration=config, session=self.mock_session)

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
    def test_get_borrow_interest_rate_success(self, mock_get_signature):
        """Test get_borrow_interest_rate() successfully with required parameters only."""

        params = {
            "loan_coin": "loan_coin_example",
        }

        expected_response = [
            {
                "asset": "BUSD",
                "flexibleDailyInterestRate": "0.001503",
                "flexibleYearlyInterestRate": "0.548595",
                "time": 1577233578000,
            },
            {
                "asset": "BTC",
                "flexibleDailyInterestRate": "0.001503",
                "flexibleYearlyInterestRate": "0.548595",
                "time": 1577233562000,
            },
        ]
        mock_get_signature.return_value = "mocked_signature"
        self.set_mock_response(expected_response)

        response = self.client.get_borrow_interest_rate(**params)

        actual_call_args = self.mock_session.request.call_args
        request_kwargs = actual_call_args.kwargs
        parsed_params = parse_qs(request_kwargs["params"])
        camel_case_params = {snake_to_camel(k): v for k, v in params.items()}
        normalized = normalize_query_values(parsed_params, camel_case_params)

        self.mock_session.request.assert_called_once()
        mock_get_signature.assert_called_once()

        assert "url" in request_kwargs
        assert "signature" in parse_qs(request_kwargs["params"])
        assert "/sapi/v1/loan/vip/request/interestRate" in request_kwargs["url"]
        assert request_kwargs["method"] == "GET"
        assert normalized["loanCoin"] == "loan_coin_example"

        assert response is not None
        is_list = isinstance(expected_response, list)
        is_flat_list = (
            is_list and not isinstance(expected_response[0], list) if is_list else False
        )
        is_oneof = is_one_of_model(GetBorrowInterestRateResponse)

        if is_list and not is_flat_list:
            expected = expected_response
        elif is_oneof or is_list:
            expected = GetBorrowInterestRateResponse.from_dict(expected_response)
        else:
            expected = GetBorrowInterestRateResponse.model_validate_json(
                json.dumps(expected_response)
            )

        assert response.data() == expected

    @patch("binance_common.utils.get_signature")
    def test_get_borrow_interest_rate_success_with_optional_params(
        self, mock_get_signature
    ):
        """Test get_borrow_interest_rate() successfully with optional parameters."""

        params = {"loan_coin": "loan_coin_example", "recv_window": 5000}

        expected_response = [
            {
                "asset": "BUSD",
                "flexibleDailyInterestRate": "0.001503",
                "flexibleYearlyInterestRate": "0.548595",
                "time": 1577233578000,
            },
            {
                "asset": "BTC",
                "flexibleDailyInterestRate": "0.001503",
                "flexibleYearlyInterestRate": "0.548595",
                "time": 1577233562000,
            },
        ]
        mock_get_signature.return_value = "mocked_signature"
        self.set_mock_response(expected_response)

        response = self.client.get_borrow_interest_rate(**params)

        actual_call_args = self.mock_session.request.call_args
        request_kwargs = actual_call_args.kwargs

        assert "url" in request_kwargs
        assert "signature" in parse_qs(request_kwargs["params"])
        assert "/sapi/v1/loan/vip/request/interestRate" in request_kwargs["url"]
        assert request_kwargs["method"] == "GET"

        self.mock_session.request.assert_called_once()
        assert response is not None
        is_list = isinstance(expected_response, list)
        is_flat_list = (
            is_list and not isinstance(expected_response[0], list) if is_list else False
        )
        is_oneof = is_one_of_model(GetBorrowInterestRateResponse)

        if is_list and not is_flat_list:
            expected = expected_response
        elif is_oneof or is_list:
            expected = GetBorrowInterestRateResponse.from_dict(expected_response)
        else:
            expected = GetBorrowInterestRateResponse.model_validate_json(
                json.dumps(expected_response)
            )

        assert response.data() == expected

    def test_get_borrow_interest_rate_missing_required_param_loan_coin(self):
        """Test that get_borrow_interest_rate() raises RequiredError when 'loan_coin' is missing."""
        params = {
            "loan_coin": "loan_coin_example",
        }
        del params["loan_coin"]

        with pytest.raises(
            RequiredError, match="Missing required parameter 'loan_coin'"
        ):
            self.client.get_borrow_interest_rate(**params)

    def test_get_borrow_interest_rate_server_error(self):
        """Test that get_borrow_interest_rate() raises an error when the server returns an error."""

        params = {
            "loan_coin": "loan_coin_example",
        }

        mock_error = Exception("ResponseError")
        self.client.get_borrow_interest_rate = MagicMock(side_effect=mock_error)

        with pytest.raises(Exception, match="ResponseError"):
            self.client.get_borrow_interest_rate(**params)

    @patch("binance_common.utils.get_signature")
    def test_get_collateral_asset_data_success(self, mock_get_signature):
        """Test get_collateral_asset_data() successfully with required parameters only."""

        expected_response = {
            "rows": [
                {
                    "collateralCoin": "BUSD",
                    "_1stCollateralRatio": "100%",
                    "_1stCollateralRange": "1-10000000",
                    "_2ndCollateralRatio": "80%",
                    "_2ndCollateralRange": "10000000-100000000",
                    "_3rdCollateralRatio": "60%",
                    "_3rdCollateralRange": "100000000-1000000000",
                    "_4thCollateralRatio": "0%",
                    "_4thCollateralRange": ">10000000000",
                }
            ],
            "total": 1,
        }
        mock_get_signature.return_value = "mocked_signature"
        self.set_mock_response(expected_response)

        response = self.client.get_collateral_asset_data()

        actual_call_args = self.mock_session.request.call_args
        request_kwargs = actual_call_args.kwargs

        self.mock_session.request.assert_called_once()
        mock_get_signature.assert_called_once()

        assert "url" in request_kwargs
        assert "signature" in parse_qs(request_kwargs["params"])
        assert "/sapi/v1/loan/vip/collateral/data" in request_kwargs["url"]
        assert request_kwargs["method"] == "GET"

        assert response is not None
        is_list = isinstance(expected_response, list)
        is_flat_list = (
            is_list and not isinstance(expected_response[0], list) if is_list else False
        )
        is_oneof = is_one_of_model(GetCollateralAssetDataResponse)

        if is_list and not is_flat_list:
            expected = expected_response
        elif is_oneof or is_list:
            expected = GetCollateralAssetDataResponse.from_dict(expected_response)
        else:
            expected = GetCollateralAssetDataResponse.model_validate_json(
                json.dumps(expected_response)
            )

        assert response.data() == expected

    @patch("binance_common.utils.get_signature")
    def test_get_collateral_asset_data_success_with_optional_params(
        self, mock_get_signature
    ):
        """Test get_collateral_asset_data() successfully with optional parameters."""

        params = {"collateral_coin": "collateral_coin_example", "recv_window": 5000}

        expected_response = {
            "rows": [
                {
                    "collateralCoin": "BUSD",
                    "_1stCollateralRatio": "100%",
                    "_1stCollateralRange": "1-10000000",
                    "_2ndCollateralRatio": "80%",
                    "_2ndCollateralRange": "10000000-100000000",
                    "_3rdCollateralRatio": "60%",
                    "_3rdCollateralRange": "100000000-1000000000",
                    "_4thCollateralRatio": "0%",
                    "_4thCollateralRange": ">10000000000",
                }
            ],
            "total": 1,
        }
        mock_get_signature.return_value = "mocked_signature"
        self.set_mock_response(expected_response)

        response = self.client.get_collateral_asset_data(**params)

        actual_call_args = self.mock_session.request.call_args
        request_kwargs = actual_call_args.kwargs

        assert "url" in request_kwargs
        assert "signature" in parse_qs(request_kwargs["params"])
        assert "/sapi/v1/loan/vip/collateral/data" in request_kwargs["url"]
        assert request_kwargs["method"] == "GET"

        self.mock_session.request.assert_called_once()
        assert response is not None
        is_list = isinstance(expected_response, list)
        is_flat_list = (
            is_list and not isinstance(expected_response[0], list) if is_list else False
        )
        is_oneof = is_one_of_model(GetCollateralAssetDataResponse)

        if is_list and not is_flat_list:
            expected = expected_response
        elif is_oneof or is_list:
            expected = GetCollateralAssetDataResponse.from_dict(expected_response)
        else:
            expected = GetCollateralAssetDataResponse.model_validate_json(
                json.dumps(expected_response)
            )

        assert response.data() == expected

    def test_get_collateral_asset_data_server_error(self):
        """Test that get_collateral_asset_data() raises an error when the server returns an error."""

        mock_error = Exception("ResponseError")
        self.client.get_collateral_asset_data = MagicMock(side_effect=mock_error)

        with pytest.raises(Exception, match="ResponseError"):
            self.client.get_collateral_asset_data()

    @patch("binance_common.utils.get_signature")
    def test_get_loanable_assets_data_success(self, mock_get_signature):
        """Test get_loanable_assets_data() successfully with required parameters only."""

        expected_response = {
            "rows": [
                {
                    "loanCoin": "BUSD",
                    "_flexibleDailyInterestRate": "0.001503",
                    "_flexibleYearlyInterestRate": "0.548595",
                    "_30dDailyInterestRate": "0.000136",
                    "_30dYearlyInterestRate": "0.03450",
                    "_60dDailyInterestRate": "0.000145",
                    "_60dYearlyInterestRate": "0.04103",
                    "minLimit": "100",
                    "maxLimit": "1000000",
                    "vipLevel": 1,
                }
            ],
            "total": 1,
        }
        mock_get_signature.return_value = "mocked_signature"
        self.set_mock_response(expected_response)

        response = self.client.get_loanable_assets_data()

        actual_call_args = self.mock_session.request.call_args
        request_kwargs = actual_call_args.kwargs

        self.mock_session.request.assert_called_once()
        mock_get_signature.assert_called_once()

        assert "url" in request_kwargs
        assert "signature" in parse_qs(request_kwargs["params"])
        assert "/sapi/v1/loan/vip/loanable/data" in request_kwargs["url"]
        assert request_kwargs["method"] == "GET"

        assert response is not None
        is_list = isinstance(expected_response, list)
        is_flat_list = (
            is_list and not isinstance(expected_response[0], list) if is_list else False
        )
        is_oneof = is_one_of_model(GetLoanableAssetsDataResponse)

        if is_list and not is_flat_list:
            expected = expected_response
        elif is_oneof or is_list:
            expected = GetLoanableAssetsDataResponse.from_dict(expected_response)
        else:
            expected = GetLoanableAssetsDataResponse.model_validate_json(
                json.dumps(expected_response)
            )

        assert response.data() == expected

    @patch("binance_common.utils.get_signature")
    def test_get_loanable_assets_data_success_with_optional_params(
        self, mock_get_signature
    ):
        """Test get_loanable_assets_data() successfully with optional parameters."""

        params = {"loan_coin": "loan_coin_example", "vip_level": 1, "recv_window": 5000}

        expected_response = {
            "rows": [
                {
                    "loanCoin": "BUSD",
                    "_flexibleDailyInterestRate": "0.001503",
                    "_flexibleYearlyInterestRate": "0.548595",
                    "_30dDailyInterestRate": "0.000136",
                    "_30dYearlyInterestRate": "0.03450",
                    "_60dDailyInterestRate": "0.000145",
                    "_60dYearlyInterestRate": "0.04103",
                    "minLimit": "100",
                    "maxLimit": "1000000",
                    "vipLevel": 1,
                }
            ],
            "total": 1,
        }
        mock_get_signature.return_value = "mocked_signature"
        self.set_mock_response(expected_response)

        response = self.client.get_loanable_assets_data(**params)

        actual_call_args = self.mock_session.request.call_args
        request_kwargs = actual_call_args.kwargs

        assert "url" in request_kwargs
        assert "signature" in parse_qs(request_kwargs["params"])
        assert "/sapi/v1/loan/vip/loanable/data" in request_kwargs["url"]
        assert request_kwargs["method"] == "GET"

        self.mock_session.request.assert_called_once()
        assert response is not None
        is_list = isinstance(expected_response, list)
        is_flat_list = (
            is_list and not isinstance(expected_response[0], list) if is_list else False
        )
        is_oneof = is_one_of_model(GetLoanableAssetsDataResponse)

        if is_list and not is_flat_list:
            expected = expected_response
        elif is_oneof or is_list:
            expected = GetLoanableAssetsDataResponse.from_dict(expected_response)
        else:
            expected = GetLoanableAssetsDataResponse.model_validate_json(
                json.dumps(expected_response)
            )

        assert response.data() == expected

    def test_get_loanable_assets_data_server_error(self):
        """Test that get_loanable_assets_data() raises an error when the server returns an error."""

        mock_error = Exception("ResponseError")
        self.client.get_loanable_assets_data = MagicMock(side_effect=mock_error)

        with pytest.raises(Exception, match="ResponseError"):
            self.client.get_loanable_assets_data()
