import json

data = []
with open('actors.txt', 'r') as f:
	for line in f:
		d = {}
		d["value"] = line[:-1]
		d["label"] = line[:-1]
		data.append(d)
		print d
	with open("actors.json", "w") as outfile:
		json.dump(data, outfile)

# delete last comma
# data[ - 1 ] = data[ - 1 ][:-2]

# outfile = 'actos.json'