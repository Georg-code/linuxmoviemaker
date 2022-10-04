# The naming conventions follow those used in github.com/AstroDigitalVideo/ADVlib
# While not exactly 'Pythonic' (i.e., not snake case), it was my judgement (Bob Anderson) that
# fewer errors would be introduced and would reduce the intellectual 'load' of comparing
# the Python code against the equivalent code in github.com/AstroDigitalVideo/ADVlib


# Define a Exception that we can throw that automatically identifies itself
# as coming from the Adv2reader package.
class AdvLibException(Exception):
    pass


S_OK = 0x00000000


def ResolveErrorMessage(AdvResult: int, kind: str = 'human') -> str:
    # The dictionary provides strings that match the enum name of the error,
    # but also a more human readable form.
    if AdvResult in error_dict.keys():
        if kind == 'human':
            return error_dict[AdvResult][1]
        else:
            return error_dict[AdvResult][0]
    else:
        return f'0x{AdvResult:08X} is not a defined AdvResult'


error_dict = {
    0x81000001: ['E_ADV_NOFILE',
                 'The file could not be found.'],
    0x81000002: ['E_ADV_IO_ERROR',
                 'An I/O error has occurred.'],
    0x81001001: ['E_ADV_STATUS_ENTRY_ALREADY_ADDED',
                 'This status TagId has been already added to the current frame.'],
    0x81001002: ['E_ADV_INVALID_STATUS_TAG_ID',
                 'Unknown status TagId'],
    0x81001003: ['E_ADV_INVALID_STATUS_TAG_TYPE',
                 'The type of the status TagId doesn''t match the currently called method.'],
    0x81001004: ['E_ADV_STATUS_TAG_NOT_FOUND_IN_FRAME',
                 'The requested status TagId is not present in the current frame.'],
    0x81001005: ['E_ADV_FRAME_STATUS_NOT_LOADED',
                 'No status has been loaded. Call GetFramePixels() first.'],
    0x81001006: ['E_ADV_FRAME_NOT_STARTED',
                 'Frame not started. Call BeginFrame() first.'],
    0x81001007: ['E_ADV_IMAGE_NOT_ADDED_TO_FRAME',
                 'No image has been added to the started frame.'],
    0x81001008: ['E_ADV_INVALID_STREAM_ID',
                 'Invalid StreamId. Must be 0 for MAIN or 1 for CALIBRATION.'],
    0x81001009: ['E_ADV_IMAGE_SECTION_UNDEFINED',
                 'No Image Section has been defined.'],
    0x8100100A: ['E_ADV_STATUS_SECTION_UNDEFINED',
                 'No Status Section has been defined.'],
    0x8100100B: ['E_ADV_IMAGE_LAYOUTS_UNDEFINED',
                 'Image layouts undefined'],
    0x8100100C: ['E_ADV_INVALID_IMAGE_LAYOUT_ID',
                 'Invalid image LayoutId.'],
    0x8100100D: ['E_ADV_CHANGE_NOT_ALLOWED_RIGHT_NOW',
                 'This change is not allowed on an existing file or once a frame insertion has started.'],
    0x8100100E: ['E_ADV_IMAGE_SECTION_ALREADY_DEFINED',
                 'The Image Section can be only defined once per file'],
    0x8100100F: ['E_ADV_STATUS_SECTION_ALREADY_DEFINED',
                 'The Status Section can be only defined once per file'],
    0x81001010: ['E_ADV_IMAGE_LAYOUT_ALREADY_DEFINED',
                 'An Image Layout with this LayoutId has been already defined.'],
    0x81001011: ['E_ADV_INVALID_IMAGE_LAYOUT_TYPE',
                 'Invalid Image Layout type.'
                 ' Accepted values are FULL-IMAGE-RAW, 12BIT-IMAGE-PACKED and 8BIT-COLOR-IMAGE.'],
    0x81001012: ['E_ADV_INVALID_IMAGE_LAYOUT_COMPRESSION',
                 'Invalid Image Layout compression. Accepted values are UNCOMPRESSED, LAGARITH16 and QUICKLZ.'],
    0x81001013: ['E_ADV_INVALID_IMAGE_LAYOUT_BPP',
                 'Invalid Image Layout bits per pixel value. Accepted range is from 1 to 32.'],
    0x81001014: ['E_ADV_FRAME_MISSING_FROM_INDEX',
                 'The requested frame cannot be located in the index.'
                 ' The file may be have been corrupted. Try rebuilding it.'],
    0x81001015: ['E_ADV_FRAME_CORRUPTED',
                 'The frame binary data appears to be corrupted.'],
    0x81001016: ['E_ADV_FILE_NOT_OPEN',
                 'File system file is not open.'],
    0x81002001: ['E_ADV_NOT_AN_ADV_FILE',
                 'This is not a valid ADV file.'],
    0x81002002: ['E_ADV_VERSION_NOT_SUPPORTED',
                 'ADV version not supported.'],
    0x81002003: ['E_ADV_NO_MAIN_STREAM',
                 "'MAIN' stream is missing."],
    0x81002004: ['E_ADV_NO_CALIBRATION_STREAM',
                 "'CALIBRATION' stream is missing."],
    0x81002005: ['E_ADV_TWO_SECTIONS_EXPECTED',
                 'ADV files must have two sections.'],
    0x81002006: ['E_ADV_NO_IMAGE_SECTION',
                 "First section must be 'IMAGE'."],
    0x81002007: ['E_ADV_NO_STATUS_SECTION',
                 "Second section must be 'STATUS'."],
    0x81002008: ['E_ADV_IMAGE_SECTION_VERSION_NOT_SUPPORTED',
                 "'IMAGE' section version is not supported."],
    0x81002009: ['E_ADV_IMAGE_LAYOUT_VERSION_NOT_SUPPORTED',
                 'Image Layout version is not supported.'],
    0x8100200A: ['E_ADV_STATUS_SECTION_VERSION_NOT_SUPPORTED',
                 "'STATUS' section version is not supported."],
    0x71000001: ['S_ADV_TAG_REPLACED',
                 'An existing tag with the same name has been replaced.'],
    0x80004005: ['E_FAIL',
                 'Error.'],
    0x80004001: ['E_NOTIMPL',
                 'Not Implemented'],
    0x00000000: ['S_OK',
                 'Success.'],
}
