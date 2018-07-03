from enum import Enum

class URL(Enum):
    TOWNWORK = {'TOKYO': 'tokyo','OSAKA':'osaka'}
    SHIFTJOB = 2

    # class TOWNWORK(Enum):
    #     TOKYO = 'tokyo'
    #     TOKYO23 = 'tokyo23'

print(URL.TOWNWORK.value['TOKYO'])
