from urllib.parse import quote_plus

# Your original credentials
username = "pablomrivera1976@gmail.com"
password = "3blinddevs24"

# Encoding the credentials
encoded_username = quote_plus(username)
encoded_password = quote_plus(password)

# Output the encoded values
print(f"Encoded username: {encoded_username}")
print(f"Encoded password: {encoded_password}")
