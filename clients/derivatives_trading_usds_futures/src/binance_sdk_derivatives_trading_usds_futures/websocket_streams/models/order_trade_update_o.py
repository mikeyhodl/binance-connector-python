# coding: utf-8

"""
Binance Derivatives Trading USDS Futures WebSocket Market Streams

OpenAPI Specification for the Binance Derivatives Trading USDS Futures WebSocket Market Streams
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
from typing import Set
from typing_extensions import Self


class OrderTradeUpdateO(BaseModel):
    """
    OrderTradeUpdateO
    """  # noqa: E501

    s: Optional[StrictStr] = None
    c: Optional[StrictStr] = None
    s: Optional[StrictStr] = Field(default=None, alias="S")
    o: Optional[StrictStr] = None
    f: Optional[StrictStr] = None
    q: Optional[StrictStr] = None
    p: Optional[StrictStr] = None
    ap: Optional[StrictStr] = None
    sp: Optional[StrictStr] = None
    x: Optional[StrictStr] = None
    x: Optional[StrictStr] = Field(default=None, alias="X")
    i: Optional[StrictInt] = None
    l: Optional[StrictStr] = None
    z: Optional[StrictStr] = None
    l: Optional[StrictStr] = Field(default=None, alias="L")
    n: Optional[StrictStr] = Field(default=None, alias="N")
    n: Optional[StrictStr] = None
    t: Optional[StrictInt] = Field(default=None, alias="T")
    t: Optional[StrictInt] = None
    b: Optional[StrictStr] = None
    a: Optional[StrictStr] = None
    m: Optional[StrictBool] = None
    r: Optional[StrictBool] = Field(default=None, alias="R")
    wt: Optional[StrictStr] = None
    ot: Optional[StrictStr] = None
    ps: Optional[StrictStr] = None
    cp: Optional[StrictBool] = None
    ap: Optional[StrictStr] = Field(default=None, alias="AP")
    cr: Optional[StrictStr] = None
    p_p: Optional[StrictBool] = Field(default=None, alias="pP")
    si: Optional[StrictInt] = None
    ss: Optional[StrictInt] = None
    rp: Optional[StrictStr] = None
    v: Optional[StrictStr] = Field(default=None, alias="V")
    pm: Optional[StrictStr] = None
    gtd: Optional[StrictInt] = None
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = [
        "s",
        "c",
        "S",
        "o",
        "f",
        "q",
        "p",
        "ap",
        "sp",
        "x",
        "X",
        "i",
        "l",
        "z",
        "L",
        "N",
        "n",
        "T",
        "t",
        "b",
        "a",
        "m",
        "R",
        "wt",
        "ot",
        "ps",
        "cp",
        "AP",
        "cr",
        "pP",
        "si",
        "ss",
        "rp",
        "V",
        "pm",
        "gtd",
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
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of OrderTradeUpdateO from a JSON string"""
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
        """Create an instance of OrderTradeUpdateO from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "s": obj.get("s"),
                "c": obj.get("c"),
                "S": obj.get("S"),
                "o": obj.get("o"),
                "f": obj.get("f"),
                "q": obj.get("q"),
                "p": obj.get("p"),
                "ap": obj.get("ap"),
                "sp": obj.get("sp"),
                "x": obj.get("x"),
                "X": obj.get("X"),
                "i": obj.get("i"),
                "l": obj.get("l"),
                "z": obj.get("z"),
                "L": obj.get("L"),
                "N": obj.get("N"),
                "n": obj.get("n"),
                "T": obj.get("T"),
                "t": obj.get("t"),
                "b": obj.get("b"),
                "a": obj.get("a"),
                "m": obj.get("m"),
                "R": obj.get("R"),
                "wt": obj.get("wt"),
                "ot": obj.get("ot"),
                "ps": obj.get("ps"),
                "cp": obj.get("cp"),
                "AP": obj.get("AP"),
                "cr": obj.get("cr"),
                "pP": obj.get("pP"),
                "si": obj.get("si"),
                "ss": obj.get("ss"),
                "rp": obj.get("rp"),
                "V": obj.get("V"),
                "pm": obj.get("pm"),
                "gtd": obj.get("gtd"),
            }
        )
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj
