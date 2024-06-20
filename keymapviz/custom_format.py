# -*- coding: utf-8 -*-
import regex as re
from wcwidth import wcswidth

def custom_center(text, width):
    visual_width = wcswidth(text)
    padding = max(0, width - visual_width)
    left_padding = padding // 2
    right_padding = padding - left_padding
    return ' ' * left_padding + text + ' ' * right_padding

def custom_format(format_string, *values):
    # Find all placeholders in the format string
    pattern = r'{(\d+):([<>^]?)(\d*)\.?(\d*)}'
    matches = re.findall(pattern, format_string)

    # Initialize the result with the original format string
    result = format_string

    for match in matches:
        index, align, width, precision = match

        # Convert index and width to integers
        index = int(index)
        width = int(width) if width else 0
        precision = int(precision) if precision else None

        # Get the corresponding value
        value = str(values[index])

        # Apply precision if specified
        if precision is not None:
            value = value[:precision]

        # Determine padding and alignment
        if align == '^':  # Center alignment
            value = custom_center(value, width)
        elif align == '>':  # Right alignment
            value = value.rjust(width)
        elif align == '<':  # Left alignment
            value = value.ljust(width)
        else:  # Default to left alignment
            value = value.ljust(width)

        # Create the placeholder string
        placeholder = f'{{{index}:{align}{width}.{precision}}}' if precision is not None else f'{{{index}:{align}{width}}}'

        # Replace the placeholder in the result
        result = result.replace(placeholder, value, 1)

    return result
