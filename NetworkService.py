from typing import Optional


DelegationType = """UNKNOWN, MANAGE_ACCOUNT, MANAGE_INVENTORY"""
DelegationStatus = """UNKNOWN, APPROVED, PENDING, REJECTED, WITHDRAWN"""
AccountStatus = """UNKNOWN, INVITED, DECLINED, PENDING_GOOGLE_APPROVAL, APPROVED, DISAPPROVED_POLICY_VIOLATION"""
DeclarationType = """NONE, DECLARED, UNKNOWN"""


class ChildPublisher():
    approvedDelegationType: DelegationType
    proposedDelegationType: DelegationType
    status: DelegationStatus
    accountStatus: AccountStatus
    childNetworkCode: str
    proposedRevenueShareMillipercent: int


class ThirdPartyDataDeclaration():
    declarationType: DeclarationType
    thirdPartyCompanyIds: list[int]


class Network():
    id: int
    displayName: str
    networkCode: str
    propertyCode: str
    timeZone: str
    currencyCode: str
    secondaryCurrencyCodes: list[str]
    effectiveRootAdUnitId: str
    isTest: bool
    childPublishers: list[ChildPublisher]


class NetworkService():
    def getAllNetworks() -> list[Network]: ...
    def getCurrentNetwork() -> Network: ...
    def getDefaultThirdPartyDataDeclaration() -> ThirdPartyDataDeclaration: ...
    def makeTestNetwork() -> Network: ...
    def updateNetwork(network: Network) -> Network: ...
