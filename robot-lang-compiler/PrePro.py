import re

class PrePro:

    def filter_comments(arguments):
        regex = r"(#[^\n]*)"
        arguments = re.sub(regex, "", arguments, 0, re.MULTILINE)
        return arguments
