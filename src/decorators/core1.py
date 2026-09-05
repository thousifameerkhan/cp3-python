from typing import Any, Callable


def uppercase(func: Callable[..., str]) -> Callable[..., str]:
    def wrapper(*args: Any, **kwargs: Any) -> str:
        result = func(*args, **kwargs)
        return result.upper()

    return wrapper
