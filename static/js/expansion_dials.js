function drawDials() {
    let blocks = document.getElementsByClassName('bm-monitor-info-block')

    for (let block of blocks) {

        let value = block.getAttribute('value')
        if (value) {
            let min = block.getAttribute('min')
            let max = block.getAttribute('max')
            let unit = block.getAttribute('unit')
            let colour = getDialColour(value, min, max)
            let dialElm = block.getElementsByClassName('bm-monitor-dial__wrapper')[0]

            let colourClassName = 'bm-monitor-info-block--' + colour
            block.classList.add(colourClassName)
            drawDial(dialElm, value, min, max, colour, unit)
        }
    }

}

function drawDial(element, value, min, max, colour, unit) {
    const knob = pureknob.createKnob(250, 150);
    knob.setProperty('angleStart', -0.6 * Math.PI);
    knob.setProperty('angleEnd', 0.6 * Math.PI);
    knob.setProperty('trackWidth', 0.5);
    knob.setProperty('valMin', min);
    knob.setProperty('valMax', max);
    knob.setProperty('readonly', true)

    setDialColour(knob, colour)

    knob.setValue(value, unit);

    const node = knob.node();
    element.appendChild(node);
}

function getDialColour(value, min, max) {
    if (value < min || value > max) {
        return 'red'
    } else {
        return 'green'
    }
}

function setDialColour(knob, colour) {
    if (colour === 'red') {
        knob.setProperty('colorFG', '#ff0000');
    } else if (colour === 'green') {
        knob.setProperty('colorFG', '#168039');
    }
}

window.onload = (event) => {
    drawDials();
};