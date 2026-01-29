port_str = "8080"

# Convert string to integer
port = int(port_str)

# Validate port range
if 1 <= port <= 65535:
    print("Valid")
else:
    print("Invalid")
