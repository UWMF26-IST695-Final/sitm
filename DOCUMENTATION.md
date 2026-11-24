# Project Documentation

Document in `README.md` under the "Project Documentation" heading, roughly based on the format already in there.

# Code Documentation

Document functions and methods using python docstrings `""" """` using the following format:


Use the Google Python Code Style for function docstrings like seen below. A brief description should be included at the top of the docstring, followed by the arguments, return value if applicable, and exceptions if applicable.
> As per the code style, function signatures should always use type hints. Therefore, types don't need to be stated once again in docstrings.

```py
def function_with_type_annotations(a: int, b: str) -> bool:
    """Example function with PEP 484 type annotations.

    Args:
        a: Description of the first parameter.
        b: Description of the second parameter.

    Returns:
        Description of the result (e.g. True for success, False otherwise)

    Raises:
        ValueError: If `a` or `b` are invalid
    """
    return True
```
