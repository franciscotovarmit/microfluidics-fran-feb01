# -*- coding: utf-8 -*-
"""
Created on Thu Mar 15 16:01:10 2018
@author: francisco
"""

# Import the Microfluidic Technology File.
from microfluidics_ipkiss3.technology import *
# Import IPKISS3 Packages.
from ipkiss3 import all as i3
# Import microfluidics API.
import microfluidics_ipkiss3.all as microfluidics
from debri_trap_singleV2 import Obstacle_BooleanBoundary
from debri_trap_singlehalfLeftV2 import Obstacle_Left
from debri_trap_singlehalfRightV2 import Obstacle_Right

class JoinedObstacles(i3.PCell):#(Structure):
    channel_template = microfluidics.ChannelTemplateProperty(default=microfluidics.ShortChannelTemplate(), doc="Channel template for ports")

    mysingleObstacle = i3.ChildCellProperty(doc='the single Obstacle child cell, which will be clonned many times',
                                            default=Obstacle_BooleanBoundary())
    leftFilling = i3.ChildCellProperty(doc='the single Obstacle child cell, which will be clonned many times',
                                            default=Obstacle_Left())
    rightFilling = i3.ChildCellProperty(doc='the single Obstacle child cell, which will be clonned many times',
                                            default=Obstacle_Right())
    wholeTrapX = i3.PositiveNumberProperty(default=500.0, doc="total X distance length of traps")
    wholeTrapY = i3.PositiveNumberProperty(default=500.0, doc="total Y distance length of traps")
    cInp = i3.Coord2Property(default=0.0, doc="")

    class Layout(i3.LayoutView):

        def _generate_instances(self, insts):
            x_inc = self.mysingleObstacle.gap_btw_barriers*1+self.mysingleObstacle.obstacle_trap_radius*2
            y_inc = self.mysingleObstacle.obstacle_trap_radius*2+self.mysingleObstacle.gap_btw_barriers

            cycles_x = int(self.wholeTrapX/(self.mysingleObstacle.gap_btw_barriers +
                                             self.mysingleObstacle.obstacle_trap_radius*2))
            cycles_y = int(self.wholeTrapY/(y_inc))

            insts += i3.ARef(reference=self.mysingleObstacle, origin=(0,0.0*self.cell.wholeTrapY),
                             period=(x_inc, 0),
                             n_o_periods=(cycles_x, 1),
                             #transformation=i3.Rotation((0.0, 0.0), 40.0)
                             )

            xf =self.mysingleObstacle.gap_btw_barriers + self.mysingleObstacle.obstacle_trap_radius*0.5
            insts += i3.ARef(reference=self.mysingleObstacle, origin=(xf,y_inc),
                             period=(x_inc, 0),
                             n_o_periods=(cycles_x, 1),
                             #transformation=i3.Rotation((0.0, 0.0), 40.0)
                             )
            insts += i3.SRef(reference=self.rightFilling, position=(cycles_x*x_inc, 0))
            insts += i3.SRef(reference=self.leftFilling, position=(0, y_inc))
                             #transformation=i3.Rotation((0.0, 0.0), 40.0)


            print 'insts',insts


            return insts

        def _generate_ports(self, ports):
            #port1
            ports += microfluidics.FluidicPort(name='in',
                                               position = (0, self.wholeTrapY*0.5),
                                               #position = (0, 'insts_0'.size_info().north*0.5),
                                               direction = i3.PORT_DIRECTION.IN,
                                               angle_deg=180,
                                               trace_template=self.cell.channel_template
                                               )
            #port2
            ports += microfluidics.FluidicPort(name='out',
                                               position = (self.wholeTrapX,self.wholeTrapY*0.5),
                                               direction = i3.PORT_DIRECTION.OUT,
                                               angle_deg=0,
                                               trace_template=self.cell.channel_template
                                               )

            return ports

# Main program
if __name__ == '__main__':
    singleObstacle = Obstacle_BooleanBoundary(obstacle_trap_radius= 90.0, #taken for radius
                                   gap_btw_barriers = 40.0,
                                    cInp = (0.0,0.0))
    singleObstacle_Layout =  singleObstacle.Layout()
    LeftFilling = Obstacle_Left(obstacle_trap_radius= 90.0, #taken for radius
                                   gap_btw_barriers = 40.0,
                                    cInp = (0.0,0.0))
    Obstacle_Left_Layout =  LeftFilling.Layout()
    RightFilling = Obstacle_Right(obstacle_trap_radius= 90.0, #taken for radius
                                   gap_btw_barriers = 40.0,
                                    cInp = (0.0,0.0))
    Obstacle_Right__Layout =  RightFilling.Layout()
    multipleObstacle = JoinedObstacles(wholeTrapX= 200,#2000,
                                       wholeTrapY=200,#2500,
                                       mysingleObstacle=singleObstacle,
                                       )
    #transformation = i3.Rotation((0.0, 0.0), 40.0)

    multipleObstacle_Layout = multipleObstacle.Layout()
    multipleObstacle_Layout.visualize(annotate = True)
    multipleObstacle_Layout.write_gdsii("Trapi3All.gds")