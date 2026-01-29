env = "production"  # current environment

if env != "production":
    print("Executing Delete")
else:
    print("Access Denied: Cannot delete in Prod!")
