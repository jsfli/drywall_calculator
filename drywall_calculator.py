class DryWall(object):
    PLUS_SIDE = -0.010
    MINUS_SIDE = -0.005
    FLAT_SIDE = -0.010
    STAR_SIDE = -0.010

    def __init__(self,
                 name,
                 design_width_m,
                 design_length_m = 2.540,
                 design_depth_m = 0.850,
                ):
        self.name = name
        self.design_width_m = design_width_m
        self.design_length_m = design_length_m
        self.design_depth_m = design_depth_m
