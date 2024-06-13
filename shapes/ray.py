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

    x_avr = (src_x + tgt_x) / 2
    y_avr = (src_y + tgt_y) / 2

    if (dx == 0):
        result = (f"|x - {x_avr}| <= {half_width} ∧ "
                  f"{dy} * (y - {src_y}) >= 0")
    elif (dy == 0):
        result = (f"|y - {y_avr}| <= {half_width} ∧ "
                  f"{dx} * (x - {src_x}) >= 0")
    else:
        gcd_dxy = 1
        if (dx_4 := dx * 4) == int(dx_4) and (dy_4 := dy * 4) == int(dy_4):
            gcd_dxy = gcd(int(dx_4), int(dy_4)) / 4.0

        norm_dx = dx / gcd_dxy
        norm_dy = dy / gcd_dxy
        norm_dsquare = my_round(norm_dx * norm_dx + norm_dy * norm_dy, 3)
        norm_dx = my_round(norm_dx, 3)
        norm_dy = my_round(norm_dy, 3)

        result = (f"|{norm_dy}(x - {x_avr}) - {norm_dx}(y - {y_avr})| <= {half_width} * √ {norm_dsquare} ∧ "
                  f"{norm_dx}(x - {src_x}) + {norm_dy}(y - {src_y}) >= 0")

    return formatize_math_expr(result)

def from_names(
        src_name: str, 
        tgt_name: str, 
        half_width: float | str
    ) -> str:

    x_avr = f"(x({src_name}) + x({tgt_name})) / 2" 
    y_avr = f"(y({src_name}) + y({tgt_name})) / 2" 
    dx = f"(x({tgt_name}) - x({src_name}))"
    dy = f"(y({tgt_name}) - y({src_name}))"
    d_square = f"((x({tgt_name}) - x({src_name})) ^ 2 + (y({tgt_name}) - y({src_name})) ^ 2)"
    result = (f"|{dy}(x - {x_avr}) - {dx}(y - {y_avr})| <= {half_width} * √ {d_square} ∧ "
              f"{dx}(x - x({src_name})) + {dy}(y - y({tgt_name})) >= 0")
    return formatize_math_expr(result)
