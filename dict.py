#Python Dictionary

prefects = {"Jss1":["Helen Martin","David John","Gracelyn"], "Jss2":"Favour Gladys", "Jss3":"John Cowell"}
print(prefects["Jss1"][1])
print(prefects["Jss2"])
print(prefects.get("Jss1"))
prefects["SS1"] = "Gift Laws"

#dictionary of a list containing 2 tuples
d1 = dict([('a', 100), ('b', 200), ['c', 300]])
print(d1)
prefects.update(d1)
print(prefects)
print(prefects.items())
print(prefects.keys())

#looping through a dictionary
for x in prefects:
    print(prefects[x])
    
for x in prefects.items():
    print(x)
    
#nested dictionary
scores = {
    "Helen":{"Math":80,"Phy":90},
    "Frank":{"Math":50,"Phy":40},
    "victor":{"Math":77,"Phy":20}
}
print(scores["Frank"]["Math"])

#accessing the nested dictionaries with for loop
for k,v in scores.items():
    print(k,v)
