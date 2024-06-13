from math import *
from common.utils import my_round, formatize_math_expr
from typing import Optional

def from_coords(
        src_x: float, src_y: float, 
        max_radius: Optional[float] = None, 
        min_radius: Optional[float] = None
    ) -> str:

    src_x = my_round(src_x, 3)
    src_y = my_round(src_y, 3)

    outer = f"(x - {src_x}) ^ 2 + (y - {src_y}) ^ 2 <= {max_radius} ^ 2"
    inner = f"(x - {src_x}) ^ 2 + (y - {src_y}) ^ 2 >= {min_radius} ^ 2"

    if (max_radius is not None and min_radius is not None):
        return f"{inner} ∧ {outer}"
    elif (max_radius is not None):
        return outer
    elif (min_radius is not None):
        return inner
    else:
        raise ValueError("Either max_radius or min_radius should be given.")

def from_names(
        src_name: str, 
        max_radius: Optional[float | str] = None, 
        min_radius: Optional[float | str] = None
    ) -> str:
    
    outer = f"(x - x({src_name})) ^ 2 + (y - y({src_name})) ^ 2 <= {max_radius} ^ 2"
    inner = f"(x - x({src_name})) ^ 2 + (y - y({src_name})) ^ 2 >= {min_radius} ^ 2"

    if (max_radius is not None and min_radius is not None):
        return f"{inner} ∧ {outer}"
    elif (max_radius is not None):
        return outer
    elif (min_radius is not None):
        return inner
    else:
        raise ValueError("Either max_radius or min_radius should be given.")