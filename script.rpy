# Declare the sprite
image criminal_bucket = "criminal_bucket.png"

# Declare backgrounds
image bg photo_1_2025-03-23_07-04-11 = "photo_1_2025-03-23_07-04-11.png"
image bg background = "background.png"

# Declare character
define buck = Character("Buck")

# The game starts here
label start:
    "I'm so tired."

    # Jump to the sprites section
    jump sprites

label sprites:
    scene bg background  # Set background first

    show criminal_bucket  # Show sprite on top of background

    buck "So, so tired."

    buck "Uhhhhh..."

    jump background  # Jump to next scene

label background:
    scene bg photo_1_2025-03-23_07-04-11  # Change the background

    show criminal_bucket  # Show sprite again after background change

    buck "Okay, time to explore new places."

    return
