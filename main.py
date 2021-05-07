with open('main.txt') as f:
    lines = f.readlines()
a = input("you want capital of which country: ").lower()

def lower_dict(d):
   new_dict = dict((k.lower(), v.lower()) for k, v in d.items())
   return new_dict
currencyDict = {}
for line in lines:
    parsed = line.split("\t")
    currencyDict[parsed[0]] = parsed[1]
    currencyDict = lower_dict(currencyDict)
try:
    print(currencyDict[a])
   except:
    raise Exception(f'''couldn't find capital for {a}''')

