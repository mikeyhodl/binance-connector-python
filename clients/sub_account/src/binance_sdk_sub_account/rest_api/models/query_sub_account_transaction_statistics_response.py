# coding: utf-8

"""
Binance Sub Account REST API

OpenAPI Specification for the Binance Sub Account REST API
The version of the OpenAPI document: 1.0.0
Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from binance_sdk_sub_account.rest_api.models.query_sub_account_transaction_statistics_response_trade_info_vos_inner import (
    QuerySubAccountTransactionStatisticsResponseTradeInfoVosInner,
)
from typing import Set
from typing_extensions import Self


class QuerySubAccountTransactionStatisticsResponse(BaseModel):
    """
    QuerySubAccountTransactionStatisticsResponse
    """  # noqa: E501

    recent30_btc_total: Optional[StrictStr] = Field(
        default=None, alias="recent30BtcTotal"
    )
    recent30_btc_futures_total: Optional[StrictStr] = Field(
        default=None, alias="recent30BtcFuturesTotal"
    )
    recent30_btc_margin_total: Optional[StrictStr] = Field(
        default=None, alias="recent30BtcMarginTotal"
    )
    recent30_busd_total: Optional[StrictStr] = Field(
        default=None, alias="recent30BusdTotal"
    )
    recent30_busd_futures_total: Optional[StrictStr] = Field(
        default=None, alias="recent30BusdFuturesTotal"
    )
    recent30_busd_margin_total: Optional[StrictStr] = Field(
        default=None, alias="recent30BusdMarginTotal"
    )
    trade_info_vos: Optional[
        List[QuerySubAccountTransactionStatisticsResponseTradeInfoVosInner]
    ] = Field(default=None, alias="tradeInfoVos")
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = [
        "recent30BtcTotal",
        "recent30BtcFuturesTotal",
        "recent30BtcMarginTotal",
        "recent30BusdTotal",
        "recent30BusdFuturesTotal",
        "recent30BusdMarginTotal",
        "tradeInfoVos",
    ]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def is_array(cls) -> bool:
        return False

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of QuerySubAccountTransactionStatisticsResponse from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        * Fields in `self.additional_properties` are added to the output dict.
        """
        excluded_fields: Set[str] = set(
            [
                "additional_properties",
            ]
        )

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of each item in trade_info_vos (list)
        _items = []
        if self.trade_info_vos:
            for _item_trade_info_vos in self.trade_info_vos:
                if _item_trade_info_vos:
                    _items.append(_item_trade_info_vos.to_dict())
            _dict["tradeInfoVos"] = _items
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of QuerySubAccountTransactionStatisticsResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "recent30BtcTotal": obj.get("recent30BtcTotal"),
                "recent30BtcFuturesTotal": obj.get("recent30BtcFuturesTotal"),
                "recent30BtcMarginTotal": obj.get("recent30BtcMarginTotal"),
                "recent30BusdTotal": obj.get("recent30BusdTotal"),
                "recent30BusdFuturesTotal": obj.get("recent30BusdFuturesTotal"),
                "recent30BusdMarginTotal": obj.get("recent30BusdMarginTotal"),
                "tradeInfoVos": (
                    [
                        QuerySubAccountTransactionStatisticsResponseTradeInfoVosInner.from_dict(
                            _item
                        )
                        for _item in obj["tradeInfoVos"]
                    ]
                    if obj.get("tradeInfoVos") is not None
                    else None
                ),
            }
        )
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj
