'''

Created by Mark Sison.

'''

# *** Material Stack. ***

# Imports.

from pysics.basics.material.material_stack import MaterialStack
from pysics.materials.electromagnetics import *
from pysics.basics.material.material import Material, MaterialFactory
from ipkiss.visualisation.display_style import DisplayStyle
from ipkiss.visualisation.color import *
from .layer_thickness import *

TECH.overwrite_allowed.append('MATERIALS')

# Custom Material.

TECH.MATERIALS = MaterialFactory()

TECH.MATERIALS.FLUID = Material(name = "fluid", display_style = DisplayStyle(color = COLOR_BLUE), solid = False)
TECH.MATERIALS.SU8 = Material(name = "su8", display_style = DisplayStyle(color = COLOR_CYAN))
TECH.MATERIALS.AIR = Material(name = "air", display_style = DisplayStyle(color = COLOR_GREEN), solid = False)
TECH.MATERIALS.SILICON_OXIDE = Material(name = "silicon oxide", display_style = DisplayStyle(color = COLOR_BLUE))
TECH.MATERIALS.SILICON = Material(name = "silicon", display_style = DisplayStyle(color = COLOR_YELLOW))

MSTACK_SU8_HEIGHT = 100

TECH.overwrite_allowed.append('MATERIAL_STACKS')
TECH.MATERIAL_STACKS = MaterialStackFactory()

TECH.MATERIAL_STACKS.MSTACK_SU8 = MaterialStack(name = "SU8",
                                                # Material Height = [(Material, Height)]
                                                materials_heights = [(TECH.MATERIALS.SU8, TECH.MSTACK_SU8_HEIGHT * 2 + TECH.MSTACK_FLUID_CHANNEL_HEIGHT)],
                                                display_style = DisplayStyle(color = COLOR_GREEN))

TECH.MATERIAL_STACKS.MSTACK_FLUID_CHANNEL = MaterialStack(name = "Fluid",
                                                    materials_heights = [(TECH.MATERIALS.SU8, TECH.MSTACK_SU8_HEIGHT),
                                                                         (TECH.MATERIALS.FLUID, TECH.MSTACK_FLUID_CHANNEL_HEIGHT),
                                                                         (TECH.MATERIALS.SU8, TECH.MSTACK_SU8_HEIGHT)],
                                                    display_style = DisplayStyle(color = COLOR_BLUE))

TECH.MATERIAL_STACKS.MSTACK_AIR_CHANNEL = MaterialStack(name = "Air",
                                                    materials_heights = [(TECH.MATERIALS.SU8, TECH.MSTACK_SU8_HEIGHT),
                                                                         (TECH.MATERIALS.AIR, TECH.MSTACK_VACUUM_CHANNEL_HEIGHT),
                                                                         (TECH.MATERIALS.SU8, TECH.MSTACK_SU8_HEIGHT)],
                                                    display_style = DisplayStyle(color = COLOR_YELLOW))
