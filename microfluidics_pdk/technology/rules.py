'''
The rules module is similar to that from technologies.silicon_photonics
The processes not relevant to the EBL silicon photonics have been removed or modified
'''

############################################################################################
# RULES
# 
# This file contains default settings which are used throughout Ipkiss and Picazzo
# - Some global settings
# - Per process layer settings, like minimum width, default width, default bend radius, ....
############################################################################################

from ipkiss.technology import get_technology
from ipkiss.technology.technology import TechnologyTree, DelayedInitTechnologyTree
from ipkiss.geometry.shapes.basic import ShapeRectangle

TECH = get_technology()

# Overall rules
# At the moment, minimum line and space are specified on a global level, not per layer.
TECH.TECH = TechnologyTree()
TECH.TECH.MINIMUM_LINE = 0.120
TECH.TECH.MINIMUM_SPACE = 0.120

# WG SETTINGS
# The following are required so that ipkiss3.all can be imported
#############
TECH.WG = TechnologyTree()
TECH.WG.WIRE_WIDTH = 0.45
TECH.WG.TRENCH_WIDTH = 2.0
TECH.WG.CLADDING_WIDTH = TECH.WG.WIRE_WIDTH + 2 * TECH.WG.TRENCH_WIDTH
TECH.WG.BEND_RADIUS = 5.0
TECH.WG.SPACING = 2.0
TECH.WG.DC_SPACING = TECH.WG.WIRE_WIDTH + 0.18
TECH.WG.SHORT_STRAIGHT = 2.0
TECH.WG.SHORT_TRANSITION_LENGTH = 5.0
TECH.WG.OVERLAP_EXTENSION = 0.020
TECH.WG.OVERLAP_TRENCH = 0.010
TECH.WG.EXPANDED_WIDTH = 0.8
TECH.WG.EXPANDED_TAPER_LENGTH = 3.0
TECH.WG.EXPANDED_STRAIGHT = 5.0
TECH.WG.ANGLE_STEP = 1.0
TECH.WG.SLOT_WIDTH = 0.15
TECH.WG.SLOTTED_WIRE_WIDTH = 0.7
# backward compatibility
TECH.WG.SHORT_TAPER_LENGTH = TECH.WG.SHORT_TRANSITION_LENGTH
