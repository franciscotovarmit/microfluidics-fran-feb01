# Collections of default PCells
#

from ipkiss.technology import get_technology
from ipkiss.technology.technology import DelayedInitTechnologyTree, TechnologyTree
from ipkiss.process.layer import PPLayer
TECH = get_technology()

# Default channel template used in routing


class FluidChannelTechTree(DelayedInitTechnologyTree):

    def initialize(self):
        from ..components.channel import FluidChannelTemplate
        self.DEFAULT = FluidChannelTemplate()

TECH.PCELLS.FLUID_CHANNEL = FluidChannelTechTree()

class VacuumChannelTechTree(DelayedInitTechnologyTree):

    def initialize(self):
        from ..components.channel import VacuumChannelTemplate
        self.DEFAULT = VacuumChannelTemplate()

TECH.PCELLS.VACUUM_CHANNEL = VacuumChannelTechTree()


# Required for ipkiss3.all import
TECH.PCELLS.WG = FluidChannelTechTree()


# Auto-transition database

class TransitionTree(DelayedInitTechnologyTree):

    def initialize(self):
        from ipkiss3.pcell.trace.transitions.auto_transition.auto_transition_db import AutoTransitionDatabase
        db = AutoTransitionDatabase()
        self.AUTO_TRANSITION_DATABASE = db


TECH.PCELLS.TRANSITION = TransitionTree()
