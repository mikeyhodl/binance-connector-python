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
from binance_common.errors import RequiredError
from binance_common.models import ApiResponse
from binance_common.signature import Signers
from binance_common.utils import send_request

from ..models import AccountApiTradingStatusResponse
from ..models import AccountInfoResponse
from ..models import AccountStatusResponse
from ..models import DailyAccountSnapshotResponse


from ..models import GetApiKeyPermissionResponse


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

    def account_api_trading_status(
        self,
        recv_window: Optional[int] = None,
    ) -> ApiResponse[AccountApiTradingStatusResponse]:
        """
                Account API Trading Status (USER_DATA)
                GET /sapi/v1/account/apiTradingStatus
                https://developers.binance.com/docs/wallet/account/Account-API-Trading-Status

                Fetch account api trading status detail.

        Weight: 1

                Args:
                    recv_window (Optional[int]):

                Returns:
                    ApiResponse[AccountApiTradingStatusResponse]

                Raises:
                    RequiredError: If a required parameter is missing.

        """

        payload = {"recv_window": recv_window}

        return send_request(
            self._session,
            self._configuration,
            method="GET",
            path="/sapi/v1/account/apiTradingStatus",
            payload=payload,
            time_unit=self._configuration.time_unit,
            response_model=AccountApiTradingStatusResponse,
            is_signed=True,
            signer=self._signer,
        )

    def account_info(
        self,
        recv_window: Optional[int] = None,
    ) -> ApiResponse[AccountInfoResponse]:
        """
                Account info (USER_DATA)
                GET /sapi/v1/account/info
                https://developers.binance.com/docs/wallet/account/Account-info

                Fetch account info detail.

        Weight: 1

                Args:
                    recv_window (Optional[int]):

                Returns:
                    ApiResponse[AccountInfoResponse]

                Raises:
                    RequiredError: If a required parameter is missing.

        """

        payload = {"recv_window": recv_window}

        return send_request(
            self._session,
            self._configuration,
            method="GET",
            path="/sapi/v1/account/info",
            payload=payload,
            time_unit=self._configuration.time_unit,
            response_model=AccountInfoResponse,
            is_signed=True,
            signer=self._signer,
        )

    def account_status(
        self,
        recv_window: Optional[int] = None,
    ) -> ApiResponse[AccountStatusResponse]:
        """
                Account Status (USER_DATA)
                GET /sapi/v1/account/status
                https://developers.binance.com/docs/wallet/account/Account-Status

                Fetch account status detail.

        Weight: 1

                Args:
                    recv_window (Optional[int]):

                Returns:
                    ApiResponse[AccountStatusResponse]

                Raises:
                    RequiredError: If a required parameter is missing.

        """

        payload = {"recv_window": recv_window}

        return send_request(
            self._session,
            self._configuration,
            method="GET",
            path="/sapi/v1/account/status",
            payload=payload,
            time_unit=self._configuration.time_unit,
            response_model=AccountStatusResponse,
            is_signed=True,
            signer=self._signer,
        )

    def daily_account_snapshot(
        self,
        type: str = None,
        start_time: Optional[int] = None,
        end_time: Optional[int] = None,
        limit: Optional[int] = None,
        recv_window: Optional[int] = None,
    ) -> ApiResponse[DailyAccountSnapshotResponse]:
        """
                Daily Account Snapshot (USER_DATA)
                GET /sapi/v1/accountSnapshot
                https://developers.binance.com/docs/wallet/account/daily-account-snapshoot

                Daily account snapshot

        * The query time period must be less then 30 days
        * Support query within the last one month only
        * If startTimeand endTime not sent, return records of the last 7 days by default

        Weight: 2400

                Args:
                    type (str):
                    start_time (Optional[int]):
                    end_time (Optional[int]):
                    limit (Optional[int]): min 7, max 30, default 7
                    recv_window (Optional[int]):

                Returns:
                    ApiResponse[DailyAccountSnapshotResponse]

                Raises:
                    RequiredError: If a required parameter is missing.

        """

        if type is None:
            raise RequiredError(
                field="type", error_message="Missing required parameter 'type'"
            )

        payload = {
            "type": type,
            "start_time": start_time,
            "end_time": end_time,
            "limit": limit,
            "recv_window": recv_window,
        }

        return send_request(
            self._session,
            self._configuration,
            method="GET",
            path="/sapi/v1/accountSnapshot",
            payload=payload,
            time_unit=self._configuration.time_unit,
            response_model=DailyAccountSnapshotResponse,
            is_signed=True,
            signer=self._signer,
        )

    def disable_fast_withdraw_switch(
        self,
        recv_window: Optional[int] = None,
    ) -> ApiResponse[None]:
        """
                Disable Fast Withdraw Switch (USER_DATA)
                POST /sapi/v1/account/disableFastWithdrawSwitch
                https://developers.binance.com/docs/wallet/account/Disable-Fast-Withdraw-Switch


        Weight: 1

                Args:
                    recv_window (Optional[int]):

                Returns:
                    ApiResponse[None]

                Raises:
                    RequiredError: If a required parameter is missing.

        """

        payload = {"recv_window": recv_window}

        return send_request(
            self._session,
            self._configuration,
            method="POST",
            path="/sapi/v1/account/disableFastWithdrawSwitch",
            payload=payload,
            time_unit=self._configuration.time_unit,
            is_signed=True,
            signer=self._signer,
        )

    def enable_fast_withdraw_switch(
        self,
        recv_window: Optional[int] = None,
    ) -> ApiResponse[None]:
        """
                Enable Fast Withdraw Switch (USER_DATA)
                POST /sapi/v1/account/enableFastWithdrawSwitch
                https://developers.binance.com/docs/wallet/account/Enable-Fast-Withdraw-Switch

                Enable Fast Withdraw Switch (USER_DATA)

        * This request will enable fastwithdraw switch under your  account. <br></br>
        * When Fast Withdraw Switch is on, transferring funds to a Binance account will be done instantly. There is no on-chain transaction, no transaction ID and no withdrawal fee.

        Weight: 1

                Args:
                    recv_window (Optional[int]):

                Returns:
                    ApiResponse[None]

                Raises:
                    RequiredError: If a required parameter is missing.

        """

        payload = {"recv_window": recv_window}

        return send_request(
            self._session,
            self._configuration,
            method="POST",
            path="/sapi/v1/account/enableFastWithdrawSwitch",
            payload=payload,
            time_unit=self._configuration.time_unit,
            is_signed=True,
            signer=self._signer,
        )

    def get_api_key_permission(
        self,
        recv_window: Optional[int] = None,
    ) -> ApiResponse[GetApiKeyPermissionResponse]:
        """
                Get API Key Permission (USER_DATA)
                GET /sapi/v1/account/apiRestrictions
                https://developers.binance.com/docs/wallet/account/api-key-permission

                Get API Key Permission

        Weight: 1

                Args:
                    recv_window (Optional[int]):

                Returns:
                    ApiResponse[GetApiKeyPermissionResponse]

                Raises:
                    RequiredError: If a required parameter is missing.

        """

        payload = {"recv_window": recv_window}

        return send_request(
            self._session,
            self._configuration,
            method="GET",
            path="/sapi/v1/account/apiRestrictions",
            payload=payload,
            time_unit=self._configuration.time_unit,
            response_model=GetApiKeyPermissionResponse,
            is_signed=True,
            signer=self._signer,
        )
