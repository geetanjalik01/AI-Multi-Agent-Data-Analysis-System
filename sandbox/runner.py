import subprocess
import os

CODE_FILE = "generated_code.py"

try:
    result = subprocess.run(
        ["python", CODE_FILE],
        capture_output=True,
        text=True,
        timeout=60
    )

    print("\n===== STDOUT =====\n")
    print(result.stdout)

    print("\n===== STDERR =====\n")
    print(result.stderr)

except subprocess.TimeoutExpired:
    print("Execution timed out")

except Exception as e:
    print(f"Error: {e}")