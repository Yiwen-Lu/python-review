import re

pattern = r"a(bc)(de)(f(g)h)i"
matched = re.match(pattern, "abcdefghijklmnop")

if matched:
	print(matched.group())
	print(matched.group(0))
	print(matched.group(1))
	print(matched.group(2))
	print(matched.group(3))
	print(matched.group(4))
	print(matched.groups())

pattern = r"1(23)(4(56)78)9(0)"
matched = re.match(pattern, "1234567890")

if matched:
	print(matched.group())
	print(matched.group(0))
	print(matched.group(1))
	print(matched.group(2))
	print(matched.group(3))
	print(matched.group(4))
	print(matched.groups())


# "(?P<name>...)" - group name; "(?:...)" - not group:
pattern = r"(?P<first>abc)(?:def)(ghi)"
matched = re.match(pattern, "abcdefghi")

if matched:
	print(matched.group())
	print(matched.group("first"))
	print(matched.groups())


# "\" + "1...99" - group repetitions:
pattern = r"(.+) \1"

if re.search(pattern, "abc abc"):
	print("Match 1")

if re.search(pattern, "abc abo"):
	print("Match 2") # not found

if re.search(pattern, "?! ?!"):
	print("Match 3")

if re.search(pattern, "?!?!"):
	print("Match 4") # not found


pattern = r"(.+)\1"

if re.search(pattern, "abcabc"):
	print("Match 1")

if re.search(pattern, "abcabo"):
	print("Match 2") # not found

if re.search(pattern, "?! ?!"):
	print("Match 3") # not found

if re.search(pattern, "?!?!"):
	print("Match 4")