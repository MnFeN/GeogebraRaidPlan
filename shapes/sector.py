from math import *

def from_point_coords(x0: float, y0: float, x1: float, y1: float, degree: float, min_radius: float = -1, max_radius: float = -1) -> str:
    dx = x1 - x0
    dy = y1 - y0

    sinθ = sin(degree * pi / 180)
    cosθ = cos(degree * pi / 180)

    vec_cw_x = round(cosθ * dx + sinθ * dy, 3)
    vec_cw_y = round(-sinθ * dx + cosθ * dy, 3)

    vec_ccw_x = round(cosθ * dx - sinθ * dy, 3)
    vec_ccw_y = round(sinθ * dx + cosθ * dy, 3)

    x0 = round(x0, 3)
    y0 = round(y0, 3)

    if degree <= 180:
        result = (f"({vec_ccw_y} * (x - {x0}) - {vec_ccw_x} * (y - {y0}) >= 0 ∧"
                  f" {vec_cw_y} * (x - {x0}) - {vec_cw_x} * (y - {y0}) <= 0)")
    else:
        result = (f"({vec_ccw_y} * (x - {x0}) - {vec_ccw_x} * (y - {y0}) >= 0 ∨"
                  f" {vec_cw_y} * (x - {x0}) - {vec_cw_x} * (y - {y0}) <= 0)")

    if min_radius > 0:
        result += f" ∧ (x - {x0}) ^ 2 + (y - {y0}) ^ 2 >= {min_radius} ^ 2"
    
    if max_radius > 0:
        result += f" ∧ (x - {x0}) ^ 2 + (y - {y0}) ^ 2 <= {max_radius} ^ 2"

    return result

def from_names(src_name: str, tgt_name: str, degree: float, min_radius: float = -1, max_radius: float = -1) -> str:
    dx = f"(x({tgt_name}) - x({src_name}))"
    dy = f"(y({tgt_name}) - y({src_name}))"

    sinθ = round(sin(degree * pi / 360), 3)
    cosθ = round(cos(degree * pi / 360), 3)

    vec_cw_x = f"({cosθ} * {dx} + {sinθ} * {dy})"
    vec_cw_y = f"(-{sinθ} * {dx} + {cosθ} * {dy})"

    vec_ccw_x = f"({cosθ} * {dx} - {sinθ} * {dy})"
    vec_ccw_y = f"({sinθ} * {dx} + {cosθ} * {dy})"

    if degree <= 180:
        result = (f"({vec_ccw_y} * (x - x({src_name})) - {vec_ccw_x} * (y - y({src_name})) >= 0 ∧"
                  f" {vec_cw_y} * (x - x({src_name})) - {vec_cw_x} * (y - y({src_name})) <= 0)")
    else:
        result = (f"({vec_ccw_y} * (x - x({src_name})) - {vec_ccw_x} * (y - y({src_name})) >= 0 ∨"
                  f" {vec_cw_y} * (x - x({src_name})) - {vec_cw_x} * (y - y({src_name})) <= 0)")

    if min_radius > 0:
        result += f" ∧ (x - x({src_name})) ^ 2 + (y - y({src_name})) ^ 2 >= {min_radius} ^ 2"
    
    if max_radius > 0:
        result += f" ∧ (x - x({src_name})) ^ 2 + (y - y({src_name})) ^ 2 <= {max_radius} ^ 2"

    return result
