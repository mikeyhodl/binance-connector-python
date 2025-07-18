"""
Binance Derivatives Trading Portfolio Margin REST API

OpenAPI Specification for the Binance Derivatives Trading Portfolio Margin REST API
The version of the OpenAPI document: 1.0.0
Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""

import json
import pytest
import requests

from unittest.mock import MagicMock

from binance_common.configuration import ConfigurationRestAPI

from binance_sdk_derivatives_trading_portfolio_margin.rest_api.api import MarketDataApi


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

    def test_test_connectivity_success(self):
        """Test test_connectivity() successfully with required parameters only."""

        self.set_mock_response({})

        response = self.client.test_connectivity()

        actual_call_args = self.mock_session.request.call_args
        request_kwargs = actual_call_args.kwargs

        self.mock_session.request.assert_called_once()

        assert "url" in request_kwargs
        assert "/papi/v1/ping" in request_kwargs["url"]
        assert request_kwargs["method"] == "GET"

        assert response is not None

        assert response.data() == {}

    def test_test_connectivity_server_error(self):
        """Test that test_connectivity() raises an error when the server returns an error."""

        mock_error = Exception("ResponseError")
        self.client.test_connectivity = MagicMock(side_effect=mock_error)

        with pytest.raises(Exception, match="ResponseError"):
            self.client.test_connectivity()
