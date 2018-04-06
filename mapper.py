#!/usr/bin/env python
"""mapper.py"""

import sys
import re

skip = 0

for line in sys.stdin:
 if skip == 1:
  line = line.strip()
  words = line.split(',')
  for word in words[-5:]:
   if word:
    print '%s\t%s' % (word, 1)
 skip = 1
