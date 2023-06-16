'''

Created by Mark Sison.

'''

# ------------
# | Metrics. |
# ------------

# Imports.

from ipkiss.technology import get_technology
from ipkiss.technology.technology import TechnologyTree

TECH = get_technology()

TECH.METRICS = TechnologyTree()
TECH.METRICS.GRID = 5E-9           # Drawing grid [m]: 5nm
TECH.METRICS.UNIT = 1E-6           # User unit [m]: um
TECH.METRICS.ANGLE_STEP = 1.0      # Angle step for curve discretization [degrees]: 1 degree
TECH.METRICS.overwrite_allowed = ["UNIT", "GRID", "ANGLE_STEP"]