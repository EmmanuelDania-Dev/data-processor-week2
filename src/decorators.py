from collections.abc import Callable
from functools import wraps
from typing import Any


def process_log(
    func: Callable[..., Any]
) -> Callable[..., Any]:
    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        try:
            print(f"Starting: {func.__name__}")

            result = func(*args, **kwargs)

            print(f"Completed: {func.__name__}")

            return result

        except Exception as error:
            print(
                f"Error in {func.__name__}: {error}"
            )
            raise

    return wrapper
