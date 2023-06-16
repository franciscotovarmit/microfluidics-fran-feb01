'''

Created by Mark Sison.

'''

# *** Traces. ***

# Imports.

from ipkiss.technology import get_technology
from ipkiss.technology.technology import DelayedInitTechnologyTree
from ipkiss.process.layer import PPLayer

TECH = get_technology()

# Traces.

class TechTraceTree(DelayedInitTechnologyTree):
    def initialize(self):
        from ipkiss.primitives.layer import Layer
        self.DEFAULT_LAYER = Layer(0)
        self.CONTROL_SHAPE_LAYER = PPLayer(TECH.PROCESS.NONE, TECH.PURPOSE.NONE)
        self.BEND_RADIUS = 5.0
        self.DRAW_CONTROL_SHAPE = False
        
# TECH.TRACE = TechTraceTree()

# FIXME - temporary default settings until waveguides have modes

TECH.DEFAULT_WAVELENGTH = 1.55

class TechWgDefaultsTree(DelayedInitTechnologyTree):
    def initialize(self):
        from ipkiss.primitives.layer import Layer
        self.N_EFF = 1.0
        self.N_GROUP   = 2.0
        self.LOSS_DB_PERM = 0.0
        self.CORE_LAYER = Layer(0)


TECH.WG_DEFAULTS = TechWgDefaultsTree()

# Default waveguide pcells

class TechWgTree(DelayedInitTechnologyTree):
    def initialize(self):
        from picazzo3.traces.wire_wg.trace import WireWaveguideTemplate
    
        self.WIRE = WireWaveguideTemplate(name="WIRE_WG_TEMPLATE",
                                          library=TECH.PCELLS.LIB)
        self.WIRE.Layout(core_width=TECH.WG.WIRE_WIDTH, 
                         cladding_width=TECH.WG.CLADDING_WIDTH,
                         core_process=TECH.PROCESS.WG
                         )
        
        self.WIRE.CapheModel(n_eff=2.86, 
                             n_g=2.86, 
                             center_wavelength=1.55, 
                             loss_dB_m=0.0) # Default values
                
        self.DEFAULT = self.WIRE

TECH.PCELLS.WG = TechWgTree()


class TechWireTree(DelayedInitTechnologyTree):
    def initialize(self):
        from picazzo3.traces.electrical_wire import ElectricalWireTemplate
        tpl = ElectricalWireTemplate(name="DEFAULT_WIRE_TEMPLATE",
                                     library=TECH.PCELLS.LIB)
        self.WIRE = tpl
        self.DEFAULT = self.WIRE

TECH.PCELLS.METAL = TechWireTree()
