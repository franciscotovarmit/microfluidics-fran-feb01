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

TECH.VFABRICATION.PROCESS_FLOW  = VFabricationProcessFlow(active_processes = [TECH.PROCESS.CHANNEL_1, TECH.PROCESS.CHANNEL_2, TECH.PROCESS.NONE, TECH.PROCESS.PART_HOLDER
                                                                              ], # *** Do Not Change! ***
                                                          process_to_material_stack_map = [
                                                              ((0, 0, 0, 0), TECH.MATERIAL_STACKS.MSTACK_SU8),
                                                              ((0, 0, 1, 0), TECH.MATERIAL_STACKS.MSTACK_SU8), 
                                                              ((0, 1, 0, 0), TECH.MATERIAL_STACKS.MSTACK_CHANNEL),
                                                              ((0, 1, 1, 0), TECH.MATERIAL_STACKS.MSTACK_SU8),
                                                              ((1, 0, 0, 0), TECH.MATERIAL_STACKS.MSTACK_TALL_CHANNEL),
                                                              ((1, 0, 1, 0), TECH.MATERIAL_STACKS.MSTACK_SU8),
                                                              ((1, 1, 0, 0), TECH.MATERIAL_STACKS.MSTACK_SU8),
                                                              ((1, 1, 0, 0), TECH.MATERIAL_STACKS.MSTACK_VALVE),
                                                              ((0, 0, 0, 1), TECH.MATERIAL_STACKS.MSTACK_EXTERNAL_PART)],

                                                          is_lf_fabrication = {TECH.PROCESS.CHANNEL_1  : False,
                                                                               TECH.PROCESS.CHANNEL_2  : False,
                                                                               TECH.PROCESS.NONE : False,
                                                                               TECH.PROCESS.PART_HOLDER : False}
                                                          )