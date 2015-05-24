import time
import numpy as np
import cPickle
import random
import json
import base64

class RubikCube():
    "Rubik Cube representation."
    

    def __init__(self):
        self.cube = dict()
        self.cube['front'] = np.array([[1 for x in range(3)] for x in range(3)])
        self.cube['left'] = np.array([[2 for x in range(3)] for x in range(3)])
        self.cube['rigth'] = np.array([[3 for x in range(3)] for x in range(3)])
        self.cube['up'] = np.array([[4 for x in range(3)] for x in range(3)])
        self.cube['back'] = np.array([[5 for x in range(3)] for x in range(3)])
        self.cube['down'] = np.array([[6 for x in range(3)] for x in range(3)])

    def update_face(self, face):
        row1 = np.copy(self.cube[face][0,:])
        row3 = np.copy(self.cube[face][2,:])
        col1 = np.copy(self.cube[face][:,0])
        col3 = np.copy(self.cube[face][:,2])
        self.cube[face][:,2] = row1
        self.cube[face][2,:] = col3[::-1]
        self.cube[face][:,0] = row3
        self.cube[face][0,:] = col1[::-1]

    def update_face_(self, face):
        row1 = np.copy(self.cube[face][0,:])
        row3 = np.copy(self.cube[face][2,:])
        col1 = np.copy(self.cube[face][:,0])
        col3 = np.copy(self.cube[face][:,2])
        self.cube[face][:,2] = row3[::-1]
        self.cube[face][2,:] = col1
        self.cube[face][:,0] = row1[::-1]
        self.cube[face][0,:] = col3

    def front(self):
        self.update_face('front')
        #update other faces
        up = np.copy(self.cube['up'][2,:])
        rigth = np.copy(self.cube['rigth'][:,0])
        down = np.copy(self.cube['down'][0,:])
        left = np.copy(self.cube['left'][:,2])
        self.cube['up'][2,:] = left[::-1]
        self.cube['rigth'][:,0] = up
        self.cube['down'][0,:] = rigth[::-1]
        self.cube['left'][:,2] = down

    def up(self):
        self.update_face('up')
        # update other faces
        back = np.copy(self.cube['back'][0,:])
        rigth = np.copy(self.cube['rigth'][0,:])
        front = np.copy(self.cube['front'][0,:])
        left = np.copy(self.cube['left'][0,:])
        self.cube['back'][0,:] = left
        self.cube['rigth'][0,:] = back
        self.cube['front'][0,:] = rigth
        self.cube['left'][0,:] = front

    def back(self):
        self.update_face('back')
        # update other faces
        up = np.copy(self.cube['up'][0,:])
        left = np.copy(self.cube['left'][:,0])
        down = np.copy(self.cube['down'][2,:])
        rigth = np.copy(self.cube['rigth'][:,2])
        self.cube['up'][0,:] = rigth
        self.cube['left'][:,0] = up[::-1]
        self.cube['down'][2,:] = left
        self.cube['rigth'][:,2] = down[::-1]

    def left(self):
        self.update_face('left')
        # update other faces
        up = np.copy(self.cube['up'][:,0])
        front = np.copy(self.cube['front'][:,0])
        down = np.copy(self.cube['down'][:,0])
        back = np.copy(self.cube['back'][:,2])
        self.cube['up'][:,0] = back[::-1]
        self.cube['front'][:,0] = up
        self.cube['down'][:,0] = front
        self.cube['back'][:,2] = down[::-1]

    def rigth(self):
        self.update_face('rigth')
        # update other faces
        up = np.copy(self.cube['up'][:,2])
        back = np.copy(self.cube['back'][:,0])
        down = np.copy(self.cube['down'][:,2])
        front = np.copy(self.cube['front'][:,2])
        self.cube['up'][:,2] = front
        self.cube['back'][:,0] = up[::-1]
        self.cube['down'][:,2] = back[::-1]
        self.cube['front'][:,2] = down
    
    def down(self):
        self.update_face('down')
        # update other faces
        front = np.copy(self.cube['front'][2,:])
        rigth = np.copy(self.cube['rigth'][2,:])
        back = np.copy(self.cube['back'][2,:])
        left = np.copy(self.cube['left'][2,:])
        self.cube['front'][2,:] = left
        self.cube['rigth'][2,:] = front
        self.cube['back'][2,:] = rigth
        self.cube['left'][2,:] = back
    
    # reverse moves
    def front_(self):
        self.update_face_('front')
        #update other faces
        up = np.copy(self.cube['up'][2,:])
        rigth = np.copy(self.cube['rigth'][:,0])
        down = np.copy(self.cube['down'][0,:])
        left = np.copy(self.cube['left'][:,2])
        self.cube['up'][2,:] = rigth
        self.cube['rigth'][:,0] = down[::-1]
        self.cube['down'][0,:] = left
        self.cube['left'][:,2] = up[::-1]


    def up_(self):
        self.update_face_('up')
        # update other faces
        back = np.copy(self.cube['back'][0,:])
        rigth = np.copy(self.cube['rigth'][0,:])
        front = np.copy(self.cube['front'][0,:])
        left = np.copy(self.cube['left'][0,:])
        self.cube['back'][0,:] = rigth
        self.cube['rigth'][0,:] = front
        self.cube['front'][0,:] = left
        self.cube['left'][0,:] = back
    
    def back_(self):
        self.update_face_('back')
        # update other faces
        up = np.copy(self.cube['up'][0,:])
        left = np.copy(self.cube['left'][:,0])
        down = np.copy(self.cube['down'][2,:])
        rigth = np.copy(self.cube['rigth'][:,2])
        self.cube['up'][0,:] = left[::-1]
        self.cube['left'][:,0] = down
        self.cube['down'][2,:] = rigth[::-1]
        self.cube['rigth'][:,2] = up
    
    def left_(self):
        self.update_face_('left')
        # update other faces
        up = np.copy(self.cube['up'][:,0])
        front = np.copy(self.cube['front'][:,0])
        down = np.copy(self.cube['down'][:,0])
        back = np.copy(self.cube['back'][:,2])
        self.cube['up'][:,0] = front
        self.cube['front'][:,0] = down
        self.cube['down'][:,0] = back[::-1]
        self.cube['back'][:,2] = up[::-1]
    
    def rigth_(self):
        self.update_face_('rigth')
        # update other faces
        up = np.copy(self.cube['up'][:,2])
        back = np.copy(self.cube['back'][:,0])
        down = np.copy(self.cube['down'][:,2])
        front = np.copy(self.cube['front'][:,2])
        self.cube['up'][:,2] = back[::-1]
        self.cube['back'][:,0] = down[::-1]
        self.cube['down'][:,2] = front
        self.cube['front'][:,2] = up

    def down_(self):
        self.update_face_('down')
        # update other faces
        front = np.copy(self.cube['front'][2,:])
        rigth = np.copy(self.cube['rigth'][2,:])
        back = np.copy(self.cube['back'][2,:])
        left = np.copy(self.cube['left'][2,:])
        self.cube['front'][2,:] = rigth
        self.cube['rigth'][2,:] = back
        self.cube['back'][2,:] = left
        self.cube['left'][2,:] = front

    def move(self, i):
        RubikCube.MOVE[i](self)

    def encode_node(self):
        permutation = ""
        json_string1 = json.dumps(self.cube['front'].tolist())
        json_string2 = json.dumps(self.cube['left'].tolist())
        json_string3 = json.dumps(self.cube['rigth'].tolist())
        json_string4 = json.dumps(self.cube['up'].tolist())
        json_string5 = json.dumps(self.cube['back'].tolist())
        json_string6 = json.dumps(self.cube['down'].tolist())
        permutation = json_string1 + "\t" + json_string2 +  "\t" + json_string3 + "\t" +  json_string4 + "\t" +  json_string5 + "\t" +  json_string6
        return stringToBase64(permutation)

    def decode_node(self, encoded_node):
        permutation = base64ToString(encoded_node)
        faces = permutation.split('\t')
        self.cube['front'] = np.array(json.loads(faces[0]))
        self.cube['left'] = np.array(json.loads(faces[1]))
        self.cube['rigth'] = np.array(json.loads(faces[2]))
        self.cube['up'] = np.array(json.loads(faces[3]))
        self.cube['back'] = np.array(json.loads(faces[4]))
        self.cube['down'] = np.array(json.loads(faces[5]))
        return self

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


