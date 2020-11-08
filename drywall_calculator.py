class DryWall():
    def __init__(self, name, design_width_m):
        self.name = name
        self.design_width_m = design_width_m
        self.design_depth_m = 0.085
        self.plus_side_width_deduction_m = 0.010
        self.minus_side_width_deduction_m = 0.005
        self.flat_side_width_deduction_m = 0.010
        self.star_side_width_deduction_m = 0.010
        self.design_height_normal_m = 2.540
        self.design_height_topfloor_m = 2.59
        self.production_width_m = (self.design_width_m -
                                 self.plus_side_width_deduction_m -
                                 self.minus_side_width_deduction_m
                                )
        self.production_height_m = self.design_height_normal_m
        self.production_depth_m = self.design_depth_m

class Panel450PlusMinus(DryWall):
    def __init__(self, name, design_width_m):
        self.serial = "450+-"
        DryWall.__init__(self, name, design_width_m)


panel_E1 = Panel450PlusMinus('E1', 0.450)

print(panel_E1.name, panel_E1.serial, panel_E1.production_width_m)
