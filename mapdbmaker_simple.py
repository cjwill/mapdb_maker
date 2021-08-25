import os
import json

dir_name = input("Directory Name: ")
mod_name = input("Mod Name: ")

false = False
true = True

data = {}
data['episodes'] = []
data['episodes'].append({
      "dir": dir_name,
      "name": mod_name,
      "needsSkillSelect": false
})


data['maps'] = []


l = []
for file in os.listdir("maps"):
    if file.endswith((".bsp", ".BSP")):
        filename = file.split('.')
        name = filename[0]
        data['maps'].append({
              "title": name,
              "bsp": name,
              "episode": dir_name,
              "game": dir_name,
              "dm": true,
              "coop": true,
              "bots": false,
              "sp": true
        },)

with open('mapdb.json', 'w') as outfile:
    json.dump(data, outfile)
