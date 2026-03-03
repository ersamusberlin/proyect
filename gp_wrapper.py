import subprocess
import config

def run_gp(command_name):
    if command_name not in config.COMMANDS:
        print(f"Unknown command: {command_name}")
        print("Available commands:", ", ".join(config.COMMANDS.keys()))
        return

    cmd = [config.GP_EXE_PATH] + config.COMMANDS[command_name]

    print("Running command:")
    print(" ".join(cmd))

    try:
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            check=True
        )
        print("=== STDOUT ===")
        print(result.stdout)
        print("=== STDERR ===")
        print(result.stderr)
    except subprocess.CalledProcessError as e:
        print("Command failed:", e.returncode)
        print("=== STDOUT ===")
        print(e.stdout)
        print("=== STDERR ===")
        print(e.stderr)

if __name__ == "__main__":
    # Change this to test different commands
    run_gp("info")
