# trashket-robot/scripts/server.py
# by Christian Moronta

from flask import Flask
from flask import render_template, request
from gpiozero import LED, PWMLED
import time

needRamp = True

app = Flask(__name__)

print("done")

lb1 = LED(17, initial_value=True)
lb2 = LED(27, initial_value=True)
lf1 = LED(22, initial_value=True)
lf2 = LED(23, initial_value=True)
rf1 = LED(9, initial_value=True)
rf2 = LED(10, initial_value=True)
rb1 = LED(24, initial_value=True)
rb2 = LED(25, initial_value=True)
# lf1.off()
# lf2.off()
# rf1.off()
# rf2.off()
# lb1.off()
# lb2.off()
# rb1.off()
# rb2.off()

speed = PWMLED(11)
speed.value = 0.16


@app.route("/")
def index():
    return render_template('index.html')


@app.route('/left_side')
def left_side():
    data1 = "LEFT"
    rf1.off()
    rf2.off()
    return 'true'


@app.route('/right_side')
def right_side():
    data1 = "RIGHT"
    lf1.off()
    lf2.off()
    return 'true'


@app.route('/up_side')
def up_side():
    data1 = "FORWARD"
    global needRamp
    lf1.off()
    lf2.off()
    rf1.off()
    rf2.off()
    needRamp = False
    return 'true'


@app.route('/down_side')
def down_side():
    data1 = "BACK"
    rb1.off()
    rb2.off()
    lb1.off()
    lb2.off()
    return 'true'


@app.route('/stop')
def stop():
    data1 = "STOP"
    global needRamp
    lf1.on()
    lf2.on()
    rf1.on()
    rf2.on()
    lb1.on()
    lb2.on()
    rb1.on()
    rb2.on()
    needRamp = True
    return 'true'


if __name__ == "__main__":
    print("Start")
    app.run(host='0.0.0.0', port=5010)
