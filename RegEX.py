import re
 
txt = "This rain in Spain"
x = re.search("^The.*Spain$",txt)
print(x)

y = re.findall("ai",txt)
print(y)

p = re.findall("Portugal",txt)
print(p)

s = re.search("\s",txt)
print(s)

ss = re.split("\s",txt)
print(ss)

text = "The rain in Spain"
xx = re.split("\s",text,1)
print(xx)

txt = "function replaces the matches with the text of your choice"


