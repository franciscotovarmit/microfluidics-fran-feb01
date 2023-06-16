'''

Created by Mark Sison.

'''

# *** Virtual Fabrication. ***

# Imports.

from ipkiss.technology import get_technology
from ipkiss.technology.technology import TechnologyTree

TECH = get_technology()

from ipkiss.plugins.vfabrication.process_flow import VFabricationProcessFlow

TECH.overwrite_allowed.append('VFABRICATION')
TECH.VFABRICATION = TechnologyTree()

# Virtual Fabrication Process Flow.
# TODO: FIX
TECH.VFABRICATION.PROCESS_FLOW = VFabricationProcessFlow(active_processes = [TECH.PROCESS.FLUID, TECH.PROCESS.VACUUM
                                                                              ], # *** Do Not Change! ***
                                                          process_to_material_stack_map = [
                                                              ((0, 0), TECH.MATERIAL_STACKS.MSTACK_SU8),
                                                              ((0, 1), TECH.MATERIAL_STACKS.MSTACK_AIR_CHANNEL),
                                                              ((1, 0), TECH.MATERIAL_STACKS.MSTACK_FLUID_CHANNEL),
                                                              ((1, 1), TECH.MATERIAL_STACKS.MSTACK_FLUID_CHANNEL)],

                                                          is_lf_fabrication = {TECH.PROCESS.FLUID  : False,
                                                                               TECH.PROCESS.VACUUM  : False
                                                                               }
                                                          )