'''

# ------------------------
# | Initialisation File. |
# ------------------------

Created by Mark Sison.

'''

# ------------
# | Imports. |
# ------------
from ipkiss.technology import TECHNOLOGY as TECH

__all__ = ["TECH"]

TECH.name = "MICROFLUIDICS"

from technologies.base_ipkiss.admin import *            # PCell Name Generators.
from technologies.base_ipkiss.mask import *            # Basic Mask Definitions.

from .metrics import *
from .process import *                      # Process Layers and Drawing Purposes.
from .rules import *                      # Rules for each layer
from .display import *                    # Visualization settings
from technologies.base_ipkiss.pcells import *        # Basic default PCells lib
from .traces import *                     # Basic trace settings and default waveguide template
from technologies.base_ipkiss.blocks import *                     # Settings for blocks and adapters
from .ports import *                      # Basic settings for ports
#from technologies.base_ipkiss.transitions import *   # Auto-TraceTransition database
from .gdsii import *                      # GDSII import/export settings
from .materials import *                  # Materials and material stacks (example for silicon photonics)
from .vfab import *                       # Virtual fabrication flow and settings
from .pcells import *                                 # All PCell that are in the TECH-tree
