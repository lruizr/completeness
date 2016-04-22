#!bin/python
import random
import math
import pdb

#pdb.set_trace()

def newAngle():
	for key in angles.keys():
		num = random.uniform(0,1) * 2 * math.pi
		angles[key] = num
		#print angle[key]
	for key in cosenes.keys():
		cosenes[key] = math.cos(angles[key])
		if key in nodo1.keys():
			if cosenes[key] >= 0:
				nodo1[key] = 0
			else:
				nodo1[key] = 1
			#print nodo1[key]
		if key in nodo2.keys():
			if cosenes[key] >= 0:
				nodo2[key] = 0
			else:
				nodo2[key] = 1
			#print nodo2[key]
		if key in nodo3.keys():
			if cosenes[key] >= 0:
				nodo3[key] = 0
			else:
				nodo3[key] = 1
			#print nodo3[key]
		if key in nodo4.keys():
			if cosenes[key] >= 0:
				nodo4[key] = 0
			else:
				nodo4[key] = 1
			#print nodo4[key]

	actives = [nodo1["x12"], nodo1["x13"], nodo2["x23"], nodo2["x24"], nodo3["x34"]]
	nodo1["output"] = [nodo1["x12"], nodo1["x13"]]
	nodo2["input"] = [nodo1["x12"]]
	nodo2["output"] = [nodo2["x23"], nodo2["x24"]]
	nodo3["input"] = [nodo3["x13"], nodo3["x23"]]
	nodo3["output"] = [nodo3["x34"]]
	nodo4["input"] = [nodo4["x24"], nodo4["x34"]]
	#print actives
	#print cosenes
	#print nodo1
	#print nodo2
	#print nodo3
	#print nodo4

def estimateH(distances_list, actives,  nodo1, nodo2, nodo3, nodo4):
	value1 = sum(nodo1["output"]) - 1
	value2 = sum(nodo2["output"]) - sum(nodo2["input"])
	value3 = sum(nodo3["output"]) - sum(nodo3["input"])
	value4 = sum(nodo4["input"]) - 1
	addition = 0
	for active, distance in zip(actives, distances_list):
		addition += active*distance
	return addition + math.pow(value1, 2) + math.pow(value2, 2) + \
			math.pow(value3, 2) + math.pow(value4, 2)

def accept(iter):
	num = random.uniform(0,1)
	prob = math.exp(-iter/total)
	if num > prob:
		return True
	else:
		return False

def check():
	# Comprobar que los nodos son diferentes de 0 (una de las salidas y una de las entradas es distinta de 0)
	if sum(nodo1["output"]) in [0,1] and sum(nodo2["input"]) in [0,1] and sum(nodo2["output"]) in [0,1] and sum(nodo3["input"]) in [0,1] and sum(nodo3["output"]) in [0,1] and \
		sum(nodo4["input"]) in [0,1] and (nodo1["x12"] + nodo1["x13"] - 1) >= 0 and (nodo2["x12"] - nodo2["x23"] - nodo2["x24"]) >= 0 and \
		(nodo3["x13"] + nodo3["x23"] - nodo3["x34"]) >= 0 and (nodo4["x24"] + nodo4["x34"] - 1) >= 0:
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
		"input": [0], # x12
		"output": [0, 0]} # x23, x24
nodo3 = {"x13": 0,
		"x23": 0,
		"x34": 0,
		"input": [0, 0], # x13, x23
		"output": [0]} # x34
nodo4 = {"x24": 0,
		"x34": 0,
		"input": [0, 0], # x24, x34
		"output": []}
distances_list = [15, 10, 5, 20, 4] #x12, x13, x23, x24, x34
actives = []
for i in nodo1["output"]:
	actives.append(i)
for i in nodo2["output"]:
	actives.append(i)
for i in nodo3["output"]:
	actives.append(i)
for i in nodo4["output"]:
	actives.append(i)
distances = {"x12": 15,
			"x13": 10,
			"x23": 5,
			"x24": 20,
			"x34": 4}
angles = {"x12": 0,
		 "x13": 0,
		 "x23": 0,
		 "x24": 0,
		 "x34": 0}
cosenes = {"x12": 0,
		 "x13": 0,
		 "x23": 0,
		 "x24": 0,
		 "x34": 0}
prev_h = 30
total = 100000
current_h = 0

# Empieza la iteracion
for i in range(total):
	newAngle()
	while not check():
		newAngle()

	current_h = estimateH(distances_list, actives,  nodo1, nodo2, nodo3, nodo4)
	if current_h < prev_h:
		if check():
			prev_h = current_h
	else:
		if accept(i):
			if check():
				prev_h = current_h

# for key in angles.keys():
# 	print angles[key]

print angles
print cosenes