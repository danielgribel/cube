import time
import numpy as np
from random import randint

start_time = time.time()

def update_current_face(face):
    row1 = np.copy(cube[face][0,:])
    row3 = np.copy(cube[face][2,:])
    col1 = np.copy(cube[face][:,0])
    col3 = np.copy(cube[face][:,2])
    cube[face][:,2] = row1
    cube[face][2,:] = col3[::-1]
    cube[face][:,0] = row3
    cube[face][0,:] = col1[::-1]

def front():
    update_current_face('front')
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
    update_current_face('up')
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
    update_current_face('back')
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
    update_current_face('left')
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
    update_current_face('rigth')
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
    update_current_face('down')
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

cube['front'] = np.array([[1 for x in range(3)] for x in range(3)])
cube['left'] = np.array([[2 for x in range(3)] for x in range(3)])
cube['rigth'] = np.array([[3 for x in range(3)] for x in range(3)])
cube['up'] = np.array([[4 for x in range(3)] for x in range(3)])
cube['down'] = np.array([[5 for x in range(3)] for x in range(3)])
cube['back'] = np.array([[6 for x in range(3)] for x in range(3)])

MOVE = {1 : front,
        2 : up,
        3 : back,
        4 : left,
        5 : rigth,
        6 : down,
        7 : front_,
        8 : up_,
        9 : back_,
        10 : left_,
        11 : rigth_,
        12 : down_
}

#moves = [0] * 1000000

for i in range(0, 99999):
    r = randint(1, 12)
    random_move(r)
    # keep moves
    #moves[i] = r
    
print cube['front']
print("%s s" % (time.time() - start_time))