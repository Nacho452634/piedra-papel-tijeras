
def on_gesture_shake():
    pass
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

hand = 0

def on_gesture_shake_1():
    global hand
    hand = randint(1, 3)
input.on_gesture(Gesture.SHAKE, on_gesture_shake_1)

hand = 0

def on_gesture_shake_2():
    global hand
    hand = randint(1, 3)
    if hand == 1:
        basic.show_icon(IconNames.SMALL_SQUARE)
input.on_gesture(Gesture.SHAKE, on_gesture_shake_2)

hand = 0

def on_gesture_shake_3():
    global hand
    hand = randint(1, 3)
    if hand == 1:
        basic.show_icon(IconNames.SMALL_SQUARE)
    elif hand == 2:
        basic.show_icon(IconNames.SQUARE)
input.on_gesture(Gesture.SHAKE, on_gesture_shake_3)

hand = 0

def on_gesture_shake_4():
    global hand
    hand = randint(1, 3)
    if hand == 1:
        basic.show_icon(IconNames.SMALL_SQUARE)
    elif hand == 2:
        basic.show_icon(IconNames.SQUARE)
    else:
        basic.show_icon(IconNames.SCISSORS)
input.on_gesture(Gesture.SHAKE, on_gesture_shake_4)