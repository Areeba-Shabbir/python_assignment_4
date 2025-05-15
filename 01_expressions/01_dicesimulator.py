from graphics import Canvas
import time

# Constants
CANVAS_WIDTH = 400
CANVAS_HEIGHT = 400
CELL_SIZE = 40
ERASER_SIZE = 20

def erase_objects(canvas, eraser):
    """Erase all blue rectangles the eraser touches."""
    mouse_x = canvas.get_mouse_x()
    mouse_y = canvas.get_mouse_y()

    left_x = mouse_x
    top_y = mouse_y
    right_x = left_x + ERASER_SIZE
    bottom_y = top_y + ERASER_SIZE

    overlapping_objects = canvas.find_overlapping(left_x, top_y, right_x, bottom_y)

    for obj in overlapping_objects:
        if obj != eraser:
            canvas.set_color(obj, 'white')

def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)

    # Create grid of blue cells
    rows = CANVAS_HEIGHT // CELL_SIZE
    cols = CANVAS_WIDTH // CELL_SIZE

    for row in range(rows):
        for col in range(cols):
            x1 = col * CELL_SIZE
            y1 = row * CELL_SIZE
            x2 = x1 + CELL_SIZE
            y2 = y1 + CELL_SIZE
            canvas.create_rectangle(x1, y1, x2, y2, 'blue')

    # Wait for user click to place eraser
    canvas.wait_for_click()
    start_x, start_y = canvas.get_last_click()

    # Create eraser
    eraser = canvas.create_rectangle(
        start_x, start_y,
        start_x + ERASER_SIZE, start_y + ERASER_SIZE,
        'pink'
    )

    # Eraser movement and erase logic
    while True:
        mouse_x = canvas.get_mouse_x()
        mouse_y = canvas.get_mouse_y()
        canvas.moveto(eraser, mouse_x, mouse_y)
        erase_objects(canvas, eraser)
        time.sleep(0.05)

# Required to run the main function
if __name__ == '__main__':
    main()
