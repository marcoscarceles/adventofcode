import sys
import re

import logging

logging.basicConfig(level=logging.DEBUG)

lowest = 999999999
highest = -1
sum = 0

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
    lowest = seatId if seatId < lowest else lowest
    sum += seatId

print(highest)
expected =  (highest)*(highest+1)/2 - (lowest)*(lowest-1)/2 # 1 2 3 | 4 5 6 
print(expected - sum)