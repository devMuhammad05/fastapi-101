from typing import Annotated, get_type_hints, get_origin, get_args

def double(x: Annotated[int, (0, 100)]) -> int:
    type_hints = get_type_hints(double, include_extras=True)
    hint = type_hints['x']

    if get_origin(hint) is Annotated:
        hint_type, *hint_args = get_args(hint)
        print(hint)
        return x * 2


result = double(499)
print(result)