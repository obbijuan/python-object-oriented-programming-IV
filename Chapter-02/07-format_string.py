from typing import Optional

class Formatter:
    def format(self, string: str) -> str:
        pass


def format_string(string: str, formatter: Optional[Formatter] = None) -> str:
    """
    Format a string using the formatter object, which
    is expected to have a format() method that accepts
    a string.
    """

    class DefaultFormatter(Formatter):
        """Format a string in title case."""

        def format(self, string: str) -> str:
            return str(string).title()

    if not formatter:
        formatter = DefaultFormatter()

    return formatter.format(string)


"""
The format_string function accepts a string and optional Formatter object and then
applies the formatter to that string. If no Formatter instance is supplied, it creates
a formatter of its own as a local class and instantiates it. Since it is created inside
the scope of the function, this class cannot be accessed from anywhere outside of
that function. Similarly, functions can be defined inside other functions as well; in
general, any Python statement can be executed at any time.
These inner classes and functions are occasionally useful for one-off items that don't
require or deserve their own scope at the module level, or only make sense inside a
single method. However, it is not common to see Python code that frequently uses
this technique.
"""
