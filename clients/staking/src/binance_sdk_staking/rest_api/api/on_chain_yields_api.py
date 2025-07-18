"""
Binance Staking REST API

OpenAPI Specification for the Binance Staking REST API
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

from ..models import GetOnChainYieldsLockedPersonalLeftQuotaResponse
from ..models import GetOnChainYieldsLockedProductListResponse
from ..models import GetOnChainYieldsLockedProductPositionResponse
from ..models import GetOnChainYieldsLockedRedemptionRecordResponse
from ..models import GetOnChainYieldsLockedRewardsHistoryResponse
from ..models import GetOnChainYieldsLockedSubscriptionPreviewResponse
from ..models import GetOnChainYieldsLockedSubscriptionRecordResponse
from ..models import OnChainYieldsAccountResponse
from ..models import RedeemOnChainYieldsLockedProductResponse
from ..models import SetOnChainYieldsLockedAutoSubscribeResponse
from ..models import SetOnChainYieldsLockedProductRedeemOptionResponse
from ..models import SubscribeOnChainYieldsLockedProductResponse


class OnChainYieldsApi:
    """API Client for OnChainYieldsApi endpoints."""

    def __init__(
        self,
        configuration: ConfigurationRestAPI = None,
        session: Session = None,
        signer: Signers = None,
    ) -> None:
        self._configuration = configuration
        self._session = session
        self._signer = signer

    def get_on_chain_yields_locked_personal_left_quota(
        self,
        project_id: str = None,
        recv_window: Optional[int] = None,
    ) -> ApiResponse[GetOnChainYieldsLockedPersonalLeftQuotaResponse]:
        """
                Get On-chain Yields Locked Personal Left Quota (USER_DATA)
                GET /sapi/v1/onchain-yields/locked/personalLeftQuota
                https://developers.binance.com/docs/staking/on-chain-yields/account/Get-Onchain-Locked-Personal-Left-Quota

                Get On-chain Yields Locked Personal Left Quota

        Weight: 50

                Args:
                    project_id (str):
                    recv_window (Optional[int]):

                Returns:
                    ApiResponse[GetOnChainYieldsLockedPersonalLeftQuotaResponse]

                Raises:
                    RequiredError: If a required parameter is missing.

        """

        if project_id is None:
            raise RequiredError(
                field="project_id",
                error_message="Missing required parameter 'project_id'",
            )

        payload = {"project_id": project_id, "recv_window": recv_window}

        return send_request(
            self._session,
            self._configuration,
            method="GET",
            path="/sapi/v1/onchain-yields/locked/personalLeftQuota",
            payload=payload,
            time_unit=self._configuration.time_unit,
            response_model=GetOnChainYieldsLockedPersonalLeftQuotaResponse,
            is_signed=True,
            signer=self._signer,
        )

    def get_on_chain_yields_locked_product_list(
        self,
        asset: Optional[str] = None,
        current: Optional[int] = None,
        size: Optional[int] = None,
        recv_window: Optional[int] = None,
    ) -> ApiResponse[GetOnChainYieldsLockedProductListResponse]:
        """
                Get On-chain Yields Locked Product List (USER_DATA)
                GET /sapi/v1/onchain-yields/locked/list
                https://developers.binance.com/docs/staking/on-chain-yields/account/

                Get available On-chain Yields Locked product list

        * Get available On-chain Yields Locked product list

        Weight: 50

                Args:
                    asset (Optional[str]): WBETH or BETH, default to BETH
                    current (Optional[int]): Currently querying page. Start from 1. Default:1
                    size (Optional[int]): Default:10, Max:100
                    recv_window (Optional[int]):

                Returns:
                    ApiResponse[GetOnChainYieldsLockedProductListResponse]

                Raises:
                    RequiredError: If a required parameter is missing.

        """

        payload = {
            "asset": asset,
            "current": current,
            "size": size,
            "recv_window": recv_window,
        }

        return send_request(
            self._session,
            self._configuration,
            method="GET",
            path="/sapi/v1/onchain-yields/locked/list",
            payload=payload,
            time_unit=self._configuration.time_unit,
            response_model=GetOnChainYieldsLockedProductListResponse,
            is_signed=True,
            signer=self._signer,
        )

    def get_on_chain_yields_locked_product_position(
        self,
        asset: Optional[str] = None,
        position_id: Optional[int] = None,
        project_id: Optional[str] = None,
        current: Optional[int] = None,
        size: Optional[int] = None,
        recv_window: Optional[int] = None,
    ) -> ApiResponse[GetOnChainYieldsLockedProductPositionResponse]:
        """
                Get On-chain Yields Locked Product Position (USER_DATA)
                GET /sapi/v1/onchain-yields/locked/position
                https://developers.binance.com/docs/staking/on-chain-yields/account/Get-Onchain-Locked-Product-Position

                Get On-chain Yields Locked Product Position

        Weight: 50

                Args:
                    asset (Optional[str]): WBETH or BETH, default to BETH
                    position_id (Optional[int]):
                    project_id (Optional[str]):
                    current (Optional[int]): Currently querying page. Start from 1. Default:1
                    size (Optional[int]): Default:10, Max:100
                    recv_window (Optional[int]):

                Returns:
                    ApiResponse[GetOnChainYieldsLockedProductPositionResponse]

                Raises:
                    RequiredError: If a required parameter is missing.

        """

        payload = {
            "asset": asset,
            "position_id": position_id,
            "project_id": project_id,
            "current": current,
            "size": size,
            "recv_window": recv_window,
        }

        return send_request(
            self._session,
            self._configuration,
            method="GET",
            path="/sapi/v1/onchain-yields/locked/position",
            payload=payload,
            time_unit=self._configuration.time_unit,
            response_model=GetOnChainYieldsLockedProductPositionResponse,
            is_signed=True,
            signer=self._signer,
        )

    def get_on_chain_yields_locked_redemption_record(
        self,
        position_id: Optional[int] = None,
        redeem_id: Optional[str] = None,
        asset: Optional[str] = None,
        start_time: Optional[int] = None,
        end_time: Optional[int] = None,
        current: Optional[int] = None,
        size: Optional[int] = None,
        recv_window: Optional[int] = None,
    ) -> ApiResponse[GetOnChainYieldsLockedRedemptionRecordResponse]:
        """
                Get On-chain Yields Locked Redemption Record (USER_DATA)
                GET /sapi/v1/onchain-yields/locked/history/redemptionRecord
                https://developers.binance.com/docs/staking/on-chain-yields/history/Get-Onchain-Locked-Redemption-Record

                Get On-chain Yields Locked Redemption Record

        * The time between `startTime` and `endTime` cannot be longer than 3 months.
        * If `startTime` and `endTime` are both not sent, then the last 30 days' data will be returned.
        * If `startTime` is sent but `endTime` is not sent, the next 30 days' data beginning from `startTime` will be returned.
        * If `endTime` is sent but `startTime` is not sent, the 30 days' data before `endTime` will be returned.

        Weight: 50

                Args:
                    position_id (Optional[int]):
                    redeem_id (Optional[str]):
                    asset (Optional[str]): WBETH or BETH, default to BETH
                    start_time (Optional[int]):
                    end_time (Optional[int]):
                    current (Optional[int]): Currently querying page. Start from 1. Default:1
                    size (Optional[int]): Default:10, Max:100
                    recv_window (Optional[int]):

                Returns:
                    ApiResponse[GetOnChainYieldsLockedRedemptionRecordResponse]

                Raises:
                    RequiredError: If a required parameter is missing.

        """

        payload = {
            "position_id": position_id,
            "redeem_id": redeem_id,
            "asset": asset,
            "start_time": start_time,
            "end_time": end_time,
            "current": current,
            "size": size,
            "recv_window": recv_window,
        }

        return send_request(
            self._session,
            self._configuration,
            method="GET",
            path="/sapi/v1/onchain-yields/locked/history/redemptionRecord",
            payload=payload,
            time_unit=self._configuration.time_unit,
            response_model=GetOnChainYieldsLockedRedemptionRecordResponse,
            is_signed=True,
            signer=self._signer,
        )

    def get_on_chain_yields_locked_rewards_history(
        self,
        position_id: Optional[str] = None,
        asset: Optional[str] = None,
        start_time: Optional[int] = None,
        end_time: Optional[int] = None,
        current: Optional[int] = None,
        size: Optional[int] = None,
        recv_window: Optional[int] = None,
    ) -> ApiResponse[GetOnChainYieldsLockedRewardsHistoryResponse]:
        """
                Get On-chain Yields Locked Rewards History (USER_DATA)
                GET /sapi/v1/onchain-yields/locked/history/rewardsRecord
                https://developers.binance.com/docs/staking/on-chain-yields/history/Get-Onchain-Locked-Rewards-History

                Get On-chain Yields Locked Rewards History

        * The time between `startTime` and `endTime` cannot be longer than 3 months.
        * If `startTime` and `endTime` are both not sent, then the last 30 days' data will be returned.
        * If `startTime` is sent but `endTime` is not sent, the next 30 days' data beginning from `startTime` will be returned.
        * If `endTime` is sent but `startTime` is not sent, the 30 days' data before `endTime` will be returned.

        Weight: 50

                Args:
                    position_id (Optional[str]):
                    asset (Optional[str]): WBETH or BETH, default to BETH
                    start_time (Optional[int]):
                    end_time (Optional[int]):
                    current (Optional[int]): Currently querying page. Start from 1. Default:1
                    size (Optional[int]): Default:10, Max:100
                    recv_window (Optional[int]):

                Returns:
                    ApiResponse[GetOnChainYieldsLockedRewardsHistoryResponse]

                Raises:
                    RequiredError: If a required parameter is missing.

        """

        payload = {
            "position_id": position_id,
            "asset": asset,
            "start_time": start_time,
            "end_time": end_time,
            "current": current,
            "size": size,
            "recv_window": recv_window,
        }

        return send_request(
            self._session,
            self._configuration,
            method="GET",
            path="/sapi/v1/onchain-yields/locked/history/rewardsRecord",
            payload=payload,
            time_unit=self._configuration.time_unit,
            response_model=GetOnChainYieldsLockedRewardsHistoryResponse,
            is_signed=True,
            signer=self._signer,
        )

    def get_on_chain_yields_locked_subscription_preview(
        self,
        project_id: str = None,
        amount: float = None,
        auto_subscribe: Optional[bool] = None,
        recv_window: Optional[int] = None,
    ) -> ApiResponse[GetOnChainYieldsLockedSubscriptionPreviewResponse]:
        """
                Get On-chain Yields Locked Subscription Preview (USER_DATA)
                GET /sapi/v1/onchain-yields/locked/subscriptionPreview
                https://developers.binance.com/docs/staking/on-chain-yields/earn/

                Get On-chain Yields Locked Subscription Preview

        Weight: 50

                Args:
                    project_id (str):
                    amount (float): Amount in SOL.
                    auto_subscribe (Optional[bool]): true or false, default true.
                    recv_window (Optional[int]):

                Returns:
                    ApiResponse[GetOnChainYieldsLockedSubscriptionPreviewResponse]

                Raises:
                    RequiredError: If a required parameter is missing.

        """

        if project_id is None:
            raise RequiredError(
                field="project_id",
                error_message="Missing required parameter 'project_id'",
            )
        if amount is None:
            raise RequiredError(
                field="amount", error_message="Missing required parameter 'amount'"
            )

        payload = {
            "project_id": project_id,
            "amount": amount,
            "auto_subscribe": auto_subscribe,
            "recv_window": recv_window,
        }

        return send_request(
            self._session,
            self._configuration,
            method="GET",
            path="/sapi/v1/onchain-yields/locked/subscriptionPreview",
            payload=payload,
            time_unit=self._configuration.time_unit,
            response_model=GetOnChainYieldsLockedSubscriptionPreviewResponse,
            is_signed=True,
            signer=self._signer,
        )

    def get_on_chain_yields_locked_subscription_record(
        self,
        purchase_id: Optional[str] = None,
        client_id: Optional[str] = None,
        asset: Optional[str] = None,
        start_time: Optional[int] = None,
        end_time: Optional[int] = None,
        current: Optional[int] = None,
        size: Optional[int] = None,
        recv_window: Optional[int] = None,
    ) -> ApiResponse[GetOnChainYieldsLockedSubscriptionRecordResponse]:
        """
                Get On-chain Yields Locked Subscription Record (USER_DATA)
                GET /sapi/v1/onchain-yields/locked/history/subscriptionRecord
                https://developers.binance.com/docs/staking/on-chain-yields/history/

                Get On-chain Yields Locked Subscription Record

        * The time between `startTime` and `endTime` cannot be longer than 3 months.
        * If `startTime` and `endTime` are both not sent, then the last 30 days' data will be returned.
        * If `startTime` is sent but `endTime` is not sent, the next 30 days' data beginning from `startTime` will be returned.
        * If `endTime` is sent but `startTime` is not sent, the 30 days' data before `endTime` will be returned.

        Weight: 50

                Args:
                    purchase_id (Optional[str]):
                    client_id (Optional[str]):
                    asset (Optional[str]): WBETH or BETH, default to BETH
                    start_time (Optional[int]):
                    end_time (Optional[int]):
                    current (Optional[int]): Currently querying page. Start from 1. Default:1
                    size (Optional[int]): Default:10, Max:100
                    recv_window (Optional[int]):

                Returns:
                    ApiResponse[GetOnChainYieldsLockedSubscriptionRecordResponse]

                Raises:
                    RequiredError: If a required parameter is missing.

        """

        payload = {
            "purchase_id": purchase_id,
            "client_id": client_id,
            "asset": asset,
            "start_time": start_time,
            "end_time": end_time,
            "current": current,
            "size": size,
            "recv_window": recv_window,
        }

        return send_request(
            self._session,
            self._configuration,
            method="GET",
            path="/sapi/v1/onchain-yields/locked/history/subscriptionRecord",
            payload=payload,
            time_unit=self._configuration.time_unit,
            response_model=GetOnChainYieldsLockedSubscriptionRecordResponse,
            is_signed=True,
            signer=self._signer,
        )

    def on_chain_yields_account(
        self,
        recv_window: Optional[int] = None,
    ) -> ApiResponse[OnChainYieldsAccountResponse]:
        """
                On-chain Yields Account (USER_DATA)
                GET /sapi/v1/onchain-yields/account
                https://developers.binance.com/docs/staking/on-chain-yields/account/Onchain-Account

                On-chain Yields Account query

        Weight: 50

                Args:
                    recv_window (Optional[int]):

                Returns:
                    ApiResponse[OnChainYieldsAccountResponse]

                Raises:
                    RequiredError: If a required parameter is missing.

        """

        payload = {"recv_window": recv_window}

        return send_request(
            self._session,
            self._configuration,
            method="GET",
            path="/sapi/v1/onchain-yields/account",
            payload=payload,
            time_unit=self._configuration.time_unit,
            response_model=OnChainYieldsAccountResponse,
            is_signed=True,
            signer=self._signer,
        )

    def redeem_on_chain_yields_locked_product(
        self,
        position_id: str = None,
        channel_id: Optional[str] = None,
        recv_window: Optional[int] = None,
    ) -> ApiResponse[RedeemOnChainYieldsLockedProductResponse]:
        """
                Redeem On-chain Yields Locked Product (TRADE)
                POST /sapi/v1/onchain-yields/locked/redeem
                https://developers.binance.com/docs/staking/on-chain-yields/earn/Redeem-Onchain-Locked-Product

                Redeem On-chain Yields Locked Product

        * You need to open `Enable Spot & Margin Trading` permission for the API Key which requests this endpoint.

        Weight: 1/3s per account

                Args:
                    position_id (str):
                    channel_id (Optional[str]):
                    recv_window (Optional[int]):

                Returns:
                    ApiResponse[RedeemOnChainYieldsLockedProductResponse]

                Raises:
                    RequiredError: If a required parameter is missing.

        """

        if position_id is None:
            raise RequiredError(
                field="position_id",
                error_message="Missing required parameter 'position_id'",
            )

        payload = {
            "position_id": position_id,
            "channel_id": channel_id,
            "recv_window": recv_window,
        }

        return send_request(
            self._session,
            self._configuration,
            method="POST",
            path="/sapi/v1/onchain-yields/locked/redeem",
            payload=payload,
            time_unit=self._configuration.time_unit,
            response_model=RedeemOnChainYieldsLockedProductResponse,
            is_signed=True,
            signer=self._signer,
        )

    def set_on_chain_yields_locked_auto_subscribe(
        self,
        position_id: str = None,
        auto_subscribe: bool = None,
        recv_window: Optional[int] = None,
    ) -> ApiResponse[SetOnChainYieldsLockedAutoSubscribeResponse]:
        """
                Set On-chain Yields Locked Auto Subscribe(USER_DATA)
                POST /sapi/v1/onchain-yields/locked/setAutoSubscribe
                https://developers.binance.com/docs/staking/on-chain-yields/earn/Set-Onchain-Locked-Auto-Subscribe

                Set On-chain Yield locked auto subscribe

        Weight: 50

                Args:
                    position_id (str):
                    auto_subscribe (bool): true or false
                    recv_window (Optional[int]):

                Returns:
                    ApiResponse[SetOnChainYieldsLockedAutoSubscribeResponse]

                Raises:
                    RequiredError: If a required parameter is missing.

        """

        if position_id is None:
            raise RequiredError(
                field="position_id",
                error_message="Missing required parameter 'position_id'",
            )
        if auto_subscribe is None:
            raise RequiredError(
                field="auto_subscribe",
                error_message="Missing required parameter 'auto_subscribe'",
            )

        payload = {
            "position_id": position_id,
            "auto_subscribe": auto_subscribe,
            "recv_window": recv_window,
        }

        return send_request(
            self._session,
            self._configuration,
            method="POST",
            path="/sapi/v1/onchain-yields/locked/setAutoSubscribe",
            payload=payload,
            time_unit=self._configuration.time_unit,
            response_model=SetOnChainYieldsLockedAutoSubscribeResponse,
            is_signed=True,
            signer=self._signer,
        )

    def set_on_chain_yields_locked_product_redeem_option(
        self,
        position_id: str = None,
        redeem_to: str = None,
        recv_window: Optional[int] = None,
    ) -> ApiResponse[SetOnChainYieldsLockedProductRedeemOptionResponse]:
        """
                Set On-chain Yields Locked Product Redeem Option(USER_DATA)
                POST /sapi/v1/onchain-yields/locked/setRedeemOption
                https://developers.binance.com/docs/staking/on-chain-yields/earn/Set-Onchain-Locked-Redeem-Option

                Set On-chain Yields redeem option for Locked product

        Weight: 50

                Args:
                    position_id (str):
                    redeem_to (str): 'SPOT','FLEXIBLE'
                    recv_window (Optional[int]):

                Returns:
                    ApiResponse[SetOnChainYieldsLockedProductRedeemOptionResponse]

                Raises:
                    RequiredError: If a required parameter is missing.

        """

        if position_id is None:
            raise RequiredError(
                field="position_id",
                error_message="Missing required parameter 'position_id'",
            )
        if redeem_to is None:
            raise RequiredError(
                field="redeem_to",
                error_message="Missing required parameter 'redeem_to'",
            )

        payload = {
            "position_id": position_id,
            "redeem_to": redeem_to,
            "recv_window": recv_window,
        }

        return send_request(
            self._session,
            self._configuration,
            method="POST",
            path="/sapi/v1/onchain-yields/locked/setRedeemOption",
            payload=payload,
            time_unit=self._configuration.time_unit,
            response_model=SetOnChainYieldsLockedProductRedeemOptionResponse,
            is_signed=True,
            signer=self._signer,
        )

    def subscribe_on_chain_yields_locked_product(
        self,
        project_id: str = None,
        amount: float = None,
        auto_subscribe: Optional[bool] = None,
        source_account: Optional[str] = None,
        redeem_to: Optional[str] = None,
        channel_id: Optional[str] = None,
        client_id: Optional[str] = None,
        recv_window: Optional[int] = None,
    ) -> ApiResponse[SubscribeOnChainYieldsLockedProductResponse]:
        """
                Subscribe On-chain Yields Locked Product(TRADE)
                POST /sapi/v1/onchain-yields/locked/subscribe
                https://developers.binance.com/docs/staking/on-chain-yields/earn/Subscribe-Onchain-Locked-Product

                Subscribe On-chain Yields Locked Product

        * You need to open `Enable Spot & Margin Trading` permission for the API Key which requests this endpoint.

        Weight: 200

                Args:
                    project_id (str):
                    amount (float): Amount in SOL.
                    auto_subscribe (Optional[bool]): true or false, default true.
                    source_account (Optional[str]): `SPOT`,`FUND`,`ALL`, default `SPOT`
                    redeem_to (Optional[str]): `SPOT`,`FLEXIBLE`, default `FLEXIBLE` Takes effect when Auto Subscribe is false
                    channel_id (Optional[str]):
                    client_id (Optional[str]):
                    recv_window (Optional[int]):

                Returns:
                    ApiResponse[SubscribeOnChainYieldsLockedProductResponse]

                Raises:
                    RequiredError: If a required parameter is missing.

        """

        if project_id is None:
            raise RequiredError(
                field="project_id",
                error_message="Missing required parameter 'project_id'",
            )
        if amount is None:
            raise RequiredError(
                field="amount", error_message="Missing required parameter 'amount'"
            )

        payload = {
            "project_id": project_id,
            "amount": amount,
            "auto_subscribe": auto_subscribe,
            "source_account": source_account,
            "redeem_to": redeem_to,
            "channel_id": channel_id,
            "client_id": client_id,
            "recv_window": recv_window,
        }

        return send_request(
            self._session,
            self._configuration,
            method="POST",
            path="/sapi/v1/onchain-yields/locked/subscribe",
            payload=payload,
            time_unit=self._configuration.time_unit,
            response_model=SubscribeOnChainYieldsLockedProductResponse,
            is_signed=True,
            signer=self._signer,
        )
