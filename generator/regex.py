import re


class Patterns:
    """
    Class to store regex patterns used in the program.
    """

    JAVADOC = re.compile(r"/\*[\s\S]*?\*/", re.MULTILINE)
    JAVA_COMMENT = re.compile(r"(?<!:)//.*$", re.MULTILINE)
    DOUBLE_SPACE = re.compile(r"(?:\s\s)+", re.MULTILINE)
    TOKEN_SPLITTER = re.compile(r'(["\-\\=,;:/(){}@[\]<>&*!|?`+#%~^$])')
    WORD = re.compile(r"(\w+)")
    LIST_ITEM_READER = re.compile(r'((?:\\"|[^"])+)')
    VALIDATOR_CLASS = re.compile(r"class (?P<name>\w+).* extends Validator")
    VALIDATOR_DESCRIPTION = r'description \(\) {return (?P<description>".+);'
    ENUM_FILTER = re.compile(r"\([^()]*\)")
    STATIC_FIELD = re.compile(
        r"(?:public|private) ?static (?:final)? ?(?P<type>[^ ]+) ?(?P<name>\w+)\s*=?\s*(?P<value>[^;]+)?"
    )
    FLOATING_POINT_NUMBER = re.compile(r"([-+]?[0-9]*\.?[0-9]+)")
