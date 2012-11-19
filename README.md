pwaudit
=======

Password statistics


Example output
--------------

	root@w00t:/usr/local/src/john-1.7.9-jumbo-5# ./pwaudit.py bla.txt

	Password length

	Count: 1        0.04 %  Length: 2
	Count: 4        0.16 %  Length: 3
	Count: 16       0.65 %  Length: 4
	Count: 22       0.89 %  Length: 5
	Count: 25       1.01 %  Length: 6
	Count: 36       1.46 %  Length: 7
	Count: 761      30.85 % Length: 8
	Count: 421      17.07 % Length: 9
	Count: 724      29.35 % Length: 10
	Count: 104      4.22 %  Length: 11
	Count: 285      11.55 % Length: 12
	Count: 29       1.18 %  Length: 13
	Count: 27       1.09 %  Length: 14
	Count: 6        0.24 %  Length: 15
	Count: 4        0.16 %  Length: 16
	Count: 2        0.08 %  Length: 17

	Regular expression matches

	Count: 1884     76.37 % Regex: LowUpAlphasDigits        Description: Lower/Upper-case Alphas followed by Digits
	Count: 10       0.41 %  Regex: LowUpAlphasDashDigits    Description: Lower/Upper-case Alphas followed by a Dash and Digits
	Count: 29       1.18 %  Regex: DigitsLowUpAlphas        Description: Digits followed by Lower/Upper-case Alphas





