import math

class DryWall():
    def __init__(self, name, design_width_m):
        self.name = name
        self.design_width_m = design_width_m

        self.design_depth_m = 0.085
        self.design_height_normal_m = 2.540
        self.design_height_topfloor_m = 2.59
        self.design_m2 = self.design_width_m * self.design_height_normal_m

        self.plus_side_width_deduction_m = 0.010
        self.minus_side_width_deduction_m = 0.005
        self.flat_side_width_deduction_m = 0.010
        self.star_side_width_deduction_m = 0.010
        self.hole_radius = 0.0016

class Panel450PlusMinus(DryWall):
    def __init__(self, name, design_width_m):
        self.serial = "450+-"
        self.holes = 6
        DryWall.__init__(self, name, design_width_m)
        self.production_width_m = (self.design_width_m -
                                   self.plus_side_width_deduction_m -
                                   self.minus_side_width_deduction_m
                                  )
        self.production_height_m = self.design_height_normal_m
        self.production_m2 = self.production_width_m * self.production_height_m
        self.production_depth_m = self.design_depth_m
        self.production_m3 = ((self.production_depth_m *
                                   self.production_width_m *
                                   self.production_height_m) -
                                  (math.pi * self.hole_radius *
                                   self.hole_radius * self.holes))

panel_E1 = Panel450PlusMinus('E1', 0.450)

print("Panel Name => " + panel_E1.name)
print("Panel Serial => " + panel_E1.serial)
print("Production Width (m) => " + str(panel_E1.production_width_m))
print("Panel design m2 => " + str(panel_E1.design_m2))
print("Panel production m2 => " + str(panel_E1.production_m2))
print("Panel production m3 => " + str(panel_E1.production_m3))
