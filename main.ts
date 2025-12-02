input.onGesture(Gesture.Shake, function on_gesture_shake() {
    
})
let hand = 0
input.onGesture(Gesture.Shake, function on_gesture_shake_1() {
    
    hand = randint(1, 3)
})
hand = 0
input.onGesture(Gesture.Shake, function on_gesture_shake_2() {
    
    hand = randint(1, 3)
    if (hand == 1) {
        basic.showIcon(IconNames.SmallSquare)
    }
    
})
hand = 0
input.onGesture(Gesture.Shake, function on_gesture_shake_3() {
    
    hand = randint(1, 3)
    if (hand == 1) {
        basic.showIcon(IconNames.SmallSquare)
    } else if (hand == 2) {
        basic.showIcon(IconNames.Square)
    }
    
})
hand = 0
input.onGesture(Gesture.Shake, function on_gesture_shake_4() {
    
    hand = randint(1, 3)
    if (hand == 1) {
        basic.showIcon(IconNames.SmallSquare)
    } else if (hand == 2) {
        basic.showIcon(IconNames.Square)
    } else {
        basic.showIcon(IconNames.Scissors)
    }
    
})
