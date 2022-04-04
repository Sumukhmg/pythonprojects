# importing pygame
import pygame
  
pygame.init()
  
# setting window size
win = pygame.display.set_mode((500, 400))
  
# setting title to the window
pygame.display.set_caption("Bubble sort")
  
# initial position
x = 40
y = 40
  
# width of each bar
width = 20
  
# height of each bar (data to be sorted)
height = [200, 50, 130, 90, 250, 61, 110,
            88, 33, 80, 70, 159, 180, 20]
  
run = True
  
# method to show the list of height
def show(height):
  
    # loop to iterate each item of list
    for i in range(len(height)):
  
        # drawing each bar with respective gap
        pygame.draw.rect(win, (255, 0, 0), (x + 30 * i, y, width, height[i]))
  
# infinite loop
while run:
  
    # execute flag to start sorting
    execute = False
  
    # time delay
    pygame.time.delay(10)
  
    # getting keys pressed
    keys = pygame.key.get_pressed()
  
    # iterating events
    for event in pygame.event.get():
  
        # if event is to quit
        if event.type == pygame.QUIT:
  
            # making run = false so break the while loop
            run = False
  
    # if space bar is pressed
    if keys[pygame.K_SPACE]:
        # make execute flag to true
        execute = True
  
    # checking if execute flag is false
    if execute == False:
  
        # fill the window with black color
        win.fill((0, 0, 0))
  
        # call the height method to show the list items
        show(height)
  
        # update the window
        pygame.display.update()
  
    # if execute flag is true
    else:
  
        # start sorting using bubble sort technique
        for i in range(len(height) - 1):
  
            # after this iteration max element will come at last
            for j in range(len(height) - i - 1):
  
                # starting is greater then next element
                if height[j] > height[j + 1]:
  
                    # save it in temporary variable
                    # and swap them using temporary variable
                    t = height[j]
                    height[j] = height[j + 1]
                    height[j + 1] = t
  
                # fill the window with black color
                win.fill((0, 0, 0))
  
                # call show method to display the list items
                show(height)
  
                # create a time delay
                pygame.time.delay(50)
  
                # update the display
                pygame.display.update()
  
# exiting the main window
pygame.quit()