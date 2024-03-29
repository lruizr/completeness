#!bin/python
import random
import math
import pdb

#pdb.set_trace()

def newAngle():
	for key in angles.keys():
		num = random.uniform(0,1) * 2 * math.pi
		angles[key] = num
	for key in cosenes.keys():
		cosenes[key] = math.cos(angles[key])
		if key in nodo1.keys():
			if cosenes[key] >= 0:
				nodo1[key] = 0
			else:
				nodo1[key] = 1
		if key in nodo2.keys():
			if cosenes[key] >= 0:
				nodo2[key] = 0
			else:
				nodo2[key] = 1
		if key in nodo3.keys():
			if cosenes[key] >= 0:
				nodo3[key] = 0
			else:
				nodo3[key] = 1
		if key in nodo4.keys():
			if cosenes[key] >= 0:
				nodo4[key] = 0
			else:
				nodo4[key] = 1
		if key in nodo5.keys():
			if cosenes[key] >= 0:
				nodo5[key] = 0
			else:
				nodo5[key] = 1
		if key in nodo6.keys():
			if cosenes[key] >= 0:
				nodo6[key] = 0
			else:
				nodo6[key] = 1
		if key in nodo7.keys():
			if cosenes[key] >= 0:
				nodo7[key] = 0
			else:
				nodo7[key] = 1
		if key in nodo8.keys():
			if cosenes[key] >= 0:
				nodo8[key] = 0
			else:
				nodo8[key] = 1
		if key in nodo9.keys():
			if cosenes[key] >= 0:
				nodo9[key] = 0
			else:
				nodo9[key] = 1
		if key in nodo10.keys():
			if cosenes[key] >= 0:
				nodo10[key] = 0
			else:
				nodo10[key] = 1
	

	actives = [nodo1["x12"], nodo1["x13"], nodo2["x23"], nodo2["x24"], nodo2["x25"], nodo3["x35"], nodo3["x36"], nodo4["x45"], nodo4["x47"], nodo4["x48"], \
			nodo5["x56"], nodo5["x57"], nodo5["x58"], nodo5["x59"], nodo6["x68"], nodo6["x69"], nodo7["x78"], nodo7["x710"], nodo8["x89"], nodo8["x810"], \
			nodo9["x910"]]

	nodo1["output"] = [nodo1["x12"], nodo1["x13"]]
	nodo2["input"] = [nodo1["x12"]]
	nodo2["output"] = [nodo2["x23"], nodo2["x24"], nodo2["x25"]]
	nodo3["input"] = [nodo3["x13"], nodo3["x23"]]
	nodo3["output"] = [nodo3["x35"], nodo3["x36"]]
	nodo4["input"] = [nodo4["x24"]]
	nodo4["output"] = [nodo4["x45"], nodo4["x47"], nodo4["x48"]]
	nodo5["input"] = [nodo5["x25"], nodo5["x35"], nodo5["x45"]]
	nodo5["output"] = [nodo5["x56"], nodo5["x57"], nodo5["x58"], nodo5["x59"]]
	nodo6["input"] = [nodo6["x36"], nodo6["x56"]]
	nodo6["output"] = [nodo6["x68"], nodo6["x69"]]
	nodo7["input"] = [nodo7["x47"], nodo7["x57"]]
	nodo7["output"] = [nodo7["x78"], nodo7["x710"]]
	nodo8["input"] = [nodo8["x48"], nodo8["x58"], nodo8["x68"], nodo8["x78"]]
	nodo8["output"] = [nodo8["x89"], nodo8["x810"]]
	nodo9["input"] = [nodo9["x59"], nodo9["x69"], nodo9["x89"]]
	nodo9["output"] = [nodo9["x910"]]
	nodo10["input"] = [nodo10["x710"], nodo10["x810"], nodo10["x910"]]


