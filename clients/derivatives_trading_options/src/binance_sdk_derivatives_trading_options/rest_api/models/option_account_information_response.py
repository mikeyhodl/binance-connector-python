# coding: utf-8

"""
Binance Derivatives Trading Options REST API

OpenAPI Specification for the Binance Derivatives Trading Options REST API
The version of the OpenAPI document: 1.0.0
Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from binance_sdk_derivatives_trading_options.rest_api.models.option_account_information_response_asset_inner import (
    OptionAccountInformationResponseAssetInner,
)
from binance_sdk_derivatives_trading_options.rest_api.models.option_account_information_response_greek_inner import (
    OptionAccountInformationResponseGreekInner,
)
from typing import Set
from typing_extensions import Self


class OptionAccountInformationResponse(BaseModel):
    """
    OptionAccountInformationResponse
    """  # noqa: E501

    asset: Optional[List[OptionAccountInformationResponseAssetInner]] = None
    greek: Optional[List[OptionAccountInformationResponseGreekInner]] = None
    time: Optional[StrictInt] = None
    risk_level: Optional[StrictStr] = Field(default=None, alias="riskLevel")
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = ["asset", "greek", "time", "riskLevel"]

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
        """Create an instance of OptionAccountInformationResponse from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in asset (list)
        _items = []
        if self.asset:
            for _item_asset in self.asset:
                if _item_asset:
                    _items.append(_item_asset.to_dict())
            _dict["asset"] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in greek (list)
        _items = []
        if self.greek:
            for _item_greek in self.greek:
                if _item_greek:
                    _items.append(_item_greek.to_dict())
            _dict["greek"] = _items
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of OptionAccountInformationResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "asset": (
                    [
                        OptionAccountInformationResponseAssetInner.from_dict(_item)
                        for _item in obj["asset"]
                    ]
                    if obj.get("asset") is not None
                    else None
                ),
                "greek": (
                    [
                        OptionAccountInformationResponseGreekInner.from_dict(_item)
                        for _item in obj["greek"]
                    ]
                    if obj.get("greek") is not None
                    else None
                ),
                "time": obj.get("time"),
                "riskLevel": obj.get("riskLevel"),
            }
        )
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj
