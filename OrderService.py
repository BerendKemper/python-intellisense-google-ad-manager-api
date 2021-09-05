from typing import Optional
if (__name__ == "__main__"):
    from GamGeneral import DateTime
else:
    from .GamGeneral import DateTime


OrderStatus = """DRAFT, PENDING_APPROVAL, APPROVED, DISAPPROVED, PAUSED, CANCELED, DELETED, UNKNOWN"""


class Money():
    currencyCode: str
    microAmount: int


class AppliedLabel():
    labelId: int
    isNegated: bool


class Order():
    id: int
    name: str
    startDateTime: DateTime
    endDateTime: DateTime
    unlimitedEndDateTime: bool
    status: OrderStatus
    isArchived: bool
    notes: str
    externalOrderId: int
    poNumber: str
    currencyCode: str
    advertiserId: int
    advertiserContactIds: list[int]
    agencyId: int
    agencyContactIds: list[int]
    creatorId: int
    traffickerId: int
    secondaryTraffickerIds: list[int]
    salespersonId: int
    secondarySalespersonIds: list[int]
    totalImpressionsDelivered: int
    totalClicksDelivered: int
    totalViewableImpressionsDelivered: int
    totalBudget: Money
    appliedLabels: list[AppliedLabel]
    effectiveAppliedLabels: list[AppliedLabel]
    lastModifiedByApp: str
    isProgrammatic: bool
    appliedTeamIds: list[int]
    lastModifiedDateTime: DateTime
    # customFieldValues: list[BaseCustomFieldValue] # https://developers.google.com/ad-manager/api/reference/v202105/OrderService.Order


class OrderService():
    def createOrders(orders: list[Order]) -> list[Order]: ...
