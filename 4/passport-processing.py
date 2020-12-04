import sys
import re

from functools import reduce

class Passport:
    """Passport Representation"""
    byr = None
    iyr = None
    eyr = None
    hgt = None
    hcl = None
    ecl = None
    pid = None
    cid = None

    def valid(self):
        return self.byr and self.iyr and self.hgt and self.hcl and self.ecl and self.pid
    
    def empty(self):
        return not self.byr and not self.iyr and not self.hgt and not self.hcl and not self.ecl and not self.pid and not self.cid

def readPassport(file):
    passport = Passport()
    while file:
        line = file.readline().strip()
        if line:
            for tokens in re.split(r'\s+', line):
                key, value = tokens.split(':')
                setattr(passport, key, value)
        else:
            break
    return None if passport.empty() else passport 


def readAll(file):
    passports = []
    while file:
        next = readPassport(file)
        if next:
            passports.append(next)
        else:
            break
    return passports

if len(sys.argv) != 2:
    sys.exit("Inpuit file expected")

filename = sys.argv[1]
with open(filename, 'r') as file:
    passports = readAll(file)
valid = reduce(lambda sofar, passport : sofar  + (1 if passport.valid() else 0), passports, 0)
print(valid)