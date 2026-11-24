# As long as it reads well

Follow PEP8 conventions as much as possible. Many editors/IDEs help enforce this easily. You may also use `uv format` to automatically format all project files. In any case, follow the below guidelines.

**At a minimum:**

- Use type hints in all function signatures and whenever the type cannot be directly inferred
  - `fun(a, b)` takes two integers `returns a boolean:
    - `def fun(a: int, b: int) -> bool`
  - obvious type is inferred from declaration
    - `foo = 3` foo is an int
  - a float value initiated to `0`
    - `bar: float = 0`
  - empty list that should only hold strings
    - `foobar: List[str] = []`
  - etc...
- Two blank lines between top-level (not indented) functions
- One blank line between methods in a class
