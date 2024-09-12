import os
import subprocess
import time
from pathlib import Path
import html
import vpn
import search
import pdf

# Directory containing OpenVPN configuration files
config_dir = Path("openvpn/configs")

# List of OpenVPN configuration files for different locations
vpn_configs = list(config_dir.glob("*.ovpn"))

# Directory to save screenshots
screenshot_dir = Path("screenshots")

# Ensure the screenshots directory is empty
if screenshot_dir.exists():
    for file in screenshot_dir.glob("*"):
        file.unlink()
else:
    screenshot_dir.mkdir()

# Rotate through VPN locations and perform the search
for config in vpn_configs:
    vpn.connect_vpn(config)
    print(f"Connected to VPN using config: {config}")
    
    # Perform the search and save screenshots
    search.search_novamar_insurance(config.stem, screenshot_dir)
    
    vpn.disconnect_vpn()
    print(f"Disconnected VPN for config: {config}")

print("VPN rotation and search completed.")

# Create PDF and HTML reports
pdf.create_pdf(screenshot_dir)
html.create_html(screenshot_dir)

print("Reports generated and saved in the 'result' directory.")
