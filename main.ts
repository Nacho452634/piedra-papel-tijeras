input.onButtonPressed(Button.A, function on_button_pressed_a() {
    
})
let hand = 0
input.onButtonPressed(Button.A, function on_button_pressed_a_1() {
    
    hand = randint(1, 3)
})
hand = 0
input.onButtonPressed(Button.A, function on_button_pressed_a_2() {
    
    hand = randint(1, 3)
    if (hand == 1) {
        basic.showIcon(IconNames.SmallSquare)
    }
    
})
hand = 0
input.onButtonPressed(Button.A, function on_button_pressed_a_3() {
    
    hand = randint(1, 3)
    if (hand == 1) {
        basic.showIcon(IconNames.SmallSquare)
    } else if (hand == 2) {
        basic.showIcon(IconNames.Square)
    }
    
})
hand = 0
input.onButtonPressed(Button.A, function on_button_pressed_a_4() {
    
    hand = randint(1, 3)
    if (hand == 1) {
        basic.showIcon(IconNames.SmallSquare)
    } else if (hand == 2) {
        basic.showIcon(IconNames.Square)
    } else {
        basic.showIcon(IconNames.Scissors)
    }
    
})
