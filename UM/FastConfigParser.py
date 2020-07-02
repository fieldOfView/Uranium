from typing import Union, Dict

import re

supported_data = Union[int, float, str]


class FastConfigParser:
    """
    This class is to replace the much slower configparser provided by Python itself.
    It's probably nowhere near as robust and supports only a fraction of the functionality of the real deal.
    """
    header_regex = re.compile("\[(.*)\]\n([^\[]*)")
    key_value_regex = re.compile("([^=\n ]+) *= *([^\n]+)")

    def __init__(self, data: str) -> None:
        header_result = self.header_regex.findall(data)

        self._parsed_data = {}  # type: Dict[str, Dict[str, supported_data]]

        for header, content in header_result:
            extracted_key_value_pairs = {}

            for key, value in self.key_value_regex.findall(content):
                extracted_key_value_pairs[key] = value
            self._parsed_data[header] = extracted_key_value_pairs

    def __contains__(self, key: str) -> bool:
        return key in self._parsed_data

    def __getitem__(self, key: str) -> Dict[str, supported_data]:
        return self._parsed_data[key]