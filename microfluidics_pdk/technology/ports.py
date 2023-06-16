
# Ports

from ipkiss.technology import get_technology
from ipkiss.technology.technology import DelayedInitTechnologyTree

TECH = get_technology()

class TechPortTree(DelayedInitTechnologyTree):
    def initialize(self):
        self.DEFAULT_LAYER = TECH.PPLAYER.NONE.PINREC
        self.DEFAULT_LENGTH = 0.1

TECH.PORT = TechPortTree()
