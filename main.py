
def on_button_pressed_a():
    pass
input.on_button_pressed(Button.A, on_button_pressed_a)

hand = 0

def on_button_pressed_a_1():
    global hand
    hand = randint(1, 3)
input.on_button_pressed(Button.A, on_button_pressed_a_1)

hand = 0

def on_button_pressed_a_2():
    global hand
    hand = randint(1, 3)
    if hand == 1:
        basic.show_icon(IconNames.SMALL_SQUARE)
input.on_button_pressed(Button.A, on_button_pressed_a_2)

hand = 0

def on_button_pressed_a_3():
    global hand
    hand = randint(1, 3)
    if hand == 1:
        basic.show_icon(IconNames.SMALL_SQUARE)
    elif hand == 2:
        basic.show_icon(IconNames.SQUARE)
input.on_button_pressed(Button.A, on_button_pressed_a_3)

hand = 0

def on_button_pressed_a_4():
    global hand
    hand = randint(1, 3)
    if hand == 1:
        basic.show_icon(IconNames.SMALL_SQUARE)
    elif hand == 2:
        basic.show_icon(IconNames.SQUARE)
    else:
        basic.show_icon(IconNames.SCISSORS)
input.on_button_pressed(Button.A, on_button_pressed_a_4)