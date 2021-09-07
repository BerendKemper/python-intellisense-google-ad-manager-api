from typing import Optional, overload
from googleads import ad_manager
if (__name__ == "__main__"):
    from Global import DateTime
else:
    from .Global import DateTime


EnvironmentType = """BROWSER, VIDEO_PLAYER"""
AdType = """TEXT, IMAGE, TEXT_AND_IMAGE"""
BorderStyle = """DEFAULT, NOT_ROUNDED, SLIGHTLY_ROUNDED, VERY_ROUNDED"""
FontFamily = """DEFAULT, ARIAL, TAHOMA, GEORGIA, TIMES, VERDANA"""
FontSize = """DEFAULT, SMALL, MEDIUM, LARGE"""
TimeUnit = """MINUTE, HOUR, DAY, WEEK, MONTH, LIFETIME, POD, STREAM, UNKNOWN"""
TargetWindow = """TOP, BLANK"""
InventoryStatus = """ACTIVE, INACTIVE, ARCHIVED"""
ValueSourceType = """PARENT, DIRECTLY_SPECIFIED, UNKNOWN"""
SmartSizeMode = """UNKNOWN, NONE, SMART_BANNER, DYNAMIC_SIZE"""


class AdUnitParent():
    id: str
    name: str
    adUnitCode: str


class Size():
    width: int
    heigth: int
    isAspectRatio: bool


class AdUnitSize():
    size: list[Size]
    environmentType: EnvironmentType
    companions: list[Optional['AdUnitSize']]
    fullDisplayString: str
    isAudio: bool


class AdSenseSettings ():
    adSenseEnabled: str
    borderColor: str
    titleColor: str
    backgroundColor: str
    textColor: str
    urlColor: str
    adType: AdType
    borderStyle: BorderStyle
    fontFamily: FontFamily
    fontSize: FontSize


class FrequencyCap():
    maxImpressions: int
    numTimeUnits: int
    timeUnit: TimeUnit


class LabelFrequencyCap():
    frequencyCap: FrequencyCap
    labelId: int


class AppliedLabel():
    labelId: str
    isNegated: bool


class AdUnit():
    id: str
    parentId: str
    hasChildren: bool
    parentPath: list[AdUnitParent]
    name: str
    description: str
    targetWindow: TargetWindow
    status: InventoryStatus
    adUnitCode: str
    adUnitSizes: list[AdUnitSize]
    isInterstitial: bool
    isNative: bool
    isFluid: bool
    explicitlyTargeted: bool
    adSenseSettings: AdSenseSettings
    adSenseSettingsSource: ValueSourceType
    appliedLabelFrequencyCaps: list[LabelFrequencyCap]
    effectiveLabelFrequencyCaps: list[LabelFrequencyCap]
    appliedLabels: list[AppliedLabel]
    effectiveAppliedLabels: list[AppliedLabel]
    effectiveTeamIds: list[int]
    appliedTeamIds: list[int]
    lastModifiedDateTime: DateTime
    smartSizeMode: SmartSizeMode
    refreshRate: int
    externalSetTopBoxChannelId: str
    isSetTopBoxEnabled: bool


AdUnits = list[AdUnit]


class Statement(ad_manager.FilterStatement):
    ...


class AdUnitPage():
    totalResultSetSize: int
    startIndex: int
    results: list[AdUnit]


class UpdateResult():
    numChanges: int


class InventoryService():
    def createAdUnits(AdUnits: list[AdUnit]) -> AdUnits: ...

    @overload
    def getAdUnitSizesByStatement(self, filterStatement=Statement(
        'WHERE adUnitCode = :adUnitCode')) -> AdUnitPage: ...

    @overload
    def getAdUnitSizesByStatement(self, filterStatement=Statement(
        'WHERE id = :id')) -> AdUnitPage: ...

    @overload
    def getAdUnitSizesByStatement(self, filterStatement=Statement(
        'WHERE name = :name')) -> AdUnitPage: ...

    @overload
    def getAdUnitSizesByStatement(self, filterStatement=Statement(
        'WHERE status = :status')) -> AdUnitPage: ...

    @overload
    def getAdUnitSizesByStatement(self, filterStatement=Statement(
        'WHERE lastModifiedDateTime = :lastModifiedDateTime')) -> AdUnitPage: ...

    @overload
    def getAdUnitsByStatement(self, filterStatement=Statement(
        'WHERE adUnitCode = :adUnitCode')) -> AdUnitPage: ...

    @overload
    def getAdUnitsByStatement(self, filterStatement=Statement(
        'WHERE id = :id')) -> AdUnitPage: ...

    @overload
    def getAdUnitsByStatement(self, filterStatement=Statement(
        'WHERE name = :name')) -> AdUnitPage: ...

    @overload
    def getAdUnitsByStatement(self, filterStatement=Statement(
        'WHERE status = :status')) -> AdUnitPage: ...

    @overload
    def getAdUnitsByStatement(self,  filterStatement=Statement(
        'WHERE lastModifiedDateTime = :lastModifiedDateTime')) -> AdUnitPage: ...

    @overload
    def performAdUnitAction(self, adUnitAction, filterStatement=Statement(
        'WHERE adUnitCode = :adUnitCode')) -> UpdateResult: ...

    @overload
    def performAdUnitAction(self, adUnitAction, filterStatement=Statement(
        'WHERE id = :id')) -> UpdateResult: ...

    @overload
    def performAdUnitAction(self, adUnitAction, filterStatement=Statement(
        'WHERE name = :name')) -> UpdateResult: ...

    @overload
    def performAdUnitAction(self, adUnitAction, filterStatement=Statement(
        'WHERE status = :status')) -> UpdateResult: ...

    @overload
    def performAdUnitAction(self, adUnitAction, filterStatement=Statement(
        'WHERE lastModifiedDateTime = :lastModifiedDateTime')) -> UpdateResult: ...

    def updateAdUnits(AdUnits: AdUnits) -> AdUnits: ...
