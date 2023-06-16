'''

# ---------------------
# | Channel Template. |
# ---------------------

  Created by Mark Sison.

*** The Channel Template provides an easy way to develop Microchannels in your design.

'''

# ------------
# | Imports. |
# ------------

from ipkiss3.pcell.trace.trace import TraceTemplate, Trace, TemplatedTrace, _CoverLayerTraceTemplate, _TemplatedCoverLayerTrace, _CoverLayerTrace, _TraceWithOtherTraceTemplate
from ipkiss3.pcell.cell.pcellproperty import ChildCellProperty
from ipcore.properties.predefined import PositiveNumberProperty
from ipcore.properties.restrictions import RestrictType, RestrictClass
from ipcore.properties.descriptor import DefinitionProperty
from ipkiss.technology import get_technology
from ipkiss.process import PPLayer
from ipkiss3.pcell.netlist.view import NetlistView
from ipkiss3.pcell.layout.view import LayoutView
from ipkiss3.pcell.layout.port import PORT_DIRECTION

from ipkiss3.pcell.trace.window.window import PathTraceWindow

# Trace Ports.
from ipkiss3.pcell.trace.trace_port import _TraceWithPorts, _TraceTemplateWithPorts
from ipkiss3.pcell.trace.trace_port import _TraceWithIoPorts, _TraceTemplateWithIoPorts, _TemplatedTraceWithIoPorts,\
     _TraceTemplateWithPortsAndOtherTraceTemplate, _TemplatedTraceWithPortsAndOtherTraceTemplate, \
     _TraceWithPorts, _TraceTemplateWithPorts, _TemplatedTraceWithPorts, \
     TraceWithPorts, TracePort, _TraceLayoutTemplatePreProcessor

from ipkiss3.pcell.trace.window_trace import WindowTraceTemplate, TemplatedWindowTrace 
from ipkiss3.pcell.trace.windows_on_trace import WindowsOnTraceTemplate, TemplatedWindowsOnTrace

from ipkiss.plugins.documentation.example_handler import example_plot, example
from ipkiss.geometry.shapes.basic import ShapeRectangle
from ipkiss.geometry.shape import Shape
from ipkiss.geometry.coord import Coord2
from ipkiss.geometry.transforms.rotation import Rotation
from ipcore.properties.descriptor import DefinitionProperty, ReadOnlyIndirectProperty

# --------------------------------
# | Custom Microfluidic Imports. |
# --------------------------------

from microfluidics_ipkiss3.pcell.channel import _Channel, _AbstractChannel, WindowChannelTemplate
from microfluidics_ipkiss3.pcell.term import MicrofluidicTerm

TECH = get_technology()

__all__ = [
    "FluidChannelTemplate",
    "VacuumChannelTemplate"
]

class FluidChannelTemplate(WindowChannelTemplate, _AbstractChannel):
    
    _templated_class = type("TemplatedChannel",
                            (TemplatedTrace, _Channel), {})
                            

    class Layout(WindowChannelTemplate.Layout, TraceTemplate.Layout, _TraceTemplateWithPorts.Layout):
        channel_width = PositiveNumberProperty(default=100, doc="Width of the Channel.")

        def _default_layer(self):
            return PPLayer(process = TECH.PROCESS.FLUID,
                           purpose = TECH.PURPOSE.DRAWING)
            
        def transform(self, transformation):
            self.channel_width = transformation.apply_to_length(self.channel_width)
            return super(_AbstractChannel.Layout, self).transform(transformation)
        
        def _default_windows(self):
            windows = []
            windows.append(PathTraceWindow(layer=self.layer,
                                           start_offset=-0.5 * self.channel_width,
                                           end_offset=+0.5 * self.channel_width))


            return windows
        
    class Netlist(TraceTemplate.Netlist, _TraceTemplateWithPorts.Netlist):
        _term_type = DefinitionProperty(restriction=RestrictClass(MicrofluidicTerm), default=MicrofluidicTerm)


class VacuumChannelTemplate(WindowChannelTemplate, _AbstractChannel):
    _templated_class = type("TemplatedChannel",
                            (TemplatedTrace, _Channel), {})

    class Layout(WindowChannelTemplate.Layout, TraceTemplate.Layout, _TraceTemplateWithPorts.Layout):
        channel_width = PositiveNumberProperty(default=100, doc="Width of the Channel.")

        def _default_layer(self):
            return PPLayer(process=TECH.PROCESS.VACUUM,
                           purpose=TECH.PURPOSE.DRAWING)

        def transform(self, transformation):
            self.channel_width = transformation.apply_to_length(self.channel_width)
            return super(_AbstractChannel.Layout, self).transform(transformation)

        def _default_windows(self):
            windows = []
            windows.append(PathTraceWindow(layer=self.layer,
                                           start_offset=-0.5 * self.channel_width,
                                           end_offset=+0.5 * self.channel_width))

            return windows

    class Netlist(TraceTemplate.Netlist, _TraceTemplateWithPorts.Netlist):
        _term_type = DefinitionProperty(restriction=RestrictClass(MicrofluidicTerm), default=MicrofluidicTerm)

