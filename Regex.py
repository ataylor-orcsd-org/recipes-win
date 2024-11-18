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
        "regex": {
            "required": True,
            "description": "String to search.",
        }
    }
    output_variables = {
        "regoutput": {
        }
    }

    def main(self):
        searchString = self.env.get('searchString')
        regex = self.env.get('regex')

        regoutput = re.search(regex, searchString)

if __name__ == "__main__":
    PROCESSOR = SampleSharedProcessor()
    PROCESSOR.execute_shell()