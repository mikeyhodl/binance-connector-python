# coding: utf-8

"""
Binance Wallet REST API

OpenAPI Specification for the Binance Wallet REST API
The version of the OpenAPI document: 1.0.0
Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from binance_sdk_wallet.rest_api.models.all_coins_information_response_inner_network_list_inner_network_list_inner import (
    AllCoinsInformationResponseInnerNetworkListInnerNetworkListInner,
)
from typing import Set
from typing_extensions import Self


class AllCoinsInformationResponseInnerNetworkListInner(BaseModel):
    """
    AllCoinsInformationResponseInnerNetworkListInner
    """  # noqa: E501

    address_regex: Optional[StrictStr] = Field(default=None, alias="addressRegex")
    coin: Optional[StrictStr] = None
    deposit_desc: Optional[StrictStr] = Field(default=None, alias="depositDesc")
    deposit_enable: Optional[StrictBool] = Field(default=None, alias="depositEnable")
    is_default: Optional[StrictBool] = Field(default=None, alias="isDefault")
    memo_regex: Optional[StrictStr] = Field(default=None, alias="memoRegex")
    min_confirm: Optional[StrictInt] = Field(default=None, alias="minConfirm")
    name: Optional[StrictStr] = None
    network: Optional[StrictStr] = None
    special_tips: Optional[StrictStr] = Field(default=None, alias="specialTips")
    un_lock_confirm: Optional[StrictInt] = Field(default=None, alias="unLockConfirm")
    withdraw_desc: Optional[StrictStr] = Field(default=None, alias="withdrawDesc")
    withdraw_enable: Optional[StrictBool] = Field(default=None, alias="withdrawEnable")
    withdraw_fee: Optional[StrictStr] = Field(default=None, alias="withdrawFee")
    withdraw_integer_multiple: Optional[StrictStr] = Field(
        default=None, alias="withdrawIntegerMultiple"
    )
    withdraw_max: Optional[StrictStr] = Field(default=None, alias="withdrawMax")
    withdraw_min: Optional[StrictStr] = Field(default=None, alias="withdrawMin")
    withdraw_internal_min: Optional[StrictStr] = Field(
        default=None, alias="withdrawInternalMin"
    )
    same_address: Optional[StrictBool] = Field(default=None, alias="sameAddress")
    estimated_arrival_time: Optional[StrictInt] = Field(
        default=None, alias="estimatedArrivalTime"
    )
    busy: Optional[StrictBool] = None
    contract_address_url: Optional[StrictStr] = Field(
        default=None, alias="contractAddressUrl"
    )
    contract_address: Optional[StrictStr] = Field(default=None, alias="contractAddress")
    deposit_all_enable: Optional[StrictBool] = Field(
        default=None, alias="depositAllEnable"
    )
    withdraw_all_enable: Optional[StrictBool] = Field(
        default=None, alias="withdrawAllEnable"
    )
    free: Optional[StrictStr] = None
    locked: Optional[StrictStr] = None
    freeze: Optional[StrictStr] = None
    withdrawing: Optional[StrictStr] = None
    ipoing: Optional[StrictStr] = None
    ipoable: Optional[StrictStr] = None
    storage: Optional[StrictStr] = None
    is_legal_money: Optional[StrictBool] = Field(default=None, alias="isLegalMoney")
    trading: Optional[StrictBool] = None
    network_list: Optional[
        List[AllCoinsInformationResponseInnerNetworkListInnerNetworkListInner]
    ] = Field(default=None, alias="networkList")
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = [
        "addressRegex",
        "coin",
        "depositDesc",
        "depositEnable",
        "isDefault",
        "memoRegex",
        "minConfirm",
        "name",
        "network",
        "specialTips",
        "unLockConfirm",
        "withdrawDesc",
        "withdrawEnable",
        "withdrawFee",
        "withdrawIntegerMultiple",
        "withdrawMax",
        "withdrawMin",
        "withdrawInternalMin",
        "sameAddress",
        "estimatedArrivalTime",
        "busy",
        "contractAddressUrl",
        "contractAddress",
        "depositAllEnable",
        "withdrawAllEnable",
        "free",
        "locked",
        "freeze",
        "withdrawing",
        "ipoing",
        "ipoable",
        "storage",
        "isLegalMoney",
        "trading",
        "networkList",
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
        """Create an instance of AllCoinsInformationResponseInnerNetworkListInner from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in network_list (list)
        _items = []
        if self.network_list:
            for _item_network_list in self.network_list:
                if _item_network_list:
                    _items.append(_item_network_list.to_dict())
            _dict["networkList"] = _items
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of AllCoinsInformationResponseInnerNetworkListInner from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "addressRegex": obj.get("addressRegex"),
                "coin": obj.get("coin"),
                "depositDesc": obj.get("depositDesc"),
                "depositEnable": obj.get("depositEnable"),
                "isDefault": obj.get("isDefault"),
                "memoRegex": obj.get("memoRegex"),
                "minConfirm": obj.get("minConfirm"),
                "name": obj.get("name"),
                "network": obj.get("network"),
                "specialTips": obj.get("specialTips"),
                "unLockConfirm": obj.get("unLockConfirm"),
                "withdrawDesc": obj.get("withdrawDesc"),
                "withdrawEnable": obj.get("withdrawEnable"),
                "withdrawFee": obj.get("withdrawFee"),
                "withdrawIntegerMultiple": obj.get("withdrawIntegerMultiple"),
                "withdrawMax": obj.get("withdrawMax"),
                "withdrawMin": obj.get("withdrawMin"),
                "withdrawInternalMin": obj.get("withdrawInternalMin"),
                "sameAddress": obj.get("sameAddress"),
                "estimatedArrivalTime": obj.get("estimatedArrivalTime"),
                "busy": obj.get("busy"),
                "contractAddressUrl": obj.get("contractAddressUrl"),
                "contractAddress": obj.get("contractAddress"),
                "depositAllEnable": obj.get("depositAllEnable"),
                "withdrawAllEnable": obj.get("withdrawAllEnable"),
                "free": obj.get("free"),
                "locked": obj.get("locked"),
                "freeze": obj.get("freeze"),
                "withdrawing": obj.get("withdrawing"),
                "ipoing": obj.get("ipoing"),
                "ipoable": obj.get("ipoable"),
                "storage": obj.get("storage"),
                "isLegalMoney": obj.get("isLegalMoney"),
                "trading": obj.get("trading"),
                "networkList": (
                    [
                        AllCoinsInformationResponseInnerNetworkListInnerNetworkListInner.from_dict(
                            _item
                        )
                        for _item in obj["networkList"]
                    ]
                    if obj.get("networkList") is not None
                    else None
                ),
            }
        )
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj
