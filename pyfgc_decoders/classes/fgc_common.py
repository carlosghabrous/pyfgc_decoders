import struct

from pyfgc_const import FGC_STAT_PRECLASS_PAD

def decode_bitmask(result, field, bitmask):
    """Summary
    
    Args:
        result (TYPE): Description
        field (TYPE): Description
        bitmask (TYPE): Description
    """
    value = result[field]
    items = list()
    for k, v in bitmask.items():
        if v & value:
            items.append(k)

    result[field] = " ".join(items)


def decode(data):
    """Summary
    
    Args:
        data (TYPE): Description
    
    Returns:
        TYPE: Description
    """
    result = dict()
    
    result['raw'] = data
    
    # DATA_STATUS, CLASS_ID, reserved, and RUNLOG_BYTE
    unpack_string = ">BBBB"

    # reserved
    unpack_string += str(FGC_STAT_PRECLASS_PAD) + "s"

    # Other fields
    unpack_string += "H"
    unpack_string += "H"

    # Unpack data
    result['DATA_STATUS'], result['CLASS_ID'], _, result['RUNLOG_BYTE'], _, result['ST_FAULTS'], result['ST_WARNINGS'] = struct.unpack_from(unpack_string, data)

    # Decode DATA_STATUS bit mask
    bitmask = dict()

    bitmask['DEVICE_IN_DB'] = 0x00000001
    bitmask['DATA_VALID'] = 0x00000002
    bitmask['CLASS_VALID'] = 0x00000004

    decode_bitmask(result, 'DATA_STATUS', bitmask)

    return result
