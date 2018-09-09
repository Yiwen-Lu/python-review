import re

# "[\w\.-]+" -  one or more word character, dot or dash:
pattern = r"([\w\.-]+)@([\w\.-]+)(\.[\w\.]+)"
hint = "Please contact info@sololearn.com for assistance"

matched = re.search(pattern, hint)
if matched:
	print(matched.group())