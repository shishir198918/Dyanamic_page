import json
file=open("data/db.json","r+")
db=file.read()
file.seek(len(db)-1)
file.write(','+'{"title":"jason"}'+']')
print (db[-1])