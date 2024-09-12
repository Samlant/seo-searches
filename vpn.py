import subprocess
import time

def connect_vpn(config_path):
    # Disconnect any existing VPN connection
    subprocess.run(["taskkill", "/F", "/IM", "openvpn.exe"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    time.sleep(2)  # Wait for the disconnection to complete

    # Connect to the new VPN location
    command = f"openvpn --config {config_path}"
    process = subprocess.Popen(command.split(), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    time.sleep(10)  # Wait for the connection to establish

    return process

def disconnect_vpn():
    subprocess.run(["taskkill", "/F", "/IM", "openvpn.exe"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    time.sleep(2)  # Wait for the disconnection to complete
