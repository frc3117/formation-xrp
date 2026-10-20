from commands import CommandInterface
from xrp import XRPServo
import math

class ArmCommand(CommandInterface):

    def __init__(self, btn_id: str):
        super().__init__(btn_id)
        self.servo = XRPServo(4)

    def _trigger(self, btn_v: bool, index: int = 0) -> None:
        if btn_v == 1:
            self.servo.setAngle(math.degrees(90))
        elif btn_v == 0:
            self.servo.setAngle(math.degrees(30))
