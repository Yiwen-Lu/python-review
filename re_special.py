import re

# "\d" - digit; "\s" - whitespace; "\w" - word char;
# "\D" - NOT digit; "\S" - NOT whitespace; "\W" - NOT word char:
pattern = r"(\D+\d)"

if re.match(pattern, "Hi 999!"):
	print("Match Hi 999!")

if not re.match(pattern, "1, 23, 456!"):
	print("NOT Match 1, 23, 456!") # not found

if not re.match(pattern, "1,23,456!"):
	print("NOT Match 1,23,456!") # not found

if not re.match(pattern, "1 23 456!"):
	print("NOT Match 1 23 456!") # not found

if not re.match(pattern, "! $?"):
	print("NOT Match ! $?") # not found

if re.search(pattern, "Hi 999!"):
	print("Match Hi 999!")

if re.search(pattern, "1, 23, 456!"):
	print("Match 1, 23, 456!")

if re.search(pattern, "1,23,456!"):
	print("Match 1,23,456!")

if re.search(pattern, "1 23 456!"):
	print("Match 1 23 456!")

if not re.search(pattern, "! $?"):
	print("NOT Match ! $?") # not found


pattern = r"(\d+\W)+"
if re.match(pattern, "123!456!"):
	print("Match (\\d+\\W)+")

pattern = r"[1-6!]"
if re.match(pattern, "123!456!"):
	print("Match [1-6!]")

pattern = r"(\D+\s?)+"
if not re.match(pattern, "123!456!"):
	print("NOT Match (\\D+\\s?)+")  # not found


# "\A" - start with a string; "\Z" - end with a string;
# "\b" - exist boundary between words; "\B" - empty string anywhere else:
pattern = r"\b(cat)\b"

if re.search(pattern, "The cat sat!"):
	print("Match The cat sat!")

if re.search(pattern, "We s>cat<tered?"):
	print("Match We s>cat<tered?")

if not re.search(pattern, "We scattered."):
	print("NOT Match We scattered.") # not found


pattern = r"\ASPAM\Z"
if not re.search(pattern, "SPAM!"):
	print("NOT Match \\ASPAM\\Z") # not found

pattern = r"SP\AM!\Z"
if not re.search(pattern, "SPAM!"):
	print("NOT Match SP\\AM!\\Z") # not found

pattern = r"\AS...\b.\Z"
if re.search(pattern, "SPAM!"):
	print("Match \\AS...\\b.\\Z")