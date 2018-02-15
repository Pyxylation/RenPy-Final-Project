# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Adam's")
define h = Character("The Man")



# The game starts here.
label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.
    # file formats need to be either .png or .jpg, dont use .gif
    scene black

    play music "spookymusic.mp3"  #Add in music, the MP3 file takes a few seconds to fade in, but you can fade with RenPy
    "Deep in the forest, there are many things learking!"
    "Some are unholy, others are demoni, and yet others are....."

    play music "bighit.mp3"
    scene bg bigfield

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    # make sure that characrer name is lowercase, or else it wont display
    show homestar realmouthopen:
        yalign .5 # y axis align, to move the characte to another position
        linear 1 xalign .9 # x axis align, there is no need to change the pic, thats mickey mouse
            #linear makes it move on the axis that the "linear" text is located next to
            # here are all the align options: https://www.renpy.org/doc/html/style_properties.html

    # These display lines of dialogue.

    h "I'm Homestar! This is a website... I mean game!!!!"
    stop music
    h "Hey! Where my body! I know I left it around here somewhere!"

    show homestar glowing
    h "Oooooo, here we go! I found it!"

    show homestar fullbody:
        yalign 1.0 # The .0 is VITAL for this statement to work, dont forget it!!!
        xalign .5


    h "Now on to the next problem..."
    h "how much money should I give Strongbad?"
<<<<<<< HEAD
    $ num = 0
=======
    $num = 0 
    renpy.
>>>>>>> a1fc2a6f5f024bdbe833883f86dc612e22104d9e



    # This ends the game.
    return
