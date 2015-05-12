cube <- new.env(hash=T, parent=emptyenv())

# initial config - solved cube
cube$front = matrix(1, 3, 3)
cube$left = matrix(2, 3, 3)
cube$rigth = matrix(3, 3, 3)
cube$up = matrix(4, 3, 3)
cube$down = matrix(5, 3, 3)
cube$back = matrix(6, 3, 3)

# current config for specific row
row_config <- function(cube, i) {
  m <- new.env(hash=T, parent=emptyenv())
  m$front = cube$front[i,]
  m$left = cube$left[i,]
  m$rigth = cube$rigth[i,]
  m$up = cube$up[i,]
  m$down = cube$down[i,]
  m$back = cube$back[i,]
  return(m)
}

# current config for specific column
column_config <- function(cube, i) {
  m <- new.env(hash=T, parent=emptyenv())
  m$front = cube$front[,i]
  m$left = cube$left[,i]
  m$rigth = cube$rigth[,i]
  m$up = cube$up[,i]
  m$down = cube$down[,i]
  m$back = cube$back[,i]
  return(m)
}

# rigth move on row i
move_rigth <- function(cube, i) {
  last_row = row_config(cube, i)
  cube$rigth[i,] = last_row$front
  cube$back[i,] = last_row$rigth
  cube$left[i,] = last_row$back
  cube$front[i,] = last_row$left
  cat('rigth', i, "\n")
}

# left move on row i
move_left <- function(cube, i) {
  last_row = row_config(cube, i)
  cube$left[i,] = last_row$front
  cube$back[i,] = last_row$left
  cube$rigth[i,] = last_row$back
  cube$front[i,] = last_row$rigth
  cat('left', i, "\n")
}

# up move on row i
move_up <- function(cube, i) {
  last_column = column_config(cube, i)
  cube$up[,i] = last_column$front
  cube$back[,i] = last_column$up
  cube$down[,i] = last_column$back
  cube$front[,i] = last_column$down
  cat('up', i, "\n")
}

# down move on row i
move_down <- function(cube, i) {
  last_column = column_config(cube, i)
  cube$down[,i] = last_column$front
  cube$back[,i] = last_column$down
  cube$up[,i] = last_column$back
  cube$front[,i] = last_column$up
  cat('down', i, "\n")
}

# outer-rigth move on row i (external move to face in question)
move_outer_rigth <- function(cube, i) {
  if(i == 1) {
    row_down = cube$down[1,]
    column_rigth = cube$rigth[,1]
    row_up = cube$up[3,]
    column_left = cube$left[,3]
    cube$rigth[,1] = row_down
    cube$up[3,] = column_rigth
    cube$left[,3] = row_up
    cube$down[1,] = column_left
  }
  if(i == 2) {
    row_down = cube$down[2,]
    column_rigth = cube$rigth[,2]
    row_up = cube$up[2,]
    column_left = cube$left[,2]
    cube$rigth[,2] = row_down
    cube$up[2,] = column_rigth
    cube$left[,2] = row_up
    cube$down[2,] = column_left
  }
  if(i == 3) {
    row_down = cube$down[3,]
    column_rigth = cube$rigth[,3]
    row_up = cube$up[1,]
    column_left = cube$left[,1]
    cube$rigth[,3] = row_down
    cube$up[1,] = column_rigth
    cube$left[,1] = row_up
    cube$down[3,] = column_left
  }
  cat('outer rigth', i, "\n")
}

# outer-left move on row i (external move to face in question)
move_outer_left <- function(cube, i) {
  if(i == 1) {
    row_down = cube$down[1,]
    column_rigth = cube$rigth[,1]
    row_up = cube$up[3,]
    column_left = cube$left[,3]
    cube$rigth[,1] = row_up
    cube$up[3,] = column_left
    cube$left[,3] = row_down
    cube$down[1,] = column_rigth
  }
  if(i == 2) {
    row_down = cube$down[2,]
    column_rigth = cube$rigth[,2]
    row_up = cube$up[2,]
    column_left = cube$left[,2]
    cube$rigth[,2] = row_up
    cube$up[2,] = column_left
    cube$left[,2] = row_down
    cube$down[2,] = column_rigth
  }
  if(i == 3) {
    row_down = cube$down[3,]
    column_rigth = cube$rigth[,3]
    row_up = cube$up[1,]
    column_left = cube$left[,1]
    cube$rigth[,3] = row_up
    cube$up[1,] = column_left
    cube$left[,1] = row_down
    cube$down[3,] = column_rigth
  }
  cat('outer left', i, "\n")  
}

# perform a random move on row/column i
random_move <- function(cube, move, i) {
  switch(move,
    '1' = {move_rigth(cube, i)},
    '2' = {move_left(cube, i)},
    '3' = {move_up(cube, i)},
    '4' = {move_down(cube, i)},
    '5' = {move_outer_rigth(cube, i)},
    '6' = {move_outer_left(cube, i)}
  )
}

for(i in 1:100) {
  move <- sample(1:6, 1)
  t <- sample(1:3, 1)
  random_move(cube, move, t)
  print(cube$front)
}