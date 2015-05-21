#import xxhash
#x = xxhash.xxh64('alalao').hexdigest()
#print(x)

import time
import numpy as np
import cPickle
import random
import json
import itertools

start_time = time.time()

def initial_config():
    cube['front'] = np.array([[1 for x in range(3)] for x in range(3)])
    cube['left'] = np.array([[2 for x in range(3)] for x in range(3)])
    cube['rigth'] = np.array([[3 for x in range(3)] for x in range(3)])
    cube['up'] = np.array([[4 for x in range(3)] for x in range(3)])
    cube['back'] = np.array([[5 for x in range(3)] for x in range(3)])
    cube['down'] = np.array([[6 for x in range(3)] for x in range(3)])

def update_face(face):
    row1 = np.copy(cube[face][0,:])
    row3 = np.copy(cube[face][2,:])
    col1 = np.copy(cube[face][:,0])
    col3 = np.copy(cube[face][:,2])
    cube[face][:,2] = row1
    cube[face][2,:] = col3[::-1]
    cube[face][:,0] = row3
    cube[face][0,:] = col1[::-1]

def update_face_(face):
    row1 = np.copy(cube[face][0,:])
    row3 = np.copy(cube[face][2,:])
    col1 = np.copy(cube[face][:,0])
    col3 = np.copy(cube[face][:,2])
    cube[face][:,2] = row3[::-1]
    cube[face][2,:] = col1
    cube[face][:,0] = row1[::-1]
    cube[face][0,:] = col3

def front():
    update_face('front')
    #update other faces
    up = np.copy(cube['up'][2,:])
    rigth = np.copy(cube['rigth'][:,0])
    down = np.copy(cube['down'][0,:])
    left = np.copy(cube['left'][:,2])
    cube['up'][2,:] = left[::-1]
    cube['rigth'][:,0] = up
    cube['down'][0,:] = rigth[::-1]
    cube['left'][:,2] = down

def up():
    update_face('up')
    # update other faces
    back = np.copy(cube['back'][0,:])
    rigth = np.copy(cube['rigth'][0,:])
    front = np.copy(cube['front'][0,:])
    left = np.copy(cube['left'][0,:])
    cube['back'][0,:] = left
    cube['rigth'][0,:] = back
    cube['front'][0,:] = rigth
    cube['left'][0,:] = front

def back():
    update_face('back')
    # update other faces
    up = np.copy(cube['up'][0,:])
    left = np.copy(cube['left'][:,0])
    down = np.copy(cube['down'][2,:])
    rigth = np.copy(cube['rigth'][:,2])
    cube['up'][0,:] = rigth
    cube['left'][:,0] = up[::-1]
    cube['down'][2,:] = left
    cube['rigth'][:,2] = down[::-1]

def left():
    update_face('left')
    # update other faces
    up = np.copy(cube['up'][:,0])
    front = np.copy(cube['front'][:,0])
    down = np.copy(cube['down'][:,0])
    back = np.copy(cube['back'][:,2])
    cube['up'][:,0] = back[::-1]
    cube['front'][:,0] = up
    cube['down'][:,0] = front
    cube['back'][:,2] = down[::-1]

def rigth():
    update_face('rigth')
    # update other faces
    up = np.copy(cube['up'][:,2])
    back = np.copy(cube['back'][:,0])
    down = np.copy(cube['down'][:,2])
    front = np.copy(cube['front'][:,2])
    cube['up'][:,2] = front
    cube['back'][:,0] = up[::-1]
    cube['down'][:,2] = back[::-1]
    cube['front'][:,2] = down
    
def down():
    update_face('down')
    # update other faces
    front = np.copy(cube['front'][2,:])
    rigth = np.copy(cube['rigth'][2,:])
    back = np.copy(cube['back'][2,:])
    left = np.copy(cube['left'][2,:])
    cube['front'][2,:] = left
    cube['rigth'][2,:] = front
    cube['back'][2,:] = rigth
    cube['left'][2,:] = back
    
# reverse moves
def front_():
    update_face_('front')
    #update other faces
    up = np.copy(cube['up'][2,:])
    rigth = np.copy(cube['rigth'][:,0])
    down = np.copy(cube['down'][0,:])
    left = np.copy(cube['left'][:,2])
    cube['up'][2,:] = rigth
    cube['rigth'][:,0] = down[::-1]
    cube['down'][0,:] = left
    cube['left'][:,2] = up[::-1]

def up_():
    update_face_('up')
    # update other faces
    back = np.copy(cube['back'][0,:])
    rigth = np.copy(cube['rigth'][0,:])
    front = np.copy(cube['front'][0,:])
    left = np.copy(cube['left'][0,:])
    cube['back'][0,:] = rigth
    cube['rigth'][0,:] = front
    cube['front'][0,:] = left
    cube['left'][0,:] = back
    
