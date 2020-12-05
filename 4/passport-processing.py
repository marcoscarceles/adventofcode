import sys
import re
import logging

from functools import reduce

# logging.basicConfig(level=logging.DEBUG)

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

    @staticmethod
    def __numberInRange(string, rangeTup):
        start, end = rangeTup
        return string and string.isnumeric() and int(string) in range(start, end+1)

    def valid(self):
        valid = bool(self.validByr() and self.validYir() and self.validEyr() and self.validHgt() and self.validHcl() and self.validEcl() and self.validPid())
        logging.info("Passport %s is %s" % (vars(self), valid))
        return valid

    def validByr(self):
        valid = self.__numberInRange(self.byr, (1920, 2002))
        logging.debug("\tvalidByr: %s" % valid)
        return valid

    def validYir(self):
        valid = self.__numberInRange(self.iyr, (2010, 2020))
        logging.debug("\tvalidYir: %s" % valid)
        return valid

    def validEyr(self):
        valid = self.__numberInRange(self.eyr, (2020, 2030))
        logging.debug("\tvalidEyr: %s" % valid)
        return valid

    def validHgt(self):
        valid = False
        if self.hgt:
            numeric = re.match(r"\d+", self.hgt)
            if re.match(r"^\d+cm$", self.hgt):
                valid = self.__numberInRange(numeric[0], (150, 193))            
            elif re.match(r"^\d+in$", self.hgt):
                valid = self.__numberInRange(numeric[0], (59, 76))
        logging.debug("\tvalidHgt: %s" % valid)
        return valid

    def validHcl(self):
        valid = bool(self.hcl and re.match(r"^\#[0-9a-f]{6}$", self.hcl))
        logging.debug("\tvalidHcl: %s" % valid)
        return valid
    
    def validEcl(self):
        valid = self.ecl in ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth')
        logging.debug("\tvalidEcl: %s" % valid)
        return valid
    
    def validPid(self):
        valid = bool(self.pid and re.match(r"^\d{9}$", self.pid))
        logging.debug("\tvalidPid: %s" % valid)
        return valid

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