import re

# "." - any char (incl. digit):
pattern = r"gr.y"

if re.match(pattern, "grey"):
	print("Match 1")

if re.match(pattern, "gray"):
	print("Match 2")

if re.match(pattern, "blue"):
	print("Match 3") # not found

if re.match(pattern, "gr3y"):
	print("Match 4")


# "^" - start with; "$" - end with:
pattern = r"^gr.y$"

if re.match(pattern, "grey"):
	print("Match 1")

if re.match(pattern, "gray"):
	print("Match 2")

if re.match(pattern, "blue"):
	print("Match 3") # not found

# "*" - zero or repetitions:
pattern = r"egg(spam)*"

if re.match(pattern, "eggspam"):
	print("Match 1")

if re.match(pattern, "eggspamspamegg"):
	print("Match 2")

if re.match(pattern, "spam"):
	print("Match 3") # not found

if re.match(pattern, "egg"):
	print("Match 4")


# "+" - one or repetitions:
pattern = r"g+"

if re.match(pattern, "g"):
	print("Match g")

if re.match(pattern, "gggggggggggggg"):
	print("Match 2")

if re.match(pattern, "abc"):
	print("Match 3") # not found


# "-" - zero or one:
pattern = r"ice(-)?cream"

if re.match(pattern, "icecream"):
	print("Match 1")

if re.match(pattern, "ice-cream"):
	print("Match 2")

if re.match(pattern, "ice--cream"):
	print("Match 3") # not found


# "{x,y}" - between x and y repetitions:
pattern = r"9{1,3}$"

if re.match(pattern, "9"):
	print("Match 1")

if re.match(pattern, "99"):
	print("Match 2")

if re.match(pattern, "999"):
	print("Match 3")

if re.match(pattern, "9999"):
	print("Match 4") # not found

if re.match(pattern, "99999"):
	print("Match 3") # not found


# "|" - or:
pattern = r"gr(e|a)y"

if re.match(pattern, "grey"):
	print("Match 1")

if re.match(pattern, "gray"):
	print("Match 2")

if re.match(pattern, "griy"):
	print("Match 3") # not found

if re.match(pattern, "blue"):
	print("Match 4") # not found