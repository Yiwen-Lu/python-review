import re

pattern = r"spam"

if re.match(pattern, "spamspamspam"):
	print("Match")
else:
	print("No match")

if re.match(pattern, "eggspamsausagespam"):
	print("Match")
else:
	print("No match")

if re.search(pattern, "eggspamsausagespam"):
	print("Match")
else:
	print("No match")

print(re.findall(pattern, "eggspamsausagespam"))

searched = re.search(pattern, "eggspamsausage")

if searched:
	print(searched.group())
	print(searched.start())
	print(searched.end())
	print(searched.span())