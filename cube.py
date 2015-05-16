import time
import numpy as np
import cPickle
from random import randint

start_time = time.time()

def initial_config():
    cube['front'] = np.array([[1 for x in range(3)] for x in range(3)])
    cube['left'] = np.array([[2 for x in range(3)] for x in range(3)])
    cube['rigth'] = np.array([[3 for x in range(3)] for x in range(3)])
    cube['up'] = np.array([[4 for x in range(3)] for x in range(3)])
    cube['down'] = np.array([[5 for x in range(3)] for x in range(3)])
    cube['back'] = np.array([[6 for x in range(3)] for x in range(3)])

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
    
# reverse moves: we have to implement them to improve performance
def front_():
    front()
    front()
    front()
    
def up_():
    up()
    up()
    up()
    
def back_():
    back()
    back()
    back()
    
def left_():
    left()
    left()
    left()
    
def rigth_():
    rigth()
    rigth()
    rigth()

def down_():
    down()
    down()
    down()

def random_move(i):
    MOVE[i]()

cube = dict()
initial_config()

MOVE = {1 : front,
        2 : front_,
        3 : up,
        4 : up_,
        5 : back,
        6 : back_,
        7 : left,
        8 : left_,
        9 : rigth,
        10 : rigth_,
        11 : down,
        12 : down_
}

#moves = [0] * 99999
#c = [0] * 99999
#visited = ["" for x in range(100000)]
#node_id = hashlib.md5(cPickle.dumps(cube)).hexdigest()
#visited[0] = node_id

node_id_source = hash(cPickle.dumps(cube))

# for i in range(0, 10):
#     cont = 0
#     t = pow(2, i+1)
#     for j in range(0, 100):
#         initial_config()
#         moves = [0] * t
#         for k in range(1, t+1):
#             cont = cont+1
#             #moves[k-1] = randint(1, 12)
#             random_move(randint(1, 12))
    
#         #for p in range(0, len(moves)):
#         #    random_move(moves[p])

#     print i+1, cont, len(moves), ("%s s" % (time.time() - start_time))
#     #print y, cont, len(moves), ("%s s" % (time.time() - start_time))


cont = 0

for i in range(0, 10):
    t = pow(2, i+1)
    for j in range(0, 100):
        initial_config()

        # execute uma DFS que parte da configuracao inicial e que termina apos visitar 2^i nos
        visited2 = ["" for x in range(t+1)]
        visited2[0] = node_id_source
        for k in range(1, t+1):
            cont = cont+1
            temp = cube
            random_move(randint(1, 12))
            node_id = hash(cPickle.dumps(cube))

            while node_id in visited2:
                cube = temp
                random_move(randint(1, 12))
                node_id = hash(cPickle.dumps(cube))

            visited2[k] = node_id
    
        # execute uma BFS que parte de v e que termina ao alcancar a config inicial
    
    print i+1, cont, t, ("%s s" % (time.time() - start_time))
    
# for i in range(1, 100000):
#     r = randint(1, 12)
#     random_move(r)
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