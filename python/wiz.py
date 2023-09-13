import json

test = "testo di prova"

with open("" + "wiz.json","w") as outfile:
  json.dump(test,outfile,indent=2)
  outfile.write('\n')
