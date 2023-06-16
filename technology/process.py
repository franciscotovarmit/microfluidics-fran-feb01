'''

# -------------------
# | Process Script. |
# -------------------

Created by Mark Sison.

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

# TECH.PROCESS = ProcessTechnologyTree()
# TECH.PROCESS.overwrite_allowed += ['CH_PRO']

TECH.PROCESS.CHANNEL_1 = ProcessLayer(name = "Channel 1.", extension = "CH1")
TECH.PROCESS.CHANNEL_2 = ProcessLayer(name = "Channel 2.", extension = "CH2")
TECH.PROCESS.PART_HOLDER = ProcessLayer(name = "Holder for External Part.", extension = "PART_H")
TECH.PROCESS.NONE = ProcessLayer(name = "None.", extension = "NONE")

# TECH.PROCESS.overwrite_allowed.remove('CH_PRO')

# ---------------------
# | Drawing Purposes. |
# ---------------------

# [What should be done with the Geometric Patterns which are defined.]

# TECH.PURPOSE = TechnologyTree()

TECH.PURPOSE.CREATE_CHANNEL = PatternPurpose(name = "Create Channel.", extension = "CH_CREATE")
TECH.PURPOSE.PLACE_PART = PatternPurpose(name = "Create Channel.", extension = "CH_CREATE")
TECH.PURPOSE.NONE = PatternPurpose(name = "None.", extension = "NONE")

# ---------------------------
# | Process Purpose Layers. |
# ---------------------------

# TECH.PPLAYER = TechnologyTree()

TECH.PPLAYER.CH1 = TechnologyTree()
TECH.PPLAYER.CH1.TRENCH = PPLayer(process = TECH.PROCESS.CHANNEL_1,
                                              purpose = TECH.PURPOSE.CREATE_CHANNEL,
                                              name = "CH_TRENCH1")

TECH.PPLAYER.CH2 = TechnologyTree()
TECH.PPLAYER.CH2.TRENCH = PPLayer(process = TECH.PROCESS.CHANNEL_2,
                                              purpose = TECH.PURPOSE.CREATE_CHANNEL,
                                              name = "CH_TRENCH2")

TECH.PPLAYER.PART_H = TechnologyTree()
TECH.PPLAYER.PART_H.PART = PPLayer(process = TECH.PROCESS.PART_HOLDER,
                                        purpose = TECH.PURPOSE.PLACE_PART,
                                        name = "PART")

TECH.PPLAYER.CH1.ALL = TECH.PPLAYER.CH1.TRENCH
TECH.PPLAYER.CH2.ALL = TECH.PPLAYER.CH2.TRENCH
TECH.PPLAYER.PART_H.ALL = TECH.PPLAYER.PART_H.PART

# End.