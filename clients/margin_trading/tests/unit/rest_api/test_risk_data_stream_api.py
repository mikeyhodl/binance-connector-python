"""
Binance Margin Trading REST API

OpenAPI Specification for the Binance Margin Trading REST API
The version of the OpenAPI document: 1.0.0
Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""

import json
import pytest
import requests

from unittest.mock import MagicMock
from urllib.parse import parse_qs

from binance_common.configuration import ConfigurationRestAPI
from binance_common.errors import RequiredError
from binance_common.utils import normalize_query_values, is_one_of_model, snake_to_camel

from binance_sdk_margin_trading.rest_api.api import RiskDataStreamApi


from binance_sdk_margin_trading.rest_api.models import StartUserDataStreamResponse


class TestRiskDataStreamApi:
    @pytest.fixture(autouse=True)
    def setup_client(self):
        """Setup a client instance with mocked session before each test method."""
        self.mock_session = MagicMock(spec=requests.Session)
        config = ConfigurationRestAPI(
            api_key="test-api-key",
            api_secret="test-api-secret",
        )
        self.client = RiskDataStreamApi(configuration=config, session=self.mock_session)

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

    def test_close_user_data_stream_success(self):
        """Test close_user_data_stream() successfully with required parameters only."""

        self.set_mock_response({})

        response = self.client.close_user_data_stream()

        actual_call_args = self.mock_session.request.call_args
        request_kwargs = actual_call_args.kwargs

        self.mock_session.request.assert_called_once()

        assert "url" in request_kwargs
        assert "/sapi/v1/margin/listen-key" in request_kwargs["url"]
        assert request_kwargs["method"] == "DELETE"

        assert response is not None

        assert response.data() == {}

    def test_close_user_data_stream_server_error(self):
        """Test that close_user_data_stream() raises an error when the server returns an error."""

        mock_error = Exception("ResponseError")
        self.client.close_user_data_stream = MagicMock(side_effect=mock_error)

        with pytest.raises(Exception, match="ResponseError"):
            self.client.close_user_data_stream()

    def test_keepalive_user_data_stream_success(self):
        """Test keepalive_user_data_stream() successfully with required parameters only."""

        params = {"listen_key": "listen_key_example"}

        self.set_mock_response({})

        response = self.client.keepalive_user_data_stream(**params)

        actual_call_args = self.mock_session.request.call_args
        request_kwargs = actual_call_args.kwargs
        parsed_params = parse_qs(request_kwargs["params"])
        camel_case_params = {snake_to_camel(k): v for k, v in params.items()}
        normalized = normalize_query_values(parsed_params, camel_case_params)

        self.mock_session.request.assert_called_once()

        assert "url" in request_kwargs
        assert "/sapi/v1/margin/listen-key" in request_kwargs["url"]
        assert request_kwargs["method"] == "PUT"
        assert normalized["listenKey"] == "listen_key_example"

        assert response is not None

        assert response.data() == {}

    def test_keepalive_user_data_stream_success_with_optional_params(self):
        """Test keepalive_user_data_stream() successfully with optional parameters."""

        params = {"listen_key": "listen_key_example"}

        self.set_mock_response({})

        response = self.client.keepalive_user_data_stream(**params)

        actual_call_args = self.mock_session.request.call_args
        request_kwargs = actual_call_args.kwargs

        assert "url" in request_kwargs
        assert "/sapi/v1/margin/listen-key" in request_kwargs["url"]
        assert request_kwargs["method"] == "PUT"

        self.mock_session.request.assert_called_once()
        assert response is not None

        assert response.data() == {}

    def test_keepalive_user_data_stream_missing_required_param_listen_key(self):
        """Test that keepalive_user_data_stream() raises RequiredError when 'listen_key' is missing."""
        params = {"listen_key": "listen_key_example"}
        del params["listen_key"]

        with pytest.raises(
            RequiredError, match="Missing required parameter 'listen_key'"
        ):
            self.client.keepalive_user_data_stream(**params)

    def test_keepalive_user_data_stream_server_error(self):
        """Test that keepalive_user_data_stream() raises an error when the server returns an error."""

        params = {"listen_key": "listen_key_example"}

        mock_error = Exception("ResponseError")
        self.client.keepalive_user_data_stream = MagicMock(side_effect=mock_error)

        with pytest.raises(Exception, match="ResponseError"):
            self.client.keepalive_user_data_stream(**params)

    def test_start_user_data_stream_success(self):
        """Test start_user_data_stream() successfully with required parameters only."""

        expected_response = {
            "listenKey": "T3ee22BIYuWqmvne0HNq2A2WsFlEtLhvWCtItw6ffhhd"
        }

        self.set_mock_response(expected_response)

        response = self.client.start_user_data_stream()

        actual_call_args = self.mock_session.request.call_args
        request_kwargs = actual_call_args.kwargs

        self.mock_session.request.assert_called_once()

        assert "url" in request_kwargs
        assert "/sapi/v1/margin/listen-key" in request_kwargs["url"]
        assert request_kwargs["method"] == "POST"

        assert response is not None
        is_list = isinstance(expected_response, list)
        is_flat_list = (
            is_list and not isinstance(expected_response[0], list) if is_list else False
        )
        is_oneof = is_one_of_model(StartUserDataStreamResponse)

        if is_list and not is_flat_list:
            expected = expected_response
        elif is_oneof or is_list:
            expected = StartUserDataStreamResponse.from_dict(expected_response)
        else:
            expected = StartUserDataStreamResponse.model_validate_json(
                json.dumps(expected_response)
            )

        assert response.data() == expected

    def test_start_user_data_stream_server_error(self):
        """Test that start_user_data_stream() raises an error when the server returns an error."""

        mock_error = Exception("ResponseError")
        self.client.start_user_data_stream = MagicMock(side_effect=mock_error)

        with pytest.raises(Exception, match="ResponseError"):
            self.client.start_user_data_stream()
