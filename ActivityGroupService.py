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


class StatementValueStr():
    xsi_type: str
    value: str


class StatementValue():
    key: str
    value: StatementValueStr


class Statement(ad_manager.FilterStatement):
    ...


Statement("")
ad_manager.FilterStatement()


class ActivityGroupPage():
    totalResultSetSize: int
    startIndex: int
    results: ActivityGroups


class ActivityGroupService():
    def createActivityGroups(
        self, activityGroups: ActivityGroups) -> ActivityGroups: ...

    def getActivityGroupsByStatement(Statement) -> ActivityGroupPage: ...

    def updateActivityGroups(
        self, activityGroups: ActivityGroups) -> ActivityGroups: ...
