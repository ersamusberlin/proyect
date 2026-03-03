# config.py

GP_EXE_PATH = r"C:\Users\conta\Downloads\gp.exe"

# Example AID for a GIDS applet (you can use a placeholder)
GIDS_AID = "A000000003000000"   # Example, replace if needed

# Predefined command profiles
COMMANDS = {
    "info": ["--info"],
    "list": ["--list"],
    "connect_gids": ["--connect", GIDS_AID],
    "send_test_apdu": ["--apdu", "00A4040000"],  # Select command example
}
