from autopkglib import Processor, ProcessorError

__all__ = ["CreateWin32Intune"]


class CreateWin32Intune(Processor):
    """This processor creates a Win32 PKG for Intune."""

    description = __doc__
    input_variables = {
        "exe": {
            "required": True,
            "description": "Path to IntuneWinAppUtil.exe",
        },
        "source": {
            "required": True,
            "description": "Path to directory to bundle",
        },
        "targetExe": {
            "required": True,
            "description": "Filename for exe/msi",
        },
        "destination": {
            "required": True,
            "description": "Output Path",
        }
    }
    output_variables = {
    }

    def main(self):
        import subprocess
        import os

        exe = self.env.get('exe')
        source = self.env.get('source')
        targetExe = self.env.get('targetExe')
        destination = self.env.get('destination')

        os.makedirs(os.path.dirname(destination), exist_ok=True)

        
        cmd = exe + ' -q -c ' + source + ' -s ' + targetExe + ' -o ' + destination
        print("CMD to process: " + cmd)
        process = subprocess.Popen(cmd, stdout=subprocess.PIPE, creationflags=0x08000000)
        process.wait()

if __name__ == "__main__":
    PROCESSOR = SampleSharedProcessor()
    PROCESSOR.execute_shell()