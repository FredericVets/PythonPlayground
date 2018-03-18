super_villains = {
    "Fiddler": "Isaac Bowin",
    "Captain Cold": "Leonard Snart",
    "Weather Wizard": "Mark Mardon",
    "Mirror Master": "Sam Scudder",
    "Pied Piper": "Thomas Peterson"
}
print(super_villains)
print(super_villains["Mirror Master"])

del super_villains["Fiddler"]
print(super_villains)

super_villains["Pied Piper"] = "Hartley Rathaway"
print(super_villains)

print("length : ", len(super_villains))
print(super_villains.get("Pied Piper"))
print(super_villains.keys())
print(super_villains.items())
print(super_villains.values())
