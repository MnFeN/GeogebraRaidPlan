import math
import re

def my_round(x: float | int, n: int) -> float | int:
    result = round(x, n)
    if isinstance(result, float) and result.is_integer():
        return int(result)
    else:
        return result

def formatize_math_expr(result: str) -> str:
    result = result.replace("- -", "+ ").replace("+ -", "- ").replace(" 1 *", " *")
    result = re.sub(r"(?<=[\(|-+]) *1 *(?=\()", " ", result)
    return result