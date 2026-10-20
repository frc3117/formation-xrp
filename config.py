import wpilib

from commands import (
    DrivetrainCommand,
    ArmCommand,
)

"""
Here is the approach we used to program the robot:

The config file is used to specify Controller Inputs, Commands and Actuators,

The Controller input should have function that returns updated data for the given input label
The Inputs are either classified as axies (float) or buttons (int)
The Input functions key are used as labels to link input events

The Commands should be instanciated in the config variable.
Each command should be created using the constructor defined in the class.
A command can take either a single input label or an array of input labels.
A command can necessitate motors or digital inputs, in either cases they should be
instanciated and populated with the correct CAN id and minimal configuration.

We want the config to remain as simple and efficient as possible so we can create and edit I/Os on the fly
"""

# We define base wpilib instances so we do not create / destroy in each lambda call
_input_remote = wpilib.Joystick(0)

config = {
    # Will be used and imported directly by subsystems and modules
    "controller": {
        "axies": {
            # ID : Function inside a tuple
            ("leftRightAxis", lambda: _input_remote.getRawAxis(0)),
            ("gasAxis", lambda: ((- _input_remote.getRawAxis(2)) + _input_remote.getRawAxis(3))),
        },
        "buttons": {
            # ID : Function inside a tuple
            ("btnA", lambda: _input_remote.getRawButton(1)),
            ("btnB", lambda: _input_remote.getRawButton(2)),
            ("btnX", lambda: _input_remote.getRawButton(3)),
            ("btnY", lambda: _input_remote.getRawButton(4)),
            ("btn5", lambda: _input_remote.getRawButton(5)),
            ("btn6", lambda: _input_remote.getRawButton(6)),
            ("btn7", lambda: _input_remote.getRawButton(7)),
            ("btn8", lambda: _input_remote.getRawButton(8)),
            ("btn9", lambda: _input_remote.getRawButton(9)),
            ("btn10", lambda: _input_remote.getRawButton(10)),
            ("btn11", lambda: _input_remote.getRawButton(11)),
        },
    },
    # List of commands to bind to the robot
    # A command only has one input trigger
    "commands": [
        # Initialize your commands here\
        DrivetrainCommand(
            ["leftRightAxis", "gasAxis"],
        ),
        ArmCommand(
            "btnA"
        )
    ],
}
