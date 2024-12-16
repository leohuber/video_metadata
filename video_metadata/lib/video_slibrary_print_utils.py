# This module provides functions to print text in different colors using ANSI escape codes.
#
# ANSI Color Codes:
#
# Text Colors:
# 30: Black
# 31: Red
# 32: Green
# 33: Yellow
# 34: Blue
# 35: Magenta
# 36: Cyan
# 37: White
# 90: Bright Black (Gray)
# 91: Bright Red
# 92: Bright Green
# 93: Bright Yellow
# 94: Bright Blue
# 95: Bright Magenta
# 96: Bright Cyan
# 97: Bright White
#
# Background Colors:
# 40: Black
# 41: Red
# 42: Green
# 43: Yellow
# 44: Blue
# 45: Magenta
# 46: Cyan
# 47: White
# 100: Bright Black (Gray)
# 101: Bright Red
# 102: Bright Green
# 103: Bright Yellow
# 104: Bright Blue
# 105: Bright Magenta
# 106: Bright Cyan
# 107: Bright White
#
# Text Styles:
# 0: Reset/Normal
# 1: Bold/Bright
# 4: Underline
# 5: Blink
# 7: Inverse
# 8: Hidden

# ANSI escape codes are used to apply text color, background color, and text styles in the terminal. These codes are embedded in the text string and interpreted by the terminal to format the text accordingly.
# \033[<style>;<text_color>;<background_color>m


def print_green(text) -> None:
    GREEN = "\033[1;92m"  # ANSI escape code for bright green text
    RESET = "\033[0m"  # ANSI escape code to reset text formatting to default
    print(f"{GREEN}{text}{RESET}")


def print_blue(text) -> None:
    BLUE = "\033[1;94m"  # ANSI escape code for bright blue text
    RESET = "\033[0m"  # ANSI escape code to reset text formatting to default
    print(f"{BLUE}{text}{RESET}")


def print_red(text) -> None:
    RED = "\033[1;91m"  # ANSI escape code for bright red text
    RESET = "\033[0m"  # ANSI escape code to reset text formatting to default
    print(f"{RED}{text}{RESET}")