def estimateH(distances_list, actives,  nodo1, nodo2, nodo3, nodo4, nodo5, nodo6, nodo7, nodo8, nodo9, nodo10):
	value1 = sum(nodo1["output"]) - 1
	value2 = sum(nodo2["output"]) - sum(nodo2["input"])
	value3 = sum(nodo3["output"]) - sum(nodo3["input"])
	value4 = sum(nodo4["output"]) - sum(nodo4["input"])
	value5 = sum(nodo5["output"]) - sum(nodo5["input"])
	value6 = sum(nodo6["output"]) - sum(nodo6["input"])
	value7 = sum(nodo7["output"]) - sum(nodo7["input"])
	value8 = sum(nodo8["output"]) - sum(nodo8["input"])
	value9 = sum(nodo9["output"]) - sum(nodo9["input"])
	value10 = sum(nodo10["input"]) - 1
	addition = 0
	for active, distance in zip(actives, distances_list):
		addition += active*distance
	return addition + math.pow(value1, 2) + math.pow(value2, 2) + math.pow(value3, 2) + math.pow(value4, 2) + math.pow(value5, 2) +\
			math.pow(value6, 2) + math.pow(value7, 2) + math.pow(value8, 2) + math.pow(value9, 2) + math.pow(value10, 2)

def accept(iter):
	num = random.uniform(0,1)
	prob = math.exp(-iter/total)
	if num <= prob:
		return True
	else:
		return False

def check():
	# Comprobar que los nodos son diferentes de 0 (una de las salidas y una de las entradas es distinta de 0)
	if sum(nodo1["output"]) in [0,1] and sum(nodo2["input"]) in [0,1] and sum(nodo2["output"]) in [0,1] and sum(nodo3["input"]) in [0,1] and \
		sum(nodo3["output"]) in [0,1] and sum(nodo4["input"]) in [0,1] and sum(nodo4["output"]) in [0,1] and sum(nodo5["input"]) in [0,1] and \
		sum(nodo5["output"]) in [0,1] and sum(nodo6["input"]) in [0,1] and sum(nodo6["output"]) in [0,1] and sum(nodo7["input"]) in [0,1] and \
		sum(nodo7["output"]) in [0,1] and sum(nodo8["input"]) in [0,1] and sum(nodo8["input"]) in [0,1] and sum(nodo8["output"]) in [0,1] and \
		sum(nodo9["input"]) in [0,1] and sum(nodo9["output"]) in [0,1] and sum(nodo10["input"]) in [0,1] and (nodo1["x12"] + nodo1["x13"] - 1) >= 0 \
		and (nodo2["x12"] - nodo2["x23"] - nodo2["x24"] - nodo2["x25"]) >= 0 and (nodo3["x13"] + nodo3["x23"] - nodo3["x35"] - nodo3["x36"]) >= 0 and \
		(nodo4["x24"] - nodo4["x45"] - nodo4["x47"] - nodo4["x48"]) >= 0 and (nodo5["x25"] + nodo5["x35"] + nodo5["x45"] - nodo5["x56"] - nodo5["x57"] - \
		nodo5["x58"] - nodo5["x59"]) >= 0 and (nodo6["x36"] + nodo6["x56"] - nodo6["x68"] - nodo6["x69"]) >= 0 and (nodo7["x47"] + nodo7["x57"] - nodo7["x78"] - \
		nodo7["x710"]) >= 0 and (nodo8["x48"] + nodo8["x58"] + nodo8["x68"] + nodo8["x78"] - nodo8["x89"] - nodo8["x810"]) >= 0 and (nodo9["x59"] + nodo9["x69"] + \
		nodo9["x89"] - nodo9["x910"]) >= 0 and (nodo10["x710"] + nodo10["x810"] + nodo10["x910"]) >= 0:
		return True
	else:
		return False

# Main program

number_cities = 4
nodo1 = {"x12": 0,
		"x13": 0,
		"input": [], 
		"output": [0, 0]} # x12, x13
nodo2 = {"x12": 0,
		"x23": 0,
		"x24": 0,
		"x25": 0,
		"input": [0], # x12
		"output": [0, 0, 0]} # x23, x24, x25
nodo3 = {"x13": 0,
		"x23": 0,
		"x35": 0,
		"x36": 0,
		"input": [0, 0], # x13, x23
		"output": [0, 0]} # x35, x36
