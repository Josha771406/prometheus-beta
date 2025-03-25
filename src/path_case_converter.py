import re

def convert_to_path_case(input_string: str) -> str:
    """
    Convert a given string to path case (lowercase with hyphens).

    Path case transforms strings by:
    - Converting to lowercase
    - Replacing spaces, underscores, and camelCase with hyphens
    - Removing any non-alphanumeric characters except hyphens
    - Removing leading/trailing hyphens

    Args:
        input_string (str): The input string to convert to path case.

    Returns:
        str: The converted path case string.

    Raises:
        TypeError: If the input is not a string.

    Examples:
        >>> convert_to_path_case("Hello World")
        'hello-world'
        >>> convert_to_path_case("snake_case_string")
        'snake-case-string'
        >>> convert_to_path_case("camelCaseString")
        'camel-case-string'
        >>> convert_to_path_case("Mixed Case String!")
        'mixed-case-string'
    """
    # Check input type
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    # Handle empty string
    if not input_string:
        return ""
    
    # Convert camelCase and PascalCase to lowercase with hyphens
    # This regex finds capital letters and adds a hyphen before them, 
    # then converts to lowercase
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1-\2', input_string)
    s2 = re.sub('([a-z0-9])([A-Z])', r'\1-\2', s1)
    
    # Convert to lowercase and replace non-alphanumeric characters with hyphens
    path_case = re.sub(r'[^a-z0-9]+', '-', s2.lower())
    
    # Remove leading and trailing hyphens
    path_case = path_case.strip('-')
    
    return path_case