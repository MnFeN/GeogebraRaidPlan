from math import *

def from_point_coords(x1: float, y1: float, x2: float, y2: float, half_width: float) -> str:
    x1, y1, x2, y2, half_width = round(x1, 3), round(y1, 3), round(x2, 3), round(y2, 3), round(half_width, 3)
    dx = x2 - x1
    dy = y2 - y1

    if (dx == 0 and dy == 0):
        print("The 2 given coordinations are the same.")
        return None
    
    gcd_dxy = 1
    if (dx_4 := dx * 4) == int(dx_4) and (dy_4 := dy * 4) == int(dy_4):
        gcd_dxy = gcd(int(dx_4), int(dy_4)) / 4.0

    x_avr = (x1 + x2) / 2
    y_avr = (y1 + y2) / 2

    if (dx == 0):
        result = (f"|x - {x_avr}| <= {half_width} ∧ "
                f"|y - {y_avr}| <= {abs(dy):.3f} / 2")
    elif (dy == 0):
        result = (f"|y - {y_avr}| <= {half_width} ∧ "
                f"|x - {x_avr}| <= {abs(dx):.3f} / 2")
    else:
        norm_dx = dx / gcd_dxy
        norm_dy = dy / gcd_dxy
        norm_dsquare = round(norm_dx * norm_dx + norm_dy * norm_dy, 3)
        norm_dx = round(norm_dx, 3)
        norm_dy = round(norm_dy, 3)

        result = (f"|{norm_dy}(x - {x_avr}) - {norm_dx}(y - {y_avr})| <= {half_width} * √ {norm_dsquare} ∧ "
                    f"|{norm_dx}(x - {x_avr}) + {norm_dy}(y - {y_avr})| <= {norm_dsquare} * {gcd_dxy} / 2")

    result = result.replace("- -", "+ ").replace("+ -", "- ")
    return result

def from_names(name1: str, name2: str, half_width: str) -> str:
    x_avr = f"(x({name1}) + x({name2})) / 2" 
    y_avr = f"(y({name1}) + y({name2})) / 2" 
    dx = f"(x({name2}) - x({name1}))"
    dy = f"(y({name2}) - y({name1}))"
    d_square = f"( (x({name2}) - x({name1})) ^ 2 + (y({name2}) - y({name1})) ^ 2)"
    result = (f"|{dy}(x - {x_avr}) - {dx}(y - {y_avr})| <= {half_width} * √ {d_square} ∧ "
                f"|{dx}(x - {x_avr}) + {dy}(y - {y_avr})| <= {d_square} / 2")
    return result
