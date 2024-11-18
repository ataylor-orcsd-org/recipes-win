from autopkglib import Processor, ProcessorError
import re

__all__ = ["Regex"]


class Regex(Processor):
    """This processor filters an incoming string based on the provided regular expression."""

    description = __doc__
    input_variables = {
        "searchString": {
            "required": True,
            "description": "String to search.",
        },
        "regexString": {
            "required": True,
            "description": "String to search.",
        }
    }
    output_variables = {
        "regoutput": {
            "description": "Result of regex search.",
        },
    }

    def main(self):
        searchString = self.env.get('searchString')
        regexString = self.env.get('regexString')

        regoutput = re.search(regexString, searchString)
        self.env['regoutput'] = regoutput

if __name__ == "__main__":
    PROCESSOR = Regex()
    PROCESSOR.execute_shell()