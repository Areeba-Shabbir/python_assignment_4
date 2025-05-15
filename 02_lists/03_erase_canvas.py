from graphics import Canvas
import time

# Canvas and Grid Setup
WIDTH = 400
HEIGHT = 400
GRID_SIZE = 40
ERASER_DIM = 20

def create_grid(canvas):
    """Draws the full blue grid on canvas."""
    for y in range(0, HEIGHT, GRID_SIZE):
        for x in range(0, WIDTH, GRID_SIZE):
            canvas.create_rectangle(x, y, x + GRID_SIZE, y + GRID_SIZE, 'blue')

def create_eraser(canvas, x, y):
    """Creates and returns an eraser rectangle."""
    return canvas.create_rectangle(x, y, x + ERASER_DIM, y + ERASER_DIM, 'pink')

def perform_erasing(canvas, eraser_id):
    """Detects and erases cells under the eraser."""
    eraser_x = canvas.get_mouse_x()
    eraser_y = canvas.get_mouse_y()
    touching = canvas.find_overlapping(eraser_x, eraser_y, eraser_x + ERASER_DIM, eraser_y + ERASER_DIM)

    for item in touching:
        if item != eraser_id:
            canvas.set_color(item, 'white')

def main():
    screen = Canvas(WIDTH, HEIGHT)
    create_grid(screen)

    screen.wait_for_click()
    click_x, click_y = screen.get_last_click()

    eraser_box = create_eraser(screen, click_x, click_y)

    while True:
        current_x = screen.get_mouse_x()
        current_y = screen.get_mouse_y()

        screen.moveto(eraser_box, current_x, current_y)
        perform_erasing(screen, eraser_box)

        time.sleep(0.05)

if __name__ == '__main__':
    main()
