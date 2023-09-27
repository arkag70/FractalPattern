import sys
import pygame
from branch import Branch

if __name__ == "__main__":
    # Initialize Pygame
    pygame.init()
    # Constants for the screen dimensions
    SCREEN_WIDTH = 800
    SCREEN_HEIGHT = 600
    BRANCHLEN = 200
    BRANCHWID = 2
    alpha = 20
    BLACK = 0
    ANGLE = 90
    ITERATION = 9
    rounds = 10
    # Create the screen surface
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    while rounds:
        iteration = 0
        branches = [Branch(SCREEN_WIDTH/2, SCREEN_HEIGHT, BRANCHLEN, BRANCHWID, ANGLE)]
        # Main game loop
        while iteration < ITERATION:

            color = (255, 255, 255, alpha) 
            # Clear the screen with a white background
            screen.fill(BLACK)
            
            for branch in branches:
                branch.draw(screen, color)
            
            children = []
            for branch in branches:
                if branch.child == False:
                    child1, child2 = branch.drawChild()
                    children.append(child1)
                    children.append(child2)
            branches.extend(children)

            # Update the display
            pygame.time.delay(1000)
            print(len(branches))
            pygame.display.update()
            iteration += 1
        rounds -= 1
    
    pygame.time.delay(2000)
    pygame.quit()
    sys.exit()
