"""
Binance Wallet REST API

OpenAPI Specification for the Binance Wallet REST API
The version of the OpenAPI document: 1.0.0
Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""

from typing import Optional
from requests import Session
from binance_common.configuration import ConfigurationRestAPI
from binance_common.models import ApiResponse
from binance_common.signature import Signers
from binance_common.utils import send_request

from ..models import GetSymbolsDelistScheduleForSpotResponse
from ..models import SystemStatusResponse


class OthersApi:
    """API Client for OthersApi endpoints."""

    def __init__(
        self,
        configuration: ConfigurationRestAPI = None,
        session: Session = None,
        signer: Signers = None,
    ) -> None:
        self._configuration = configuration
        self._session = session
        self._signer = signer

    def get_symbols_delist_schedule_for_spot(
        self,
        recv_window: Optional[int] = None,
    ) -> ApiResponse[GetSymbolsDelistScheduleForSpotResponse]:
        """
                Get symbols delist schedule for spot (MARKET_DATA)
                GET /sapi/v1/spot/delist-schedule
                https://developers.binance.com/docs/wallet/others/delist-schedule

                Get symbols delist schedule for spot

        Weight: 100

                Args:
                    recv_window (Optional[int]):

                Returns:
                    ApiResponse[GetSymbolsDelistScheduleForSpotResponse]

                Raises:
                    RequiredError: If a required parameter is missing.

        """

        payload = {"recv_window": recv_window}

        return send_request(
            self._session,
            self._configuration,
            method="GET",
            path="/sapi/v1/spot/delist-schedule",
            payload=payload,
            time_unit=self._configuration.time_unit,
            response_model=GetSymbolsDelistScheduleForSpotResponse,
        )

    def system_status(
        self,
    ) -> ApiResponse[SystemStatusResponse]:
        """
                System Status (System)
                GET /sapi/v1/system/status
                https://developers.binance.com/docs/wallet/others/System-Status

                Fetch system status.

        Weight: 1

                Args:

                Returns:
                    ApiResponse[SystemStatusResponse]

                Raises:
                    RequiredError: If a required parameter is missing.

        """

        payload = None

        return send_request(
            self._session,
            self._configuration,
            method="GET",
            path="/sapi/v1/system/status",
            payload=payload,
            time_unit=self._configuration.time_unit,
            response_model=SystemStatusResponse,
        )
