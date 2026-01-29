# VM dictionary
vm = {
    "id": "vm01",
    "ip": "192.168.1.10",
    "status": "running",
    "region": "us-east-1"
}

# Update status
vm["status"] = "stopped"

# Add new key
vm["instance_type"] = "t3.large"

# Print updated VM
print(vm)
