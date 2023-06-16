'''

Created by Mark Sison.

'''

# *** Display. ***

from ipkiss.technology import get_technology
from ipkiss.technology.technology import TechnologyTree, DelayedInitTechnologyTree

TECH = get_technology()

class TechDisplayTree(DelayedInitTechnologyTree):
    def initialize(self):
        from ipkiss.process import PPLayer
        from ipkiss.visualisation.display_style import DisplayStyle, DisplayStyleSet
        from ipkiss.visualisation import color
    
        self.PREDEFINED_STYLE_SETS = TechnologyTree()        
    
        # colorful purpose map
        DISPLAY_BLACK = DisplayStyle(color=color.COLOR_BLACK, edgewidth=0.0, alpha=0.5)
        DISPLAY_WHITE = DisplayStyle(color=color.COLOR_WHITE, edgewidth=0.0)
        DISPLAY_INVERSION = DisplayStyle(color=color.COLOR_BLUE, alpha=0.5, edgewidth=1.0)
        DISPLAY_DF = DisplayStyle(color=color.COLOR_GREEN, alpha=0.5, edgewidth=1.0)
        DISPLAY_LF = DisplayStyle(color=color.COLOR_YELLOW, alpha=0.5, edgewidth=1.0)
        DISPLAY_TEXT = DisplayStyle(color=color.COLOR_MAGENTA, alpha=0.5, edgewidth=1.0)
        DISPLAY_HOLE = DisplayStyle(color=color.COLOR_RED, alpha=0.5, edgewidth=1.0)
        DISPLAY_ALIGNMENT = DisplayStyle(color=color.COLOR_CYAN, alpha=0.5, edgewidth=1.0) 
        DISPLAY_DOC = DisplayStyle(color=color.COLOR_BLACK, alpha=.5, edgewidth=1.0) 
        DISPLAY_P = DisplayStyle(color=color.COLOR_BLUE, alpha=0.4, edgewidth=0.0)
        DISPLAY_N = DisplayStyle(color=color.COLOR_RED, alpha=0.4, edgewidth=0.0)
        DISPLAY_PPLUS = DisplayStyle(color=color.COLOR_BLUE_CRAYOLA, alpha=0.6, edgewidth=0.0)
        DISPLAY_NPLUS = DisplayStyle(color=color.COLOR_SCARLET, alpha=0.6, edgewidth=0.0)        
        DISPLAY_CON = DisplayStyle(color=color.COLOR_BLACK, alpha=1.0, edgewidth=0.0)
        DISPLAY_SIL = DisplayStyle(color=color.COLOR_COPPER, alpha=0.9, edgewidth=0.0)
        DISPLAY_METAL = DisplayStyle(color=color.COLOR_GRAY, alpha=0.6, edgewidth=0.0)
        
        style_set = DisplayStyleSet()
        style_set.background = DISPLAY_WHITE
        process_display_order = [ 
            TECH.PROCESS.NONE,
            TECH.PROCESS.CHANNEL_1,
            TECH.PROCESS.CHANNEL_2
        ]

    
        for process in process_display_order:
            style_set += [(PPLayer(process, TECH.PURPOSE.CREATE_CHANNEL), DISPLAY_INVERSION),
                          (PPLayer(process, TECH.PURPOSE.CREATE_CHANNEL), DISPLAY_INVERSION)]

        style_set += [(PPLayer(TECH.PROCESS.CHANNEL_1, TECH.PURPOSE.CREATE_CHANNEL), DISPLAY_P),
                      (PPLayer(TECH.PROCESS.CHANNEL_2, TECH.PURPOSE.CREATE_CHANNEL), DISPLAY_N),
                      ]
        
        from ipkiss.visualisation.color import Color
        from numpy import linspace
        style_set += [(i, DisplayStyle(color=Color(name="gray_" + str(i),
                                                   red=c_val,
                                                   green=c_val,
                                                   blue=c_val),
                                                   alpha=.5)) 
                      for i, c_val in enumerate(linspace(.9, 0.0, num=256))]
        
        self.PREDEFINED_STYLE_SETS.PURPOSE_HIGHLIGHT = style_set
        self.DEFAULT_DISPLAY_STYLE_SET = style_set
    
# TECH.DISPLAY = TechDisplayTree()