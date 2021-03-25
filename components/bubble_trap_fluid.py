# Import the Microfluidic Technology File.

from microfluidics_ipkiss3.technology import *

# Import IPKISS3 Packages.

from ipkiss3 import all as i3

# Import microfluidics API.

import microfluidics_ipkiss3.all as microfluidics

# Define a Custom Class.
class Obstacle_BooleanBoundary(i3.PCell):

    # Properties of trap
    channel_template = microfluidics.ChannelTemplateProperty(default=microfluidics.ShortChannelTemplate(),
                                                             doc="Channel template of the tee")
    _name_prefix = "VacTrapV" # a prefix added to the unique identifier

    radius =i3.PositiveNumberProperty(default=400., doc="radius of the circular vacuum section collecting air")
    vacuum_channel_circular =i3.PositiveNumberProperty(default=100., doc="width of circular channel collecting air")
    inlet_channel_length = i3.PositiveNumberProperty(default=300., doc="length of inlet channel vac")
    offset_matching = i3.PositiveNumberProperty(default=50., doc="length of inlet channel vac")
    layer = i3.LayerProperty(default=i3.TECH.PPLAYER.CH2.TRENCH, doc='Layer to drawn on')
    cInp = i3.Coord2Property(default = (0.0,0.0),required = True)

    class Layout(i3.LayoutView):
        def _generate_instances(self, insts):

            sr1 = i3.ShapeCircle(center=(0.0,0.0),
                                        radius=self.radius)#, line_width = 200)
            br1 = i3.Boundary(layer = self.layer, shape = sr1)
            s= i3.Structure(elements = br1)
            insts += i3.SRef(s)

            #Input channel - segment
            channel1 = microfluidics.Channel(trace_template = self.cell.channel_template)
            channel1_lo = channel1.Layout(shape=[(self.inlet_channel_length+self.offset_matching*0.5, 0), (0, 0)])
            insts += i3.SRef(channel1_lo, position=(-(self.inlet_channel_length*0.99+self.radius), 0), transformation=i3.Rotation((0.0, 0.0), 0.0))

            channel1_lo = channel1.Layout(shape=[(self.inlet_channel_length+self.offset_matching*0.5, 0), (0, 0)])
            insts += i3.SRef(channel1_lo, position=(-(self.inlet_channel_length*0.99+self.radius), 0), transformation=i3.Rotation((0.0, 0.0), 0.0))

            #############################routing
            from ipkiss.plugins.photonics.routing.manhattan import RouteManhattan

            channel_4 = microfluidics.RoundedChannel(trace_template=self.cell.channel_template)  # used for routing
            channel_4_layout = channel_4.Layout()
            p1 = (-self.radius, -self.radius) #near cylinders
            p2 = (-self.radius, -2*self.radius) #bottom
            p3 = (2*self.radius,  -2*self.radius) #right
            p4 = (2*self.radius, 0) #top
            p5 = (2*self.radius+500, 0) #out

            in_port_1= microfluidics.FluidicPort(trace_template=self.cell.channel_template)
            out_port_1 = microfluidics.FluidicPort(trace_template=self.cell.channel_template)
            in_port_1.angle_deg = -45
            out_port_1.angle_deg = 40
            channel_4_layout.set(bend_radius = 150.0, shape = RouteManhattan(input_port = in_port_1,
                                               points=[p1,p2,p3,p4,p5],output_port=out_port_1, bend_radius = 300.0))
            insts += i3.SRef(name = "Route_1", reference = channel_4)
            ##############################routing

            return insts

        #Thach added to define one inlet and one outlet
        def _generate_ports(self, ports):  # Use _generate_ports method to define ports
            #ports += i3.InFluidicPort(name = "in", position = (0., 10.), angle = 180.0)
            ports += i3.OpticalPort(name = "in", position = (0., self.radius+self.inlet_channel_length), angle = 180.0)
            #ports += i3.OutFluidicPort(name ="out", position = (30., 10.), angle = 0.0)
            #ports += i3.OpticalPort(name ="out", position = ((self.obstacle_trap_length+self.gap_btw_barriers)*2, self.channel_trap_width*0.5), angle = 0.0)

            return ports

# Main program
if __name__ == "__main__":
    trap = Obstacle_BooleanBoundary()
    trap_layout = trap.Layout()
    trap_layout.visualize(annotate=True)
    trap_layout.visualize_2d()
    # visualize_2d displays a top down view of the fabricated layout
    #trap_layout.cross_section(i3.Shape([(0, 25), (100, 25)]), process_flow=TECH.VFABRICATION.PROCESS_FLOW).visualize()
    #lay.cross_section(i3.Shape([(-9, 3), (9, 3)]), process_flow=vfab_flow).visualize()
    trap_layout.write_gdsii("erik_trapI3.gds")

