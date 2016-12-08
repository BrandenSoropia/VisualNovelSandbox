## The script of the game goes in this file.

## Declare characters used by this game. The color argument colorizes the name
## of the character.

define e = Character('Eileen')

## Images etc
image bg city = "city.jpg"
image bg park = "park.jpg"
image bg library = "library.jpg"
image bg table_top = 'table_top.jpg'

## The game starts here.
init python:
    ## CONSTANTS
    SEARCH_TIME = 5

    visited_city = False
    visited_park = False
    visited_library = False

    import math

    ## TODO: Be able to push objects off sides of window
    ## TODO: Better reaction to mouse movement
    def repulsor_update(st):

        # If we don't know where the mouse is, give up.
        if repulsor_pos is None:
            return .01

        px, py = repulsor_pos

        # For each sprite...
        for i in repulsor_sprites:

            # Compute the vector between it and the mouse.
            vx = i.x - px
            vy = i.y - py

            # Get the vector length, normalize the vector.
            vl = math.hypot(vx, vy)
            if vl >= 150:
                continue

            # Compute the distance to move.
            distance = 3.0 * (150 - vl) / 150

            # Move
            i.x += (distance * vx / vl) * 2
            i.y += (distance * vx / vl) * 2

            # Ensure we stay on the screen.
            if i.x < 2:
                i.x = 2

            if i.x > repulsor.width - 2:
                i.x = repulsor.width - 2

            if i.y < 2:
                i.y = 2

            if i.y > repulsor.height - 2:
                i.y = repulsor.height - 2

        return .01

    def toggleDoneSearchingLetters ():
        doneSearchingLetters = not doneSearchingLetters

    # On an event, record the mouse position.
    def repulsor_event(ev, x, y, st):
        store.repulsor_pos = (x, y)

label start:

    scene black
    "Hello world."

    e "I am me. And I exist here. But are there others like me? Ones that exist and share this place?"

    jump city

label city:

    scene bg city
    if visited_city:
        e "Still no one in sight... I may as well continue my search."
    else:
        $visited_city = True
        e "Not a soul to be found. What is going on?"
        e "Maybe if I search I'll find an answer."

    menu:
        "Search park":
            jump park

        "Search library":
            jump library

        "End":
            jump end

label park:
    scene bg park
    if visited_park:
        e "Still beautiful. Still empty..."
    else:
        $ visited_park = True
        e "This tranquil and serence scene frees my soul from the shackles of the hustling, bustling city."
        e "My only regret is that I have no one to share it with..."
        e "Something like this... Oh, how I wish to share it!"
        e "But I am alone. Empty. Without a hope."

    "Searched Park Saved"
    $renpy.take_screenshot()
    $renpy.save('1-4', 'Park')

    menu:
        "Return to city":
            jump city

label library:
    scene bg library

    if visited_library:
        e "All this belongs to me. And only me..."
    else:
        $ visited_library = True
        e "All this knowledge, gathered and bound here."
        e "Nothing to hear except for the soft patter of my own footsteps againts the cold stone floors."
        e "Wait... What's this?"
        jump written_letters

        scene bg

    "Searched Library Saved"
    $renpy.take_screenshot()
    $renpy.save('1-5', 'Library')

    menu:
        "Return to city":
            jump city

label written_letters:
    python:
        # Create a sprite manager.
        repulsor = SpriteManager(update=repulsor_update, event=repulsor_event)
        repulsor_sprites = [ ]
        repulsor_pos = None

        # Ensure we only have one smile displayable.
        smile = Image("letter.jpg")

        # Add 400 sprites.
        for i in range(25):
            repulsor_sprites.append(repulsor.create(smile))

        # Position the 400 sprites.
        for i in repulsor_sprites:
            i.x = renpy.random.randint(2, 798)
            i.y = renpy.random.randint(2, 598)

        del smile
        del i

    # Add the repulsor to the screen.
    scene bg table_top
    "..."
    show expression repulsor as repulsor
    ## TODO: Figure out how to toggle interaction
    e "~reads a few letters~ 'The end is here'... 'This is the end'... 'Go to the end'..."
    e "They all say the same thing, who wrote all these?"

    menu:
        "Return to city":
            hide repulsor

            # Clean up.
            python:
                del repulsor
                del repulsor_sprites
                del repulsor_pos

            jump city

label end:
    scene black

    e "This is the end."
    e "Nothing stirs. Not a sound is made."
    e "Goodnight, sweet prince."

    return
