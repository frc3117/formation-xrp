
#!/usr/bin/env python3
# partir la sim: on ajoute venv, on tape robotpy sim
# pour partir le robot: py -3 -m robotpy sim --xrp
# pour arrêter faire control-c
# Copyright (c) FIRST et autres contributeurs WPILib.
# Open Source Software; you can modify and/or share it under the terms of
# the WPILib BSD license file in the root directory of this project.
#
# Les servent à écrire des commentaires.
#  Démarrer le programme
# ---------------
# pour démarrer le programme, il faut passer par le ws-client.
#
#    # Windows
#    py -3 -m robotpy sim --xrp
# C’est avec cette commande, tapée dans le terminal, qu’on démarre le programme.
#
#    # Linux/macOS/Chromebook
#    python -m robotpy sim --xrp
#
# Par défault la simulation WPILib GUI sera affichée. C'est le dashboard. Pour ne pas
# l'afficher vous pouvez faire ajouter: --nogui
#


import os
import wpilib

# Ceci rejoint le XRP par défault.
os.environ["HALSIMXRP_HOST"] = "192.168.42.1"
os.environ["HALSIMXRP_PORT"] = "3540"

import wpilib

from commands import CommandInterface
from config import config
from subsystems.remote import RemoteControllerSS


"""
The Robot class 
"""

class Robot(wpilib.TimedRobot):
    """
    Entrypoint of the program
    """
    def robotInit(self):
        """
        We fetch the config here
        It is here we bind and setup the command
        """
        self._controller = RemoteControllerSS(config.get("controller"))
        self._commands: list[CommandInterface] = config["commands"]

        for command in self._commands:
            command.bind(self._controller)

    def teleopPeriodic(self):
        self._controller.update()
        self._controller.execute()
        
        for command in self._commands:
            command.update()