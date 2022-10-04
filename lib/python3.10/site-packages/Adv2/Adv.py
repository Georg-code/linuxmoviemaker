# The naming conventions follow those used in github.com/AstroDigitalVideo/ADVlib
# While not exactly 'Pythonic' (i.e., not snake case), it was my judgement (Bob Anderson) that
# fewer errors would be introduced and would reduce the intellectual 'load' of comparing
# the Python code against the equivalent code in github.com/AstroDigitalVideo/ADVlib

# This module holds all of the enums and structures that are defined
# in the C# file PInvoke.cs in the namespace Adv (equivalent to a Python module/file)

# We use type hinting so that it is easy to see the intent as matching the C++/C# code

from dataclasses import dataclass
from enum import Enum


class StreamId(Enum):
    Main = 0
    Calibration = 1


class Adv2TagType(Enum):
    Int8 = 0
    Int16 = 1
    Int32 = 2
    Int64 = 3
    Real = 4
    UTF8String = 5


class TagPairType(Enum):
    MainStream = 0
    CalibrationStream = 1
    SystemMetaData = 2
    UserMetaData = 3
    ImageSection = 4
    FirstImageLayout = 100


@dataclass
class AdvImageLayoutInfo:
    ImageLayoutId: int = 0
    ImageLayoutTagsCount: int = 0
    ImageLayoutBpp: int = 0
    IsFullImageRaw: bool = False
    Is12BitImagePacked: bool = False
    Is8BitColourPacked: bool = False


@dataclass
class AdvFileInfo:
    Width: int = 0
    Height: int = 0
    CountMainFrames: int = 0  # spelling change here --- is CountMaintFrames in C# code
    CountCalibrationFrames: int = 0
    DataBpp: int = 0
    MaxPixelValue: int = 0
    MainClockFrequency: int = 0
    MainStreamAccuracy: int = 0
    CalibrationClockFrequency: int = 0
    CalibrationStreamAccuracy: int = 0
    MainStreamTagsCount: int = 0
    CalibrationStreamTagsCount: int = 0
    SystemMetadataTagsCount: int = 0
    UserMetadataTagsCount: int = 0
    UtcTimestampAccuracyInNanoseconds: int = 0
    IsColourImage: bool = False
    ImageLayoutsCount: int = 0
    StatusTagsCount: int = 0
    ImageSectionTagsCount: int = 0
    ErrorStatusTagId: int = 0


@dataclass
class AdvIndexEntry:
    ElapsedTicks: int = 0
    FrameOffset: int = 0
    BytesCount: int = 0


@dataclass
class AdvFrameInfo:
    StartTicksLo: int = 0
    StartTicksHi: int = 0
    EndTicksLo: int = 0
    EndTicksHi: int = 0

    UtcMidExposureTimestampLo: int = 0
    UtcMidExposureTimestampHi: int = 0
    Exposure: int = 0

    DateString: str = ''                   # This a new item, not included in C# AdvFrameInfo
    StartOfExposureTimestampString = ''    # This a new item, not included in C# AdvFrameInfo

    Gamma: float = 0.0
    Gain: float = 0.0
    Shutter: float = 0.0
    Offset: float = 0.0

    GPSTrackedSatellites: int = 0  # Spelling correction for satellites applied here
    GPSAlmanacStatus: int = 0
    GPSFixStatus: int = 0
    GPSAlmanacOffset: int = 0

    VideoCameraFrameIdLo: int = 0
    VideoCameraFrameIdHi: int = 0
    HardwareTimerFrameIdLo: int = 0
    HardwareTimerFrameIdHi = 0

    SystemTimestampLo: int = 0
    SystemTimestampHi: int = 0

    ImageLayoutId = 0
    RawDataBlockSize = 0
