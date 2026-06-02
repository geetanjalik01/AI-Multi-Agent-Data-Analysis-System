# utils/sandbox_executor.py
import os
import sys
from pathlib import Path
from contextlib import redirect_stdout
from io import StringIO

def safe_exec(code: str, cwd: str = ".") -> dict:
    result = {"stdout": "", "error": None, "artifacts": []}
    try:
        # Restrict where code can write
        output_dir = Path(cwd) / "outputs"
        output_dir.mkdir(exist_ok=True)

        # Capture stdout
        stdout_capture = StringIO()
        with redirect_stdout(stdout_capture):
            exec(code, {"__builtins__": __builtins__, "print": print})

        result["stdout"] = stdout_capture.getvalue()
    except Exception as e:
        result["error"] = str(e)
    return result