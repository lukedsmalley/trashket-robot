<div align="center">
  <h1>Trashket Robot</h1>
  <h3>Trash-catching mobile wastebasket</h3>
  <h4>Term project for GSU's Embedded Systems course in the spring of 2020 by Luke Smalley, Byron Mouen, and Christian Montoya</h4>
</div>
  
The course instructor was [Doctor Michael Weeks](https://hallertau.cs.gsu.edu/~mweeks/index.html), who maintains [this webpage](https://hallertau.cs.gsu.edu/~mweeks/csc4110/) for the course in current and past terms (Those links are active as this document is written, but is apparently running on some box inside the GSU CS department, so may not be available forever).

The statement submitted for the project abstract/goal was the following:
> Trashketball is the game that every ambitious person with a wad of trash will probably engage in. One plays trashketball using a wad of trash and a trash basket (trashket). A game of trashket ball consists of one or more attempts to toss one's trash into the basket from any distance. One wins at trashketball by throwing the trash such that it lands inside the trashket.
The goal of this project is to create a trashket that moves by itself so that it will catch any trash thrown at it with as much success as possible. To accomplish this, we must construct a mobile robotic system with the capability to track thrown objects. This requires a wastebasket be assembled with a number of other distinct subsystems:<br>- A mobility subsystem that can change direction and move quickly<br>- A vision subsystem to track thrown trash<br>- A subsystem to detect caught trash and keep score (optionally)

Prior art research yielded only the mobile trash can developed by Japanese engineer Minoru Kurata (See Kurata's [development and home demo video](https://www.youtube.com/watch?v=NqDTE6dHpJw) and [expo demo](https://www.youtube.com/watch?v=ZNWd4FFYDv0)). Kurata's trash can uses an elaborate custom-fabricated driving base that allows it to change its direction of travel without rotating the chassis or wastebasket. Thrown trash was tracked using a wall-mounted Microsoft Kinect. Duplicating the mobility system of this device was well beyond our fabrication capabilities. Based on this research, we knew we could either approach object tracking using a stationary camera or a camera mounted to the mobile assembly.

We had plenty of hobby microcontrollers and cameras available between ourselves, but no suitable sets of compatible chassis parts and motors. Since suitably-powerful motors are expensive in the context of a college course, we designed the driving base using the minimum number of motors necessary. A two-wheel, two-motor driving base would minimize the cost of parts, albeit sacrificing our ability to turn quickly. We prepared to buy the lowest-cost motors, but a friend lent us a pair of [VEX 393 motors](https://www.vexrobotics.com/motors.html), along with the 7.2V batteries used by the VEX system.

LEGO Technic parts were the most readily accessible material for a chassis, but the VEX motors needed to be attached to the LEGO beams, gearing, and wheels. Because we had access to a 3D printer, we designed and printed components to connect VEX motors and axle to Technic parts.

*Render of the VEX-LEGO axle coupler:*

![Axle coupler render](./images/axle-coupler.jpg)

*Render of the VEX-LEGO motor-mounting bracket:*

![Motor mount render](./images/motor-mount.jpg)

*VEX motors with 1/8" axle mounted and interfaced with the final LEGO chassis:*

![Printed parts installed](./images/printed-parts-installed.jpg)

An initial prototype served as proof-of-concept for the circuitry, though it was all super basic (and remained elementary for the duration of the project). The chassis was constructed to carry the minimum necessary electronics, but not a full-sized trash can. This first assembly was also a test of strength for the chassis and gearing, to see if the LEGO parts could support the torque of the VEX motors. The prototype only used two MOSFETs to control the motors, and could only drive forward.

The electronics configuration of the first prototype was as follows:
```
    +--------------+                 +--------+     +------------+
    | 7.2V Battery | -----------.--> | MOSFET | --> | Left Motor |
    +--------------+            |    +--------+     +------------+
           |                    v         ^ 
           v                 +--------+   |    +-------------+
+-----------------------+    | MOSFET | --:--> | Right Motor |
| 6-12V to 5V Converter |    +--------+   |    +-------------+
+-----------------------+         ^       |
           |                      |       |
           v                      |       |
   +-----------------+            |       |
   | Raspberry Pi 3B | -----------'-------' 
   +-----------------+
```

*Wonderful photo of the first prototype:*

![Initial prototype](./images/initial-prototype.jpg)