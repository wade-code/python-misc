#!/usr/bin/env python
# Modifed version of the SAR code found at https://stackoverflow.com/questions/64963170/how-to-do-arithmetic-right-shift-in-python-for-signed-and-unsigned-values
def sar8(x, m):
  if x & 0x80 != 0:
    filler = 0
    for i in range(m):
      filler |= 1 << 7-i
    x = (x >> m) | filler
    return x
  else:
    return x >> m


def sar16(x, m):
  if x & 0x8000 != 0:
    filler = 0
    for i in range(m):
      filler |= 1 << 15-i
    x = (x >> m) | filler
    return x
  else:
    return x >> m


def sar32(x, m):
  if x & 0x80000000 != 0:
    filler = 0
    for i in range(m):
      filler |= 1 << 31-i
    x = (x >> m) | filler
    return x
  else:
    return x >> m


def sar64(x, m):
  if x & 0x8000000000000000 != 0:
    filler = 0
    for i in range(m):
      filler |= 1 << 63-i
    x = (x >> m) | filler
    return x
  else:
    return x >> m
