# Python Snake

This is my first venture with pygame!
This is a solo project creating the classic Snake game with python and Pygame.

## Technologies

- Pygame 2.5.2
- Python

## Installation

- `pip install pygame`
- Download or clone this repo
  `git clone`

## How Games Work

- Game loop
  1. Get player input
  2. Position elements
  3. Draw graphics
- Keep rendering elements per cycle
- Not for large scale games

### Why Pygame?

- Displays images easily (+ play sounds)
- Check for user input: (input() stop your code)
- dev tools like collisions, text, timer
- Good for coding & programming

### Surfaces & Rectangles

- **Display surface:** the canvas the entire game is drawn on, theres only one, displayed by default
- **Surface:** a layer that displays graphics, can have multiple, not displayed by default
  - Create surface (import image, text, or empty space)
  - Display surface
- **Rectangle:** can be used for drawing, placement, movement and collision
  - define rectangle: `rectangle = pygame.Rect(x,y,w,h)`
  - draw rectangle: `pygame.draw.rect(screen, color, rectangle)`
  - different shapes instead of `rect()`:
    - `circle(screen, color, (x_center,y_center), r)`,
    - `ellipse(screen, color, x,y,w,h)`,
    - `polygon()`,
    - `arc(screen, color, (x,y,w,h), radian, radian)`,
    - `line(screen, color, (x_start,y_start), (x_end,y_end), line_w)`
