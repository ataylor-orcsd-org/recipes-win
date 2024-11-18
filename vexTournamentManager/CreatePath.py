from autopkglib import Processor, ProcessorError

__all__ = ["CreatePath"]


class CreatePath(Processor):
    """This processor creates a path if it does not exist."""

    description = __doc__
    input_variables = {
        "filepath": {
            "required": True,
            "description": "Path to create.",
        }
    }
    output_variables = {
        "new_path": {"description": "Outputs the newly created path."}
    }

    def main(self):
        filepath = self.env.get('filepath')
        import os
        os.makedirs(os.path.dirname(filepath), exist_ok=True)

if __name__ == "__main__":
    PROCESSOR = SampleSharedProcessor()
    PROCESSOR.execute_shell()