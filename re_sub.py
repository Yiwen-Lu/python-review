import re

sent = "My name is David. Hi David."
pattern = r"David"
new_sent = re.sub(pattern, "Amy", sent)
print(new_sent)