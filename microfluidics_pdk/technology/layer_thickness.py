'''
Default layer thickness

'''

from ipkiss.technology import TECHNOLOGY as TECH

try:
    TECH.MSTACK_SU8_HEIGHT = 100
except:
    pass


try:
    TECH.MSTACK_FLUID_CHANNEL_HEIGHT = 100
except:
    pass

try:
    TECH.MSTACK_VACUUM_CHANNEL_HEIGHT = 100
except:
    pass
