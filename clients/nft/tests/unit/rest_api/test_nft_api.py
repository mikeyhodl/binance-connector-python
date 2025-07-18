"""
Binance NFT REST API

OpenAPI Specification for the Binance NFT REST API
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

from binance_sdk_nft.rest_api.api import NFTApi
from binance_sdk_nft.rest_api.models import GetNFTAssetResponse
from binance_sdk_nft.rest_api.models import GetNFTDepositHistoryResponse
from binance_sdk_nft.rest_api.models import GetNFTTransactionHistoryResponse
from binance_sdk_nft.rest_api.models import GetNFTWithdrawHistoryResponse


class TestNFTApi:
    @pytest.fixture(autouse=True)
    def setup_client(self):
        """Setup a client instance with mocked session before each test method."""
        self.mock_session = MagicMock(spec=requests.Session)
        config = ConfigurationRestAPI(
            api_key="test-api-key",
            api_secret="test-api-secret",
        )
        self.client = NFTApi(configuration=config, session=self.mock_session)

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
    def test_get_nft_asset_success(self, mock_get_signature):
        """Test get_nft_asset() successfully with required parameters only."""

        expected_response = {
            "total": 347,
            "list": [
                {
                    "network": "BSC",
                    "contractAddress": "REGULAR11234567891779",
                    "tokenId": "100900000017",
                },
                {
                    "network": "BSC",
                    "contractAddress": "SSMDQ8W59",
                    "tokenId": "200500000011",
                },
                {
                    "network": "BSC",
                    "contractAddress": "SSMDQ8W59",
                    "tokenId": "200500000019",
                },
            ],
        }
        mock_get_signature.return_value = "mocked_signature"
        self.set_mock_response(expected_response)

        response = self.client.get_nft_asset()

        actual_call_args = self.mock_session.request.call_args
        request_kwargs = actual_call_args.kwargs

        self.mock_session.request.assert_called_once()
        mock_get_signature.assert_called_once()

        assert "url" in request_kwargs
        assert "signature" in parse_qs(request_kwargs["params"])
        assert "/sapi/v1/nft/user/getAsset" in request_kwargs["url"]
        assert request_kwargs["method"] == "GET"

        assert response is not None
        is_list = isinstance(expected_response, list)
        is_flat_list = (
            is_list and not isinstance(expected_response[0], list) if is_list else False
        )
        is_oneof = is_one_of_model(GetNFTAssetResponse)

        if is_list and not is_flat_list:
            expected = expected_response
        elif is_oneof or is_list:
            expected = GetNFTAssetResponse.from_dict(expected_response)
        else:
            expected = GetNFTAssetResponse.model_validate_json(
                json.dumps(expected_response)
            )

        assert response.data() == expected

    @patch("binance_common.utils.get_signature")
    def test_get_nft_asset_success_with_optional_params(self, mock_get_signature):
        """Test get_nft_asset() successfully with optional parameters."""

        params = {"limit": 50, "page": 1, "recv_window": 5000}

        expected_response = {
            "total": 347,
            "list": [
                {
                    "network": "BSC",
                    "contractAddress": "REGULAR11234567891779",
                    "tokenId": "100900000017",
                },
                {
                    "network": "BSC",
                    "contractAddress": "SSMDQ8W59",
                    "tokenId": "200500000011",
                },
                {
                    "network": "BSC",
                    "contractAddress": "SSMDQ8W59",
                    "tokenId": "200500000019",
                },
            ],
        }
        mock_get_signature.return_value = "mocked_signature"
        self.set_mock_response(expected_response)

        response = self.client.get_nft_asset(**params)

        actual_call_args = self.mock_session.request.call_args
        request_kwargs = actual_call_args.kwargs

        assert "url" in request_kwargs
        assert "signature" in parse_qs(request_kwargs["params"])
        assert "/sapi/v1/nft/user/getAsset" in request_kwargs["url"]
        assert request_kwargs["method"] == "GET"

        self.mock_session.request.assert_called_once()
        assert response is not None
        is_list = isinstance(expected_response, list)
        is_flat_list = (
            is_list and not isinstance(expected_response[0], list) if is_list else False
        )
        is_oneof = is_one_of_model(GetNFTAssetResponse)

        if is_list and not is_flat_list:
            expected = expected_response
        elif is_oneof or is_list:
            expected = GetNFTAssetResponse.from_dict(expected_response)
        else:
            expected = GetNFTAssetResponse.model_validate_json(
                json.dumps(expected_response)
            )

        assert response.data() == expected

    def test_get_nft_asset_server_error(self):
        """Test that get_nft_asset() raises an error when the server returns an error."""

        mock_error = Exception("ResponseError")
        self.client.get_nft_asset = MagicMock(side_effect=mock_error)

        with pytest.raises(Exception, match="ResponseError"):
            self.client.get_nft_asset()

    @patch("binance_common.utils.get_signature")
    def test_get_nft_deposit_history_success(self, mock_get_signature):
        """Test get_nft_deposit_history() successfully with required parameters only."""

        expected_response = {
            "total": 2,
            "list": [
                {
                    "network": "ETH",
                    "txID": None,
                    "contractAdrress": "0xe507c961ee127d4439977a61af39c34eafee0dc6",
                    "tokenId": "10014",
                    "timestamp": 1629986047000,
                },
                {
                    "network": "BSC",
                    "txID": None,
                    "contractAdrress": "0x058451b463bab04f52c0799d55c4094f507acfa9",
                    "tokenId": "10016",
                    "timestamp": 1630083581000,
                },
            ],
        }
        mock_get_signature.return_value = "mocked_signature"
        self.set_mock_response(expected_response)

        response = self.client.get_nft_deposit_history()

        actual_call_args = self.mock_session.request.call_args
        request_kwargs = actual_call_args.kwargs

        self.mock_session.request.assert_called_once()
        mock_get_signature.assert_called_once()

        assert "url" in request_kwargs
        assert "signature" in parse_qs(request_kwargs["params"])
        assert "/sapi/v1/nft/history/deposit" in request_kwargs["url"]
        assert request_kwargs["method"] == "GET"

        assert response is not None
        is_list = isinstance(expected_response, list)
        is_flat_list = (
            is_list and not isinstance(expected_response[0], list) if is_list else False
        )
        is_oneof = is_one_of_model(GetNFTDepositHistoryResponse)

        if is_list and not is_flat_list:
            expected = expected_response
        elif is_oneof or is_list:
            expected = GetNFTDepositHistoryResponse.from_dict(expected_response)
        else:
            expected = GetNFTDepositHistoryResponse.model_validate_json(
                json.dumps(expected_response)
            )

        assert response.data() == expected

    @patch("binance_common.utils.get_signature")
    def test_get_nft_deposit_history_success_with_optional_params(
        self, mock_get_signature
    ):
        """Test get_nft_deposit_history() successfully with optional parameters."""

        params = {
            "start_time": 1623319461670,
            "end_time": 1641782889000,
            "limit": 50,
            "page": 1,
            "recv_window": 5000,
        }

        expected_response = {
            "total": 2,
            "list": [
                {
                    "network": "ETH",
                    "txID": None,
                    "contractAdrress": "0xe507c961ee127d4439977a61af39c34eafee0dc6",
                    "tokenId": "10014",
                    "timestamp": 1629986047000,
                },
                {
                    "network": "BSC",
                    "txID": None,
                    "contractAdrress": "0x058451b463bab04f52c0799d55c4094f507acfa9",
                    "tokenId": "10016",
                    "timestamp": 1630083581000,
                },
            ],
        }
        mock_get_signature.return_value = "mocked_signature"
        self.set_mock_response(expected_response)

        response = self.client.get_nft_deposit_history(**params)

        actual_call_args = self.mock_session.request.call_args
        request_kwargs = actual_call_args.kwargs

        assert "url" in request_kwargs
        assert "signature" in parse_qs(request_kwargs["params"])
        assert "/sapi/v1/nft/history/deposit" in request_kwargs["url"]
        assert request_kwargs["method"] == "GET"

        self.mock_session.request.assert_called_once()
        assert response is not None
        is_list = isinstance(expected_response, list)
        is_flat_list = (
            is_list and not isinstance(expected_response[0], list) if is_list else False
        )
        is_oneof = is_one_of_model(GetNFTDepositHistoryResponse)

        if is_list and not is_flat_list:
            expected = expected_response
        elif is_oneof or is_list:
            expected = GetNFTDepositHistoryResponse.from_dict(expected_response)
        else:
            expected = GetNFTDepositHistoryResponse.model_validate_json(
                json.dumps(expected_response)
            )

        assert response.data() == expected

    def test_get_nft_deposit_history_server_error(self):
        """Test that get_nft_deposit_history() raises an error when the server returns an error."""

        mock_error = Exception("ResponseError")
        self.client.get_nft_deposit_history = MagicMock(side_effect=mock_error)

        with pytest.raises(Exception, match="ResponseError"):
            self.client.get_nft_deposit_history()

    @patch("binance_common.utils.get_signature")
    def test_get_nft_transaction_history_success(self, mock_get_signature):
        """Test get_nft_transaction_history() successfully with required parameters only."""

        params = {
            "order_type": 56,
        }

        expected_response = {
            "total": 2,
            "list": [
                {
                    "orderNo": "1_470502070600699904",
                    "tokens": [
                        {
                            "network": "BSC",
                            "tokenId": "216000000496",
                            "contractAddress": "MYSTERY_BOX0000087",
                        }
                    ],
                    "tradeTime": 1626941236000,
                    "tradeAmount": "19.60000000",
                    "tradeCurrency": "BNB",
                },
                {
                    "orderNo": "1_488306442479116288",
                    "tokens": [
                        {
                            "network": "BSC",
                            "tokenId": "132900000007",
                            "contractAddress": "0xAf12111a592e408DAbC740849fcd5e68629D9fb6",
                        }
                    ],
                    "tradeTime": 1631186130000,
                    "tradeAmount": "192.00000000",
                    "tradeCurrency": "BNB",
                },
            ],
        }
        mock_get_signature.return_value = "mocked_signature"
        self.set_mock_response(expected_response)

        response = self.client.get_nft_transaction_history(**params)

        actual_call_args = self.mock_session.request.call_args
        request_kwargs = actual_call_args.kwargs
        parsed_params = parse_qs(request_kwargs["params"])
        camel_case_params = {snake_to_camel(k): v for k, v in params.items()}
        normalized = normalize_query_values(parsed_params, camel_case_params)

        self.mock_session.request.assert_called_once()
        mock_get_signature.assert_called_once()

        assert "url" in request_kwargs
        assert "signature" in parse_qs(request_kwargs["params"])
        assert "/sapi/v1/nft/history/transactions" in request_kwargs["url"]
        assert request_kwargs["method"] == "GET"
        assert normalized["orderType"] == 56

        assert response is not None
        is_list = isinstance(expected_response, list)
        is_flat_list = (
            is_list and not isinstance(expected_response[0], list) if is_list else False
        )
        is_oneof = is_one_of_model(GetNFTTransactionHistoryResponse)

        if is_list and not is_flat_list:
            expected = expected_response
        elif is_oneof or is_list:
            expected = GetNFTTransactionHistoryResponse.from_dict(expected_response)
        else:
            expected = GetNFTTransactionHistoryResponse.model_validate_json(
                json.dumps(expected_response)
            )

        assert response.data() == expected

    @patch("binance_common.utils.get_signature")
    def test_get_nft_transaction_history_success_with_optional_params(
        self, mock_get_signature
    ):
        """Test get_nft_transaction_history() successfully with optional parameters."""

        params = {
            "order_type": 56,
            "start_time": 1623319461670,
            "end_time": 1641782889000,
            "limit": 50,
            "page": 1,
            "recv_window": 5000,
        }

        expected_response = {
            "total": 2,
            "list": [
                {
                    "orderNo": "1_470502070600699904",
                    "tokens": [
                        {
                            "network": "BSC",
                            "tokenId": "216000000496",
                            "contractAddress": "MYSTERY_BOX0000087",
                        }
                    ],
                    "tradeTime": 1626941236000,
                    "tradeAmount": "19.60000000",
                    "tradeCurrency": "BNB",
                },
                {
                    "orderNo": "1_488306442479116288",
                    "tokens": [
                        {
                            "network": "BSC",
                            "tokenId": "132900000007",
                            "contractAddress": "0xAf12111a592e408DAbC740849fcd5e68629D9fb6",
                        }
                    ],
                    "tradeTime": 1631186130000,
                    "tradeAmount": "192.00000000",
                    "tradeCurrency": "BNB",
                },
            ],
        }
        mock_get_signature.return_value = "mocked_signature"
        self.set_mock_response(expected_response)

        response = self.client.get_nft_transaction_history(**params)

        actual_call_args = self.mock_session.request.call_args
        request_kwargs = actual_call_args.kwargs

        assert "url" in request_kwargs
        assert "signature" in parse_qs(request_kwargs["params"])
        assert "/sapi/v1/nft/history/transactions" in request_kwargs["url"]
        assert request_kwargs["method"] == "GET"

        self.mock_session.request.assert_called_once()
        assert response is not None
        is_list = isinstance(expected_response, list)
        is_flat_list = (
            is_list and not isinstance(expected_response[0], list) if is_list else False
        )
        is_oneof = is_one_of_model(GetNFTTransactionHistoryResponse)

        if is_list and not is_flat_list:
            expected = expected_response
        elif is_oneof or is_list:
            expected = GetNFTTransactionHistoryResponse.from_dict(expected_response)
        else:
            expected = GetNFTTransactionHistoryResponse.model_validate_json(
                json.dumps(expected_response)
            )

        assert response.data() == expected

    def test_get_nft_transaction_history_missing_required_param_order_type(self):
        """Test that get_nft_transaction_history() raises RequiredError when 'order_type' is missing."""
        params = {
            "order_type": 56,
        }
        del params["order_type"]

        with pytest.raises(
            RequiredError, match="Missing required parameter 'order_type'"
        ):
            self.client.get_nft_transaction_history(**params)

    def test_get_nft_transaction_history_server_error(self):
        """Test that get_nft_transaction_history() raises an error when the server returns an error."""

        params = {
            "order_type": 56,
        }

        mock_error = Exception("ResponseError")
        self.client.get_nft_transaction_history = MagicMock(side_effect=mock_error)

        with pytest.raises(Exception, match="ResponseError"):
            self.client.get_nft_transaction_history(**params)

    @patch("binance_common.utils.get_signature")
    def test_get_nft_withdraw_history_success(self, mock_get_signature):
        """Test get_nft_withdraw_history() successfully with required parameters only."""

        expected_response = {
            "total": 178,
            "list": [
                {
                    "network": "ETH",
                    "txID": "0x2be5eed31d787fdb4880bc631c8e76bdfb6150e137f5cf1732e0416ea206f57f",
                    "contractAdrress": "0xe507c961ee127d4439977a61af39c34eafee0dc6",
                    "tokenId": "1000001247",
                    "timestamp": 1633674433000,
                    "fee": 0.1,
                    "feeAsset": "ETH",
                },
                {
                    "network": "ETH",
                    "txID": "0x3b3aea5c0a4faccd6f306641e6deb9713ab229ac233be3be227f580311e4362a",
                    "contractAdrress": "0xe507c961ee127d4439977a61af39c34eafee0dc6",
                    "tokenId": "40000030",
                    "timestamp": 1633677022000,
                    "fee": 0.1,
                    "feeAsset": "ETH",
                },
            ],
        }
        mock_get_signature.return_value = "mocked_signature"
        self.set_mock_response(expected_response)

        response = self.client.get_nft_withdraw_history()

        actual_call_args = self.mock_session.request.call_args
        request_kwargs = actual_call_args.kwargs

        self.mock_session.request.assert_called_once()
        mock_get_signature.assert_called_once()

        assert "url" in request_kwargs
        assert "signature" in parse_qs(request_kwargs["params"])
        assert "/sapi/v1/nft/history/withdraw" in request_kwargs["url"]
        assert request_kwargs["method"] == "GET"

        assert response is not None
        is_list = isinstance(expected_response, list)
        is_flat_list = (
            is_list and not isinstance(expected_response[0], list) if is_list else False
        )
        is_oneof = is_one_of_model(GetNFTWithdrawHistoryResponse)

        if is_list and not is_flat_list:
            expected = expected_response
        elif is_oneof or is_list:
            expected = GetNFTWithdrawHistoryResponse.from_dict(expected_response)
        else:
            expected = GetNFTWithdrawHistoryResponse.model_validate_json(
                json.dumps(expected_response)
            )

        assert response.data() == expected

    @patch("binance_common.utils.get_signature")
    def test_get_nft_withdraw_history_success_with_optional_params(
        self, mock_get_signature
    ):
        """Test get_nft_withdraw_history() successfully with optional parameters."""

        params = {
            "start_time": 1623319461670,
            "end_time": 1641782889000,
            "limit": 50,
            "page": 1,
            "recv_window": 5000,
        }

        expected_response = {
            "total": 178,
            "list": [
                {
                    "network": "ETH",
                    "txID": "0x2be5eed31d787fdb4880bc631c8e76bdfb6150e137f5cf1732e0416ea206f57f",
                    "contractAdrress": "0xe507c961ee127d4439977a61af39c34eafee0dc6",
                    "tokenId": "1000001247",
                    "timestamp": 1633674433000,
                    "fee": 0.1,
                    "feeAsset": "ETH",
                },
                {
                    "network": "ETH",
                    "txID": "0x3b3aea5c0a4faccd6f306641e6deb9713ab229ac233be3be227f580311e4362a",
                    "contractAdrress": "0xe507c961ee127d4439977a61af39c34eafee0dc6",
                    "tokenId": "40000030",
                    "timestamp": 1633677022000,
                    "fee": 0.1,
                    "feeAsset": "ETH",
                },
            ],
        }
        mock_get_signature.return_value = "mocked_signature"
        self.set_mock_response(expected_response)

        response = self.client.get_nft_withdraw_history(**params)

        actual_call_args = self.mock_session.request.call_args
        request_kwargs = actual_call_args.kwargs

        assert "url" in request_kwargs
        assert "signature" in parse_qs(request_kwargs["params"])
        assert "/sapi/v1/nft/history/withdraw" in request_kwargs["url"]
        assert request_kwargs["method"] == "GET"

        self.mock_session.request.assert_called_once()
        assert response is not None
        is_list = isinstance(expected_response, list)
        is_flat_list = (
            is_list and not isinstance(expected_response[0], list) if is_list else False
        )
        is_oneof = is_one_of_model(GetNFTWithdrawHistoryResponse)

        if is_list and not is_flat_list:
            expected = expected_response
        elif is_oneof or is_list:
            expected = GetNFTWithdrawHistoryResponse.from_dict(expected_response)
        else:
            expected = GetNFTWithdrawHistoryResponse.model_validate_json(
                json.dumps(expected_response)
            )

        assert response.data() == expected

    def test_get_nft_withdraw_history_server_error(self):
        """Test that get_nft_withdraw_history() raises an error when the server returns an error."""

        mock_error = Exception("ResponseError")
        self.client.get_nft_withdraw_history = MagicMock(side_effect=mock_error)

        with pytest.raises(Exception, match="ResponseError"):
            self.client.get_nft_withdraw_history()
