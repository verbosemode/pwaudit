#!/usr/bin/env python
#
# Example output:
#
#    root@w00t:/usr/local/src/john-1.7.9-jumbo-5# ./pwaudit.py bla.txt
#
#    Password length
#
#    Count: 1        0.04 %  Length: 2
#    Count: 4        0.16 %  Length: 3
#    Count: 16       0.65 %  Length: 4
#    Count: 22       0.89 %  Length: 5
#    Count: 25       1.01 %  Length: 6
#    Count: 36       1.46 %  Length: 7
#    Count: 761      30.85 % Length: 8
#    Count: 421      17.07 % Length: 9
#    Count: 724      29.35 % Length: 10
#    Count: 104      4.22 %  Length: 11
#    Count: 285      11.55 % Length: 12
#    Count: 29       1.18 %  Length: 13
#    Count: 27       1.09 %  Length: 14
#    Count: 6        0.24 %  Length: 15
#    Count: 4        0.16 %  Length: 16
#    Count: 2        0.08 %  Length: 17
#
#    Regular expression matches
#
#    Count: 1884     76.37 % Regex: LowUpAlphasDigits        Description: Lower/Upper-case Alphas followed by Digits
#    Count: 10       0.41 %  Regex: LowUpAlphasDashDigits    Description: Lower/Upper-case Alphas followed by a Dash and Digits
#    Count: 29       1.18 %  Regex: DigitsLowUpAlphas        Description: Digits followed by Lower/Upper-case Alphas
#
#
#
#

import sys
import re


class PasswordLength(object):
    def __init__(self):
        self.stats = {}
        self.passwordcount = 0

    def add_password(self, password):
        self.passwordcount += 1

        pwdlen = len(password)

        if not pwdlen in self.stats:
            self.stats[pwdlen] = 1
        else:
            self.stats[pwdlen] += 1

    def print_report(self):
        print "Password length\n"

        for k in self.stats:
            print "Count: %i\t%.2f %%\tLength: %i" % (self.stats[k], 100.0 / self.passwordcount * self.stats[k], k)


class PasswordRegexMatches(object):
    def __init__(self):
        self.stats = {}
        self.passwordcount = 0

    def add_rgx(self, regexname, regexpattern, regexdescr=None, regexignorecase=False):
        if regexignorecase == True:
            self.stats[regexname] = {'regexpattern': re.compile(regexpattern, re.I), 'regexdescr': regexdescr, 'count': 0}
        else:
            self.stats[regexname] = {'regexpattern': re.compile(regexpattern), 'regexdescr': regexdescr, 'count': 0}

    def add_password(self, password):
        self.passwordcount += 1

        for rgx in self.stats:
            r = self.stats[rgx]['regexpattern'].match(password)

            if r:
                self.stats[rgx]['count'] += 1

    def print_report(self):
        print "Regular expression matches\n"

        for rgx in self.stats:
            print "Count: %i\t%.2f %%\tRegex: %s\tDescription: %s" % (self.stats[rgx]['count'], 100.0 / self.passwordcount * self.stats[rgx]['count'], rgx, self.stats[rgx]['regexdescr'])


pwdlen = PasswordLength()
rgxmatch = PasswordRegexMatches()

rgxmatch.add_rgx('LowUpAlphasDigits', '^[a-zA-Z]+\d+$', 'Lower/Upper-case Alphas followed by Digits') 
rgxmatch.add_rgx('DigitsLowUpAlphas', '^\d+[a-zA-Z]+', 'Digits followed by Lower/Upper-case Alphas') 
rgxmatch.add_rgx('LowUpAlphasDashDigits', '^[a-zA-Z]+-\d+$', 'Lower/Upper-case Alphas followed by a Dash and Digits') 
#rgxmatch.add_rgx('Password', '.*(kennwort|passwort|password).*', 'Match the word password', regexignorecase=True)



f = file(sys.argv[1], "r")

for l in f:
    l = l.strip()

    pwdlen.add_password(l)
    rgxmatch.add_password(l)

f.close()

pwdlen.print_report()
print

rgxmatch.print_report()
print 

sys.exit(0)
