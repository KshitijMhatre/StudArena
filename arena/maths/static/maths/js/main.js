var red = anime({
    targets: 'div.box.red',
    translateY: {
    value: 250,
    duration: 800
    },
    rotate: {
    value: 360,
    duration: 1800,
    easing: 'easeInOutSine'
    },
    scale: {
    value: .5,
    duration: 1600,
    delay: 800,
    easing: 'easeInOutQuart'
    },
    autoplay:false,   
    delay: 250 // All properties except 'scale' inherit 250ms delay
    
});

var blue = anime({
    targets: 'div.box.blue',
    translateY: {
    value: 250,
    duration: 800
    },
    rotate: {
    value: 270,
    duration: 1800,
    easing: 'easeInOutSine'
    },
    scale: {
    value: 2,
    duration: 1600,
    delay: 800,
    easing: 'easeInOutQuart'
    },
    autoplay:false,   
    delay: 250 // All properties except 'scale' inherit 250ms delay
});

var green = anime({
    targets: 'div.box.green',
    translateY: {
    value: 250,
    duration: 800
    },
    rotate: {
    value: 200,
    duration: 1800,
    easing: 'easeInOutSine'
    },
    scale: {
    value: 1.2,
    duration: 1600,
    delay: 800,
    easing: 'easeInOutQuart'
    },
    autoplay:false,   
    delay: 250 // All properties except 'scale' inherit 250ms delay
});

var yellow = anime({
    targets: 'div.box.yellow',
    translateX: {
    value: 250,
    duration: 800
    },
    rotate: {
    value: 180,
    duration: 1800,
    easing: 'easeInOutSine'
    },
    scale: {
    value: 2,
    duration: 1600,
    delay: 800,
    easing: 'easeInOutQuart'
    },
    autoplay:false,   
    delay: 250 // All properties except 'scale' inherit 250ms delay
});


