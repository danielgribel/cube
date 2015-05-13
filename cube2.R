cube = new.env(hash=T, parent=emptyenv())

# initial config - solved cube
cube$front = matrix(1, 3, 3)
cube$left = matrix(2, 3, 3)
cube$rigth = matrix(3, 3, 3)
cube$up = matrix(4, 3, 3)
cube$down = matrix(5, 3, 3)
cube$back = matrix(6, 3, 3)

update_current_face <- function(face) {
  # update face
  row1 = cube[[face]][1,]
  row3 = cube[[face]][3,]
  col1 = cube[[face]][,1]
  col3 = cube[[face]][,3]
  cube[[face]][,3] = row1
  cube[[face]][3,] = rev(col3)
  cube[[face]][,1] = row3
  cube[[face]][1,] = rev(col1)
}

front <- function() {
  update_current_face('front')
  # update other faces
  up = cube$up[3,]
  rigth = cube$rigth[,1]
  down = cube$down[1,]
  left = cube$left[,3]
  cube$up[3,] = rev(left)
  cube$rigth[,1] = up
  cube$down[1,] = rev(rigth)
  cube$left[,3] = down
}

up <- function() {
  update_current_face('up')
  # update other faces
  back = cube$back[1,]
  rigth = cube$rigth[1,]
  front = cube$front[1,]
  left = cube$left[1,]
  cube$back[1,] = left
  cube$rigth[1,] = back
  cube$front[1,] = rigth
  cube$left[1,] = front
}

back <- function() {
  update_current_face('back')
  # update other faces
  up = cube$up[1,]
  left = cube$left[,1]
  down = cube$down[3,]
  rigth = cube$rigth[,3]
  cube$up[1,] = rigth
  cube$left[,1] = rev(up)
  cube$down[3,] = left
  cube$rigth[,3] = rev(down)
}

left <- function() {
  update_current_face('left')
  # update other faces
  up = cube$up[,1]
  front = cube$front[,1]
  down = cube$down[,1]
  back = cube$back[,3]
  cube$up[,1] = rev(back)
  cube$front[,1] = up
  cube$down[,1] = front
  cube$back[,3] = rev(down)
}


rigth <- function() {
  update_current_face('rigth')
  # update other faces
  up = cube$up[,3]
  back = cube$back[,1]
  down = cube$down[,3]
  front = cube$front[,3]
  cube$up[,3] = front
  cube$back[,1] = rev(up)
  cube$down[,3] = rev(back)
  cube$front[,3] = down
}

down <- function() {
  update_current_face('down')
  # update other faces
  front = cube$front[3,]
  rigth = cube$rigth[3,]
  back = cube$back[3,]
  left = cube$left[3,]
  cube$front[3,] = left
  cube$rigth[3,] = front
  cube$back[3,] = rigth
  cube$left[3,] = back
}

# reverse moves
front_ <- function() {
  front()
  front()
  front()
}

up_ <- function() {
  up()
  up()
  up()
}

back_ <- function() {
  back()
  back()
  back()
}

left_ <- function() {
  left()
  left()
  left()
}

rigth_ <- function() {
  rigth()
  rigth()
  rigth()
}

down_ <- function() {
  down()
  down()
  down()
}

back()
left_()

print(cube$front)