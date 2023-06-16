'''

# -------------------
# | Process Script. |
# -------------------

Author: Thach Nguyen

'''

# ------------
# | Imports. |
# ------------

from ipkiss.technology.technology import ProcessTechnologyTree, TechnologyTree, DelayedInitTechnologyTree
from ipkiss.technology import get_technology
from ipkiss.process.layer import ProcessLayer, PatternPurpose, PPLayer

TECH = get_technology()

# -------------------
# | Process Layers. |
# -------------------

# [The Lithography Step using the Fabrication Process.]

TECH.PROCESS = ProcessTechnologyTree()

TECH.PROCESS.FLUID = ProcessLayer(name = "Microfluidics process", extension = "FLUID")
TECH.PROCESS.VACUUM = ProcessLayer(name = "Vacumm process", extension = "VACUUM")
TECH.PROCESS.MISC = ProcessLayer(name = "Misc process ", extension = "MISC")
TECH.PROCESS.NONE = ProcessLayer(name = "None.", extension = "NONE")

# The WG process is required so that ipkiss3.all can be imported
TECH.PROCESS.WG = TECH.PROCESS.FLUID

# ---------------------
# | Drawing Purposes. |
# ---------------------

# [What should be done with the Geometric Patterns which are defined.]

TECH.PURPOSE = TechnologyTree()

TECH.PURPOSE.DRAWING = PatternPurpose(name="Drawing", extension="DRW")
TECH.PURPOSE.NONE = PatternPurpose(name = "None.", extension = "NONE")
TECH.PURPOSE.LOGOTXT = PatternPurpose("LOGOTXT","TXT")
TECH.PURPOSE.DOC = PatternPurpose(name="Documentation", extension="DOC")
TECH.PURPOSE.BBOX = PatternPurpose(name="Bounding Box", extension="BBOX")
TECH.PURPOSE.PINREC = PatternPurpose(name="Pin recognition", extension="PIN", doc="Pin marker for extraction")
TECH.PURPOSE.DEVREC = PatternPurpose(name="Device recognition", extension="DEV", doc="Device marker for extraction")
TECH.PURPOSE.LABEL = PatternPurpose(name="Device/pin label", extension="LAB", doc="Label for devices or pins")
TECH.PURPOSE.TRACE = PatternPurpose(name="Trace", extension="TRC", doc="Control shape of trace")
TECH.PURPOSE.ERROR = PatternPurpose(name="Error", extension="ERR", doc="Errors")
TECH.PURPOSE.TEXT = PatternPurpose(name="Text", extension="TXT", doc="Text")

# ---------------------------
# | Process Purpose Layers. |
# ---------------------------

TECH.PPLAYER = TechnologyTree()

TECH.PPLAYER.FLUID = TechnologyTree()
TECH.PPLAYER.FLUID.TRENCH = PPLayer(process = TECH.PROCESS.FLUID,
                                              purpose = TECH.PURPOSE.DRAWING,
                                              name = "FLUID_TRENCH")

TECH.PPLAYER.VACUUM = TechnologyTree()
TECH.PPLAYER.VACUUM.TRENCH = PPLayer(process = TECH.PROCESS.VACUUM,
                                              purpose = TECH.PURPOSE.DRAWING,
                                              name = "VACUUM_TRENCH")

TECH.PPLAYER.MISC = TechnologyTree()
TECH.PPLAYER.MISC.TRENCH = PPLayer(process = TECH.PROCESS.MISC,
                                        purpose = TECH.PURPOSE.DRAWING,
                                        name = "MISC")

TECH.PPLAYER.FLUID.ALL = TECH.PPLAYER.FLUID.TRENCH
TECH.PPLAYER.VACUUM.ALL = TECH.PPLAYER.VACUUM.TRENCH
TECH.PPLAYER.MISC.ALL = TECH.PPLAYER.MISC.TRENCH

TECH.PPLAYER.NONE = TechnologyTree()
TECH.PPLAYER.NONE.LOGOTXT = PPLayer(TECH.PROCESS.NONE, TECH.PURPOSE.LOGOTXT,name="LOGOTXT")
TECH.PPLAYER.NONE.DOC = PPLayer(TECH.PROCESS.NONE, TECH.PURPOSE.DOC, name="NONE_DOC") # Just  for documentation purpuses.
TECH.PPLAYER.NONE.BBOX= PPLayer(TECH.PROCESS.NONE, TECH.PURPOSE.BBOX, name="Bounding Box")
TECH.PPLAYER.NONE.PINREC = PPLayer(TECH.PROCESS.NONE, TECH.PURPOSE.PINREC, name="PINREC")

TECH.PPLAYER.ERROR = TechnologyTree()
TECH.PPLAYER.ERROR.GENERIC = PPLayer(TECH.PROCESS.NONE, TECH.PURPOSE.ERROR, name="ERROR") # Generic Error indication
TECH.PPLAYER.ERROR.CROSSING = TECH.PPLAYER.ERROR.GENERIC

# Required for ipkiss3.all import
TECH.PPLAYER.WG = TechnologyTree() # we assume a DF mask
TECH.PPLAYER.WG.CORE = PPLayer(TECH.PROCESS.NONE, TECH.PURPOSE.TRACE)
TECH.PPLAYER.WG.CLADDING = PPLayer(TECH.PROCESS.NONE, TECH.PURPOSE.TRACE)
TECH.PPLAYER.WG.TRENCH = PPLayer(TECH.PROCESS.NONE, TECH.PURPOSE.TRACE)
TECH.PPLAYER.WG.HOLE = PPLayer(TECH.PROCESS.NONE, TECH.PURPOSE.TRACE)
TECH.PPLAYER.WG.TEXT = PPLayer(TECH.PROCESS.NONE, TECH.PURPOSE.TRACE)

# End.