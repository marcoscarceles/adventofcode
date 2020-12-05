import sys
import re

import logging

logging.basicConfig(level=logging.DEBUG)

highest = -1

for line in sys.stdin.readlines():
    line = line.strip()
    logging.debug("\tRead %s" % line)
    row, column = line[:7], line[7:]
    logging.debug("\tSplit: Column %s, Row %s" % (column, row))
    row = int(row.replace("F", "0").replace("B", "1"), 2)
    column = int(column.replace("L","0").replace("R","1"), 2)
    logging.debug("\tValue: Row %s, Column %s" % (row, column))

    seatId = row*8 + column
    logging.info("Seat ID %s", seatId)

    highest = seatId if seatId > highest else highest

print(highest)