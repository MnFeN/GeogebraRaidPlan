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

    d_square = f"(x - {src_x}) ^ 2 + (y - {src_y}) ^ 2"

    if (max_radius is not None and min_radius is not None):
        return f"{min_radius} ^ 2 <= {d_square} <= {max_radius} ^ 2"
    elif (max_radius is not None):
        return f"{d_square} <= {max_radius} ^ 2"
    elif (min_radius is not None):
        return f"{d_square} >= {min_radius} ^ 2"
    else:
        raise ValueError("Either max_radius or min_radius should be given.")

def from_names(
        src_name: str, 
        max_radius: Optional[float | str] = None, 
        min_radius: Optional[float | str] = None
    ) -> str:
    
    d_square = f"(x - x({src_name})) ^ 2 + (y - y({src_name})) ^ 2"

    if (max_radius is not None and min_radius is not None):
        return f"{min_radius} ^ 2 <= {d_square} <= {max_radius} ^ 2"
    elif (max_radius is not None):
        return f"{d_square} <= {max_radius} ^ 2"
    elif (min_radius is not None):
        return f"{d_square} >= {min_radius} ^ 2"
    else:
        raise ValueError("Either max_radius or min_radius should be given.")