nodo4 = {"x24": 0,
		"x45": 0,
		"x47": 0,
		"x48": 0,
		"input": [0], # x24
		"output": [0, 0, 0]} # x45, x47, x48
nodo5 = {"x25": 0,
		"x35": 0,
		"x45": 0,
		"x56": 0,
		"x57": 0,
		"x58": 0,
		"x59": 0,
		"input": [0, 0, 0], #x25, x35, x45
		"output": [0, 0, 0, 0]} #x56, x57, x58, x59
nodo6 = {"x36": 0,
		"x56": 0,
		"x68": 0,
		"x69": 0,
		"input": [0, 0], # x36, x56
		"output": [0, 0]} # x68, x69
nodo7 = {"x47": 0,
		"x57": 0,
		"x78": 0,
		"x710": 0,
		"input": [0, 0], #x47, x57
		"output": [0, 0]} #x78, x710
nodo8 = {"x48": 0,
		"x58": 0,
		"x68": 0,
		"x78": 0,
		"x89": 0,
		"x810": 0,
		"input": [0, 0, 0, 0], # x48, x58, x68, x78
		"output": [0, 0]} # x89, x810
nodo9 = {"x59": 0,
		"x69": 0,
		"x89": 0,
		"x910": 0,
		"input": [0, 0, 0], # x59, x69. x89
		"output": [0]} # x910
nodo10 = {"x710": 0,
		"x810": 0,
		"x910": 0,
		"input": [0, 0, 0], # x710, x810, x910
		"output": []}
actives = []
for i in nodo1["output"]:
	actives.append(i)
for i in nodo2["output"]:
	actives.append(i)
for i in nodo3["output"]:
	actives.append(i)
for i in nodo4["output"]:
	actives.append(i)
for i in nodo5["output"]:
	actives.append(i)
for i in nodo6["output"]:
	actives.append(i)
for i in nodo7["output"]:
	actives.append(i)
for i in nodo8["output"]:
	actives.append(i)
for i in nodo9["output"]:
	actives.append(i)
for i in nodo10["output"]:
	actives.append(i)
distances = {"x12": 15,
			"x13": 10,
			"x23": 5,
			"x24": 12,
			"x25": 4,
			"x35": 7,
			"x36": 8,
			"x45": 6,
			"x47": 6,
			"x48": 7,
			"x56": 4,
			"x57": 3,
			"x58": 4,
			"x59": 6,
			"x68": 5,
			"x69": 4,
			"x78": 7,
			"x710": 8,
			"x89": 5,
			"x810": 3,
			"x910": 2}
distances_list = [] # All distances
keys = distances.keys()
keys.sort()
for key in keys:
	distances_list.append(distances[key])
angles = {"x12": 0,
		"x13": 0,
		"x23": 0,
		"x24": 0,
		"x25": 0,
		"x35": 0,
		"x36": 0,
		"x45": 0,
		"x47": 0,
		"x48": 0,
		"x56": 0,
		"x57": 0,
		"x58": 0,
		"x59": 0,
		"x68": 0,
		"x69": 0,
		"x78": 0,
		"x710": 0,
		"x89": 0,
		"x810": 0,
		"x910": 0}
cosenes = {"x12": 0,
		"x13": 0,
		"x23": 0,
		"x24": 0,
		"x25": 0,
		"x35": 0,
		"x36": 0,
		"x45": 0,
		"x47": 0,
		"x48": 0,
		"x56": 0,
		"x57": 0,
		"x58": 0,
		"x59": 0,
		"x68": 0,
		"x69": 0,
		"x78": 0,
		"x710": 0,
		"x89": 0,
		"x810": 0,
		"x910": 0}
prev_h = 100
total = 100000
current_h = 0

# Empieza la iteracion
for i in range(total):
	newAngle()
	while not check():
		newAngle()

	current_h = estimateH(distances_list, actives,  nodo1, nodo2, nodo3, nodo4, nodo5, nodo6, nodo7, nodo8, nodo9, nodo10)
	if current_h < prev_h:
		if check():
			prev_h = current_h
	else:
		if accept(i):
			if check():
				prev_h = current_h

#for key in angles.keys():
#	print angles[key]

print angles
print cosenes