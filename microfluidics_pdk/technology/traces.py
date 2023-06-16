'''
The traces module is similar to that from technologies.silicon_photonics
'''

# Traces,  waveguides

from ipkiss.technology import get_technology
from ipkiss.technology.technology import DelayedInitTechnologyTree
from ipkiss.process.layer import PPLayer

TECH = get_technology()


# TRACES
class TechTraceTree(DelayedInitTechnologyTree):
    def initialize(self):
        from ipkiss.primitives.layer import Layer
        self.DEFAULT_LAYER = Layer(0)
        self.CONTROL_SHAPE_LAYER = PPLayer(TECH.PROCESS.NONE, TECH.PURPOSE.TRACE)
        self.BEND_RADIUS = 20
        self.DRAW_CONTROL_SHAPE = False


TECH.TRACE = TechTraceTree()

# FIXME - temporary default settings until waveguides have modes

TECH.DEFAULT_WAVELENGTH = 1.55


class TechWgDefaultsTree(DelayedInitTechnologyTree):
    def initialize(self):
        from ipkiss.primitives.layer import Layer
        self.N_EFF = 1.0
        self.N_GROUP = 2.0
        self.LOSS_DB_PERM = 0.0
        self.CORE_LAYER = Layer(0)


TECH.WG_DEFAULTS = TechWgDefaultsTree()

