"""
Binance Margin Trading REST API

OpenAPI Specification for the Binance Margin Trading REST API
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

from ..models import CrossMarginCollateralRatioResponse
from ..models import GetAllCrossMarginPairsResponse
from ..models import GetAllIsolatedMarginSymbolResponse
from ..models import GetAllMarginAssetsResponse
from ..models import GetDelistScheduleResponse
from ..models import GetListScheduleResponse
from ..models import QueryIsolatedMarginTierDataResponse
from ..models import QueryLiabilityCoinLeverageBracketInCrossMarginProModeResponse
from ..models import QueryMarginAvailableInventoryResponse
from ..models import QueryMarginPriceindexResponse


class MarketDataApi:
    """API Client for MarketDataApi endpoints."""

    def __init__(
        self,
        configuration: ConfigurationRestAPI = None,
        session: Session = None,
        signer: Signers = None,
    ) -> None:
        self._configuration = configuration
        self._session = session
        self._signer = signer

    def cross_margin_collateral_ratio(
        self,
    ) -> ApiResponse[CrossMarginCollateralRatioResponse]:
        """
                Cross margin collateral ratio (MARKET_DATA)
                GET /sapi/v1/margin/crossMarginCollateralRatio
                https://developers.binance.com/docs/margin_trading/market-data/Cross-margin-collateral-ratio

                Cross margin collateral ratio

        Weight: 100(IP)

                Args:

                Returns:
                    ApiResponse[CrossMarginCollateralRatioResponse]

                Raises:
                    RequiredError: If a required parameter is missing.

        """

        payload = None

        return send_request(
            self._session,
            self._configuration,
            method="GET",
            path="/sapi/v1/margin/crossMarginCollateralRatio",
            payload=payload,
            time_unit=self._configuration.time_unit,
            response_model=CrossMarginCollateralRatioResponse,
        )

    def get_all_cross_margin_pairs(
        self,
        symbol: Optional[str] = None,
    ) -> ApiResponse[GetAllCrossMarginPairsResponse]:
        """
                Get All Cross Margin Pairs (MARKET_DATA)
                GET /sapi/v1/margin/allPairs
                https://developers.binance.com/docs/margin_trading/market-data/Get-All-Cross-Margin-Pairs

                Get All Cross Margin Pairs

        Weight: 1(IP)

                Args:
                    symbol (Optional[str]): isolated margin pair

                Returns:
                    ApiResponse[GetAllCrossMarginPairsResponse]

                Raises:
                    RequiredError: If a required parameter is missing.

        """

        payload = {"symbol": symbol}

        return send_request(
            self._session,
            self._configuration,
            method="GET",
            path="/sapi/v1/margin/allPairs",
            payload=payload,
            time_unit=self._configuration.time_unit,
            response_model=GetAllCrossMarginPairsResponse,
        )

    def get_all_isolated_margin_symbol(
        self,
        symbol: Optional[str] = None,
        recv_window: Optional[int] = None,
    ) -> ApiResponse[GetAllIsolatedMarginSymbolResponse]:
        """
                Get All Isolated Margin Symbol(MARKET_DATA)
                GET /sapi/v1/margin/isolated/allPairs
                https://developers.binance.com/docs/margin_trading/market-data/Get-All-Isolated-Margin-Symbol

                Get All Isolated Margin Symbol

        Weight: 10(IP)

                Args:
                    symbol (Optional[str]): isolated margin pair
                    recv_window (Optional[int]): No more than 60000

                Returns:
                    ApiResponse[GetAllIsolatedMarginSymbolResponse]

                Raises:
                    RequiredError: If a required parameter is missing.

        """

        payload = {"symbol": symbol, "recv_window": recv_window}

        return send_request(
            self._session,
            self._configuration,
            method="GET",
            path="/sapi/v1/margin/isolated/allPairs",
            payload=payload,
            time_unit=self._configuration.time_unit,
            response_model=GetAllIsolatedMarginSymbolResponse,
        )

    def get_all_margin_assets(
        self,
        asset: Optional[str] = None,
    ) -> ApiResponse[GetAllMarginAssetsResponse]:
        """
                Get All Margin Assets (MARKET_DATA)
                GET /sapi/v1/margin/allAssets
                https://developers.binance.com/docs/margin_trading/market-data/Get-All-Margin-Assets

                Get All Margin Assets.

        Weight: 1(IP)

                Args:
                    asset (Optional[str]):

                Returns:
                    ApiResponse[GetAllMarginAssetsResponse]

                Raises:
                    RequiredError: If a required parameter is missing.

        """

        payload = {"asset": asset}

        return send_request(
            self._session,
            self._configuration,
            method="GET",
            path="/sapi/v1/margin/allAssets",
            payload=payload,
            time_unit=self._configuration.time_unit,
            response_model=GetAllMarginAssetsResponse,
        )

    def get_delist_schedule(
        self,
        recv_window: Optional[int] = None,
    ) -> ApiResponse[GetDelistScheduleResponse]:
        """
                Get Delist Schedule (MARKET_DATA)
                GET /sapi/v1/margin/delist-schedule
                https://developers.binance.com/docs/margin_trading/market-data/Get-Delist-Schedule

                Get tokens or symbols delist schedule for cross margin and isolated margin

        Weight: 100

                Args:
                    recv_window (Optional[int]): No more than 60000

                Returns:
                    ApiResponse[GetDelistScheduleResponse]

                Raises:
                    RequiredError: If a required parameter is missing.

        """

        payload = {"recv_window": recv_window}

        return send_request(
            self._session,
            self._configuration,
            method="GET",
            path="/sapi/v1/margin/delist-schedule",
            payload=payload,
            time_unit=self._configuration.time_unit,
            response_model=GetDelistScheduleResponse,
        )

    def get_list_schedule(
        self,
        recv_window: Optional[int] = None,
    ) -> ApiResponse[GetListScheduleResponse]:
        """
                Get list Schedule (MARKET_DATA)
                GET /sapi/v1/margin/list-schedule
                https://developers.binance.com/docs/margin_trading/market-data/Get-list-Schedule

                Get the upcoming tokens or symbols listing schedule for Cross Margin and Isolated Margin.

        Weight: 100

                Args:
                    recv_window (Optional[int]): No more than 60000

                Returns:
                    ApiResponse[GetListScheduleResponse]

                Raises:
                    RequiredError: If a required parameter is missing.

        """

        payload = {"recv_window": recv_window}

        return send_request(
            self._session,
            self._configuration,
            method="GET",
            path="/sapi/v1/margin/list-schedule",
            payload=payload,
            time_unit=self._configuration.time_unit,
            response_model=GetListScheduleResponse,
        )

    def query_isolated_margin_tier_data(
        self,
        symbol: str = None,
        tier: Optional[int] = None,
        recv_window: Optional[int] = None,
    ) -> ApiResponse[QueryIsolatedMarginTierDataResponse]:
        """
                Query Isolated Margin Tier Data (USER_DATA)
                GET /sapi/v1/margin/isolatedMarginTier
                https://developers.binance.com/docs/margin_trading/market-data/Query-Isolated-Margin-Tier-Data

                Get isolated margin tier data collection with any tier as https://www.binance.com/en/margin-data

        Weight: 1(IP)

                Args:
                    symbol (str):
                    tier (Optional[int]): All margin tier data will be returned if tier is omitted
                    recv_window (Optional[int]): No more than 60000

                Returns:
                    ApiResponse[QueryIsolatedMarginTierDataResponse]

                Raises:
                    RequiredError: If a required parameter is missing.

        """

        if symbol is None:
            raise RequiredError(
                field="symbol", error_message="Missing required parameter 'symbol'"
            )

        payload = {"symbol": symbol, "tier": tier, "recv_window": recv_window}

        return send_request(
            self._session,
            self._configuration,
            method="GET",
            path="/sapi/v1/margin/isolatedMarginTier",
            payload=payload,
            time_unit=self._configuration.time_unit,
            response_model=QueryIsolatedMarginTierDataResponse,
            is_signed=True,
            signer=self._signer,
        )

    def query_liability_coin_leverage_bracket_in_cross_margin_pro_mode(
        self,
    ) -> ApiResponse[QueryLiabilityCoinLeverageBracketInCrossMarginProModeResponse]:
        """
                Query Liability Coin Leverage Bracket in Cross Margin Pro Mode(MARKET_DATA)
                GET /sapi/v1/margin/leverageBracket
                https://developers.binance.com/docs/margin_trading/market-data/Query-Liability-Coin-Leverage-Bracket-in-Cross-Margin-Pro-Mode

                Liability Coin Leverage Bracket in Cross Margin Pro Mode

        Weight: 1

                Args:

                Returns:
                    ApiResponse[QueryLiabilityCoinLeverageBracketInCrossMarginProModeResponse]

                Raises:
                    RequiredError: If a required parameter is missing.

        """

        payload = None

        return send_request(
            self._session,
            self._configuration,
            method="GET",
            path="/sapi/v1/margin/leverageBracket",
            payload=payload,
            time_unit=self._configuration.time_unit,
            response_model=QueryLiabilityCoinLeverageBracketInCrossMarginProModeResponse,
        )

    def query_margin_available_inventory(
        self,
        type: str = None,
    ) -> ApiResponse[QueryMarginAvailableInventoryResponse]:
        """
                Query Margin Available Inventory(USER_DATA)
                GET /sapi/v1/margin/available-inventory
                https://developers.binance.com/docs/margin_trading/market-data/Query-margin-avaliable-inventory

                Margin available Inventory query

        Weight: 50

                Args:
                    type (str): `MARGIN`,`ISOLATED`

                Returns:
                    ApiResponse[QueryMarginAvailableInventoryResponse]

                Raises:
                    RequiredError: If a required parameter is missing.

        """

        if type is None:
            raise RequiredError(
                field="type", error_message="Missing required parameter 'type'"
            )

        payload = {"type": type}

        return send_request(
            self._session,
            self._configuration,
            method="GET",
            path="/sapi/v1/margin/available-inventory",
            payload=payload,
            time_unit=self._configuration.time_unit,
            response_model=QueryMarginAvailableInventoryResponse,
            is_signed=True,
            signer=self._signer,
        )

    def query_margin_priceindex(
        self,
        symbol: str = None,
    ) -> ApiResponse[QueryMarginPriceindexResponse]:
        """
                Query Margin PriceIndex (MARKET_DATA)
                GET /sapi/v1/margin/priceIndex
                https://developers.binance.com/docs/margin_trading/market-data/Query-Margin-PriceIndex

                Query Margin PriceIndex

        Weight: 10(IP)

                Args:
                    symbol (str):

                Returns:
                    ApiResponse[QueryMarginPriceindexResponse]

                Raises:
                    RequiredError: If a required parameter is missing.

        """

        if symbol is None:
            raise RequiredError(
                field="symbol", error_message="Missing required parameter 'symbol'"
            )

        payload = {"symbol": symbol}

        return send_request(
            self._session,
            self._configuration,
            method="GET",
            path="/sapi/v1/margin/priceIndex",
            payload=payload,
            time_unit=self._configuration.time_unit,
            response_model=QueryMarginPriceindexResponse,
        )
