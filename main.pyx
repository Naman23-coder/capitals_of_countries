with open('main.txt') as f:
    lines = f.readlines()
a = input("just test: ").lower()

def lower_dict(d):
   new_dict = dict((k.lower(), v.lower()) for k, v in d.items())
   return new_dict

currencyDict = {}
for line in lines:
    parsed = line.split("\t")
    currencyDict[parsed[0]] = parsed[1]
    currencyDict = lower_dict(currencyDict)
print(currencyDict[a])

