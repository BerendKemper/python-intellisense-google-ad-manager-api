from typing import Optional, Literal
from googleads import ad_manager
from GamGeneral import DateTime


class Enumerations():
    EnvironmentType: Literal['BROWSER', 'VIDEO_PLAYER']
    AdType: Literal['TEXT', 'IMAGE', 'TEXT_AND_IMAGE']
    BorderStyle: Literal['DEFAULT', 'NOT_ROUNDED',
                         'SLIGHTLY_ROUNDED', 'VERY_ROUNDED']
    FontFamily: Literal['DEFAULT', 'ARIAL',
                        'TAHOMA', 'GEORGIA', 'TIMES', 'VERDANA']
    FontSize: Literal['DEFAULT', 'SMALL', 'MEDIUM', 'LARGE']
    TimeUnit: Literal['MINUTE', 'HOUR', 'DAY', 'WEEK',
                      'MONTH', 'LIFETIME', 'POD', 'STREAM', 'UNKNOWN']
    TargetWindow: Literal['TOP', 'BLANK']
    InventoryStatus: Literal['ACTIVE', 'INACTIVE', 'ARCHIVED']
    ValueSourceType:  Literal['PARENT', 'DIRECTLY_SPECIFIED', 'UNKNOWN']
    SmartSizeMode: Literal['UNKNOWN', 'NONE', 'SMART_BANNER', 'DYNAMIC_SIZE']


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
    environmentType: Enumerations.EnvironmentType
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
    adType: Enumerations.AdType
    borderStyle: Enumerations.BorderStyle
    fontFamily: Enumerations.FontFamily
    fontSize: Enumerations.FontSize


class FrequencyCap():
    maxImpressions: int
    numTimeUnits: int
    timeUnit: Enumerations.TimeUnit


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
    targetWindow: Enumerations.TargetWindow
    status: Enumerations.InventoryStatus
    adUnitCode: str
    adUnitSizes: list[AdUnitSize]
    isInterstitial: bool
    isNative: bool
    isFluid: bool
    explicitlyTargeted: bool
    adSenseSettings: AdSenseSettings
    adSenseSettingsSource: Enumerations.ValueSourceType
    appliedLabelFrequencyCaps: list[LabelFrequencyCap]
    effectiveLabelFrequencyCaps: list[LabelFrequencyCap]
    appliedLabels: list[AppliedLabel]
    effectiveAppliedLabels: list[AppliedLabel]
    effectiveTeamIds: list[int]
    appliedTeamIds: list[int]
    lastModifiedDateTime: DateTime
    smartSizeMode: Enumerations.SmartSizeMode
    refreshRate: int
    externalSetTopBoxChannelId: str
    isSetTopBoxEnabled: bool


class String_ValueMapEntry():
    # don't know how to apply this into the Statement class yet
    adUnitCode: str
    id: str
    name: str
    parentId: str
    status: Enumerations.InventoryStatus
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
