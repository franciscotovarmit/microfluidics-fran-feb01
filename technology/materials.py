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

TECH.overwrite_allowed.append('MATERIALS')

# Custom Material.

TECH.MATERIALS = MaterialFactory()

TECH.MATERIALS.FLUID = Material(name = "fluid", display_style = DisplayStyle(color = COLOR_BLUE), solid = False)
TECH.MATERIALS.SU8 = Material(name = "su8", display_style = DisplayStyle(color = COLOR_CYAN))
TECH.MATERIALS.AIR = Material(name = "air", display_style = DisplayStyle(color = COLOR_GREEN), solid = False)
TECH.MATERIALS.SILICON_OXIDE = Material(name = "silicon oxide", display_style = DisplayStyle(color = COLOR_BLUE))
TECH.MATERIALS.SILICON = Material(name = "silicon", display_style = DisplayStyle(color = COLOR_YELLOW))

MSTACK_SU8_HEIGHT = 100
MSTACK_CHANNEL_HEIGHT = 100

TECH.overwrite_allowed.append('MATERIAL_STACKS')
TECH.MATERIAL_STACKS = MaterialStackFactory()

TECH.MATERIAL_STACKS.MSTACK_SU8 = MaterialStack(name = "SU8",
                                                # Material Height = [(Material, Height)]
                                                materials_heights = [(TECH.MATERIALS.SU8, MSTACK_SU8_HEIGHT * 2 + MSTACK_CHANNEL_HEIGHT)],
                                                display_style = DisplayStyle(color = COLOR_GREEN))

TECH.MATERIAL_STACKS.MSTACK_CHANNEL = MaterialStack(name = "Channel",
                                                    materials_heights = [(TECH.MATERIALS.SU8, MSTACK_SU8_HEIGHT),
                                                                         (TECH.MATERIALS.FLUID, MSTACK_CHANNEL_HEIGHT),
                                                                         (TECH.MATERIALS.SU8, MSTACK_SU8_HEIGHT)],
                                                    display_style = DisplayStyle(color = COLOR_BLUE))

TECH.MATERIAL_STACKS.MSTACK_TALL_CHANNEL = MaterialStack(name = "Tall Channel",
                                                         materials_heights = [(TECH.MATERIALS.SU8, MSTACK_SU8_HEIGHT),
                                                                              (TECH.MATERIALS.FLUID, MSTACK_CHANNEL_HEIGHT * 2),
                                                                              (TECH.MATERIALS.SU8, MSTACK_SU8_HEIGHT)],
                                                         display_style = DisplayStyle(color = COLOR_RED))

TECH.MATERIAL_STACKS.MSTACK_EXTERNAL_PART = MaterialStack(name = "Biosensor Base",
                                                         materials_heights = [(TECH.MATERIALS.SU8, MSTACK_SU8_HEIGHT),
                                                                              (TECH.MATERIALS.FLUID, MSTACK_CHANNEL_HEIGHT * 3),
                                                                              (TECH.MATERIALS.SU8, MSTACK_CHANNEL_HEIGHT)],
                                                         display_style = DisplayStyle(color = COLOR_YELLOW))

TECH.MATERIAL_STACKS.MSTACK_VALVE = MaterialStack(name = "Valve Layer",
                                                         materials_heights = [(TECH.MATERIALS.SU8, MSTACK_SU8_HEIGHT),
                                                                              (TECH.MATERIALS.FLUID, MSTACK_CHANNEL_HEIGHT * 4),
                                                                              (TECH.MATERIALS.SU8, MSTACK_CHANNEL_HEIGHT)],
                                                         display_style = DisplayStyle(color = COLOR_GRAY))