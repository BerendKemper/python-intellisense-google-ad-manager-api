
from typing import Optional
from googleads import ad_manager
if (__name__ == "__main__"):
    from GamGeneral import DateTime
else:
    from .GamGeneral import DateTime


class Enum():
    ...


EnvironmentType = """BROWSER, VIDEO_PLAYER"""
AdType = """TEXT, IMAGE, TEXT_AND_IMAGE"""
BorderStyle = """DEFAULT, NOT_ROUNDED, SLIGHTLY_ROUNDED, VERY_ROUNDED"""
FontFamily = """DEFAULT, ARIAL, TAHOMA, GEORGIA, TIMES, VERDANA"""
FontSize = """DEFAULT, SMALL, MEDIUM, LARGE"""
TimeUnit = """MINUTE, HOUR, DAY, WEEK, MONTH, LIFETIME, POD, STREAM, UNKNOWN"""
TargetWindow = """TOP, BLANK"""
InventoryStatus = """ACTIVE, INACTIVE, ARCHIVED"""
ValueSourceType = """PARENT, DIRECTLY_SPECIFIED, UNKNOWN"""
SmartSizeMode = """UNKNOWN, NONE, SMART_BANNER,DYNAMIC_SIZE"""


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


class String_ValueMapEntry():
    # don't know how to apply this into the Statement class yet
    adUnitCode: str
    id: str
    name: str
    parentId: str
    status: InventoryStatus
    lastModifiedDateTime: DateTime


class Statement(ad_manager.FilterStatement):
    ...


class AdUnitPage():
    totalResultSetSize: int
    startIndex: int
    results: list[AdUnit]


class UpdateResult():
    numChanges: int


class InventoryService():
    def createAdUnits(AdUnits: list[AdUnit]) -> list[AdUnit]: ...
    def getAdUnitSizesByStatement(Statement: Statement) -> AdUnitPage: ...
    def getAdUnitsByStatement() -> AdUnitPage: ...
    def performAdUnitAction() -> UpdateResult: ...
    def updateAdUnits(AdUnits: list[AdUnit]) -> list[AdUnit]: ...


# InventoryService().createAdUnits()[0].adUnitSizes[0].environmentType
