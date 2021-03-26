# Import the Microfluidic Technology File.

from microfluidics_ipkiss3.technology import *

# Import IPKISS3 Packages.

from ipkiss3 import all as i3

# Import microfluidics API.

import microfluidics_ipkiss3.all as microfluidics

# Define a Custom Class.
class Obstacle_Right(i3.PCell):

    layer = i3.LayerProperty(default=i3.TECH.PPLAYER.CH2.TRENCH, doc='Layer to drawn on')
    # Properties of trap
    obstacle_trap_radius = i3.PositiveNumberProperty(default=10., doc="width or radius of obstacle")
    gap_btw_barriers = i3.PositiveNumberProperty(default=10., doc="gap between obstacles")
    cInp = i3.Coord2Property(default = (0.0,0.0),required = True)

    class Layout(i3.LayoutView):
        def _generate_instances(self, insts):
            # First create shapes
            # Break the channel that contain two obstacles into three segments
            # Obstacles need to intersect these three segments
            #  Obs 1. Segment 1:2,   Obs 2 Segment 2:3
            #define points will be helpful to make schematic
            p1 = (self.cInp.x+0.0,self.cInp.y+0.0)
            p2 = ((self.gap_btw_barriers*0.5+self.obstacle_trap_radius),0.0)
            p3 = ((self.gap_btw_barriers*0.5+self.obstacle_trap_radius),self.gap_btw_barriers+self.obstacle_trap_radius*2)
            p4 = (0.0,self.gap_btw_barriers+self.obstacle_trap_radius*2)

            sr1 = i3.Shape(points = [p1,p2,p3,p4], closed =True)

            #Internal holes as Circles  #to do: define position of SC2 as a function of perpendicular GAP
            sc1 = i3.ShapeCircle(center = (self.cInp.x+self.gap_btw_barriers*0.5+self.obstacle_trap_radius, self.gap_btw_barriers*0.5+self.obstacle_trap_radius), radius = (self.obstacle_trap_radius))

            #Define the boundaries for shapes
            br1 = i3.Boundary(layer = self.layer, shape = sr1)
            bc1 = i3.Boundary(layer = self.layer, shape = sc1)

            #Substruct boundaries and add to the element list
            b_sub = br1-bc1

            s= i3.Structure(elements = b_sub)
            insts += i3.SRef(s)

            return insts

        #Thach added to define one inlet and one outlet
        def _generate_ports(self, ports):  # Use _generate_ports method to define ports
            ports += i3.OpticalPort(name = "in", position = (0., self.obstacle_trap_radius+self.gap_btw_barriers), angle = 180.0)
            ports += i3.OpticalPort(name ="out", position = ((self.gap_btw_barriers*1.5+self.obstacle_trap_radius*3), self.obstacle_trap_radius+self.gap_btw_barriers), angle = 0.0)

            return ports

# Main program
if __name__ == "__main__":
    trap = Obstacle_BooleanBoundary(obstacle_trap_radius= 90.0, #taken for radius
                                   gap_btw_barriers = 40.0,
                                    cInp = (0.0,0.0))
    
    trap_layout = trap.Layout()
    trap_layout.visualize(annotate=True)
    trap_layout.visualize_2d()
    # visualize_2d displays a top down view of the fabricated layout
    #trap_layout.cross_section(i3.Shape([(0, 25), (100, 25)]), process_flow=TECH.VFABRICATION.PROCESS_FLOW).visualize()
    #lay.cross_section(i3.Shape([(-9, 3), (9, 3)]), process_flow=vfab_flow).visualize()
    trap_layout.write_gdsii("erik_trapI3.gds")

