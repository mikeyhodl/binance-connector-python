"""
Binance Derivatives Trading Portfolio Margin Pro REST API

OpenAPI Specification for the Binance Derivatives Trading Portfolio Margin Pro REST API
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
from .api.account_api import AccountApi
from .api.market_data_api import MarketDataApi

from .models import BnbTransferResponse
from .models import ChangeAutoRepayFuturesStatusResponse
from .models import FundAutoCollectionResponse
from .models import FundCollectionByAssetResponse
from .models import GetAutoRepayFuturesStatusResponse
from .models import GetPortfolioMarginProAccountBalanceResponse
from .models import GetPortfolioMarginProAccountInfoResponse
from .models import GetPortfolioMarginProSpanAccountInfoResponse
from .models import GetTransferableEarnAssetBalanceForPortfolioMarginResponse
from .models import MintBfusdForPortfolioMarginResponse
from .models import PortfolioMarginProBankruptcyLoanRepayResponse
from .models import QueryPortfolioMarginProBankruptcyLoanAmountResponse
from .models import QueryPortfolioMarginProBankruptcyLoanRepayHistoryResponse
from .models import QueryPortfolioMarginProNegativeBalanceInterestHistoryResponse
from .models import RedeemBfusdForPortfolioMarginResponse
from .models import RepayFuturesNegativeBalanceResponse
from .models import TransferLdusdtForPortfolioMarginResponse
from .models import GetPortfolioMarginAssetLeverageResponse
from .models import PortfolioMarginCollateralRateResponse
from .models import PortfolioMarginProTieredCollateralRateResponse
from .models import QueryPortfolioMarginAssetIndexPriceResponse


T = TypeVar("T")


class DerivativesTradingPortfolioMarginProRestAPI:
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

        self._accountApi = AccountApi(self.configuration, self._session, self._signer)
        self._marketDataApi = MarketDataApi(
            self.configuration, self._session, self._signer
        )

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

    def bnb_transfer(
        self,
        amount: float = None,
        transfer_side: str = None,
        recv_window: Optional[int] = None,
    ) -> ApiResponse[BnbTransferResponse]:
        """
                BNB transfer(USER_DATA)

                BNB transfer can be between Margin Account and USDM Account


        * You can only use this function 2 times per 10 minutes in a rolling manner

        Weight: 1500

                Args:
                    amount (float):
                    transfer_side (str): "TO_UM","FROM_UM"
                    recv_window (Optional[int]):

                Returns:
                    ApiResponse[BnbTransferResponse]

                Raises:
                    RequiredError: If a required parameter is missing.

        """

        return self._accountApi.bnb_transfer(amount, transfer_side, recv_window)

    def change_auto_repay_futures_status(
        self,
        auto_repay: str = None,
        recv_window: Optional[int] = None,
    ) -> ApiResponse[ChangeAutoRepayFuturesStatusResponse]:
        """
                Change Auto-repay-futures Status(TRADE)

                Change Auto-repay-futures Status

        Weight: 1500

                Args:
                    auto_repay (str): Default: `true`; `false` for turn off the auto-repay futures negative balance function
                    recv_window (Optional[int]):

                Returns:
                    ApiResponse[ChangeAutoRepayFuturesStatusResponse]

                Raises:
                    RequiredError: If a required parameter is missing.

        """

        return self._accountApi.change_auto_repay_futures_status(
            auto_repay, recv_window
        )

    def fund_auto_collection(
        self,
        recv_window: Optional[int] = None,
    ) -> ApiResponse[FundAutoCollectionResponse]:
        """
                Fund Auto-collection(USER_DATA)

                Transfers all assets from Futures Account to Margin account

        * The BNB would not be collected from UM-PM account to the Portfolio Margin account.
        * You can only use this function 500 times per hour in a rolling manner.

        Weight: 1500

                Args:
                    recv_window (Optional[int]):

                Returns:
                    ApiResponse[FundAutoCollectionResponse]

                Raises:
                    RequiredError: If a required parameter is missing.

        """

        return self._accountApi.fund_auto_collection(recv_window)

    def fund_collection_by_asset(
        self,
        asset: str = None,
        recv_window: Optional[int] = None,
    ) -> ApiResponse[FundCollectionByAssetResponse]:
        """
                Fund Collection by Asset(USER_DATA)

                Transfers specific asset from Futures Account to Margin account

        * The BNB transfer is not be supported

        Weight: 60

                Args:
                    asset (str): `LDUSDT` only
                    recv_window (Optional[int]):

                Returns:
                    ApiResponse[FundCollectionByAssetResponse]

                Raises:
                    RequiredError: If a required parameter is missing.

        """

        return self._accountApi.fund_collection_by_asset(asset, recv_window)

    def get_auto_repay_futures_status(
        self,
        recv_window: Optional[int] = None,
    ) -> ApiResponse[GetAutoRepayFuturesStatusResponse]:
        """
                Get Auto-repay-futures Status(USER_DATA)

                Query Auto-repay-futures Status

        Weight: 30

                Args:
                    recv_window (Optional[int]):

                Returns:
                    ApiResponse[GetAutoRepayFuturesStatusResponse]

                Raises:
                    RequiredError: If a required parameter is missing.

        """

        return self._accountApi.get_auto_repay_futures_status(recv_window)

    def get_portfolio_margin_pro_account_balance(
        self,
        asset: Optional[str] = None,
        recv_window: Optional[int] = None,
    ) -> ApiResponse[GetPortfolioMarginProAccountBalanceResponse]:
        """
                Get Portfolio Margin Pro Account Balance(USER_DATA)

                Query Portfolio Margin Pro account balance

        Weight: 20

                Args:
                    asset (Optional[str]):
                    recv_window (Optional[int]):

                Returns:
                    ApiResponse[GetPortfolioMarginProAccountBalanceResponse]

                Raises:
                    RequiredError: If a required parameter is missing.

        """

        return self._accountApi.get_portfolio_margin_pro_account_balance(
            asset, recv_window
        )

    def get_portfolio_margin_pro_account_info(
        self,
        recv_window: Optional[int] = None,
    ) -> ApiResponse[GetPortfolioMarginProAccountInfoResponse]:
        """
                Get Portfolio Margin Pro Account Info(USER_DATA)

                Get Portfolio Margin Pro Account Info

        Weight: 5

                Args:
                    recv_window (Optional[int]):

                Returns:
                    ApiResponse[GetPortfolioMarginProAccountInfoResponse]

                Raises:
                    RequiredError: If a required parameter is missing.

        """

        return self._accountApi.get_portfolio_margin_pro_account_info(recv_window)

    def get_portfolio_margin_pro_span_account_info(
        self,
        recv_window: Optional[int] = None,
    ) -> ApiResponse[GetPortfolioMarginProSpanAccountInfoResponse]:
        """
                Get Portfolio Margin Pro SPAN Account Info(USER_DATA)

                Get Portfolio Margin Pro SPAN Account Info (For Portfolio Margin Pro SPAN users only)

        Weight: 5

                Args:
                    recv_window (Optional[int]):

                Returns:
                    ApiResponse[GetPortfolioMarginProSpanAccountInfoResponse]

                Raises:
                    RequiredError: If a required parameter is missing.

        """

        return self._accountApi.get_portfolio_margin_pro_span_account_info(recv_window)

    def get_transferable_earn_asset_balance_for_portfolio_margin(
        self,
        asset: str = None,
        transfer_type: str = None,
        recv_window: Optional[int] = None,
    ) -> ApiResponse[GetTransferableEarnAssetBalanceForPortfolioMarginResponse]:
        """
                Get Transferable Earn Asset Balance for Portfolio Margin (USER_DATA)

                Get transferable earn asset balance for all types of Portfolio Margin account

        Weight: 1500

                Args:
                    asset (str): `LDUSDT` only
                    transfer_type (str): `EARN_TO_FUTURE` /`FUTURE_TO_EARN`
                    recv_window (Optional[int]):

                Returns:
                    ApiResponse[GetTransferableEarnAssetBalanceForPortfolioMarginResponse]

                Raises:
                    RequiredError: If a required parameter is missing.

        """

        return (
            self._accountApi.get_transferable_earn_asset_balance_for_portfolio_margin(
                asset, transfer_type, recv_window
            )
        )

    def mint_bfusd_for_portfolio_margin(
        self,
        from_asset: str = None,
        target_asset: str = None,
        amount: float = None,
        recv_window: Optional[int] = None,
    ) -> ApiResponse[MintBfusdForPortfolioMarginResponse]:
        """
                Mint BFUSD for Portfolio Margin(TRADE)

                Mint BFUSD for all types of Portfolio Margin account

        Weight: 1500

                Args:
                    from_asset (str): `BFUSD` only
                    target_asset (str): `USDT` `USDC`
                    amount (float):
                    recv_window (Optional[int]):

                Returns:
                    ApiResponse[MintBfusdForPortfolioMarginResponse]

                Raises:
                    RequiredError: If a required parameter is missing.

        """

        return self._accountApi.mint_bfusd_for_portfolio_margin(
            from_asset, target_asset, amount, recv_window
        )

    def portfolio_margin_pro_bankruptcy_loan_repay(
        self,
        var_from: Optional[str] = None,
        recv_window: Optional[int] = None,
    ) -> ApiResponse[PortfolioMarginProBankruptcyLoanRepayResponse]:
        """
                Portfolio Margin Pro Bankruptcy Loan Repay

                Repay Portfolio Margin Pro Bankruptcy Loan

        Weight: 3000

                Args:
                    var_from (Optional[str]): SPOT or MARGIN，default SPOT
                    recv_window (Optional[int]):

                Returns:
                    ApiResponse[PortfolioMarginProBankruptcyLoanRepayResponse]

                Raises:
                    RequiredError: If a required parameter is missing.

        """

        return self._accountApi.portfolio_margin_pro_bankruptcy_loan_repay(
            var_from, recv_window
        )

    def query_portfolio_margin_pro_bankruptcy_loan_amount(
        self,
        recv_window: Optional[int] = None,
    ) -> ApiResponse[QueryPortfolioMarginProBankruptcyLoanAmountResponse]:
        """
                Query Portfolio Margin Pro Bankruptcy Loan Amount(USER_DATA)

                Query Portfolio Margin Pro Bankruptcy Loan Amount

        * If there’s no classic portfolio margin bankruptcy loan, the amount would be 0

        Weight: 500

                Args:
                    recv_window (Optional[int]):

                Returns:
                    ApiResponse[QueryPortfolioMarginProBankruptcyLoanAmountResponse]

                Raises:
                    RequiredError: If a required parameter is missing.

        """

        return self._accountApi.query_portfolio_margin_pro_bankruptcy_loan_amount(
            recv_window
        )

    def query_portfolio_margin_pro_bankruptcy_loan_repay_history(
        self,
        start_time: Optional[int] = None,
        end_time: Optional[int] = None,
        current: Optional[int] = None,
        size: Optional[int] = None,
        recv_window: Optional[int] = None,
    ) -> ApiResponse[QueryPortfolioMarginProBankruptcyLoanRepayHistoryResponse]:
        """
                Query Portfolio Margin Pro Bankruptcy Loan Repay History(USER_DATA)

                Query repay history of pmloan for portfolio margin pro.

        * `startTime` and `endTime` cannot be longer than 360 days
        * If `startTime` and `endTime` not sent, return records of the last 30 days by default.
        * If `startTime`is sent and `endTime` is not sent, return records of [startTime, startTime+30d].
        * If `startTime` is not sent and `endTime` is sent, return records of [endTime-30d, endTime].

        Weight: 500

                Args:
                    start_time (Optional[int]):
                    end_time (Optional[int]):
                    current (Optional[int]): Currently querying page. Start from 1. Default:1
                    size (Optional[int]): Default:10 Max:100
                    recv_window (Optional[int]):

                Returns:
                    ApiResponse[QueryPortfolioMarginProBankruptcyLoanRepayHistoryResponse]

                Raises:
                    RequiredError: If a required parameter is missing.

        """

        return (
            self._accountApi.query_portfolio_margin_pro_bankruptcy_loan_repay_history(
                start_time, end_time, current, size, recv_window
            )
        )

    def query_portfolio_margin_pro_negative_balance_interest_history(
        self,
        asset: Optional[str] = None,
        start_time: Optional[int] = None,
        end_time: Optional[int] = None,
        size: Optional[int] = None,
        recv_window: Optional[int] = None,
    ) -> ApiResponse[QueryPortfolioMarginProNegativeBalanceInterestHistoryResponse]:
        """
                Query Portfolio Margin Pro Negative Balance Interest History(USER_DATA)

                Query interest history of negative balance for portfolio margin.

        Weight: 50

                Args:
                    asset (Optional[str]):
                    start_time (Optional[int]):
                    end_time (Optional[int]):
                    size (Optional[int]): Default:10 Max:100
                    recv_window (Optional[int]):

                Returns:
                    ApiResponse[QueryPortfolioMarginProNegativeBalanceInterestHistoryResponse]

                Raises:
                    RequiredError: If a required parameter is missing.

        """

        return self._accountApi.query_portfolio_margin_pro_negative_balance_interest_history(
            asset, start_time, end_time, size, recv_window
        )

    def redeem_bfusd_for_portfolio_margin(
        self,
        from_asset: str = None,
        target_asset: str = None,
        amount: float = None,
        recv_window: Optional[int] = None,
    ) -> ApiResponse[RedeemBfusdForPortfolioMarginResponse]:
        """
                Redeem BFUSD for Portfolio Margin(TRADE)

                Redeem BFUSD for all types of Portfolio Margin account

        Weight: 1500

                Args:
                    from_asset (str): `BFUSD` only
                    target_asset (str): `USDT` `USDC`
                    amount (float):
                    recv_window (Optional[int]):

                Returns:
                    ApiResponse[RedeemBfusdForPortfolioMarginResponse]

                Raises:
                    RequiredError: If a required parameter is missing.

        """

        return self._accountApi.redeem_bfusd_for_portfolio_margin(
            from_asset, target_asset, amount, recv_window
        )

    def repay_futures_negative_balance(
        self,
        var_from: Optional[str] = None,
        recv_window: Optional[int] = None,
    ) -> ApiResponse[RepayFuturesNegativeBalanceResponse]:
        """
                Repay futures Negative Balance(USER_DATA)

                Repay futures Negative Balance

        Weight: 1500

                Args:
                    var_from (Optional[str]): SPOT or MARGIN，default SPOT
                    recv_window (Optional[int]):

                Returns:
                    ApiResponse[RepayFuturesNegativeBalanceResponse]

                Raises:
                    RequiredError: If a required parameter is missing.

        """

        return self._accountApi.repay_futures_negative_balance(var_from, recv_window)

    def transfer_ldusdt_for_portfolio_margin(
        self,
        asset: str = None,
        transfer_type: str = None,
        amount: float = None,
        recv_window: Optional[int] = None,
    ) -> ApiResponse[TransferLdusdtForPortfolioMarginResponse]:
        """
                Transfer LDUSDT for Portfolio Margin(TRADE)

                Transfer LDUSDT as collateral for all types of Portfolio Margin account

        Weight: 1500

                Args:
                    asset (str): `LDUSDT` only
                    transfer_type (str): `EARN_TO_FUTURE` /`FUTURE_TO_EARN`
                    amount (float):
                    recv_window (Optional[int]):

                Returns:
                    ApiResponse[TransferLdusdtForPortfolioMarginResponse]

                Raises:
                    RequiredError: If a required parameter is missing.

        """

        return self._accountApi.transfer_ldusdt_for_portfolio_margin(
            asset, transfer_type, amount, recv_window
        )

    def get_portfolio_margin_asset_leverage(
        self,
    ) -> ApiResponse[GetPortfolioMarginAssetLeverageResponse]:
        """
                Get Portfolio Margin Asset Leverage(USER_DATA)

                Get Portfolio Margin Asset Leverage

        Weight: 50

                Args:

                Returns:
                    ApiResponse[GetPortfolioMarginAssetLeverageResponse]

                Raises:
                    RequiredError: If a required parameter is missing.

        """

        return self._marketDataApi.get_portfolio_margin_asset_leverage()

    def portfolio_margin_collateral_rate(
        self,
    ) -> ApiResponse[PortfolioMarginCollateralRateResponse]:
        """
                Portfolio Margin Collateral Rate(MARKET_DATA)

                Portfolio Margin Collateral Rate

        Weight: 50

                Args:

                Returns:
                    ApiResponse[PortfolioMarginCollateralRateResponse]

                Raises:
                    RequiredError: If a required parameter is missing.

        """

        return self._marketDataApi.portfolio_margin_collateral_rate()

    def portfolio_margin_pro_tiered_collateral_rate(
        self,
        recv_window: Optional[int] = None,
    ) -> ApiResponse[PortfolioMarginProTieredCollateralRateResponse]:
        """
                Portfolio Margin Pro Tiered Collateral Rate(USER_DATA)

                Portfolio Margin PRO Tiered Collateral Rate

        Weight: 50

                Args:
                    recv_window (Optional[int]):

                Returns:
                    ApiResponse[PortfolioMarginProTieredCollateralRateResponse]

                Raises:
                    RequiredError: If a required parameter is missing.

        """

        return self._marketDataApi.portfolio_margin_pro_tiered_collateral_rate(
            recv_window
        )

    def query_portfolio_margin_asset_index_price(
        self,
        asset: Optional[str] = None,
    ) -> ApiResponse[QueryPortfolioMarginAssetIndexPriceResponse]:
        """
                Query Portfolio Margin Asset Index Price (MARKET_DATA)

                Query Portfolio Margin Asset Index Price

        Weight: 1 if send asset or 50 if not send asset

                Args:
                    asset (Optional[str]):

                Returns:
                    ApiResponse[QueryPortfolioMarginAssetIndexPriceResponse]

                Raises:
                    RequiredError: If a required parameter is missing.

        """

        return self._marketDataApi.query_portfolio_margin_asset_index_price(asset)
