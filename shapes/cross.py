from math import *
from common.utils import my_round, formatize_math_expr

def from_coords(
        src_x: float, src_y: float, 
        tgt_x: float, tgt_y: float, 
        half_width: float
    ) -> str:

    src_x, src_y = my_round(src_x, 3), my_round(src_y, 3)
    tgt_x, tgt_y = my_round(tgt_x, 3), my_round(tgt_y, 3)
    half_width = my_round(half_width, 3)

    dx = tgt_x - src_x
    dy = tgt_y - src_y

    if (dx == 0 and dy == 0):
        raise ValueError("The 2 given coordinations are the same.")

    if (dx == 0 or dy == 0):
        result = (f"|x - {tgt_x}| <= {half_width} ∨ "
                  f"|y - {tgt_y}| <= {half_width}")
    else:
        gcd_dxy = 1
        if (dx_4 := dx * 4) == int(dx_4) and (dy_4 := dy * 4) == int(dy_4):
            gcd_dxy = gcd(int(dx_4), int(dy_4)) / 4.0

        norm_dx = dx / gcd_dxy
        norm_dy = dy / gcd_dxy
        norm_dsquare = my_round(norm_dx * norm_dx + norm_dy * norm_dy, 3)
        norm_dx = my_round(norm_dx, 3)
        norm_dy = my_round(norm_dy, 3)

        result = (f"|{norm_dy}(x - {tgt_x}) - {norm_dx}(y - {tgt_y})| <= {half_width} * √ {norm_dsquare} ∨ "
                  f"|{norm_dx}(x - {tgt_x}) + {norm_dy}(y - {tgt_y})| <= {half_width} * √ {norm_dsquare}")

    return formatize_math_expr(result)

def from_names(
        src_name: str, 
        tgt_name: str, 
        half_width: float | str
    ) -> str:
 
    dx = f"(x({tgt_name}) - x({src_name}))"
    dy = f"(y({tgt_name}) - y({src_name}))"
    d_square = f"((x({tgt_name}) - x({src_name})) ^ 2 + (y({tgt_name}) - y({src_name})) ^ 2)"
    result = (f"|{dy}(x - x({tgt_name})) - {dx}(y - y({tgt_name}))| <= {half_width} * √ {d_square} ∨ "
              f"|{dx}(x - x({tgt_name})) + {dy}(y - y({tgt_name}))| <= {half_width} * √ {d_square}")
    return formatize_math_expr(result)
