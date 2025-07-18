"""
Binance Derivatives Trading Options REST API

OpenAPI Specification for the Binance Derivatives Trading Options REST API
The version of the OpenAPI document: 1.0.0
Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""

from typing import Optional
from requests import Session
from binance_common.configuration import ConfigurationRestAPI
from binance_common.errors import RequiredError
from binance_common.models import ApiResponse
from binance_common.signature import Signers
from binance_common.utils import send_request

from ..models import AccountFundingFlowResponse
from ..models import GetDownloadIdForOptionTransactionHistoryResponse
from ..models import GetOptionTransactionHistoryDownloadLinkByIdResponse
from ..models import OptionAccountInformationResponse


class AccountApi:
    """API Client for AccountApi endpoints."""

    def __init__(
        self,
        configuration: ConfigurationRestAPI = None,
        session: Session = None,
        signer: Signers = None,
    ) -> None:
        self._configuration = configuration
        self._session = session
        self._signer = signer

    def account_funding_flow(
        self,
        currency: str = None,
        record_id: Optional[int] = None,
        start_time: Optional[int] = None,
        end_time: Optional[int] = None,
        limit: Optional[int] = None,
        recv_window: Optional[int] = None,
    ) -> ApiResponse[AccountFundingFlowResponse]:
        """
                Account Funding Flow (USER_DATA)
                GET /eapi/v1/bill
                https://developers.binance.com/docs/derivatives/option/account/Account-Funding-Flow

                Query account funding flows.

        Weight: 1

                Args:
                    currency (str): Asset type, only support USDT  as of now
                    record_id (Optional[int]): Return the recordId and subsequent data, the latest data is returned by default, e.g 100000
                    start_time (Optional[int]): Start Time, e.g 1593511200000
                    end_time (Optional[int]): End Time, e.g 1593512200000
                    limit (Optional[int]): Number of result sets returned Default:100 Max:1000
                    recv_window (Optional[int]):

                Returns:
                    ApiResponse[AccountFundingFlowResponse]

                Raises:
                    RequiredError: If a required parameter is missing.

        """

        if currency is None:
            raise RequiredError(
                field="currency", error_message="Missing required parameter 'currency'"
            )

        payload = {
            "currency": currency,
            "record_id": record_id,
            "start_time": start_time,
            "end_time": end_time,
            "limit": limit,
            "recv_window": recv_window,
        }

        return send_request(
            self._session,
            self._configuration,
            method="GET",
            path="/eapi/v1/bill",
            payload=payload,
            time_unit=self._configuration.time_unit,
            response_model=AccountFundingFlowResponse,
            is_signed=True,
            signer=self._signer,
        )

    def get_download_id_for_option_transaction_history(
        self,
        start_time: int = None,
        end_time: int = None,
        recv_window: Optional[int] = None,
    ) -> ApiResponse[GetDownloadIdForOptionTransactionHistoryResponse]:
        """
                Get Download Id For Option Transaction History (USER_DATA)
                GET /eapi/v1/income/asyn
                https://developers.binance.com/docs/derivatives/option/account/Get-Download-Id-For-Option-Transaction-History

                Get download id for option transaction history

        * Request Limitation is 5 times per month, shared by > front end download page and rest api
        * The time between `startTime` and `endTime` can not be longer than 1 year

        Weight: 5

                Args:
                    start_time (int): Timestamp in ms
                    end_time (int): Timestamp in ms
                    recv_window (Optional[int]):

                Returns:
                    ApiResponse[GetDownloadIdForOptionTransactionHistoryResponse]

                Raises:
                    RequiredError: If a required parameter is missing.

        """

        if start_time is None:
            raise RequiredError(
                field="start_time",
                error_message="Missing required parameter 'start_time'",
            )
        if end_time is None:
            raise RequiredError(
                field="end_time", error_message="Missing required parameter 'end_time'"
            )

        payload = {
            "start_time": start_time,
            "end_time": end_time,
            "recv_window": recv_window,
        }

        return send_request(
            self._session,
            self._configuration,
            method="GET",
            path="/eapi/v1/income/asyn",
            payload=payload,
            time_unit=self._configuration.time_unit,
            response_model=GetDownloadIdForOptionTransactionHistoryResponse,
            is_signed=True,
            signer=self._signer,
        )

    def get_option_transaction_history_download_link_by_id(
        self,
        download_id: str = None,
        recv_window: Optional[int] = None,
    ) -> ApiResponse[GetOptionTransactionHistoryDownloadLinkByIdResponse]:
        """
                Get Option Transaction History Download Link by Id (USER_DATA)
                GET /eapi/v1/income/asyn/id
                https://developers.binance.com/docs/derivatives/option/account/Get-Option-Transaction-History-Download-Link-by-Id

                Get option transaction history download Link by Id

        * Download link expiration: 24h

        Weight: 5

                Args:
                    download_id (str): get by download id api
                    recv_window (Optional[int]):

                Returns:
                    ApiResponse[GetOptionTransactionHistoryDownloadLinkByIdResponse]

                Raises:
                    RequiredError: If a required parameter is missing.

        """

        if download_id is None:
            raise RequiredError(
                field="download_id",
                error_message="Missing required parameter 'download_id'",
            )

        payload = {"download_id": download_id, "recv_window": recv_window}

        return send_request(
            self._session,
            self._configuration,
            method="GET",
            path="/eapi/v1/income/asyn/id",
            payload=payload,
            time_unit=self._configuration.time_unit,
            response_model=GetOptionTransactionHistoryDownloadLinkByIdResponse,
            is_signed=True,
            signer=self._signer,
        )

    def option_account_information(
        self,
        recv_window: Optional[int] = None,
    ) -> ApiResponse[OptionAccountInformationResponse]:
        """
                Option Account Information(TRADE)
                GET /eapi/v1/account
                https://developers.binance.com/docs/derivatives/option/account/Option-Account-Information

                Get current account information.

        Weight: 3

                Args:
                    recv_window (Optional[int]):

                Returns:
                    ApiResponse[OptionAccountInformationResponse]

                Raises:
                    RequiredError: If a required parameter is missing.

        """

        payload = {"recv_window": recv_window}

        return send_request(
            self._session,
            self._configuration,
            method="GET",
            path="/eapi/v1/account",
            payload=payload,
            time_unit=self._configuration.time_unit,
            response_model=OptionAccountInformationResponse,
            is_signed=True,
            signer=self._signer,
        )
