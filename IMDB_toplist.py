import requests, re

r = requests.get("http://www.imdb.com/chart/top")
if r.raise_for_status() != None:
	print("Die Seite kann nicht erreicht werden, verbinden sie sich mit dem Interent!")
	exit()
#print(r.text)

nameReg = re.compile(r'title=".* \(dir.\), .*, .* >(.*)</a>')
names = nameReg.findall(r.text)
for objekt in names:
	print(objekt)