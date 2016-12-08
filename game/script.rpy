## The script of the game goes in this file.

## Declare characters used by this game. The color argument colorizes the name
## of the character.

define e = Character('Eileen')

## Game State
init python:
    visited_city = False
    visited_park = False
    visited_library = False


## Images etc
image bg city = "city.jpg"
image bg park = "park.jpg"
image bg library = "library.jpg"

## The game starts here.

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

    "Searched Library Saved"
    $renpy.take_screenshot()
    $renpy.save('1-5', 'Library')

    menu:
        "Return to city":
            jump city

label end:
    scene black

    e "This is the end."
    e "Nothing stirs. Not a sound is made."
    e "Goodnight, sweet prince."

    return
