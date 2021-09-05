from typing import Optional, Literal


class Enumerations():
    DelegationType: Literal['UNKNOWN', 'MANAGE_ACCOUNT', 'MANAGE_INVENTORY']
    DelegationStatus: Literal['UNKNOWN', 'APPROVED',
                              'PENDING', 'REJECTED', 'WITHDRAWN']
    AccountStatus: Literal['UNKNOWN', 'INVITED',
                           'DECLINED', 'PENDING_GOOGLE_APPROVAL', 'APPROVED', 'DISAPPROVED_POLICY_VIOLATION', 'DISAPPROVED_DUPLICATE_ACCOUNT', 'EXPIRED', 'INACTIVE', 'DEACTIVATED_BY_AD_MANAGER']
    DeclarationType: Literal['NONE', 'DECLARED', 'UNKNOWN']


class ChildPublisher():
    approvedDelegationType: Enumerations.DelegationType
    proposedDelegationType: Enumerations.DelegationType
    status: Enumerations.DelegationStatus
    accountStatus: Enumerations.AccountStatus
    childNetworkCode: str
    proposedRevenueShareMillipercent: int


class ThirdPartyDataDeclaration():
    declarationType: Enumerations.DeclarationType
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
