class DryWall():
    def __init__(self,
                 design_width_m,
                 left_side_shape,
                 right_side_shape,
                 top_panel,
                 star_position,
                 holes,
                 gangs,
                 design_length_m = 2.540,
                 design_depth_m = 0.850,
                ):
        self.design_width_m = design_width_m
        self.design_length_m = design_length_m
        self.design_depth_m = design_depth_m

panel_1 = DryWall('450+-', 450, 2540)

print(panel_1.design_depth_m)
