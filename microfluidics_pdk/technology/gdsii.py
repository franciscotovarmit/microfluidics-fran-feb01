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

TECH.GDSII = TechnologyTree()

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

##################################
# LAYER MAP
##################################

TECH.GDSII.LAYERTABLE = {
    # (ProcessLayer, PatternPurpose) : (GDSIILayer, GDSIIDatatype)
    # WG
    (TECH.PROCESS.FLUID, TECH.PURPOSE.DRAWING): (1, 1),
    (TECH.PROCESS.VACUUM, TECH.PURPOSE.DRAWING): (1, 1),
    (TECH.PROCESS.MISC, TECH.PURPOSE.DRAWING): (3, 1),

    # other layers
    (TECH.PROCESS.NONE, TECH.PURPOSE.LOGOTXT): (100, 0),
    (TECH.PROCESS.NONE, TECH.PURPOSE.DOC): (100, 1),
    (TECH.PROCESS.NONE, TECH.PURPOSE.BBOX): (100, 2),

}
TECH.GDSII.EXPORT_LAYER_MAP = GenericGdsiiPPLayerOutputMap(pplayer_map=TECH.GDSII.LAYERTABLE,
                                                           ignore_undefined_mappings=True)
TECH.GDSII.IMPORT_LAYER_MAP = GenericGdsiiPPLayerInputMap(pplayer_map=TECH.GDSII.LAYERTABLE)

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