# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import typing

from .field_condition import FieldCondition
from .has_id_condition import HasIdCondition
from .has_vector_condition import HasVectorCondition
from .is_empty_condition import IsEmptyCondition
from .is_null_condition import IsNullCondition

if typing.TYPE_CHECKING:
    from .filter import Filter
    from .filter_must_not_item import FilterMustNotItem
    from .nested_condition import NestedCondition
FilterMustNot = typing.Union[
    typing.List["FilterMustNotItem"],
    FieldCondition,
    IsEmptyCondition,
    IsNullCondition,
    HasIdCondition,
    HasVectorCondition,
    "NestedCondition",
    "Filter",
]
