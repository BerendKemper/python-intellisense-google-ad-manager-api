from typing import Optional, overload
from googleads import ad_manager
import typing

Status = """ACTIVE, INACTIVE"""


class ActivityGroup():
    id: int
    name: str
    companyIds: list[int]
    impressionsLookback: int
    clicksLookback: int
    status: Status


ActivityGroups = list[ActivityGroup]

where_id = """WHERE id = :id"""
where_name = """WHERE name = :name"""


class StatementValueStr():
    xsi_type: str
    value: str


class StatementValue():
    key: str
    value: StatementValueStr


class Statement(ad_manager.FilterStatement):
    @overload
    def __init__(self, where_clause='WHERE id = :id',
                 values=list[dict], limit=int, offset=int) -> ad_manager.FilterStatement: ...

    @overload
    def __init__(self, where_clause='WHERE name = :name',
                 values=list[int], limit=int, offset=int) -> ad_manager.FilterStatement: ...

    # @overload
    # def __init__(
    #     self, where_clause="WHERE impressionsLookback = :impressionsLookback", values=None): ...

    # @overload
    # def __init__(
    #     self, where_clause="WHERE clicksLookback = :clicksLookback", values=None): ...

    # @overload
    # def __init__(self, where_clause="WHERE status = :status", values=None): ...


Statement("")
ad_manager.FilterStatement()


class ActivityGroupPage():
    totalResultSetSize: int
    startIndex: int
    results: ActivityGroups


class ActivityGroupService():
    def createActivityGroups(
        activityGroups: ActivityGroups) -> ActivityGroups: ...

    def getActivityGroupsByStatement() -> ActivityGroupPage: ...

    def updateActivityGroups(
        activityGroups: ActivityGroups) -> ActivityGroups: ...

# ActivityGroupService.createActivityGroups([])
