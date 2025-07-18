# coding: utf-8

"""
Binance VIP Loan REST API

OpenAPI Specification for the Binance VIP Loan REST API
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
from typing import Set
from typing_extensions import Self


class GetVIPLoanOngoingOrdersResponseRowsInner(BaseModel):
    """
    GetVIPLoanOngoingOrdersResponseRowsInner
    """  # noqa: E501

    order_id: Optional[StrictInt] = Field(default=None, alias="orderId")
    loan_coin: Optional[StrictStr] = Field(default=None, alias="loanCoin")
    total_debt: Optional[StrictStr] = Field(default=None, alias="totalDebt")
    residual_interest: Optional[StrictStr] = Field(
        default=None, alias="residualInterest"
    )
    collateral_account_id: Optional[StrictStr] = Field(
        default=None, alias="collateralAccountId"
    )
    collateral_coin: Optional[StrictStr] = Field(default=None, alias="collateralCoin")
    total_collateral_value_after_haircut: Optional[StrictStr] = Field(
        default=None, alias="totalCollateralValueAfterHaircut"
    )
    locked_collateral_value: Optional[StrictStr] = Field(
        default=None, alias="lockedCollateralValue"
    )
    current_ltv: Optional[StrictStr] = Field(default=None, alias="currentLTV")
    expiration_time: Optional[StrictInt] = Field(default=None, alias="expirationTime")
    loan_date: Optional[StrictStr] = Field(default=None, alias="loanDate")
    loan_term: Optional[StrictStr] = Field(default=None, alias="loanTerm")
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = [
        "orderId",
        "loanCoin",
        "totalDebt",
        "residualInterest",
        "collateralAccountId",
        "collateralCoin",
        "totalCollateralValueAfterHaircut",
        "lockedCollateralValue",
        "currentLTV",
        "expirationTime",
        "loanDate",
        "loanTerm",
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
        """Create an instance of GetVIPLoanOngoingOrdersResponseRowsInner from a JSON string"""
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
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of GetVIPLoanOngoingOrdersResponseRowsInner from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "orderId": obj.get("orderId"),
                "loanCoin": obj.get("loanCoin"),
                "totalDebt": obj.get("totalDebt"),
                "residualInterest": obj.get("residualInterest"),
                "collateralAccountId": obj.get("collateralAccountId"),
                "collateralCoin": obj.get("collateralCoin"),
                "totalCollateralValueAfterHaircut": obj.get(
                    "totalCollateralValueAfterHaircut"
                ),
                "lockedCollateralValue": obj.get("lockedCollateralValue"),
                "currentLTV": obj.get("currentLTV"),
                "expirationTime": obj.get("expirationTime"),
                "loanDate": obj.get("loanDate"),
                "loanTerm": obj.get("loanTerm"),
            }
        )
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj
