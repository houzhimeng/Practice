import re
A = "<input type=\"hidden\" name=\"formhash\" value=\"8a3ffba2\"/>"
p = re.findall("formhash\" value=\"(.*)\"", A)
print(p)