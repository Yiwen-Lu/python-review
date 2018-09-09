import re

# "[]" - any one:
pattern = r"[aeiou]"

if re.search(pattern, "grey"):
	print("Match 1")

if re.search(pattern, "qwertyuiop"):
	print("Match 2")

if re.search(pattern, "rhythm myths"):
	print("Match 3") # not found

# "-" - from ... to ...:
pattern = r"[A-Z][A-Z][0-9]"

if re.search(pattern, "LS8"):
	print("Match 1")

if re.search(pattern, "E3"):
	print("Match 2") # not found

if re.search(pattern, "1ab"):
	print("Match 3") # not found

# "^" inside "[]" - invert:
pattern = r"[^A-Z]" # not entirely composed of uppercase letters:

if re.search(pattern, "this is all quiet"):
	print("Match 1")

if re.search(pattern, "thisisallquiet"):
	print("Match 2")

if re.search(pattern, "AbCdEfG123"):
	print("Match 3")

if re.search(pattern, "THISISALLSHOUTING"):
	print("Match 4") # not found

if re.search(pattern, "THIS IS ALL SHOUTING"):
	print("Match 5")