def back_():
    update_face_('back')
    # update other faces
    up = np.copy(cube['up'][0,:])
    left = np.copy(cube['left'][:,0])
    down = np.copy(cube['down'][2,:])
    rigth = np.copy(cube['rigth'][:,2])
    cube['up'][0,:] = left[::-1]
    cube['left'][:,0] = down
    cube['down'][2,:] = rigth[::-1]
    cube['rigth'][:,2] = up
    
def left_():
    update_face_('left')
    # update other faces
    up = np.copy(cube['up'][:,0])
    front = np.copy(cube['front'][:,0])
    down = np.copy(cube['down'][:,0])
    back = np.copy(cube['back'][:,2])
    cube['up'][:,0] = front
    cube['front'][:,0] = down
    cube['down'][:,0] = back[::-1]
    cube['back'][:,2] = up[::-1]
    
def rigth_():
    update_face_('rigth')
    # update other faces
    up = np.copy(cube['up'][:,2])
    back = np.copy(cube['back'][:,0])
    down = np.copy(cube['down'][:,2])
    front = np.copy(cube['front'][:,2])
    cube['up'][:,2] = back[::-1]
    cube['back'][:,0] = down[::-1]
    cube['down'][:,2] = front
    cube['front'][:,2] = up

def down_():
    update_face_('down')
    # update other faces
    front = np.copy(cube['front'][2,:])
    rigth = np.copy(cube['rigth'][2,:])
    back = np.copy(cube['back'][2,:])
    left = np.copy(cube['left'][2,:])
    cube['front'][2,:] = rigth
    cube['rigth'][2,:] = back
    cube['back'][2,:] = left
    cube['left'][2,:] = front

def move(i):
    MOVE[i]()

def hash_node():
	permutation = ""
	json_string1 = json.dumps(cube['front'].tolist())
	json_string2 = json.dumps(cube['left'].tolist())
	json_string3 = json.dumps(cube['rigth'].tolist())
	json_string4 = json.dumps(cube['up'].tolist())
	json_string5 = json.dumps(cube['back'].tolist())
	json_string6 = json.dumps(cube['down'].tolist())
	permutation = json_string1 + json_string2 + json_string3 + json_string4 + json_string5 + json_string6
	h = hash(permutation)
	#h_cube[h] = cube
	return h

MOVE = {
    1 : front,
    -1 : front_,
    2 : up,
    -2 : up_,
    3 : back,
    -3 : back_,
    4 : left,
    -4 : left_,
    5 : rigth,
    -5 : rigth_,
    6 : down,
    -6 : down_
}

#h_cube = dict()
cube = dict()
initial_config()

neighbor = dict()

def visit_neighbors(node_id):
	visited = set()
	for i in range(1, 7):
		move(i)
		visited.add(hash_node())
		move(i*(-1))

		move(i*(-1))
		visited.add(hash_node())
		move(i)

	neighbor[node_id] = visited

def bfs(n):
	l = list(itertools.product(lista, repeat=n))
	for perm in l:
		for i in range(0,n):
			move(perm[i])

		node_id = hash_node()
		if(node_id not in neighbor):
			visit_neighbors(node_id)
		initial_config()

lista = [1,-1,2,-2,3,-3,4,-4,5,-5,6,-6]

for i in range(0,2):
	bfs(i)

print len(neighbor)

# def visit_next_layer():
# 	for i in range(1, 7):
# 		move(i)
# 		visit_neighbors(hash_node())
# 		move(i*(-1))

# 		move(i*(-1))
# 		visit_neighbors(hash_node())
# 		move(i)

#visit_neighbors(node_id)
#visit_next_layer()

#for i in range(1, 7):
#	move(i)
#	visit_next_layer()
#	move(i*(-1))

#	move(i*(-1))
#	visit_next_layer()
#	move(i)

# def layer_explorer(n):
# 	p = [0] * n
# 	for i in range(0, n):
# 		p[i] = 1

# 	mv = [1,-1,2,-2,3,-3,4,-4,5,-5,6,-6]
# 	c = [1] * n

# 	for i in range(0, 12):
# 		c[2] = mv[i]
# 		for u in c:
# 			move(u)

# 		visit_neighbors(hash_node())
# 		initial_config()

#import itertools
#print list(itertools.permutations([1,-1,2]))

#i = 1
#signal = 1
#cont = 1

#while cont <= 12:
#	move(i)
#	visit_neighbors2(hash_node())
#	i = i*(-1)
#	if cont %2 == 0:
#		i = i+1
#	cont = cont+1
#	initial_config()

#print len(neighbor)
#print neighbor

print("%s s" % (time.time() - start_time))