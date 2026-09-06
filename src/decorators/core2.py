from typing import Any, Callable


def hello_deco(func: Callable[..., Any]) -> Callable[..., Any]:
    def wrapper_function(*args: Any, **kwargs: Any) -> str:
        return "hello world from decorator"

    return wrapper_function
