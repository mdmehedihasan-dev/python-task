bucket_name = "My Project Backup "

safe_name = (
    bucket_name
    .strip()              
    .replace(" ", "-")
    .lower()   
)

print(safe_name)
