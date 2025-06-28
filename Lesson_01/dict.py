band = {
    "name": "Band",
    "members": "Alice, Bob, Charlie",
     "genre": "Rock", 
} 

band2 = dict(vocals="Alice", guitar="Bob" )  

print(band["name"])
print(band2["vocals"])
print(type(band))
print(len(band))
print(band2.get("guitar"))
print("Alex" in band2)

band.update({"Rock": "Charlie"})
print(band)