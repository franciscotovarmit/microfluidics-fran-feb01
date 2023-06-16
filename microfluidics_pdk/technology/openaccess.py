
# OpenAccess settings
from ipkiss.technology import get_technology
from ipkiss.technology.technology import TechnologyTree, DelayedInitTechnologyTree
from oatools.to_oa.export_layer_map import AutoOALayerExportMap, AutoOAPurposeExportMap

TECH = get_technology()

TECH.OPENACCESS = TechnologyTree()

process_map = {TECH.PROCESS.WG          :  1,
               TECH.PROCESS.RWG         :  4,
               TECH.PROCESS.RWG_DENSE   :  6,
               TECH.PROCESS.HEATER      :  10,
               TECH.PROCESS.METAL       :  11,
               TECH.PROCESS.NONE        :  100
               }

purpose_map = {TECH.PURPOSE.DRAWING     :  20,
               TECH.PURPOSE.LF.LINE     :  1,
               TECH.PURPOSE.LF_AREA     :  2,
               TECH.PURPOSE.DF.LINE     :  3,
               TECH.PURPOSE.DF.POLYGON  :  4,
               TECH.PURPOSE.DF.TEXT     :  5,   
               TECH.PURPOSE.LOGOTXT     :  0,
               TECH.PURPOSE.TRACE       :  10,
               TECH.PURPOSE.PINREC      :  11,
               TECH.PURPOSE.DOC         :  12,
               TECH.PURPOSE.BBOX        :  13
               }

TECH.OPENACCESS.EXPORT_LAYER_MAP = AutoOALayerExportMap(base_counter=1000, known_layers=process_map)
TECH.OPENACCESS.EXPORT_PURPOSE_MAP = AutoOAPurposeExportMap(base_counter=1000, known_purposes=purpose_map)
    
##################################
# FILTERS
##################################

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
f["cut_path"] = False
f["path_to_boundary"] = True
f["cut_boundary"] = True
f["write_empty"]=True
f["name_error_filter"] = False
TECH.OPENACCESS.FILTER = f

# Routing in IPKISS-EDA

class RoutingTechTree(DelayedInitTechnologyTree):
    
    def initialize(self):
        from asp_silicon_photonics.components.waveguides.wire.trace import RoundedWireWaveguide
        from asp_silicon_photonics.components.waveguides.rib.trace import RoundedRibWaveguide
        self.WAVEGUIDE_GENERATION_GUIDE_LAYERS = {TECH.PPLAYER.WG_TRACE: RoundedWireWaveguide,
                                                      TECH.PPLAYER.RWG_TRACE: RoundedRibWaveguide}
    
TECH.ROUTING = RoutingTechTree()
