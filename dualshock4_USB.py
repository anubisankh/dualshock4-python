import pygame
import os

pygame.init()
pygame.joystick.init()

controller = pygame.joystick.Joystick(0)
controller.init()

# Three types of controls: axis, button, and hat
axis = {}
button = {}
hat = {}

# Assign initial data values
# Axes are initialized to 0.0
for i in range(controller.get_numaxes()):
	axis[i] = 0.0
# Buttons are initialized to False
for i in range(controller.get_numbuttons()):
	button[i] = False
# Hats are initialized to 0
for i in range(controller.get_numhats()):
	hat[i] = (0, 0)

# Labels for DS4 controller axes
AXIS_LEFT_STICK_X = 0
AXIS_LEFT_STICK_Y = 1
AXIS_RIGHT_STICK_X = 2
AXIS_RIGHT_STICK_Y = 3
AXIS_R2 = 4
AXIS_L2 = 5

# Labels for DS4 controller buttons
# Note that there are 14 buttons (0 to 13 for pygame, 1 to 14 for Windows setup)
BUTTON_SQUARE = 0
BUTTON_CROSS = 1
BUTTON_CIRCLE = 2
BUTTON_TRIANGLE = 3

BUTTON_L1 = 4
BUTTON_R1 = 5
BUTTON_L2 = 6
BUTTON_R2 = 7

BUTTON_SHARE = 8
BUTTON_OPTIONS = 9

BUTTON_LEFT_STICK = 10
BUTTON_RIGHT_STICK = 11

BUTTON_PS = 12
BUTTON_PAD = 13

# Labels for DS4 controller hats (Only one hat control)
HAT_1 = 0

# Main loop, one can press the PS button to break
quit = False
while quit == False:

    # Get events
    for event in pygame.event.get():

        if event.type == pygame.JOYAXISMOTION:
            axis[event.axis] = round(event.value,3)
        elif event.type == pygame.JOYBUTTONDOWN:
            button[event.button] = True
        elif event.type == pygame.JOYBUTTONUP:
            button[event.button] = False
        elif event.type == pygame.JOYHATMOTION:
        	hat[event.hat] = event.value

    quit = button[BUTTON_PS]

    # Print out results
    os.system('cls')
    # Axes
    print("Left stick X:", axis[AXIS_LEFT_STICK_X])
    print("Left stick Y:", axis[AXIS_LEFT_STICK_Y])
    print("Right stick X:", axis[AXIS_RIGHT_STICK_X])
    print("Right stick Y:", axis[AXIS_RIGHT_STICK_Y])
    print("L2 strength:", axis[AXIS_L2])
    print("R2 strength:", axis[AXIS_R2],"\n")
    # Buttons
    print("Square:", button[BUTTON_SQUARE])
    print("Cross:", button[BUTTON_CROSS])
    print("Circle:", button[BUTTON_CIRCLE])
    print("Triangle:", button[BUTTON_TRIANGLE])
    print("L1:", button[BUTTON_L1])
    print("R1:", button[BUTTON_R1])
    print("L2:", button[BUTTON_L2])
    print("R2:", button[BUTTON_R2])
    print("Share:", button[BUTTON_SHARE])
    print("Options:", button[BUTTON_OPTIONS])
    print("Left stick press:", button[BUTTON_LEFT_STICK])
    print("Right stick press:", button[BUTTON_RIGHT_STICK])
    print("PS:", button[BUTTON_PS])
    print("Touch Pad:", button[BUTTON_PAD],"\n")
    # Hats
    print("Hat X:", hat[HAT_1][0])
    print("Hat Y:", hat[HAT_1][1],"\n")

    print("Press PS button to quit:", quit)

    # Limited to 30 frames per second to make the display not so flashy
    clock = pygame.time.Clock()
    clock.tick(30) 