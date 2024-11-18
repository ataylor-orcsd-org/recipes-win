from autopkglib import Processor, ProcessorError
import re

__all__ = ["Regex"]


class Regex(Processor):
    """This processor filters an incoming string based on the provided regular expression."""

    description = __doc__
    input_variables = {
        "string": {
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
        string = self.env.get('string')
        regex = self.env.get('regex')

        regoutput = re.search(regex, string)

if __name__ == "__main__":
    PROCESSOR = SampleSharedProcessor()
    PROCESSOR.execute_shell()