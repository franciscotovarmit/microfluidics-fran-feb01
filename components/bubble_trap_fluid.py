# Import the Microfluidic Technology File.

from microfluidics_ipkiss3.technology import *

# Import IPKISS3 Packages.

from ipkiss3 import all as i3

# Import microfluidics API.

import microfluidics_ipkiss3.all as microfluidics
import math
from debri_trap_arrayV2 import JoinedObstacles

# Define a Custom Class.
class Obstacle_BooleanBoundary(i3.PCell):

    # Properties of trap
    width = 200#i3.PositiveNumberProperty(default=200.,doc="width main channel")
    channel_template = microfluidics.ChannelTemplateProperty(default=microfluidics.ShortChannelTemplate().Layout(width=width),
                                                             doc="Channel template of the tee")
    _name_prefix = "VacTrapV" # a prefix added to the unique identifier

    radius =i3.PositiveNumberProperty(default=400., doc="radius of the circular vacuum section collecting air")
    vacuum_channel_circular =i3.PositiveNumberProperty(default=100., doc="width of circular channel collecting air")
    inlet_channel_length = i3.PositiveNumberProperty(default=300., doc="length of inlet channel vac")
    offset_matching = i3.PositiveNumberProperty(default=50., doc="length of inlet channel vac")
    obstacles = i3.ChildCellProperty(doc='the single Obstacle child cell, which will be clonned many times',
                                            default=JoinedObstacles(wholeTrapX=width))
    layer = i3.LayerProperty(default=i3.TECH.PPLAYER.CH2.TRENCH, doc='Layer to drawn on')
    cInp = i3.Coord2Property(default = (0.0,0.0),required = True)

    class Layout(i3.LayoutView):
        def _generate_instances(self, insts):
            width =200.0
            p1 = (-self.radius, -self.radius) #near cylinders
            p2 = (-self.radius, -2*self.radius) #bottom
            p3 = (2*self.radius,  -2*self.radius) #right
            p4 = (2*self.radius, 0) #top
            p5 = (2*self.radius+500, 0) #out
            pax = (-width*0.5*math.cos(45),width*0.5*math.sin(45) )

            #generate a circle
            sr1 = i3.ShapeCircle(center=(0.0,0.0),
                                        radius=self.radius)#, line_width = 200)
            br1 = i3.Boundary(layer = self.layer, shape = sr1)
            #s= i3.Structure(elements = br1)

            #rectangle
            sc1 = i3.ShapeRectangle(center = p1,
                                    box_size = (self.radius*4,self.radius*0.25))
            bc1 = i3.Boundary(layer = self.layer, shape = sc1,
                              transformation = i3.Rotation((0, 0), -45.0))  # was -35
            #Substruct boundaries and add to the element list
            b_sub = br1-bc1
            s= i3.Structure(elements = b_sub)
            insts += i3.SRef(s)

            #Input channel - segment
            channel1 = microfluidics.Channel(trace_template = self.cell.channel_template)
            #channel_template = microfluidics.ShortChannelTemplate().Layout(width=200.0)
            channel1_lo = channel1.Layout(shape=[(self.inlet_channel_length+self.offset_matching*0.5, 0), (0, 0)])
            insts += i3.SRef(channel1_lo, position=(-(self.inlet_channel_length+self.radius), 0), transformation=i3.Rotation((0.0, 0.0), 0.0))


    #############################routing


            from ipkiss.plugins.photonics.routing.manhattan import RouteManhattan

            channel_4 = microfluidics.RoundedChannel(trace_template=self.cell.channel_template)  # used for routing
            channel_4_layout = channel_4.Layout()


            import operator
            p1Array=tuple(map(operator.add, p1,pax))

            print 'p1: ', p1
            print 'pax: ', pax
            print 'p1Array: ', p1Array

            #obstacles
            insts += i3.SRef(reference=self.obstacles, position=p1Array,
                             transformation=i3.Rotation((0,0), -45.0))


            in_port_1 = microfluidics.FluidicPort(position=p1, trace_template=self.cell.channel_template)
            out_port_1 = microfluidics.FluidicPort(trace_template=self.cell.channel_template)
            in_port_1.angle_deg = 225
            out_port_1.angle_deg = 45

            in_port_2 = microfluidics.FluidicPort(position=p2, trace_template=self.cell.channel_template)
            in_port_2.angle_deg = 225
            channel_4_layout.set(bend_radius = 150.0, shape = RouteManhattan(input_port=in_port_2,
                                                                             points=[p2,p3,p4,p5],
                                                                             output_port=out_port_1,
                                                                             bend_radius = 300.0))
            insts += i3.SRef(name = "Route_1", reference = channel_4)
            ##############################routing

            from ipkiss3.pcell.routing import RouteToAngle

            # create the route object
            channel_1 = microfluidics.RoundedChannel(trace_template=self.cell.channel_template)  # used for routing
            channel_1_layout = channel_1.Layout()
            channel_1_layout.set(bend_radius = 50.0, shape = RouteToAngle(input_port = in_port_1,
                                                                           start_straight = 300,
                                                                           end_straight =300,
                                                                           angle_out = 45))
            #insts += i3.SRef(name = "Route_2", reference = channel_1)



            from ipkiss3.pcell.routing import RouteToEastAtMaxY,RouteToEastAtMinY,RouteToEastAtY

            # create the route object
            input_portx = i3.OpticalPort(name="in", position=(-self.radius,-self.radius), angle_deg=225.0)
            channel_x = microfluidics.RoundedChannel(trace_template=self.cell.channel_template)  # used for routing
            channel_x_layout = channel_x.Layout()
            channel_x_layout.set(bend_radius = 150.0, shape = RouteToEastAtY(input_port = input_portx,
                                                                           start_straight = 200,
                                                                           end_straight =200,
                                                                           y_position = -2*self.radius))
            insts += i3.SRef(name = "Route_x", reference = channel_x)

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

