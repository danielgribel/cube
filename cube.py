import time
import numpy as np
import cPickle
import random
import json

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
    return hash(permutation)

cube = dict()
initial_config()

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

#moves = [0] * 99999
#c = [0] * 99999
#visited = ["" for x in range(100000)]
#node_id = hashlib.md5(cPickle.dumps(cube)).hexdigest()
#visited[0] = node_id

#node_id_source = hash(cPickle.dumps(cube))
node_id_source = hash_node()

# for i in range(0, 10):
#     cont = 0
#     t = pow(2, i+1)
#     for j in range(0, 100):
#         initial_config()
#         moves = [0] * t
#         for k in range(1, t+1):
#             cont = cont+1
#             #moves[k-1] = randint(1, 12)
#             move(randint(1, 12))
    
#         #for p in range(0, len(moves)):
#         #    move(moves[p])

#     print i+1, cont, len(moves), ("%s s" % (time.time() - start_time))
#     #print y, cont, len(moves), ("%s s" % (time.time() - start_time))

cont = 0
#nodes_on_graph = set()

for i in range(0, 14):
    t = pow(2, i+1)
    for j in range(0, 100):
        initial_config()
        #moves = [0] * t
        # execute uma DFS que parte da configuracao inicial e que termina apos visitar 2^i nos
        visited2 = set()        
        visited2.add(node_id_source)

        for k in range(1, t+1):
            cont = cont+1
            r = random.choice(range(-6,0) + range(1,7))
            move(r)
            # generate a key for current cube config. this is slow!!
            #node_id = hash(cPickle.dumps(cube))
            node_id = hash_node()
            # check if node was already visited
            while node_id in visited2:
                move(r*(-1))
                r = random.choice(range(-6,0) + range(1,7))
                move(r)
                #node_id = hash(cPickle.dumps(cube))
                node_id = hash_node()
            #moves[k-1] = r
            visited2.add(node_id)

            #nodes_on_graph.add(node_id)

        # execute uma BFS que parte de v e que termina ao alcancar a config inicial
        #for y in reversed(moves):
        #    move(y*(-1))

    print i+1, cont, t, ("%s s" % (time.time() - start_time))

# for i in range(1, 100000):
#     r = randint(1, 12)
#     move(r)
#     node_id = hashlib.md5(cPickle.dumps(cube)).hexdigest()
    
#     if node_id in visited:
#         c[k] = i-1
#         k = k+1

#     visited[i] = node_id
#     moves[i-1] = r

# print moves
# print c

# for x in c:
#     if(x != 0):
#         print (moves[x-3],moves[x-2],moves[x-1],moves[x])

# print i+1, cont, ("%s s" % (time.time() - start_time))