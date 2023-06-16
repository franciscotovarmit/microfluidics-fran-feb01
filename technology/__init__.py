'''

# ------------------------
# | Initialisation File. |
# ------------------------

Created by Mark Sison.

'''

# ------------
# | Imports. |
# ------------

from technologies.silicon_photonics import TECH

__all__ = ["TECH"]

TECH.name = "MICROFLUIDICS"

from technologies.base_ipkiss.admin import *            # PCell Name Generators.
from technologies.base_ipkiss.mask import *            # Basic Mask Definitions.

# from .metrics import *
from .process import *                      # Process Layers and Drawing Purposes.
from .gdsii import *                        # GDSII Import and Export Settings.
from .display import *

from technologies.base_ipkiss.pcells import *          # Basic PCell Library.

from .materials import *                    # Materials and Material Stack.
# from .traces import *
from .vfab import *                         # Virtual Fabrication Flow and Settings.
