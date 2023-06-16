'''

# ---------------
# | GDSII File. |
# ---------------

Created by Mark Sison.

'''

# ------------
# | Imports. |
# ------------

from ipkiss.technology import get_technology
from ipkiss.technology.technology import TechnologyTree
from ipkiss.process.layer_map import GenericGdsiiPPLayerOutputMap, GenericGdsiiPPLayerInputMap
import string

TECH = get_technology()

from ipkiss.technology.technology import DelayedInitTechnologyTree

TECH = get_technology()

# TECH.GDSII = TechnologyTree()

# -------------------
# | GDSII Settings. |
# -------------------

TECH.GDSII.STRNAME_CHARACTER_DICT = {" -./" : "_"}
TECH.GDSII.STRNAME_ALLOWED_CHARACTERS = string.ascii_letters + string.digits + '_$'

TECH.GDSII.MAX_COORDINATES = 200
TECH.GDSII.MAX_PATH_LENGTH = 100
TECH.GDSII.MAX_VERTEX_COUNT = 4000
TECH.GDSII.MAX_NAME_LENGTH = 255

# --------------
# | Layer Map. |
# --------------

# *** Process: Channel 1. ***
#         Layer: 2.

TECH.GDSII.overwrite_allowed.append('PROCESS_LAYER_MAP')
TECH.GDSII.PROCESS_LAYER_MAP =   {
    TECH.PROCESS.CHANNEL_1: 2,
}

# *** Process: Channel 2. ***
#         Layer: 3.

TECH.GDSII.overwrite_allowed.append('PROCESS_LAYER_MAP')
TECH.GDSII.PROCESS_LAYER_MAP =   {
    TECH.PROCESS.CHANNEL_2: 3,
}

# *** Purpose: Create Channel. ***
#         Data Type: 2.

TECH.GDSII.overwrite_allowed.append('PURPOSE_DATATYPE_MAP')
TECH.GDSII.PURPOSE_DATATYPE_MAP = { 
    TECH.PURPOSE.CREATE_CHANNEL: 2,
}

# *** PPLayer Map. ***

pplayer_map = {(TECH.PROCESS.CHANNEL_1, TECH.PURPOSE.CREATE_CHANNEL) : (2, 1),
               (TECH.PROCESS.CHANNEL_2, TECH.PURPOSE.CREATE_CHANNEL) : (3, 1)
               }

from ipkiss.process.layer_map import UnconstrainedGdsiiPPLayerInputMap, GenericGdsiiPPLayerOutputMap, GenericGdsiiPPLayerInputMap

TECH.GDSII.overwrite_allowed.append('EXPORT_LAYER_MAP')        
TECH.GDSII.overwrite_allowed.append('IMPORT_LAYER_MAP')        

TECH.GDSII.EXPORT_LAYER_MAP = GenericGdsiiPPLayerOutputMap(pplayer_map = pplayer_map,
                                                           ignore_undefined_mappings = True)

TECH.GDSII.IMPORT_LAYER_MAP = UnconstrainedGdsiiPPLayerInputMap(process_layer_map = TECH.GDSII.PROCESS_LAYER_MAP, purpose_datatype_map = TECH.GDSII.PURPOSE_DATATYPE_MAP)

# ------------
# | Filters. |
# ------------

from ipkiss.primitives.filters.path_cut_filter import PathCutFilter
from ipkiss.primitives.filters.empty_filter import EmptyFilter
from ipkiss.primitives.filters.path_to_boundary_filter import PathToBoundaryFilter
from ipkiss.primitives.filters.boundary_cut_filter import BoundaryCutFilter
from ipkiss.primitives.filters.name_scramble_filter import NameScrambleFilter
from ipkiss.primitives.filters.name_error_filter import PCellNameErrorFilter
from ipkiss.primitives.filter import ToggledCompoundFilter

f = ToggledCompoundFilter()
f += PathCutFilter(name="cut_path", 
                   max_path_length=TECH.GDSII.MAX_COORDINATES, 
                   grids_per_unit=int(TECH.METRICS.UNIT/TECH.METRICS.GRID), 
                   overlap=1)
f += PathToBoundaryFilter(name="path_to_boundary")
f += BoundaryCutFilter(name="cut_boundary", max_vertex_count=TECH.GDSII.MAX_VERTEX_COUNT)
f += EmptyFilter(name="write_empty")
f += PCellNameErrorFilter(name="name_error_filter", allowed_characters=TECH.GDSII.STRNAME_ALLOWED_CHARACTERS)
f["cut_path"] = True
f["path_to_boundary"] = True
f["cut_boundary"] = True
f["write_empty"]=True
f["name_error_filter"] = False
TECH.GDSII.FILTER = f

TECH.GDSII.NAME_FILTER = NameScrambleFilter(allowed_characters=TECH.GDSII.STRNAME_ALLOWED_CHARACTERS,
                                            replace_characters=TECH.GDSII.STRNAME_CHARACTER_DICT,
                                            default_replacement="",
                                            max_name_length=TECH.GDSII.MAX_NAME_LENGTH, 
                                            scramble_all=False)

# End.