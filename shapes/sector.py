from math import *
from common.utils import my_round, formatize_math_expr
from typing import Optional

def from_coords(
        src_x: float, src_y: float, 
        tgt_x: float, tgt_y: float, 
        degree: float, 
        max_radius: Optional[float] = None, 
        min_radius: Optional[float] = None
    ) -> str:

    dx = tgt_x - src_x
    dy = tgt_y - src_y

    sinθ = sin(degree * pi / 360)
    cosθ = cos(degree * pi / 360)

    vec_cw_x = my_round(cosθ * dx + sinθ * dy, 3)
    vec_cw_y = my_round(-sinθ * dx + cosθ * dy, 3)

    vec_ccw_x = my_round(cosθ * dx - sinθ * dy, 3)
    vec_ccw_y = my_round(sinθ * dx + cosθ * dy, 3)

    src_x = my_round(src_x, 3)
    src_y = my_round(src_y, 3)

    if degree <= 180:
        result = (f"({vec_ccw_y}(x - {src_x}) - {vec_ccw_x}(y - {src_y}) >= 0 ∧"
                  f" {vec_cw_y}(x - {src_x}) - {vec_cw_x}(y - {src_y}) <= 0)")
    else:
        result = (f"({vec_ccw_y}(x - {src_x}) - {vec_ccw_x}(y - {src_y}) >= 0 ∨"
                  f" {vec_cw_y}(x - {src_x}) - {vec_cw_x}(y - {src_y}) <= 0)")

    if min_radius is not None:
        result += f" ∧ (x - {src_x}) ^ 2 + (y - {src_y}) ^ 2 >= {min_radius} ^ 2"
    
    if max_radius is not None:
        result += f" ∧ (x - {src_x}) ^ 2 + (y - {src_y}) ^ 2 <= {max_radius} ^ 2"

    return formatize_math_expr(result)

def from_names(
        src_name: str, 
        tgt_name: str, 
        degree: float, 
        max_radius: Optional[float | str] = None, 
        min_radius: Optional[float | str] = None
    ) -> str:
    
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

    if min_radius is not None:
        result += f" ∧ (x - x({src_name})) ^ 2 + (y - y({src_name})) ^ 2 >= {min_radius} ^ 2"
    
    if max_radius is not None:
        result += f" ∧ (x - x({src_name})) ^ 2 + (y - y({src_name})) ^ 2 <= {max_radius} ^ 2"

    return formatize_math_expr(result)
