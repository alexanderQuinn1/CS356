function draw_dials() {


    const flasks = document.getElementsByName('flask_monitor_display');

    flasks.forEach(flask => {

    })

    const node = knob.node();
    const knob = pureknob.createKnob(300, 300);
    knob.setProperty('angleStart', -0.75 * Math.PI);
    knob.setProperty('angleEnd', 0.75 * Math.PI);
    knob.setProperty('colorFG', '#88ff88');
    knob.setProperty('trackWidth', 0.4);
    knob.setProperty('valMin', 0);
    knob.setProperty('valMax', 100);
    knob.setValue(37.2);

    elem.appendChild(node);

}