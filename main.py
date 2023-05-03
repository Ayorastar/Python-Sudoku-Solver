import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
from solver import *
from tkinter import *
from tkinter import messagebox

board = None
def clearBoard():
  global board
  board = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0]]
  screen.fill((255,255,255))
  drawGrid()
  drawButtons()
  pygame.display.update()
  

pygame.font.init()
myFont = pygame.font.SysFont(None, 65)
pygame.display.set_caption("Sudoku Solver")
(width, height) = (700, 503)
screen = pygame.display.set_mode((width, height))
background_colour = (255,255,255)
screen.fill(background_colour)
resetButton = None
solveButton = None
#sets up a window with a white background and a title

x = 0
y = 0
actualx = 0
actualy = 0

def drawGrid():
    pygame.draw.rect(screen, (0,0,0), (1, 1, 500 ,500), 4)
    for i in range(8):
        if (i+1) % 3 == 0 and i != 0:
            thick = 3
        else:
            thick = 1
        gridInterval = ((i+1)/9)*501
        pygame.draw.line(screen, (0,0,0), (0, gridInterval), (501, gridInterval), thick)
        pygame.draw.line(screen, (0, 0, 0), (gridInterval, 0), (gridInterval, 501), thick)
        #draws a square and 8 lines across and down, changing thickness to make the board

def getSelected(pos):
    global x
    global y
    global actualx
    global actualy
    global board
    if pos <= (501, 501):
        x = int(((pos[0]-1) // 55.5556))
        y = int(((pos[1]-1) // 55.5556))
        actualx = ((x/9)*500)+1
        actualy = ((y/9)*500)+1
    elif resetButton.collidepoint(pos):
        clearBoard()
        pygame.display.update()
    elif solveButton.collidepoint(pos):
        valid = validateBoard(board)
        if all(valid):
          solve(board)
          drawNumbers(board)
          pygame.display.update()
        else:
          if valid[0] == False:
            Tk().wm_withdraw()
            messagebox.showinfo('Error','The Sudoku entered does not have enough numbers (Minimum is 17).')
          if valid[1] == False:
            Tk().wm_withdraw()
            messagebox.showinfo('Error','The Sudoku entered violates Sudoku Rules.')
            
    #calculates which box or button the mouse has clicked on and where to draw the blue outline
    
def drawSelectedCell(pos):
    global x
    global y
    getSelected(pos)
    screen.fill((255,255,255))
    drawGrid()
    drawButtons()
    drawNumbers(board)
    pygame.draw.rect(screen, (0, 85, 255), (actualx, actualy, 55.5556, 55.5556), 3)
    pygame.display.update()
    #wipes the screen and draws the grid and new blue box

def drawNumbers(board):
    screen.fill((255,255,255))
    drawGrid()
    drawButtons()
    pygame.draw.rect(screen, (0, 85, 255), (actualx, actualy, 55.5556, 55.5556), 3)
    for i in range(9):
        for j in range(9):
            if board[i][j] != 0:
              text = myFont.render(str(board[i][j]), False, (0,0,0))
              screen.blit(text, ((j/9*500) + 17, (i/9*500) + 8))
    pygame.display.update()
    #draws numbers from left to right, top to bottom after clearing the image and drawing the grid and cursor

def drawButtons():
    global resetButton
    global solveButton
    buttonBackground = pygame.image.load(r'C:\Users\brett\OneDrive\Pictures\Sudoku\buttonBackground.png')
    buttonBackground = pygame.transform.scale(buttonBackground, (126, 48))
    resetButton = screen.blit(buttonBackground, (545, 145))
    solveButton = screen.blit(buttonBackground, (545, 310))
    text = myFont.render("Reset", False, (0,0,0))
    screen.blit(text, (550, 150))
    text = myFont.render("Solve", False, (0,0,0))
    screen.blit(text, (550, 315))
    #draws the buttons and button text

def validateBoard(board):
    count = 0
    for i in range(9):
        count = count + board[i].count(0)
    sudokuRules = True
    for i in range(9):
      for j in range(9):
        if board[i][j] != 0 and valid(board, board[i][j], (i,j)) == False:
            sudokuRules = False
    conditions = [count <= 64, sudokuRules]
    return conditions
    #checks the board can be solved

clearBoard()
drawGrid()
drawButtons()
pygame.display.update()
pygame.display.flip()


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
          running = False
        if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    board[y][x] = 1
                    drawNumbers(board)
                if event.key == pygame.K_2:
                    board[y][x] = 2
                    drawNumbers(board)
                if event.key == pygame.K_3:
                    board[y][x] = 3
                    drawNumbers(board)
                if event.key == pygame.K_4:
                    board[y][x] = 4
                    drawNumbers(board)
                if event.key == pygame.K_5:
                    board[y][x] = 5
                    drawNumbers(board)
                if event.key == pygame.K_6:
                    board[y][x] = 6
                    drawNumbers(board)
                if event.key == pygame.K_7:
                    board[y][x] = 7
                    drawNumbers(board)
                if event.key == pygame.K_8:
                    board[y][x] = 8
                    drawNumbers(board)
                if event.key == pygame.K_9:
                    board[y][x] = 9
                    drawNumbers(board)
                if event.key == pygame.K_DELETE or event.key == pygame.K_BACKSPACE:
                    board[y][x] = 0
                    drawNumbers(board)
                if pos:
                  if event.key == pygame.K_UP:
                    if y > 0:
                      y = y - 1
                      pos = (pos[0], (y * 55.5556)+5)
                      drawSelectedCell(pos)            
                  if event.key == pygame.K_DOWN:
                    if y < 8:
                      y = y + 1
                      pos = (pos[0], (y * 55.5556)+5)
                      drawSelectedCell(pos)
                  if event.key == pygame.K_LEFT:
                    if x > 0:
                      x = x - 1
                      pos = ((x * 55.5556)+5, pos[1])
                      drawSelectedCell(pos)
                  if event.key == pygame.K_RIGHT:
                    if x < 8:
                      x = x + 1
                      pos = ((x * 55.5556)+5, pos[1])
                      drawSelectedCell(pos)
                    
        if event.type == pygame.MOUSEBUTTONDOWN:
          pos = pygame.mouse.get_pos()
          drawSelectedCell(pos)
          #main loop: checks for any input

pygame.quit()

