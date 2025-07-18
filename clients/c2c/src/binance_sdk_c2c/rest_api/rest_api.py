"""
Binance C2C REST API

OpenAPI Specification for the Binance C2C REST API
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
from .api.c2_c_api import C2CApi

from .models import GetC2CTradeHistoryResponse


T = TypeVar("T")


class C2CRestAPI:
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

        self._c2CApi = C2CApi(self.configuration, self._session, self._signer)

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

    def get_c2_c_trade_history(
        self,
        start_time: Optional[int] = None,
        end_time: Optional[int] = None,
        page: Optional[int] = None,
        recv_window: Optional[int] = None,
    ) -> ApiResponse[GetC2CTradeHistoryResponse]:
        """
                Get C2C Trade History (USER_DATA)

                Get C2C Trade History

        * The max interval between startTime and endTime is 30 days.
        * If startTime and endTime are not sent, the recent 7 days' data will be returned.
        * The earliest startTime is supported on June 10, 2020
        * Return up to 200 records per request.

        Weight: 1

                Args:
                    start_time (Optional[int]):
                    end_time (Optional[int]):
                    page (Optional[int]): Default 1
                    recv_window (Optional[int]):

                Returns:
                    ApiResponse[GetC2CTradeHistoryResponse]

                Raises:
                    RequiredError: If a required parameter is missing.

        """

        return self._c2CApi.get_c2_c_trade_history(
            start_time, end_time, page, recv_window
        )