def stringToBase64(s):
    return base64.b64encode(s.encode('utf-8'))

def base64ToString(b):
    return base64.b64decode(b).decode('utf-8')

def bfs(cube, goal):
    test = RubikCube()
    vertex = cube.encode_node()
    queue = [(vertex, [vertex])]
    while queue:
        (vertex, path) = queue.pop(0)
        for next in expand(cube, vertex):
            if next == goal:
                print 'BFS found a path of ' + str(len(path + [next]))
                return path + [next]
            else:
                queue.append((next, path + [next]))

def expand(cube, vertex):
    childs = []
    cube.decode_node(vertex)
    for i in range(-6,0) + range(1,7):
        cube.move(i)
        childs.append(cube.encode_node())
        cube.move(-i)
    return childs    

def dfs():

    start_time = time.time()
    cube = RubikCube()
    
    node_id_source = cube.encode_node()
    cont = 0
    for i in range(0, 14):
        t = pow(2, i+1)
        for j in range(0, 2):
            # execute uma DFS que parte da configuracao inicial e que termina apos visitar 2^i nos
            visited = set()
            visited.add(node_id_source)
            for k in range(1, t+1):
                cont = cont+1
                r = random.choice(range(-6,0) + range(1,7))
                cube.move(r)
                node_id = cube.encode_node()
                # check if node was already visited
                while node_id in visited:
                    cube.move(r*(-1))
                    r = random.choice(range(-6,0) + range(1,7))
                    cube.move(r)
                    node_id = cube.encode_node()
                visited.add(node_id)
            print 'DFS done for ' + str(k) + ' nodes.'
            bfs(cube, node_id_source)
        print i+1, cont, t, ("%s s" % (time.time() - start_time))

def main():
    dfs()
main()
