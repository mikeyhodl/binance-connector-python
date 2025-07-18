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
from binance_sdk_sub_account.rest_api.models.get_detail_on_sub_accounts_margin_account_response_margin_trade_coeff_vo import (
    GetDetailOnSubAccountsMarginAccountResponseMarginTradeCoeffVo,
)
from binance_sdk_sub_account.rest_api.models.get_detail_on_sub_accounts_margin_account_response_margin_user_asset_vo_list_inner import (
    GetDetailOnSubAccountsMarginAccountResponseMarginUserAssetVoListInner,
)
from typing import Set
from typing_extensions import Self


class GetDetailOnSubAccountsMarginAccountResponse(BaseModel):
    """
    GetDetailOnSubAccountsMarginAccountResponse
    """  # noqa: E501

    email: Optional[StrictStr] = None
    margin_level: Optional[StrictStr] = Field(default=None, alias="marginLevel")
    total_asset_of_btc: Optional[StrictStr] = Field(
        default=None, alias="totalAssetOfBtc"
    )
    total_liability_of_btc: Optional[StrictStr] = Field(
        default=None, alias="totalLiabilityOfBtc"
    )
    total_net_asset_of_btc: Optional[StrictStr] = Field(
        default=None, alias="totalNetAssetOfBtc"
    )
    margin_trade_coeff_vo: Optional[
        GetDetailOnSubAccountsMarginAccountResponseMarginTradeCoeffVo
    ] = Field(default=None, alias="marginTradeCoeffVo")
    margin_user_asset_vo_list: Optional[
        List[GetDetailOnSubAccountsMarginAccountResponseMarginUserAssetVoListInner]
    ] = Field(default=None, alias="marginUserAssetVoList")
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = [
        "email",
        "marginLevel",
        "totalAssetOfBtc",
        "totalLiabilityOfBtc",
        "totalNetAssetOfBtc",
        "marginTradeCoeffVo",
        "marginUserAssetVoList",
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
        """Create an instance of GetDetailOnSubAccountsMarginAccountResponse from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of margin_trade_coeff_vo
        if self.margin_trade_coeff_vo:
            _dict["marginTradeCoeffVo"] = self.margin_trade_coeff_vo.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in margin_user_asset_vo_list (list)
        _items = []
        if self.margin_user_asset_vo_list:
            for _item_margin_user_asset_vo_list in self.margin_user_asset_vo_list:
                if _item_margin_user_asset_vo_list:
                    _items.append(_item_margin_user_asset_vo_list.to_dict())
            _dict["marginUserAssetVoList"] = _items
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of GetDetailOnSubAccountsMarginAccountResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "email": obj.get("email"),
                "marginLevel": obj.get("marginLevel"),
                "totalAssetOfBtc": obj.get("totalAssetOfBtc"),
                "totalLiabilityOfBtc": obj.get("totalLiabilityOfBtc"),
                "totalNetAssetOfBtc": obj.get("totalNetAssetOfBtc"),
                "marginTradeCoeffVo": (
                    GetDetailOnSubAccountsMarginAccountResponseMarginTradeCoeffVo.from_dict(
                        obj["marginTradeCoeffVo"]
                    )
                    if obj.get("marginTradeCoeffVo") is not None
                    else None
                ),
                "marginUserAssetVoList": (
                    [
                        GetDetailOnSubAccountsMarginAccountResponseMarginUserAssetVoListInner.from_dict(
                            _item
                        )
                        for _item in obj["marginUserAssetVoList"]
                    ]
                    if obj.get("marginUserAssetVoList") is not None
                    else None
                ),
            }
        )
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj
