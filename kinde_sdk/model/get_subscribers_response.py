# coding: utf-8

"""
    Kinde Management API

    Provides endpoints to manage your Kinde Businesses  # noqa: E501

    The version of the OpenAPI document: 1
    Contact: support@kinde.com
    Generated by: https://openapi-generator.tech
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from kinde_sdk import schemas  # noqa: F401


class GetSubscribersResponse(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        
        class properties:
            code = schemas.StrSchema
            message = schemas.StrSchema
            
            
            class subscribers(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['SubscribersSubscriber']:
                        return SubscribersSubscriber
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple['SubscribersSubscriber'], typing.List['SubscribersSubscriber']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'subscribers':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'SubscribersSubscriber':
                    return super().__getitem__(i)
            next_token = schemas.StrSchema
            __annotations__ = {
                "code": code,
                "message": message,
                "subscribers": subscribers,
                "next_token": next_token,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["code"]) -> MetaOapg.properties.code: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["message"]) -> MetaOapg.properties.message: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["subscribers"]) -> MetaOapg.properties.subscribers: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["next_token"]) -> MetaOapg.properties.next_token: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["code", "message", "subscribers", "next_token", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["code"]) -> typing.Union[MetaOapg.properties.code, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["message"]) -> typing.Union[MetaOapg.properties.message, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["subscribers"]) -> typing.Union[MetaOapg.properties.subscribers, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["next_token"]) -> typing.Union[MetaOapg.properties.next_token, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["code", "message", "subscribers", "next_token", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        code: typing.Union[MetaOapg.properties.code, str, schemas.Unset] = schemas.unset,
        message: typing.Union[MetaOapg.properties.message, str, schemas.Unset] = schemas.unset,
        subscribers: typing.Union[MetaOapg.properties.subscribers, list, tuple, schemas.Unset] = schemas.unset,
        next_token: typing.Union[MetaOapg.properties.next_token, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'GetSubscribersResponse':
        return super().__new__(
            cls,
            *_args,
            code=code,
            message=message,
            subscribers=subscribers,
            next_token=next_token,
            _configuration=_configuration,
            **kwargs,
        )

from kinde_sdk.model.subscribers_subscriber import SubscribersSubscriber
