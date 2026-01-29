bucket_name = "My Project Backup "

safe_name = (
    bucket_name
    .strip()              # remove leading & trailing spaces
    .replace(" ", "-")    # replace spaces with hyphens
    .lower()              # convert to lowercase
)

print(safe_name)
