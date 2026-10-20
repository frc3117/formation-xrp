from commands import CommandInterface
from xrp import XRPMotor

TAG = "Drivetrain:"


class DrivetrainCommand(CommandInterface):

    def __init__(
        self, btns: list[str]
    ):
        """Needs two joystick, first steer and second gas"""
        super().__init__(btns)
        self.leftMotor = XRPMotor(0)
        self.rightMotor = XRPMotor(1)
        self.steerValue = 0
        self.gasValue = 0
        print(f"{TAG} Initialized")

    def update(self) -> None:
        pass

    def _drive(self) -> None:
        self.leftMotor = self.gasValue - self.steerValue
        self.rightMotor = self.gasValue + self.steerValue 

    def _trigger(self, btn_v: float, index: int = 0) -> None:
        if index == 0:
            self.steerValue = btn_v
        elif index == 1:
            self.gasValue = btn_v

        self._drive()